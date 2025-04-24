# Copyright (c) 2025, Nazmul Hossain and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class LGEDProject(Document):
    def on_update(self):
        """This function is called when the document is updated."""

        if self.total_cost and self.project_budget and self.bill_received_amount:
            if self.total_cost > self.project_budget:
                self.bill_status = 'Over Budget'
            elif self.bill_received_amount < self.project_budget:
                self.bill_status = 'Bill Due'
            elif self.bill_received_amount == self.project_budget:
                self.bill_status = 'Bill Received'
            
        
        


