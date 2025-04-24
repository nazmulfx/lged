# Copyright (c) 2025, Nazmul Hossain and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LGEDPayment(Document):
	def on_submit(self):
		self.update_total_payment_amount()
  
	def on_cancel(self):
		self.retrive_total_payment_amount()
	
	def update_total_payment_amount(self):
		# update/add payment/cost on Project
		project = frappe.get_doc("LGED Project", self.project)
		project.total_cost += self.total_amount
		project.save()
  
		# update on Bank Account
		bank_account = frappe.get_doc("Bank Account", self.bank)
		bank_account.current_balance -= self.total_amount
		bank_account.save()

		frappe.db.commit()
		frappe.msgprint(f"Total payment amount {self.total_amount} TK updated successfully.", "Bank Account & Project Cost updated")
	
	def retrive_total_payment_amount(self):
		# update/add payment/cost on Project
		project = frappe.get_doc("LGED Project", self.project)
		project.total_cost -= self.total_amount
		project.save()
  
		# update on Bank Account
		bank_account = frappe.get_doc("Bank Account", self.bank)
		bank_account.current_balance += self.total_amount
		bank_account.save()

		frappe.db.commit()
		frappe.msgprint(f"Total payment amount {self.total_amount} TK updated successfully.", "Bank Account & Project Cost restored")
	
  
	
		