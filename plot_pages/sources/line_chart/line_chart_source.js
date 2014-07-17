$(document).ready(function(){
   plot_line();
});

function get_line_data(){
   data = [];
   for (i=0; i< line_items_.x_axis.length; i++) {
      data.push({x: line_items_.x_axis[i], y: line_items_.y_axis[i]});
   }
   create_stats([{label: 'Count', value: line_items_.count}, {label: 'Mean', value: line_items_.mean}]);
   return [{values: data, key: line_items_.line_label, color: line_items_.color}];
}


function plot_line(){
   data = get_line_data();
   nv.addGraph(function(){
      var chart = nv.models.lineChart().useInteractiveGuideline(false);
      chart.xAxis
         .axisLabel(line_items_.xlabel)
         .tickFormat(d3.format(',r'));
      chart.yAxis
         .axisLabel(line_items_.ylabel)
         .tickFormat(d3.format('.02f'));
      d3.select('#chart').select('svg')
        .datum(data)
        .transition().duration(200)
        .call(chart);
      
      nv.utils.windowResize(chart.update);
   
      return chart;
   });
}


function create_stats(stat_item) {
   var $cells = "";
   for (i in stat_item){
      $cells += "<div class='stat_row'><div class='stat_cell'>"+stat_item[i].label+"</div><div class='stat_cell'>"+stat_item[i].value+"</div></div>";
   }
   $('.stats_table').append($cells);
   
   //create chart title
   $('.chart_title').text(line_items_.plot_title);
}