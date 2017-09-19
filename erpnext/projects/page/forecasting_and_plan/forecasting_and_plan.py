
from __future__ import unicode_literals
import frappe

from frappe import _

@frappe.whitelist()
def get_data(from_date, to_date ,employee=None):
	sqlstring = """select * from `tabTask`
		where (date(exp_start_date) between " """+from_date+""" " and " """+to_date+""" " )
		or (date(exp_end_date) between " """+from_date+""" " and " """+to_date+""" " )"""
	
	sqlstring_leave = """select * from `tabLeave Application`
		where (date(from_date) between " """+from_date+""" " and " """+to_date+""" " )
		or (date(to_date) between " """+from_date+""" " and " """+to_date+""" " )"""
	
	the_list = []
	mployee_dict ={}
	active_tasks = frappe.db.sql(sqlstring, as_dict=True)
	active_leaves = frappe.db.sql(sqlstring_leave, as_dict=True)
	import ast
	
	for task in active_tasks :
		if task._assign:
			for user_assigned in ast.literal_eval(task._assign):
				emp_list = frappe.get_list("Employee",
					fields=["name","user_id","employee_name"],
					filters = {
						"user_id": user_assigned,
					})
				if emp_list:
					mployee_dict[ emp_list[0]["user_id"] ] = emp_list[0]["name"]
					the_list.append({"id":emp_list[0]["name"],"text" : emp_list[0]["employee_name"] ,
					 #~ "start_date":task.exp_start_date.strftime('%d-%m-%Y'),
						#~ "end_date":task.exp_end_date.strftime('%d-%m-%Y'),
						 "open": True})
	
	for task in active_tasks : 
		if task._assign:
			for user_assigned in ast.literal_eval(task._assign):
				the_list.append({"id":task.name,"text" : task.name +" "+task.project , "start_date":task.exp_start_date.strftime('%d-%m-%Y'),
					"end_date":task.exp_end_date.strftime('%d-%m-%Y'), "open": True, "parent":mployee_dict[user_assigned]})
	
	
	for leave in active_leaves : 
		the_list.append({"id":leave.name,"text" :leave.employee_name , "start_date":leave.from_date.strftime('%d-%m-%Y'),
			"end_date":leave.to_date.strftime('%d-%m-%Y'), "open": True, "parent":leave.employee})
	
	
	return the_list
