var dataset;
d3.json("./json/d3datasets_v1.json", function(error, data) {
	dataset = data[0];
	updateData("0", "default");
});

function updateData(label, key) {
	d3.select("#support-strength").selectAll("svg").remove();
	d3.select("#vehicles-inventory").selectAll("svg").remove();
	switch(key) {
		case "default":
			$(".snapshot").html("<em>National</em>");
			d3.select("#support-strength")
				.datum(dataset[0].staffing.total)
				.call(donutChart()
					.width(360)
					.height(175)
					.cornerRadius(3)
					.padAngle(0.015)
					.variable('value')
					.category('label')
					.color(d3.scaleOrdinal().range(["#27ae60", "#e74c3c"]))
					.label(["Vacant", "Staffed"])
					.legendValues([dataset[0].staffing.total[0].value, dataset[0].staffing.total[1].value])
					.middleLabel(true));

			d3.select("#vehicles-inventory")
				.datum(dataset[0].vehicles)
				.call(donutChart()
					.width(360)
					.height(175)
					.cornerRadius(3)
					.padAngle(0.015)
					.variable('value')
					.category('label')
					.color(d3.scaleOrdinal().range(["rgb(255, 127, 14)", "rgb(31, 119, 180)"]))
					.label(["Not Issued", "Issued"])
					.legendValues([dataset[0].vehicles[0].value, dataset[0].vehicles[1].value])
					.middleLabel(false))
				.style("display", "block");
			
//			d3.select("#firearms-inventory")
//				.datum(dataset[0].firearms)
//				.call(donutChart()
//					.width(360)
//					.height(175)
//					.cornerRadius(3)
//					.padAngle(0.015)
//					.variable('value')
//					.category('label')
//					.color(d3.scaleOrdinal().range(["rgb(255, 127, 14)", "rgb(31, 119, 180)"]))
//					.label(["Not Issued", "Issued"])
//					.legendValues([dataset[0].firearms[0].value, dataset[0].firearms[1].value])
//					.middleLabel(false))
//				.style("display", "none");
			
			$("#caseload").html(dataset[0].clients.total);
			$("#caseload-average").html(dataset[0].clients.ratio.total.toFixed(2));
			$("#highest-caseload-average").html("Highest: <b>" + dataset[0].clients.highest_ratio.total.office + ", #" + dataset[0].clients.highest_ratio.total.office_code + " (" + (dataset[0].clients.highest_ratio.total.ratio).toFixed(2) + ")</b>");
			$("#lowest-caseload-average").html("Lowest: <b>" + dataset[0].clients.lowest_ratio.total.office + ", #" + dataset[0].clients.lowest_ratio.total.office_code + " (" + (dataset[0].clients.lowest_ratio.total.ratio).toFixed(2) + ")</b>");
			break;
		default:
			$(".snapshot").html("<em>" + label + "</em>");
			d3.select("#support-strength")
				.datum(dataset[key].staffing.total)
				.call(donutChart()
					.width(360)
					.height(175)
					.cornerRadius(3)
					.padAngle(0.015)
					.variable('value')
					.category('label')
					.color(d3.scaleOrdinal().range(["#27ae60", "#e74c3c"]))
					.label(["Vacant", "Staffed"])
					.legendValues([dataset[key].staffing.total[0].value, dataset[key].staffing.total[1].value])
					.middleLabel(true)
				);

			d3.select("#vehicles-inventory")
				.datum(dataset[key].vehicles)
				.call(donutChart()
					.width(360)
					.height(175)
					.cornerRadius(3)
					.padAngle(0.015)
					.variable('value')
					.category('label')
					.color(d3.scaleOrdinal().range(["rgb(255, 127, 14)", "rgb(31, 119, 180)"]))
					.label(["Not Issued", "Issued"])
					.legendValues([dataset[key].vehicles[0].value, dataset[key].vehicles[1].value])
					.middleLabel(false))
				.style("display", "block");
			
//			d3.select("#firearms-inventory")
//				.datum(dataset[0].firearms)
//				.call(donutChart()
//					.width(360)
//					.height(175)
//					.cornerRadius(3)
//					.padAngle(0.015)
//					.variable('value')
//					.category('label')
//					.color(d3.scaleOrdinal().range(["rgb(255, 127, 14)", "rgb(31, 119, 180)"]))
//					.label(["Not Issued", "Issued"])
//					.legendValues([dataset[0].firearms[0].value, dataset[0].firearms[1].value])
//					.middleLabel(false))
			
			d3.select("#firearms-inventory").style("display", "none");

			$("#caseload").html(dataset[key].clients.total);
			$("#caseload-average").html(dataset[key].clients.ratio.total.toFixed(2));
			$("#highest-caseload-average").html("Highest: <b>" + dataset[key].clients.highest_ratio.total.office + ", #" + dataset[0].clients.highest_ratio.total.office_code + " (" + (dataset[key].clients.highest_ratio.total.ratio).toFixed(2) + ")</b>");
			$("#lowest-caseload-average").html("Lowest: <b>" + dataset[key].clients.lowest_ratio.total.office + ", #" + dataset[0].clients.lowest_ratio.total.office_code + " (" + (dataset[key].clients.lowest_ratio.total.ratio).toFixed(2) + ")</b>");
			break;
	}
}

