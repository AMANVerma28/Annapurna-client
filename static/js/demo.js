type = ['','info','success','warning','danger'];
demo = {
  initPickColor: function(){
    $('.pick-class-label').click(function(){
      var new_class = $(this).attr('new-class');  
      var old_class = $('#display-buttons').attr('data-class');
      var display_div = $('#display-buttons');
      if(display_div.length) {
        var display_buttons = display_div.find('.btn');
        display_buttons.removeClass(old_class);
        display_buttons.addClass(new_class);
        display_div.attr('data-class', new_class);
      }
    });
  },
    
  initChartist: function(year){    
    var crops=[]
    $.getJSON( "../../static/json/crop.json", function( datas ){ 
      var plot = []
      for (var i=0; i<datas.length;i++){  
        if (crops.indexOf(datas[i].Crop)==-1){
          crops.push(datas[i].Crop)
        }
      }
      
      $.getJSON( "../../static/json/season.json", function( seasonData ){
        for(var i=1;i<=seasonData.length;i++){
          var temp=[]
          for (var j=0;j<crops.length;j++){
            temp.push(0)
          }
          for(var k=0; k<datas.length;k++){ 
            if(datas[k].season==i && datas[k].year==year){ 
              temp[crops.indexOf(datas[k].Crop)]=datas[k].Extent
            }
          }
          plot.push(temp)
        }

        var data = {
          labels: crops,
          series: plot
        };
            
        var options = {
          seriesBarDistance: 10,
          axisX: {
            showGrid: false
          },
          height: "245px"
        };
            
        var responsiveOptions = [
          ['screen and (max-width: 640px)', {
            seriesBarDistance: 10,
            axisX: {
              labelInterpolationFnc: function (value) {
                return value[0];
              }
            }
          }]
        ];
            
        Chartist.Bar('#chartActivity', data, options, responsiveOptions);
      });
    });
          
    var dataPreferences = {
      series: [
          [25, 30, 20, 25]
      ]
    };
        
    var optionsPreferences = {
      donut: true,
      donutWidth: 40,
      startAngle: 0,
      total: 100,
      showLabel: false,
      axisX: {
        showGrid: false
      }
    };
  },
}