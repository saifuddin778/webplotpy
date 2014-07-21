$(document).ready(function(){
   plot_scatter();
   create_stats();
});

function plot_scatter(){
   $('#chart').highcharts({
      chart: {
         type: 'scatter',
         zoomType: 'xy'
      },
      
      title: {
         text: ''
      },
      
      xAxis: {
         title: {
            enabled: true,
            text: scatter_items_.xlabel
         },
         startOnTick: true,
         endOnTick: true,
         showLastLabel: true
      },
      yAxis: {
         title: {
            enabled: true,
            text: scatter_items_.ylabel
         }
      },
      credits: {
         enabled: false
      },
      exporting: { enabled: false },
      plotOptions: {
         scatter: {
            marker: {
               radius: 3.5,
                  states: {
                     hover: {
                        enabled: true,
                        lineColor: 'black'
                     }
                  }
            },
            states: {
               hover: {
                  marker: {
                     enabled: true
                  }
               }
            },
            tooltip: {
               headerFormat: '<b>{series.name}</b><br>',
               pointFormat: '({point.x}, {point.y})'
            }
         }
      },
      series: scatter_items_.data
   });
}


function create_stats(stat_item) {
   var $cells = "";
   
   $cells += "<div class='stat_row'><div class='stat_cell'><b>Set</b></div><div class='stat_cell'><b>Points</b></div></div>";
   for (a in scatter_items_.data) {
      len_ = scatter_items_.data[a].data.length;
      name_ = scatter_items_.data[a].name;
      $cells += "<div class='stat_row'><div class='stat_cell'>"+name_+"</div><div class='stat_cell'>"+len_+"</div></div>";
   }
   $('.stats_table').append($cells);
   $('.chart_title').text(scatter_items_.plot_title);
}