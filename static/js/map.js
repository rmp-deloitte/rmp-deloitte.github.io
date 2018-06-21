var margin = { top : 20, right : 5, bottom : 5, left : 0 },
    width = $("#Map-Container").width(),
    height = $("#Map-Container").height(),
    centered,
    projection = d3.geoAlbersUsa().translate([width / 2, height / 2]).scale([width]),
    path = d3.geoPath().projection(projection);

const svg = d3.select("#Map")
    .append("svg")
    .attr("id", "Map-SVG")
    .attr("width", width)
    .attr("height", height);

svg.append("rect")
    .attr("id", "Map-Canvas")
    .attr('fill', 'none')
    .attr("width", width)
    .attr("height", height);

const g = svg.append('g')

d3.json("../static/json/us.json", function(error, us) {
    if (error) throw error;

    var stabbv = {
        1 : 'AL', 2 : 'AK', 4 : 'AZ', 5 :  'AR', 6 : 'CA', 8 : 'CO', 9 : 'CT',
        10 : 'DE', 11 : 'DC', 12 : 'FL', 13 : 'GA', 15 : 'HI', 16 : 'ID',
        17 : 'IL', 18 : 'IN', 19 : 'IA', 20 : 'KS', 21 : 'LA', 22 : 'LA',
        23 : 'ME', 24 : 'MD', 25 : 'MA', 26 : 'MI', 27 : 'MN', 28 : 'MS',
        29 : 'MO', 30 : 'MT', 31 : 'NE', 32 : 'NV', 33 : 'NH', 34 : 'NJ',
        35 : 'NM', 36 : 'NY', 37 : 'NC', 38 : 'ND', 39 : 'OH', 40 : 'OK',
        41 : 'OR', 42 : 'PA', 44 : 'RI', 45 : 'SC', 46 : 'SD', 47 : 'TN',
        48 : 'TX', 49 : 'UT', 50 : 'VT', 51 : 'VA', 53 : 'WA', 54 : 'WV',
        55 : 'WI', 56 : 'WY', 72 : 'PR' }

    g.append("g")
        .attr("id", "states")
        .selectAll("path")
        .data(topojson.feature(us, us.objects.states).features)
        .enter()
        .append("path")
        .attr("d", path)
        .attr("fill", "none")
        .attr("stroke", "#333333")
        .attr("stroke-width", 3)
        .attr("class", "state");

    g.selectAll("text")
        .data(topojson.feature(us, us.objects.states).features)
        .enter()
        .append("text")
        .attr('font-weight', 600)
        .text(function(d) {
            return stabbv[d.id];
        })
        .attr("class", "state-name")
        .attr('style', 'text-shadow: -1px -1px white, -1px 1px white, 1px 1px white, 1px -1px white, -1px 0 white, 0 1px white, 1px 0 white, 0 -1px white')
        .attr("x", function(d) {
            switch(d.id) {
                case 72:
                case 78:
                    break;
                default:
                    return path.centroid(d)[0];
                    break;
            }
        })
        .attr("y", function(d) {
            switch(d.id) {
                case 72:
                case 78:
                    break;
                default:
                    return path.centroid(d)[1];
                    break;
            }
        })
        .attr("text-anchor", "middle");
});

d3.json("../static/json/us-districts.json", function(error, data) {
    g.append("g")
        .attr("id", "counties")
        .selectAll("path")
        .data(topojson.feature(data, data.objects.counties).features)
        .enter()
        .append("path")
        .attr("d", path)
        .attr("fill", 'none')
        .attr("stroke", "#333333")
        .attr("class", "county");

    g.append("g")
        .attr("id", "districts")
        .selectAll("path")
        .data(topojson.feature(data, data.objects.districts).features)
        .enter()
        .append("path")
        .attr("d", path)
        .attr("fill", 'none')
        .attr("stroke", "tomato")
        .attr("class", "district");
});
