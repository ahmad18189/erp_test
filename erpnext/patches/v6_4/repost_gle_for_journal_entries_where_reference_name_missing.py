# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

<<<<<<< HEAD
from __future__ import print_function, unicode_literals
=======
from __future__ import unicode_literals
>>>>>>> 95d706d57b6cac6113b64196e32dafd821e302b7
import frappe

def execute():
	je_list = frappe.db.sql_list("""select distinct parent from `tabJournal Entry Account` je
		where docstatus=1 and ifnull(reference_name, '') !='' and creation > '2015-03-01'
			and not exists(select name from `tabGL Entry` 
				where voucher_type='Journal Entry' and voucher_no=je.parent 
				and against_voucher_type=je.reference_type 
				and against_voucher=je.reference_name)""")

	for d in je_list:
<<<<<<< HEAD
		print(d)
=======
		print d
>>>>>>> 95d706d57b6cac6113b64196e32dafd821e302b7
		
		# delete existing gle
		frappe.db.sql("delete from `tabGL Entry` where voucher_type='Journal Entry' and voucher_no=%s", d)

		# repost gl entries
		je = frappe.get_doc("Journal Entry", d)
		je.make_gl_entries()