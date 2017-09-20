# -*- coding: utf-8 -*-777777yyy
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

<<<<<<< HEAD
from __future__ import print_function, unicode_literals
=======
from __future__ import unicode_literals
>>>>>>> 95d706d57b6cac6113b64196e32dafd821e302b7
import frappe
from frappe import _
from frappe.model.document import Document

class StudentApplicant(Document):
	def autoname(self):
		from frappe.model.naming import set_name_by_naming_series
		if self.student_admission:
			naming_series = frappe.db.get_value('Student Admission', self.student_admission,
				'naming_series_for_student_applicant')
<<<<<<< HEAD
			print(naming_series)
=======
			print naming_series
>>>>>>> 95d706d57b6cac6113b64196e32dafd821e302b7

			if naming_series:
				self.naming_series = naming_series

		set_name_by_naming_series(self)

	def validate(self):
		self.title = " ".join(filter(None, [self.first_name, self.middle_name, self.last_name]))

	def on_update_after_submit(self):
		student = frappe.get_list("Student",  filters= {"student_applicant": self.name})
		if student:
			frappe.throw(_("Cannot change status as student {0} is linked with student application {1}").format(student[0].name, self.name))

	def on_payment_authorized(self, *args, **kwargs):
		self.db_set('paid', 1)
