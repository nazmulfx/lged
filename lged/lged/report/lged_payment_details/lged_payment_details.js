// Copyright (c) 2025, Nazmul Hossain and contributors
// For license information, please see license.txt

frappe.query_reports["LGED Payment Details"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"reqd": 1,
			"default": frappe.datetime.add_months(frappe.datetime.get_today(), -1),
		},
		{
			"fieldname": "to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"reqd": 1,
			"default": frappe.datetime.get_today(),
		},
		{
			"fieldname": "project",
			"label": __("Project"),
			"fieldtype": "Link",
			"options": "LGED Project",
		},
		{
			"fieldname": "bank_account",
			"label": __("Bank Account"),
			"fieldtype": "Link",
			"options": "Bank Account",
		}
		
	]
};
