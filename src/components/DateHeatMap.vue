<template>
  <div id="dateheatmap" style="height: 600px; width: 100%;"></div>
</template>

<script>


import * as echarts from 'echarts';

export default {
  name: 'DateHeatMap',
  mounted() {
    var chartDom = document.getElementById('dateheatmap');
    var myChart = echarts.init(chartDom);
    var option;

    function draw(original_data) {
      var data = [];
      for (let i = 0; i < original_data.length; i++) {
        data.push([
          original_data[i].date,
          original_data[i].value
        ]);
      }

      var start_date = original_data[0].date;
      var end_date = original_data[original_data.length - 1].date;
      var max_value = Math.max.apply(null, original_data.map(function(item) {
        return item.value;
      }));

      console.log(data.map(function(item) {
        return item[1];
      }));
      
      option = {
        visualMap: {
          show: false,
          min: 0,
          max: max_value,
          inRange: {
            color: ['white', 'green']
          }
        },
        calendar: {
          top: 'middle',
          left: 100,
          range: [start_date, end_date],
          cellSize: [20, 20],
          splitLine: {
            show: true,
            lineStyle: {
              color: 'green',
              width: 1,
              type: 'solid',
            },
          },
          dayLabel: {
            nameMap: ['', 'Mon', '', 'Wen', '', 'Fri', ''],
          },
          yearLabel: {
            show: false,
          },
          itemStyle: {
            borderWidth: 5,
            borderColor: 'rgba(0, 0, 0, 0)',

          },
        },
        series: {
          type: 'heatmap',
          coordinateSystem: 'calendar',
          data: data,
          emphasis: {
            itemStyle: {
              shadowBlur: 10,
              shadowColor: 'rgba(0, 0, 0, 0.5)'
            }
          }
        },
        tooltip: {
          position: 'top',
          formatter: function(params) {
            return '日期: ' + params.value[0] + '<br>' + '提交次数: ' + params.value[1];
          }
        },
        visualMap: {
          min: 0,
          max: max_value,
          calculable: true,
          orient: 'vertical',
          left: 0,
          top: 'center',
          inRange: {
            color: ['white', 'green']
          },
        },
      };

      option && myChart.setOption(option);

    }

    fetch('../../data/dateheatmap.json')
      .then(response => response.json())
      .then(data => {
        draw(data);
      });

    }
}

</script>