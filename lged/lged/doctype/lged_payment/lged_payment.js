// Copyright (c) 2025, Nazmul Hossain and contributors
// For license information, please see license.txt

frappe.ui.form.on("LGED Payment", {
	refresh(frm) {
        // enter your code here
	},
	bank(frm) {
		frm.events.set_row_value(frm);
	},
	project(frm) {
		frm.events.set_row_value(frm);
	},
	payment_date(frm) {
		frm.events.set_row_value(frm);
	},

    // set child row values when parent row values change
	set_row_value(frm) {
		(frm.doc.payment_details || []).forEach(row => {
			row.project = frm.doc.project;
			row.bank = frm.doc.bank;
			row.payment_date = frm.doc.payment_date;
		});
		frm.refresh_field("payment_details");
	}
});

frappe.ui.form.on('LGED Site Payment Items', {
	payment_details_add: function(frm, cdt, cdn) {
		calculate_total(frm);
	},
	amount: function(frm, cdt, cdn) {
		calculate_total(frm);
	},
	payment_details_remove: function(frm, cdt, cdn) {
		calculate_total(frm);
	},
});

// Utility function to calculate total
function calculate_total(frm) {
	let total = 0;
	(frm.doc.payment_details || []).forEach(row => {
		total += flt(row.amount); // Use flt to ensure it's a float
	});
	frm.set_value("total_amount", total);
	frm.refresh_field("total_amount");
}
