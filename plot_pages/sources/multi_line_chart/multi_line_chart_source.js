$(document).ready(function(){
   plot_line();
});

function get_line_data(){
   create_stats();
   return multi_line_items_.data;
}


function plot_line(){
   data = get_line_data();
   nv.addGraph(function(){
      var chart = nv.models.lineChart().useInteractiveGuideline(true);
      chart.xAxis
         .axisLabel(multi_line_items_.xlabel)
         .tickFormat(d3.format(',r'));
      chart.yAxis
         .axisLabel(multi_line_items_.ylabel)
         .tickFormat(d3.format('.02f'));
      d3.select('#chart').select('svg')
        .datum(data)
        .transition().duration(200)
        .call(chart);
      
      if (multi_line_items_.colors != 'default') {
         chart.colors(multi_line_items_.colors);
      }
      
      nv.utils.windowResize(chart.update);
   
      return chart;
   });
}


function create_stats(stat_item) {
   var $cells = "";
   
   $cells += "<div class='stat_row'><div class='stat_cell'><b>Series</b></div><div class='stat_cell'><b>Length</b></div></div>";
   for (a in multi_line_items_.data) {
      len_ = multi_line_items_.data[a].length;
      name_ = multi_line_items_.data[a].key;
      $cells += "<div class='stat_row'><div class='stat_cell'>"+name_+"</div><div class='stat_cell'>"+len_+"</div></div>";
   }
   $('.stats_table').append($cells);
   
   
   /*
   for (i in stat_item){
      $cells += "<div class='stat_row'><div class='stat_cell'>"+stat_item[i].label+"</div><div class='stat_cell'>"+stat_item[i].value+"</div></div>";
   }
   $('.stats_table').append($cells);
   */
   //create chart title
   $('.chart_title').text(multi_line_items_.plot_title);
}