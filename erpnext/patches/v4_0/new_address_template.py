<<<<<<< HEAD
from __future__ import print_function, unicode_literals
=======
from __future__ import unicode_literals
>>>>>>> 95d706d57b6cac6113b64196e32dafd821e302b7
import frappe

def execute():
	frappe.reload_doc("utilities", "doctype", "address_template")
	if not frappe.db.sql("select name from `tabAddress Template`"):
		try:
			d = frappe.new_doc("Address Template")
			d.update({"country":frappe.db.get_default("country") or
				frappe.db.get_value("Global Defaults", "Global Defaults", "country")})
			d.insert()
		except:
<<<<<<< HEAD
			print(frappe.get_traceback())
=======
			print frappe.get_traceback()
>>>>>>> 95d706d57b6cac6113b64196e32dafd821e302b7

