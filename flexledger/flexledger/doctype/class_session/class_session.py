# Copyright (c) 2026, R B Rohanth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utills import today

class ClassSession(Document):
	def validate(self):
		if(self.session_date > today()):
			frappe.throw("session_date cannot be in the past for a Draft record")
		if not self.expiry_date >= self.session_date and self.status != "Active":
			frappe.throw("The package's status should be Active and expiry_date must be greater than session_date")
		else:
			frappe.msgprint("this works")
			frappe.msgprint(today())
		if not self.credits_remaining >= self.credits_charged:
			frappe.throw("A package's credits_remaining should be greater than credits_charged")
			
