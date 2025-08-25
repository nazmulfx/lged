# Copyright (c) 2025, Nazmul Hossain and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    
    return columns, data

def get_data(filters):
    # return [
    #     {
    #         "project": "Project A",
    #         "payment_date": "2023-01-01",
    #         "work_details": "Excavation",
    #         "amount": 1000.00,
    #         "bank": "Bank A"
    #     }
    # ]
    condition = {}
    condition["docstatus"] = 1
    if filters.get("to_date") and filters.get("from_date"):
        condition["payment_date"] = ["between", [filters.get('from_date'), filters.get('to_date')]]
    if filters.get("project"):
        condition["project"] = filters.get("project")
    if filters.get("bank_account"):
        condition["bank"] = filters.get("bank_account")
    # print("Condition:", condition)
        
    
    
    data = []
    
    payment_entries = frappe.get_list("LGED Payment", filters=condition, fields=["name"])
    # print(payment_entries)
    
    for payment_entry in payment_entries:
        # print("Payment Entry:", payment_entry)
        Payemnt_doc = frappe.get_doc("LGED Payment", payment_entry.name)
        for item in Payemnt_doc.payment_details:
            item_data = {
                "project": Payemnt_doc.get("project"),
                "payment_invoice": Payemnt_doc.get("name"),
                "payment_date": Payemnt_doc.get("payment_date"),
                "work_details": item.get("details"),
                "amount": item.get("amount"),
                "bank": item.get("bank")
            }
            data.append(item_data)
    
    # ['date', 'between', ['2020-04-01', '2021-03-31']]
    return data

def get_columns():
    return [
        {
            "fieldname": "payment_invoice",
            "label": "Payment Invoice",
            "fieldtype": "Link",
            "options": "LGED Payment",
            "width": 200
        },
        {
            "fieldname": "project",
            "label": "Project",
            "fieldtype": "Link",
            "options": "LGED Project",
            "width": 200
        },
        {
            "fieldname": "payment_date",
            "label": "Payment Date",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "fieldname": "work_details",
            "label": "Work Details",
            "fieldtype": "Data",
            "width": 500
        },
        {
            "fieldname": "amount",
            "label": "Amount",
            "fieldtype": "Currency",
            "options": "currency",
            "width": 120
        },
        {
            "fieldname": "bank",
            "label": "Bank",
            "fieldtype": "Link",
            "options": "Bank Account",
        }
    ]
    
