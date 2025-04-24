# Copyright (c) 2025, Nazmul Hossain and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LGEDBillEntry(Document):
    def on_submit(self):
        self.update_bill_amount()

    def on_cancel(self):
        self.retrive_bill_amount()
    
    def update_bill_amount(self):
        # Logic to update the bank account balance
        bank_account = frappe.get_doc("Bank Account", self.bill_received_bank_account)
        bank_account.current_balance += self.bill_amount
        bank_account.save()
        
        # Logic to update the bill received amount in Project
        project = frappe.get_doc("LGED Project", self.project)
        project.bill_received_amount += self.bill_amount
        project.save()
        
        frappe.db.commit()
        frappe.msgprint(f"Bank Account: {bank_account.bank_account_name} Added {self.bill_amount}TK <br/> Project Bill Received Amount updated.", "Updated Project & Bank Account")
        
    def retrive_bill_amount(self):
        # Logic to update the bank account balance
        bank_account = frappe.get_doc("Bank Account", self.bill_received_bank_account)
        bank_account.current_balance -= self.bill_amount
        bank_account.save()
        
        # Logic to update the bill received amount in Project
        project = frappe.get_doc("LGED Project", self.project)
        project.bill_received_amount -= self.bill_amount
        project.save()
        
        frappe.db.commit()
        frappe.msgprint(f"Bank Account: {bank_account.bank_account_name} Added {self.bill_amount}TK <br/> Project Bill Received Amount updated.", "Updated Project & Bank Account")
        

