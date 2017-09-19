frappe.pages['forecasting-and-plan'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Forecasting and Planning',
		single_column: true
		
	});
	$(frappe.render_template('forecasting_and_plan')).appendTo(page.body);
	wrapper.sales_funnel = new erpnext.ForcastingAndPlan(wrapper);
	frappe.breadcrumbs.add("Projects");


}

erpnext.ForcastingAndPlan = Class.extend({
	init: function(wrapper) {
		var me = this;
		// 0 setTimeout hack - this gives time for canvas to get width and height
		setTimeout(function() {
			me.setup(wrapper);
			me.get_data();
		}, 0);
	},

	setup: function(wrapper) {
		var me = this;

		this.elements = {
			layout: $(wrapper).find(".layout-main"),
			from_date: wrapper.page.add_date(__("From Date")),
			to_date: wrapper.page.add_date(__("To Date")),
			refresh_btn: wrapper.page.set_primary_action(__("Refresh"),
				function() { me.get_data(); }, "fa fa-refresh"),
		};
		//~ this.employee_field = frappe.ui.form.make_control({
			//~ df: {
				//~ fieldtype: 'Link',
				//~ label: 'Employee',
				//~ fieldname: 'employee',
				//~ options: 'Employee',
				//~ reqd: 0,
				//~ onchange: () => {
					//~ alert(this.employee_field.get_value());
					//~ this.events.on_employee_change(this.employee_field.get_value());
					//~ me.get_data();
				//~ }
			//~ },
			//~ parent: $(wrapper).find('#employee_loc'),
			//~ render_input: true
		//~ });
		this.elements.no_data = $('<div class="alert alert-warning" style="text-align: center;">' + __("No Data, Please Check the dates selected.") + '</div>')
			.toggle(false)
			.appendTo(this.elements.layout);

		//~ this.elements.main_conten_wrapper = $('<div class="funnel-wrapper text-center"></div>')
		this.elements.main_conten_wrapper = $('<div class="main_conten text-center"></div>')
			.appendTo(this.elements.layout);

		this.options = {
			from_date: frappe.datetime.add_months(frappe.datetime.get_today(), -1),
			to_date: frappe.datetime.get_today()
		};

		// set defaults and bind on change
		$.each(this.options, function(k, v) {
			me.elements[k].val(frappe.datetime.str_to_user(v));
			me.elements[k].on("change", function() {
				me.options[k] = frappe.datetime.user_to_str($(this).val());
				me.get_data();
			});
		});

		// bind refresh
		this.elements.refresh_btn.on("click", function() {
			me.get_data(this);
			//~ alert("btn");
		});

		//~ // bind resize
		//~ $(window).resize(function() {
			//~ me.render();
		//~ });
	},

	get_data: function(btn) {
		var me = this;
		frappe.call({
			method: "erpnext.projects.page.forecasting_and_plan.forecasting_and_plan.get_data",
			args: {
				from_date: this.options.from_date,
				to_date: this.options.to_date
			},
			btn: btn,
			callback: function(r) {
				if(!r.exc) {
					console.log("Message",r.message);
					 if ( typeof r.message !== "undefined"){
						me.options.data = r.message;
						me.elements.no_data.toggle(false);
						$("#chart_div").show();
						me.render(r.message);
					}
					else 
					{
						me.elements.no_data.toggle(true);
						$("#chart_div").hide();
						return;
						
					}
				}
			}
		});
	},

	render: function(theData) {
       
			gantt.config.columns = [
				{name:"text",       label:"Assigned Users",  width:250, tree:true },
				{name:"id",       label:"Doc Id",  width:120 ,   align: "left"},
				//~ {name:"start_date", label:"Start time", width: 90, align: "center" },
				//~ {name:"end_date", label:"End time", width: 90, align: "center" },
				{name:"duration",   label:"Duration", width: 40 ,  align: "center" },
			];
			gantt.config.readonly = true;			
			gantt.config.autosize = "y";
			gantt.init("chart_div"); 
			gantt.parse ({data:theData});

	},

});
