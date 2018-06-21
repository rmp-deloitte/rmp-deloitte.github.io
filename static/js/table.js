function format (table, d) {
	var content;
	switch(table) {
		case "office":
			content = "<tr><td><b>Bodyguard FTEs (Staffed / Allocated):</b>&nbsp;&nbsp;" + d.staffed_bodyguard_ftes +  " / " + d.allocated_bodyguard_ftes + "</td><td>";
			content += "<tr><td><b>Administrator FTEs (Staffed / Allocated):</b>&nbsp;&nbsp;" + d.staffed_administrator_ftes +  " / " + d.allocated_administrator_ftes + "</td><td>";
			content += "<tr><td><b>Vehicles (Issued / Not Issued):</b>&nbsp;&nbsp;" + d.staffed_bodyguard_ftes +  " / " + d.vacant_bodyguard_ftes + "</td><td>";
			content += "<tr><td><b>Total Armored Vehicles:</b>&nbsp;&nbsp;" + d.total_armored_vehicles + "</td><td>";
			content += "<tr><td><b>Firearms (Issued / Not Issued):</b>&nbsp;&nbsp;" + d.staffed_bodyguard_ftes +  " / " + d.vacant_bodyguard_ftes + "</td><td>";
			content += "<hr\>"
			content += '<table class="table table-striped table-bordered" cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;">' + 
					'<thead>' +
						'<tr><th>Employee ID</th><th>Last Name</th><th>First Name</th><th>Title</th><th>Assigned Client</th><th>Issued Vehicel</th><th>Issued Firearm</th></tr></thead>';// <th>Title</th><th>Years</th><th>Cases</th><th>Vehicle</th></tr></thead>';

			d.bodyguards.forEach(function(b) {
				content += "<tr><td>" + b.employee_id + "</td><td>" + b.last_name + "</td><td>" + b.first_name + "</td><td>" + b.title + "</td><td><a href='#'>" + b.assigned_client + "</a><td><a href='#'>" + b.vehicle + "</a><td><a href='#'>" + b.firearm + "</a></td></tr>";// + b.title + "</td><td>" + k.years + "</td><td>" + k.cases + "</td><td>" + k.vehicle +"</td></tr>";
			});
			
			d.administrators.forEach(function(a) {
				content += "<tr><td>" + a.employee_id + "</td><td>" + a.last_name + "</td><td>" + a.first_name + "</td><td>" + a.title + "</td><td><a href='#'>" + a.assigned_client + "</a><td><a href='#'>" + a.vehicle + "</a><td><a href='#'>" + a.firearm + "</a></td></tr>";
			});
			
			content += "</table>";
				
			return content;
			break;
		case "staff":
			console.log(d);
			content = "<tr><td><b>Issued Vehicle:</b>&nbsp;&nbsp;<a href='#'>" + d.vehicle + "</a></td><td>";
			content += "<tr><td><b>Issued Firearm:</b>&nbsp;&nbsp;<a href='#'>" + d.firearm + "</a></td><td>";
			content += "<tr><td><b>Client Assignments:</b>&nbsp;&nbsp;" + d.assigned_clients + "</td><td>";
			content += "<tr><td><b>Office Number:</b>&nbsp;&nbsp;TBD</td><td>";
			content += "<tr><td><b>Phone Number:</b>&nbsp;&nbsp;TBD</td><td>";
			return content;
			break;
		case "clients":			
			content = "<tr><td><b>Mobile Phone No.:</b>&nbsp;&nbsp;" + d.mobile_phone + "</td><td>";
			content += "<tr><td><b>Home Phone No.:</b>&nbsp;&nbsp;" + d.home_phone + "</td><td>";			
			content += "<tr><td><b>Email:</b>&nbsp;&nbsp;" + d.email + "</td><td>";			
			content += "<tr><td><b>Assigned Office:</b>&nbsp;&nbsp;<a href='#'>" + d.assigned_office + " (#" + d.assigned_office_code + ")" + "</a></td><td>";
			content += "<tr><td><b>Assigned Bodyguard:</b>&nbsp;&nbsp;<a href='#'>" + d.assigned_bodyguard + "</a></td><td>";
			return content;
		default:
			break;
	}
}

