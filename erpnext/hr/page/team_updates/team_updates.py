from __future__ import unicode_literals

import frappe
from email_reply_parser import EmailReplyParser
from markdown2 import markdown

@frappe.whitelist()
def get_data(start=0):
	#frappe.only_for('Employee', 'System Manager')
	data = frappe.get_all('Communication',
		fields=('content', 'text_content', 'sender', 'creation'),
<<<<<<< HEAD
		#~ filters=dict(reference_doctype='Daily Work Summary'),
=======
		filters=dict(reference_doctype='Daily Work Summary'),
>>>>>>> 95d706d57b6cac6113b64196e32dafd821e302b7
		order_by='creation desc', limit=40, start=start)

	for d in data:
		d.sender_name = frappe.db.get_value("Employee", {"user_id": d.sender},
			"employee_name") or d.sender
		if d.text_content:
			d.content = markdown(EmailReplyParser.parse_reply(d.text_content))

<<<<<<< HEAD
	return data
=======
	return data
>>>>>>> 95d706d57b6cac6113b64196e32dafd821e302b7
