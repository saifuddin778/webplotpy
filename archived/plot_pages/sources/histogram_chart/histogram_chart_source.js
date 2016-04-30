$(document).ready(function(){
   plot_histogram();
});

function plot_histogram(){
   plot_data = histogram_items_.plot_data;
   nv.addGraph(function() {
   var chart = nv.models.discreteBarChart()
     .x(function(d) { return d.key })
     .y(function(d) { return d.value })
     .staggerLabels(false)
     .showXAxis(histogram_items_.show_xaxis)
     .tooltips(true)
     .color(['cornflowerblue'])
     .showValues(histogram_items_.show_values);

   d3.select('#chart svg')
     .datum(plot_data)
     .transition().duration(300)
     .call(chart);

     nv.utils.windowResize(chart.update);

     return chart;
   });
   
   create_stats([{label: 'Count', value: histogram_items_.count}]);
}


function create_stats(stat_item) {
   var $cells = "";
   for (i in stat_item){
      $cells += "<div class='stat_row'><div class='stat_cell'>"+stat_item[i].label+"</div><div class='stat_cell'>"+stat_item[i].value+"</div></div>";
   }
   $('.stats_table').append($cells);
   
   //create chart title
   $('.chart_title').text(histogram_items_.plot_title);
}