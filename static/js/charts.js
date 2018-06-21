var staffed_ftes = 0, allocated_ftes = 0, caseload = 0;

d3.csv("../data/employees.csv", function(employees) {
	d3.csv("../data/offices.csv", function(offices) {					
			var office_dict = {}, employees_dict = {};
			var staffing = []
			offices.forEach(function(office) {
				office_dict[office.metro_office] = {
					marshals : [],
					staffed_ftes : 0,
					caseload : 0,
					allocated_ftes : parseInt(office.allocate_marshal_ftes)
				}
				$('#offices-filter').append("<li><a class='' tabindex='-1' href='#'><b>" + office.office_code + ":</b> " + office.metro_office + "</a></li>")
			});
		
			$('#offices-filter').append("<li role='separator' class='divider'></li>");
			$('#offices-filter').append("<li><a href='#'>Clear Filter</a></li>");
		
			employees.forEach(function(employee) {
				if (employee.role === "Marshal") {
					a = new Array(employee.case_ids);
					a.forEach(function(elem) {
						s = elem.split("],")
						if (s) {
							office_dict[employee.metro_office].caseload += s.length; 
						}
						s.forEach(function(t) {
							regexp = /H\d{3}/.exec(t);
							if (regexp) {
								office_dict[employee.metro_office].marshals.push({
									id : employee.pid,
									case : regexp[0],
									count : s.length
								});
							}
						});
					})
					office_dict[employee.metro_office].staffed_ftes += 1;
				}
			});
		
			var max = ["", 0];
			var min = ["", 10000];

			Object.keys(office_dict).forEach(function(k) {
				caseload_ratio = office_dict[k].caseload / office_dict[k].staffed_ftes
				staffed_ftes += office_dict[k]["staffed_ftes"];
				allocated_ftes += office_dict[k]["allocated_ftes"];
				caseload += office_dict[k]["caseload"];
				var value = [k, caseload_ratio];

				if (value[1] > max[1]) {
					min = max;
					max = value;
				}
				if (value[1] < min[1]) {
					min = value;
				}
			});

			marshals = [
				{ label : "vacant", value : 1 - (staffed_ftes / allocated_ftes), difference : allocated_ftes - staffed_ftes },
				{ label : "filled", value : staffed_ftes / allocated_ftes, difference : staffed_ftes }
			]

			// Marshals Staffing Donut Chart
			var width = 360;
			var height = 150;
			var radius = Math.min(width, height / 2);

			var color = d3.scaleOrdinal()
				.range(["#e74c3c", "#27ae60"]);

			var svg = d3.select("#staffing-chart")
				.append("g")
				.attr('transform', 'translate(' + (width / 2) + ', ' + (height / 2) + ')');

			var donutWidth = 35;

			var arc = d3.arc()
				.innerRadius(radius - donutWidth)
				.outerRadius(radius);

			var pie = d3.pie()
				.value(function(d) { return d.value})
				.sort(null)

			var path = svg.selectAll('path')
				.data(pie(marshals))
				.enter()
				.append('path')
				.attr('d', arc)
				.attr('id', function(d, i) { return "arcPath_" + i; })
				.attr('fill', function(d, i) {
					return color(d.data.label)
				});

			svg.append('rect')
				.attr('x', -160)
				.attr('y', -45)
				.attr('width', 15)
				.attr('height', 15)
				.attr("fill", "#e74c3c")

			svg.append('text')
				.attr('x', -140)
				.attr('y', -32)
				.html("Vacant")

			svg.append('rect')
				.attr('x', -160)
				.attr('y', -70)
				.attr('width', 15)
				.attr('height', 15)
				.attr("fill", "#27ae60")

			svg.append('text')
				.attr('x', -140)
				.attr('y', -57.5)
				.html("Staffed")

			svg.append("text")
				.attr('id', 'metric')
				.attr('x', 0)
				.attr('y', 10)
				.attr('text-anchor', 'middle')
				.html((marshals[1].value * 100).toFixed(0) + "%");		

			svg.append('text')
				.attr('x', -140)
				.attr('y', 55)
				.html("Staffed")

			svg.append('text')
				.attr('x', -135)
				.attr('y', 75)
				.attr('font-weight', 'bold')
				.attr('fill', '#27ae60')
				.attr('font-size', 20)
				.html(marshals[1].difference)

			svg.append('text')
				.attr('x', 90)
				.attr('y', 55)
				.html("Vacant")

			svg.append('text')
				.attr('x', 105)
				.attr('y', 75)
				.attr('font-weight', 'bold')
				.attr('fill', '#e74c3c')
				.attr('font-size', 20)
				.html(marshals[0].difference)
					
			d3.select("#total-cases")
				.html(caseload);
			d3.select("#caseload-ratio")
				.html((caseload / staffed_ftes).toFixed(2));
			d3.select("#highest-caseload-ratio")
				.html(max[0] + " (" + max[1] + ")");
			d3.select("#lowest-caseload-ratio")
				.html(min[0] + " (" + min[1] + ")");
	});
	
	d3.csv("../data/vehicles.csv", function(vehicles) {
		// Vehicle Type Inventory Donut Chart
		armored = 0;
		nonarmored = 0;
		vehicles.forEach(function(vehicle) {
			if (vehicle.armored === 'Yes') {
				armored += 1;
			} else {
				nonarmored += 1;
			}
		});

		vehicles_dataset = [
			{ label : "armored", value : armored },
			{ label : "nonarmored", value : nonarmored }
		]

		width = 360;
		height = 150;
		radius = Math.min(width, height / 2);

		var color = d3.scaleOrdinal(d3.schemeCategory10);
			//.range(["steelblue", "#000080"]);

		var svg = d3.select("#vehicles-chart")
			.append("g")
			.attr('transform', 'translate(' + (width / 2) + ', ' + (height / 2) + ')');

		var donutWidth = 35;

		var arc = d3.arc()
			.innerRadius(radius - donutWidth)
			.outerRadius(radius);

		var pie = d3.pie()
			.value(function(d) { return d.value})
			.sort(null)

		var path = svg.selectAll('path')
			.data(pie(vehicles_dataset))
			.enter()
			.append('path')
			.attr('d', arc)
			.attr('id', function(d, i) { return "arcPath_" + i; })
			.attr('fill', function(d, i) {
				return color(d.data.label)
			});

		svg.append('rect')
			.attr('x', -160)
			.attr('y', -45)
			.attr('width', 15)
			.attr('height', 15)
			.attr("fill", "rgb(31, 119, 180)")

		svg.append('text')
			.attr('x', -140)
			.attr('y', -32)
			.html("Armored")

		svg.append('rect')
			.attr('x', -160)
			.attr('y', -70)
			.attr('width', 15)
			.attr('height', 15)
			.attr("fill", "rgb(255, 127, 14)")

		svg.append('text')
			.attr('x', -140)
			.attr('y', -57.5)
			.html("Non-Armored")

		svg.append("text")
			.attr('id', 'metric')
			.attr('x', 0)
			.attr('y', 15)
			.attr('text-anchor', 'middle')

		svg.append('text')
			.attr('x', -160)
			.attr('y', 55)
			.html("Non-Armored")

		svg.append('text')
			.attr('x', -130)
			.attr('y', 75)
			.attr('font-weight', 'bold')
			.attr('font-size', 20)
			.attr('fill', 'rgb(255, 127, 14)')
			.html(vehicles_dataset[1].value)

		svg.append('text')
			.attr('x', 80)
			.attr('y', 55)
			.html("Armored")

		svg.append('text')
			.attr('x', 95)
			.attr('y', 75)
			.attr('font-weight', 'bold')
			.attr('fill', 'rgb(31, 119, 180)')
			.attr('font-size', 20)
			.html(vehicles_dataset[0].value)
	});
});