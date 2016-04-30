$(document).ready(function(){
   create_stats();
   plot_bar();
   
   
});

function plot_bar(){
   $('#chart').highcharts({
      chart: {
          type: 'bar'
      },
      title: {
          text: ''
      },
      subtitle: {
          text: ''
      },
      xAxis: {
          categories: bar_items_.data_labels,
          title: {
              text: bar_items_.ylabel
          }
      },
      yAxis: {
          //min: 0,
          labels: {
              overflow: 'justify'
          },
          title: {
              text: bar_items_.xlabel
          }
      },
      tooltip: {
          //valueSuffix: '',
          //valuePrefix: ''
          enabled: true
      },
      plotOptions: {
          bar: {
              dataLabels: {
                  enabled: true
              }
          }
      },
      legend: {
          enabled: true,
          layout: 'horizontal',
          align: 'center',
          verticalAlign: 'bottom',
          floating: false,
          borderWidth: 1,
          shadow: false
      },
      credits: {
          enabled: false
      },
      series: [{
          name: 'Bar Chart',
          data: bar_items_.data_values
      }]
   });
}


function create_stats() {
   var stat_item = bar_items_.data_labels;
   var $cells = "";
   
   $cells += "<div class='stat_row'><div class='stat_cell'><b>Segment</b></div><div class='stat_cell'><b>Value</b></div></div>";
   
   for (a in stat_item) {
      count_ = bar_items_.data_values[a];
      name_ = stat_item[a];
      $cells += "<div class='stat_row'><div class='stat_cell'>"+name_+"</div><div class='stat_cell'>"+count_+"</div></div>";
   }
   $('.stats_table').append($cells);
   
   $('.chart_title').text(bar_items_.plot_title);
}