from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Item",
			"_doctype": "Item",
<<<<<<< HEAD
			"color": "#f39c12",
=======
			"color": "#183A60",
>>>>>>> 95d706d57b6cac6113b64196e32dafd821e302b7
			"icon": "octicon octicon-package",
			"type": "link",
			"link": "List/Item"
		},
<<<<<<< HEAD
		{
			"module_name": "Customer",
			"_doctype": "Customer",
			"color": "#1abc9c",
=======
     	{
			"module_name": "Customer",
			"_doctype": "Customer",
			"color": "#183A60",
>>>>>>> 95d706d57b6cac6113b64196e32dafd821e302b7
			"icon": "octicon octicon-tag",
			"type": "link",
			"link": "List/Customer"
		},
<<<<<<< HEAD
		{
			"module_name": "Supplier",
			"_doctype": "Supplier",
			"color": "#c0392b",
=======
        	{
			"module_name": "Risk Assessment",
			"_doctype": "Risk",
			"color": "#183A60",
			"icon": "octicon octicon-tag",
			"type": "link",
			"link": "List/Risk"
		},
		{
			"module_name": "Supplier",
			"_doctype": "Supplier",
			"color": "#183A60",
>>>>>>> 95d706d57b6cac6113b64196e32dafd821e302b7
			"icon": "octicon octicon-briefcase",
			"type": "link",
			"link": "List/Supplier"
		},
		{
			"_doctype": "Employee",
			"module_name": "Employee",
<<<<<<< HEAD
			"color": "#2ecc71",
=======
			"color": "#183A60",
>>>>>>> 95d706d57b6cac6113b64196e32dafd821e302b7
			"icon": "octicon octicon-organization",
			"type": "link",
			"link": "List/Employee"
		},
		{
			"module_name": "Project",
			"_doctype": "Project",
<<<<<<< HEAD
			"color": "#8e44ad",
=======
			"color": "#183A60",
>>>>>>> 95d706d57b6cac6113b64196e32dafd821e302b7
			"icon": "octicon octicon-rocket",
			"type": "link",
			"link": "List/Project"
		},
		{
			"module_name": "Issue",
<<<<<<< HEAD
			"color": "#2c3e50",
=======
			"color": "#183A60",
>>>>>>> 95d706d57b6cac6113b64196e32dafd821e302b7
			"icon": "octicon octicon-issue-opened",
			"_doctype": "Issue",
			"type": "link",
			"link": "List/Issue"
		},
		{
			"module_name": "Lead",
<<<<<<< HEAD
			"icon": "octicon octicon-broadcast",
=======
						"color": "#183A60",

			"icon": "octicon octicon-broadcast",
						"color": "#183A60",

>>>>>>> 95d706d57b6cac6113b64196e32dafd821e302b7
			"type": "module",
			"_doctype": "Lead",
			"type": "link",
			"link": "List/Lead"
		},
		{
			"module_name": "Profit and Loss Statement",
			"_doctype": "Account",
<<<<<<< HEAD
			"color": "#3498db",
=======
			"color": "#183A60",
>>>>>>> 95d706d57b6cac6113b64196e32dafd821e302b7
			"icon": "octicon octicon-repo",
			"type": "link",
			"link": "query-report/Profit and Loss Statement"
		},

		# old
		{
			"module_name": "Accounts",
<<<<<<< HEAD
			"color": "#3498db",
=======
			"color": "#183A60",
>>>>>>> 95d706d57b6cac6113b64196e32dafd821e302b7
			"icon": "octicon octicon-repo",
			"type": "module",
			"hidden": 1
		},
<<<<<<< HEAD
		{
			"module_name": "Stock",
			"color": "#f39c12",
			"icon": "fa fa-truck",
			"icon": "octicon octicon-package",
			"type": "module",
			"hidden": 1
		},
		{
			"module_name": "CRM",
			"color": "#EF4DB6",
=======
#		{
#			"module_name": "Stock",
			# "color": "#183A60",
#			"icon": "fa fa-truck",
#			"icon": "octicon octicon-package",
#			"type": "module",
#			"hidden": 1
#		},
		{
			"module_name": "CRM",
			"color": "#183A60",
>>>>>>> 95d706d57b6cac6113b64196e32dafd821e302b7
			"icon": "octicon octicon-broadcast",
			"type": "module",
			"hidden": 1
		},
<<<<<<< HEAD
		{
			"module_name": "Selling",
			"color": "#1abc9c",
			"icon": "fa fa-tag",
			"icon": "octicon octicon-tag",
			"type": "module",
			"hidden": 1
		},
		{
			"module_name": "Buying",
			"color": "#c0392b",
=======
#		{
#			"module_name": "Selling",
			# "color": "#183A60",
#			"icon": "fa fa-tag",
#			"icon": "octicon octicon-tag",
#			"type": "module",
#			"hidden": 1
#		},
		{
			"module_name": "Buying",
			"color": "#183A60",
>>>>>>> 95d706d57b6cac6113b64196e32dafd821e302b7
			"icon": "fa fa-shopping-cart",
			"icon": "octicon octicon-briefcase",
			"type": "module",
			"hidden": 1
		},
		{
			"module_name": "HR",
<<<<<<< HEAD
			"color": "#2ecc71",
=======
			"color": "#183A60",
>>>>>>> 95d706d57b6cac6113b64196e32dafd821e302b7
			"icon": "fa fa-group",
			"icon": "octicon octicon-organization",
			"label": _("Human Resources"),
			"type": "module",
			"hidden": 1
		},
<<<<<<< HEAD
		{
			"module_name": "Manufacturing",
			"color": "#7f8c8d",
			"icon": "fa fa-cogs",
			"icon": "octicon octicon-tools",
			"type": "module",
			"hidden": 1
		},
		{
			"module_name": "POS",
			"color": "#589494",
			"icon": "fa fa-th",
			"icon": "octicon octicon-credit-card",
			"type": "page",
			"link": "pos",
			"label": _("POS")
		},
		{
			"module_name": "Projects",
			"color": "#8e44ad",
=======
#		{
#			"module_name": "Manufacturing",
#			"color": "#7f8c8d",
#			"icon": "fa fa-cogs",
#			"icon": "octicon octicon-tools",
#			"type": "module",
#			"hidden": 1
#		},
#		{
#			"module_name": "POS",
#			"color": "#589494",
#			"icon": "fa fa-th",
#			"icon": "octicon octicon-credit-card",
#			"type": "page",
#			"link": "pos",
#			"label": _("POS")
#		},
		{
			"module_name": "Projects",
			"color": "#183A60",
>>>>>>> 95d706d57b6cac6113b64196e32dafd821e302b7
			"icon": "fa fa-puzzle-piece",
			"icon": "octicon octicon-rocket",
			"type": "module",
			"hidden": 1
		},
		{
			"module_name": "Support",
<<<<<<< HEAD
			"color": "#2c3e50",
=======
			"color": "#183A60",
>>>>>>> 95d706d57b6cac6113b64196e32dafd821e302b7
			"icon": "fa fa-phone",
			"icon": "octicon octicon-issue-opened",
			"type": "module",
			"hidden": 1
		},
<<<<<<< HEAD
		{
			"module_name": "Learn",
			"color": "#FF888B",
			"icon": "octicon octicon-device-camera-video",
			"type": "module",
			"is_help": True,
			"label": _("Learn"),
			"hidden": 1
		},
		{
			"module_name": "Maintenance",
			"color": "#FF888B",
			"icon": "octicon octicon-tools",
			"type": "module",
			"label": _("Maintenance")
		},
		{
			"module_name": "Student",
			"color": "#c0392b",
			"icon": "octicon octicon-person",
			"label": _("Student"),
			"link": "List/Student",
			"_doctype": "Student",
			"type": "list"
		},
		{
			"module_name": "Student Group",
			"color": "#d59919",
			"icon": "octicon octicon-organization",
			"label": _("Student Group"),
			"link": "List/Student Group",
			"_doctype": "Student Group",
			"type": "list"
		},
		{
			"module_name": "Course Schedule",
			"color": "#fd784f",
			"icon": "octicon octicon-calendar",
			"label": _("Course Schedule"),
			"link": "Calendar/Course Schedule",
			"_doctype": "Course Schedule",
			"type": "list"
		},
		{
			"module_name": "Student Attendance",
			"color": "#3aacba",
			"icon": "octicon octicon-checklist",
			"label": _("Student Attendance"),
			"link": "List/Student Attendance",
			"_doctype": "Student Attendance",
			"type": "list"
		},
		{
			"module_name": "Course",
			"color": "#8e44ad",
			"icon": "octicon octicon-book",
			"label": _("Course"),
			"link": "List/Course",
			"_doctype": "Course",
			"type": "list"
		},
		{
			"module_name": "Program",
			"color": "#9b59b6",
			"icon": "octicon octicon-repo",
			"label": _("Program"),
			"link": "List/Program",
			"_doctype": "Program",
			"type": "list"
		},
		{
			"module_name": "Student Applicant",
			"color": "#4d927f",
			"icon": "octicon octicon-clippy",
			"label": _("Student Applicant"),
			"link": "List/Student Applicant",
			"_doctype": "Student Applicant",
			"type": "list"
		},
		{
			"module_name": "Fees",
			"color": "#83C21E",
			"icon": "fa fa-money",
			"label": _("Fees"),
			"link": "List/Fees",
			"_doctype": "Fees",
			"type": "list"
		},
		{
			"module_name": "Instructor",
			"color": "#a99e4c",
			"icon": "octicon octicon-broadcast",
			"label": _("Instructor"),
			"link": "List/Instructor",
			"_doctype": "Instructor",
			"type": "list"
		},
		{
			"module_name": "Room",
			"color": "#f22683",
			"icon": "fa fa-map-marker",
			"label": _("Room"),
			"link": "List/Room",
			"_doctype": "Room",
			"type": "list"
		},
		{
			"module_name": "Schools",
			"color": "#DE2B37",
			"icon": "octicon octicon-mortar-board",
			"type": "module",
			"label": _("Schools")
		}
=======
#		{
#			"module_name": "Learn",
#			"color": "#FF888B",
#			"icon": "octicon octicon-device-camera-video",
#			"type": "module",
#			"is_help": True,
#			"label": _("Learn"),
#			"hidden": 1
#		},
#		{
#			"module_name": "Maintenance",
#			"color": "#FF888B",
#			"icon": "octicon octicon-tools",
#			"type": "module",
#			"label": _("Maintenance")
#		},
#		{
#			"module_name": "Student",
#			"color": "#c0392b",
#			"icon": "octicon octicon-person",
#			"label": _("Student"),
#			"link": "List/Student",
#			"_doctype": "Student",
#			"type": "list"
#		},
#		{
#			"module_name": "Student Group",
#			"color": "#d59919",
#			"icon": "octicon octicon-organization",
#			"label": _("Student Group"),
#			"link": "List/Student Group",
#			"_doctype": "Student Group",
#			"type": "list"
#		},
#		{
#			"module_name": "Course Schedule",
#			"color": "#fd784f",
#			"icon": "octicon octicon-calendar",
#			"label": _("Course Schedule"),
#			"link": "Calendar/Course Schedule",
#			"_doctype": "Course Schedule",
#			"type": "list"
#		},
#		{
#			"module_name": "Student Attendance",
#			"color": "#3aacba",
#			"icon": "octicon octicon-checklist",
#			"label": _("Student Attendance"),
#			"link": "List/Student Attendance",
#			"_doctype": "Student Attendance",
#			"type": "list"
#		},
#		{
#			"module_name": "Course",
#			"color": "#8e44ad",
#			"icon": "octicon octicon-book",
#			"label": _("Course"),
#			"link": "List/Course",
#			"_doctype": "Course",
#			"type": "list"
#		},
#		{
#			"module_name": "Program",
#			"color": "#9b59b6",
#			"icon": "octicon octicon-repo",
#			"label": _("Program"),
#			"link": "List/Program",
#			"_doctype": "Program",
#			"type": "list"
#		},
#		{
#			"module_name": "Student Applicant",
#			"color": "#4d927f",
#			"icon": "octicon octicon-clippy",
#			"label": _("Student Applicant"),
#			"link": "List/Student Applicant",
#			"_doctype": "Student Applicant",
#			"type": "list"
#		},
#		{
#			"module_name": "Fees",
#			"color": "#83C21E",
#			"icon": "fa fa-money",
#			"label": _("Fees"),
#			"link": "List/Fees",
#			"_doctype": "Fees",
#			"type": "list"
#		},
#		{
#			"module_name": "Instructor",
#			"color": "#a99e4c",
#			"icon": "octicon octicon-broadcast",
#			"label": _("Instructor"),
#			"link": "List/Instructor",
#			"_doctype": "Instructor",
#			"type": "list"
#		},
#		{
#			"module_name": "Room",
#			"color": "#f22683",
#			"icon": "fa fa-map-marker",
#			"label": _("Room"),
#			"link": "List/Room",
#			"_doctype": "Room",
#			"type": "list"
#		},
#		{
#			"module_name": "Schools",
#			"color": "#DE2B37",
#			"icon": "octicon octicon-mortar-board",
#			"type": "module",
#			"label": _("Schools")
#		}
>>>>>>> 95d706d57b6cac6113b64196e32dafd821e302b7
	]
