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

	def before_submit(self):
		if not self.status == "Completed":
			frappe.throw("the session isn't completed yet , thus wait till it is completed")

	def on_submit(self):
		pass

	def on_trash(self):
		if not self.status == "Cancelled" or not self.status == "Draft":
			frappe.throw("This document is neither a Draft nor a Cancelled Document , thus you can't delete this")

	def on_update(self):
		self.save()
