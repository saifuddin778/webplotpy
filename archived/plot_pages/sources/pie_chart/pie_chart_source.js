$(document).ready(function(){
   create_stats(pie_items_.data);
   plot_pie();
   
   
});

function plot_pie(){
   // Make monochrome colors and set them as default for all pies
   Highcharts.getOptions().plotOptions.pie.colors = (function () {
      var colors = [],
      base = '#558ed5', i

      for (i = 0; i < 10; i++) {
         colors.push(Highcharts.Color(base).brighten((i - 4) / 7).get());
      }
      return colors;
   }());
   
   var ch = $('#chart').highcharts({
      chart: {
         plotBackgroundColor: null,
         plotBorderWidth: null,
         plotShadow: false
      },
      title: {
         text: ''
      },
      credits: {
         enabled: false
      },
      tooltip: {
         pointFormat: '{series.name}: <b>{point.y}</b>'
      },
      
      
      plotOptions: {
         pie: {
               allowPointSelect: true,
               cursor: 'pointer',
               dataLabels: {
                  enabled: true,
                  format: '<b>{point.name}</b>: {point.y}',
                  style:{
                     color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                  }
               }
         }
      },
      series: [{
         type: 'pie',
         name: pie_items_.item_type,
         data: pie_items_.data
      }]
   });
}


function create_stats(stat_item) {
   var $cells = "";
   
   console.log(stat_item)
   
   $cells += "<div class='stat_row'><div class='stat_cell'><b>Segment</b></div><div class='stat_cell'><b>Value</b></div></div>";
   
   for (a in stat_item) {
      count_ = stat_item[a][1];
      name_ = stat_item[a][0];
      $cells += "<div class='stat_row'><div class='stat_cell'>"+name_+"</div><div class='stat_cell'>"+count_+"</div></div>";
   }
   $('.stats_table').append($cells);
   
   $('.chart_title').text(pie_items_.plot_title);
}