function donutChart() {
	var data = [],
		width,
		height,
		margin = { top : 10, right : 10, bottom : 10, left : 10 },
		color,
		variable,
		category,
		padAngle,
		transTime,
		updateData,
		label,
		legendValues,
		cornerRadius,
		middleLabel;
		
	function chart(selection) {
		selection.each(function() {
			// generate chart
			// set up constructors for making donut
			var radius = Math.min(width, height) / 2;
			
			// creates a new pie generator
			var pie = d3.pie()
				.value(function(d) { return d[variable] })
				.sort(null);
			
			// construct arc generator
			// used to make donut
			// difference between outer and inner radius dictates donut thickness
			var arc = d3.arc()
				.outerRadius(radius * 0.8)
				.innerRadius(radius * 0.5)
				.cornerRadius(cornerRadius)
				.padAngle(padAngle);
			
			// append the svg object to the selection
			var svg = selection.append('svg')
				.attr('width', width)
				.attr('height', height)
				.attr('class', 'donut-chart')
				.append('g')
				.attr('transform', 'translate(' + width / 2 + ',' + height / 2 + ')');
			
			// g elements to keep elements within svg modular
			svg.append('g').attr('class', 'slices');
			svg.append('g').attr('class', 'labelName');
			svg.append('g').attr('class', 'lines');
			
			if (middleLabel) {
				svg.append("text")
					.attr('id', 'metric')
					.attr('x', 0)
					.attr('y', 10)
					.attr('text-anchor', 'middle')
					.html(((legendValues[0] / (legendValues[0] + legendValues[1])).toPrecision() * 100).toFixed(0) + "%")
				n = new Number(legendValues[1] / (legendValues[0] + legendValues[1]));
			}
						
			svg.append('rect')
				.attr('x', -160)
				.attr('y', -65)
				.attr('width', 15)
				.attr('height', 15)
				.attr("fill", color.range()[1])
			
			svg.append('text')
				.attr('x', -140)
				.attr('y', -52.5)
				.html(label[0])

			svg.append('rect')
				.attr('x', -160)
				.attr('y', -85)
				.attr('width', 15)
				.attr('height', 15)
				.attr("fill", color.range()[0])

			svg.append('text')
				.attr('x', -140)
				.attr('y', -72.5)
				.html(label[1])
			
			//--------------------

			svg.append('text')
				.attr('x', 100)
				.attr('y', 25)
				.attr('font-weight', 'bold')
				.attr('font-size', 25)
				.attr('fill', color.range()[0])
				.attr('text-anchor', 'start')
				.html(legendValues[0]);

			svg.append('text')
				.attr('x', -100)
				.attr('y', 25)
				.attr('font-weight', 'bold')
				.attr('fill', color.range()[1])
				.attr('font-size', 25)
				.attr('text-anchor', 'end')
				.html(legendValues[1]);
			
			// add and color the donut slices
			var path = svg.select('.slices')
				.selectAll('path')
				.data(pie)
				.enter()
				.append('path')
				.attr('fill', function(d) { return color(d.data[category])})
				.attr('d', arc)
		});
	}
	
	// getter and setter functions
	chart.data = function(value) {
		if (!arguments.length) return data;
		data = value;
		return chart;
	}
	chart.width = function(value) {
		if (!arguments.length) return width;
		width = value;
		return chart;
	}
	chart.height = function(value) {
		if (!arguments.length) return height;
		height = value;
		return chart;
	}
	chart.margin = function(value) {
		if (!arguments.length) return margin;
		margin = value;
		return chart;
	}
	chart.radius = function(value) {
		if (!arguments.length) return radius;
		radius = value;
		return chart;
	}
	chart.padAngle = function(value) {
		if (!arguments.length) return padAngle;
		padAngle = value;
		return chart;
	}
	chart.cornerRadius = function(value) {
		if (!arguments.length) return cornerRadius;
		cornerRadius = value;
		return chart;
	}
	chart.color = function(value) {
		if (!arguments.length) return color;
		color = value;
		return chart;
	}
	chart.variable = function(value) {
		if (!arguments.length) return variable;
		variable = value;
		return chart;
	}
	chart.category = function(value) {
		if (!arguments.length) return category;
		category = value;
		return chart;
	}
	chart.label = function(value) {
		if (!arguments.length) return label;
		label = value;
		return chart;
	}
	chart.legendValues = function(value) {
		if (!arguments.length) return legendValues;
		legendValues = value;
		return chart;
	}
	chart.middleLabel = function(value) {
		if (!arguments.length) return middleLabel;
		middleLabel = value;
		return chart;
	}
	return chart;
}

function precisionRound(number, precision) {
  var factor = Math.pow(10, precision);
  return Math.round(number * factor) / factor;
}