$(document).ready(function() {
	var office_table = $('#office-table').DataTable({
		"ajax" : "./json/offices_table_v1.json",
		"columnDefs" : [
			{ "width" : "5%", "targets" : 0},
		],
		"columns": [
			{
				"className" : 'details-control',
				"orderable" : false,
				"data" : null,
				"defaultContent" : ''
			},
			{ "data" : "office_code" },
			{ "data" : "office" },
			{ "data" : "state" },
			{ "data" : "region" },
			{ "data" : "allocated_ftes" },
			{ "data" : "staffed_ftes"},
			{ "data" : "total_vehicles" },
			{ "data" : "total_firearms" },
			{ "data" : "total_clients" },
		],
		"order" : [[1, 'asc']],
		"paging" : true,
		"scrollY" : "300px",
		"scrollX" : "auto",
		"scrollCollapse": true
	});

	var staff_table = $('#staff-table').DataTable({
		"ajax" : "./json/staff_table_v1.json",
		"columnDefs" : [
			{ "width" : "5%", "targets" : 0}
		],
		"columns": [
			{
				"className" : 'details-control',
				"orderable" : false,
				"data" : null,
				"defaultContent" : ''
			},
			{ "data" : "employee_id" },
			{ "data" : "last_name" },
			{ "data" : "first_name" },
			{ "data" : "title" },
			{ "data" : "office_code"},
			{ "data" : "office" },
			{ "data" : "state" },
			{ "data" : "region" },
		],
		"order" : [[1, 'asc']],
		"paging" : true,
		"scrollY" : "300px",
		"scrollX" : "auto",
		"scrollCollapse": true
	});
	
	var vehicle_table = $('#vehicle-table').DataTable({
		"ajax" : "./json/vehicles_table_v1.json",
		"columnDefs" : [
			{ "width" : "5%", "targets" : 0},
			{ "targets" : [0], visible : false }
		],
		"columns": [
			{
				"className" : 'details-control',
				"orderable" : false,
				"data" : null,
				"defaultContent" : ''
			},
			{ "data" : "office_code"},
			{ "data" : "office" },
			{ "data" : "state" },
			{ "data" : "region" },
			{ "data" : "vin" },
			{ "data" : "make" },
			{ "data" : "armored" },
			{ "data" : "assigned_to" },
		],
		"order" : [[1, 'asc']],
		"paging" : true,
		"scrollY" : "300px",
		"scrollX" : "auto",
		"scrollCollapse": true
	});

	var firearm_table = $('#firearm-table').DataTable({
		"ajax" : "./json/firearms_table_v1.json",
		"columnDefs" : [
			{ "width" : "5%", "targets" : 0},
			{ "targets" : [0], visible : false }
		],
		"columns": [
			{
				"className" : 'details-control',
				"orderable" : false,
				"data" : null,
				"defaultContent" : ''
			},
			{ "data" : "office_code"},
			{ "data" : "office" },
			{ "data" : "state" },
			{ "data" : "region" },
			{ "data" : "serial_no" },
			{ "data" : "model" },
			{ "data" : "assigned_to" },
		],
		"order" : [[1, 'asc']],
		"paging" : true,
		"scrollY" : "300px",
		"scrollX" : "auto",
		"scrollCollapse": true
	});

	var client_table = $('#client-table').DataTable({
		"ajax" : "./json/clients_table_v1.json",
		"columnDefs" : [
			{ "width" : "5%", "targets" : 0},
		],
		"columns": [
			{
				"className" : 'details-control',
				"orderable" : false,
				"data" : null,
				"defaultContent" : ''
			},
			{ "data" : "client_id" },
			{ "data" : "last_name" },
			{ "data" : "first_name" },
			{ "data" : "address" },
			{ "data" : "city"},
			{ "data" : "state" },
			{ "data" : "zipcode" },
			{ "data" : "region" },
			{ "data" : "assigned_office" },
		],
		"order" : [[1, 'asc']],
		"paging" : true,
		"scrollY" : "300px",
		"scrollX" : "auto",
		"scrollCollapse": true
	});
	
	$('a[data-toggle="tab"]').on('shown.bs.tab', function(e){
		$($.fn.dataTable.tables(true)).DataTable()
			.columns.adjust();
	});
	
	$('#office-table tbody').on('click', 'td.details-control', function() {
		var tr = $(this).closest('tr');
		var row = office_table.row(tr);
		if (row.child.isShown()) {
			row.child.hide();
			tr.removeClass('shown');
		} else {
			row.child(format("office", row.data()) ).show();
			tr.addClass('shown');
		}
	});
	
	$('#staff-table tbody').on('click', 'td.details-control', function() {
		var tr = $(this).closest('tr');
		var row = staff_table.row(tr);
		if (row.child.isShown()) {
			row.child.hide();
			tr.removeClass('shown');
		} else {
			row.child(format("staff", row.data()) ).show();
			tr.addClass('shown');
		}
	});
	
	$('#client-table tbody').on('click', 'td.details-control', function() {
		var tr = $(this).closest('tr');
		var row = client_table.row(tr);
		if (row.child.isShown()) {
			row.child.hide();
			tr.removeClass('shown');
		} else {
			row.child(format("clients", row.data()) ).show();
			tr.addClass('shown');
		}
	});
});