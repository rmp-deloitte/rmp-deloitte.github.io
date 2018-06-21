$(document).ready(function(){
	$("#Filters-toggle").click(function() {
		$("#Filters-dashboard").toggle(function() {
			$(".filters-toggle").toggleClass("glyphicon-eye-close");
		});
	});
	$("#Filters-btn").click(function() {
		$("#Filters-navbar").toggle(function() {
			$(".filters-navbar-toggle").toggleClass("glyphicon-filter");
		});
	});
	$("#Legend-toggle").click(function() {
		$(".legend-svg").toggle("slow");
		$(".legend-toggle").toggleClass("glyphicon-eye-close");
	});
	
	$("#Layerslist-toggle").click(function() {
		$(".layerslist-svg").toggle("slow");
		$(".layerslist-toggle").toggleClass("glyphicon-eye-close");
	});
	
//	$("#Inventory-toggle").click(function() {		
//		$("#firearms-inventory").toggle();
//		$("#vehicles-inventory").toggle();
//		
//		var title = $("#vehicles-inventory").css("display") === "none" ? "Armory Inventory" : "Vehicle Inventory";
//				
//		$("#inventory").html("<b>" + title + "</b>");
//	});
	
	$("#region-selector").change(function(evt) {
		var region = $(this).val();
	
		$(this).children().get()[0].innerHTML = "Select Region...";
		
		$("#state-selector").val("0");
		$("#state-selector").children().get()[0].innerHTML = "Select State...";
		
		$("#office-selector").val("0");
		$("#office-selector").children().get()[0].innerHTML = "Select State...";
		
		
		if (parseInt(region)) {
			$(this).children().get()[0].innerHTML = "[Clear Filter]";

			$("#state-selector").children().get().forEach(function(opt) {
				opt.hidden = opt.dataset.regionId !== region && parseInt(opt.value) ? true : false;
			});
			$("#office-selector").children().get().forEach(function(opt) {
				opt.hidden = opt.dataset.regionId !== region && parseInt(opt.value) ? true : false;
			});
			
			updateData(evt.target.selectedOptions[0].dataset.region + " Region", region);
			
			$("#office-table").DataTable()
				.columns(4)
				.search(evt.target.selectedOptions[0].dataset.region, true, false).draw();
	
			$("#staff-table").DataTable()
				.columns(7)
				.search(evt.target.selectedOptions[0].dataset.region, true, false).draw();

			$("#vehicle-table").DataTable()
				.columns(4)
				.search(evt.target.selectedOptions[0].dataset.region, true, false).draw();			
			
			$("#firearm-table").DataTable()
				.columns(4)
				.search(evt.target.selectedOptions[0].dataset.region, true, false).draw();
			
			$("#client-table").DataTable()
				.columns(8)
				.search(evt.target.selectedOptions[0].dataset.region, true, false).draw();

		} else {
			$(this).children().get()[0].innerHTML = "Select Region...";
			
			$("#state-selector").val(region);
			$("#state-selector").children().get()[0].innerHTML = "Select State...";
			$("#state-selector").children().get().forEach(function(opt) {
				opt.hidden = false;
			});
			
			$("#office-selector").val(region);
			$("#office-selector").children().get()[0].innerHTML = "Select Office...";
			$("#office-selector").children().get().forEach(function(opt) {
				opt.hidden = false;
			});	

			updateData("National", region);
			
			$("#office-table").DataTable()
				.columns([2, 3, 4])
				.search('', true, false).draw();
			
			$("#state-table").DataTable()
				.columns([5, 6, 7])
				.search('', true, false).draw();
			
			$("#vehicle-table").DataTable()
				.columns([2, 3, 4])
				.search('', true, false).draw();
			
			$("#firearm-table").DataTable()
				.columns([2, 3, 4])
				.search('', true, false).draw();
			
			$("#client-table").DataTable()
				.columns([6, 8, 9])
				.search('', true, false).draw();
		}
	});
	
	$("#state-selector").change(function(evt) {
		var state = $(this).val();
		$(this).children().get()[0].innerHTML = "[Clear Filter]";
		$("#office-selector").children().get()[0].innerHTML = "Select Office...";
		$("#office-selector").val("0");
		
		if (parseInt(state)) {
			$("#region-selector").val(evt.target.selectedOptions[0].dataset.regionId);
			$("#office-selector").children().get().forEach(function(opt) {
				opt.hidden = opt.dataset.fips !== state && parseInt(opt.value) ? true : false;
			});
		
			updateData(evt.target.selectedOptions[0].dataset.state, state);

			$("#office-table").DataTable()
				.columns(3)
				.search(evt.target.selectedOptions[0].dataset.state, true, false).draw();			
			
			$("#staff-table").DataTable()
				.columns(6)
				.search(evt.target.selectedOptions[0].dataset.state, true, false).draw();			

			$("#vehicle-table").DataTable()
				.columns(3)
				.search(evt.target.selectedOptions[0].dataset.state, true, false).draw();					
			
			$("#firearm-table").DataTable()
				.columns(3)
				.search(evt.target.selectedOptions[0].dataset.state, true, false).draw();					

			$("#client-table").DataTable()
				.columns(6)
				.search(evt.target.selectedOptions[0].dataset.state, true, false).draw();					
			
			//zoomTo(evt.target.selectedOptions[0].dataset.fips);
		} else {
			$(this).children().get()[0].innerHTML = "Select State...";
			$("#region-selector").val(state);
			$("#region-selector").children().get()[0].innerHTML = "Select Region...";
			
			$("#office-selector").val(state);
			$("#office-selector").children().get()[0].innerHTML = "Select Office...";
			$("#office-selector").children().get().forEach(function(opt) {
				opt.hidden = false;
			});
			
			$("#state-selector").children().get().forEach(function(opt) {
				opt.hidden = false;
			});
			
			$("#office-selector").children().get().forEach(function(opt) {
				opt.hidden = false;
			});
			
			updateData("National", state);
			
			$("#office-table").DataTable()
				.columns([2, 3, 4])
				.search('', true, false).draw();
			
			$("#staff-table").DataTable()
				.columns([5, 6, 7])
				.search('', true, false).draw();

			$("#vehicle-table").DataTable()
				.columns([2, 3, 4])
				.search('', true, false).draw();

			$("#firearm-table").DataTable()
				.columns([2, 3, 4])
				.search('', true, false).draw();
			
			$("#client-table").DataTable()
				.columns([6, 8, 9])
				.search('', true, false).draw();
		}
	});
	
	$("#office-selector").change(function(evt) {
		var office = $(this).val();
		$(this).children().get()[0].innerHTML = "[Clear Filter]";
		if (parseInt(office)) {
			$("#region-selector").val(evt.target.selectedOptions[0].dataset.regionId);
			$("#state-selector").val(evt.target.selectedOptions[0].dataset.fips);
			var label = "Office #" + evt.target.selectedOptions[0].dataset.officeCode + ": " + evt.target.selectedOptions[0].dataset.office;
			
			updateData(label, office);

			$("#office-table").DataTable()
				.columns(2)
				.search(evt.target.selectedOptions[0].dataset.office, true, false).draw();

			$("#staff-table").DataTable()
				.columns(5)
				.search(evt.target.selectedOptions[0].dataset.office, true, false).draw();			
			
			$("#vehicle-table").DataTable()
				.columns(2)
				.search(evt.target.selectedOptions[0].dataset.office, true, false).draw();			
		
			$("#firearm-table").DataTable()
				.columns(2)
				.search(evt.target.selectedOptions[0].dataset.office, true, false).draw();			

			$("#client-table").DataTable()
				.columns(9)
				.search(evt.target.selectedOptions[0].dataset.office, true, false).draw();			
		} else {
			$(this).children().get()[0].innerHTML = "Select Office...";
			
			$("#region-selector").val(office);
			$("#region-selector").children().get()[0].innerHTML = "Select Region...";
			
			$("#state-selector").val(office);
			$("#state-selector").children().get([0]).innerHTML = "Select State...";
			
			$("#state-selector").children().get().forEach(function(opt) {
				opt.hidden = false;
			});
			
			$("#office-selector").children().get().forEach(function(opt) {
				opt.hidden = false;
			});
			
			updateData("National", office);
			
			$("#office-table").DataTable()
				.columns([2, 3, 4])
				.search('', true, false).draw();
			
			$("#staff-table").DataTable()
				.columns([5, 6, 7])
				.search('', true, false).draw();
			
			$("#vehicle-table").DataTable()
				.columns([2, 3, 4])
				.search('', true, false).draw();

			$("#firearm-table").DataTable()
				.columns([2, 3, 4])
				.search('', true, false).draw();

			$("#client-table").DataTable()
				.columns([6, 8, 9])
				.search('', true, false).draw();
		
		}
	});
});