

// Load CSV file
airTemp();

var dataset;

function airTemp() {

d3.csv("static/data/sensorData.csv", function(data){

    data.forEach(function(d) {
      d.daysPast = parseFloat(d.daysPast);
      d.airTemp = parseFloat(d.airTemp);
    });

  var data = d3.nest()
      .sortKeys((a, b) => a - b)
      .entries(data);

      console.log(data)

      dataset = data;

      var yScale = d3.scaleLinear()
        .domain([50,
                d3.max(data, function(d) { return d.airTemp})])
        .range([ height, 0 ]);


    var xScale = d3.scaleLinear()
  		.domain([d3.min(data, function(d) { return d.daysPast;}),
  						d3.max(data, function(d) { return d.daysPast})])
      .range([ padding, width]);


    	var xAxis = d3.axisBottom()
    		.scale(xScale);

      var yAxis = d3.axisBottom()
    		.scale(yScale)


      svg.append("g")
   	 	.style("font-size", "12" )
   	 	.attr("transform", "translate(50,20)")
      .style("stroke", "#77A88B")
   	   .call(d3.axisLeft(yScale).ticks(5));



     var area = d3.area()
  	     .x(function(d) { return xScale(d.daysPast); })
  	     .y0(height)
  	     .y1(function(d) { return yScale(d.airTemp); });

       svg.append("path")
  		     .datum(data)
  				 .style("fill","#77A88B")
  		     .attr("class", "area")
  		     .attr("d", area)

  })

  	var margin = {top: 20, right: 10, bottom: 10, left: 10};
  	var width = 500 - margin.left - margin.right,
        height = 200 - margin.top;

  	var padding = 0;

  	// LEFT CHART
  	var svg = d3.select("#chart-airTemp").append("svg")
  	    .attr("width", width + margin.left + margin.right)
  	    .attr("height", height + margin.top + margin.bottom)
  	    .append("g")
  	    .attr("transform", "translate(" + 0 + "," + 0 + ")");

    var selectBox = d3.select("#dash-type");

  		d3.select("#dash-type")
	    .on("change", function(d) {

	      function rescale() {
          console.log(selectBox.property('value'))


          var xScale = d3.scaleLinear()
            .domain([d3.min(dataset, function(d) { return d.daysPast;}),
                    d3.max(dataset, function(d) { return d.daysPast})])
            .range([ padding, width]);

          var yScale = d3.scaleLinear()
            .domain([40,
                    d3.max(dataset, function(d) {
                      if (selectBox.property('value') == 'airTemp')
                        return   d.airTemp
                      if (selectBox.property('value') == 'waterTemp')
                        return d.waterTemp
                      if (selectBox.property('value') == 'hum')
                        return   d.airHumidity
                      })
                    ])
            .range([ height, 0 ]);

        var area = d3.area()
            .x(function(d) { return xScale(d.daysPast); })
            .y0(height)
            .y1(function(d) {
              if (selectBox.property('value') == 'airTemp')
  	            return   d.airTemp
  	          if (selectBox.property('value') == 'waterTemp')
  	            return d.waterTemp
  						if (selectBox.property('value') == 'hum')
  							return   d.airHumidity
            });


						svg.selectAll("path")
						  	.datum(dataset)
								.transition()
								.duration(2000)
								.attr("d", area)
                .call(d3.axisLeft(yScale).ticks(3));

}
rescale();

});
};


$('#bologna-list a').on('click', function (e) {
  e.preventDefault()
  $(this).tab('show')
})
