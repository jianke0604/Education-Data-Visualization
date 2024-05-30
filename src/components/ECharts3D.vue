<template>
  <div id="main" style="height: 100%; width:100%"></div>
</template>

<script>
import * as echarts from 'echarts/core';
import { Scatter3DChart } from 'echarts-gl/charts';
import { TooltipComponent, VisualMapComponent } from 'echarts/components';
import { CanvasRenderer } from 'echarts/renderers';
import { Grid3DComponent } from 'echarts-gl/components';

const customTheme = {
  backgroundColor: 'rgb(12, 28, 48)',
  // 你可以在这里添加更多的自定义样式
};

echarts.registerTheme('customTheme', customTheme);

export default {
  name: 'ECharts3D',
  mounted() {
    this.initChart();
  },
  methods: {
    initChart() {
      echarts.use([
        TooltipComponent,
        VisualMapComponent,
        Grid3DComponent,
        Scatter3DChart,
        CanvasRenderer
      ]);

      var chartDom = document.getElementById('main');
      var myChart = echarts.init(chartDom, 'customTheme');
      var option;

      var schema = [
        { name: 'id', index: 0 },
        { name: 'total_answers', index: 1 },
        { name: 'correct_rate', index: 2 },
        { name: 'average_time', index: 3 }
      ];

      var fieldIndices = schema.reduce(function (obj, item) {
        obj[item.name] = item.index;
        return obj;
      }, {});

      var config = {
        xAxis3D: 'total_answers',
        yAxis3D: 'correct_rate',
        zAxis3D: 'average_time_seconds',
        color: 'correct_rate',
        symbolSize: 'total_answers'
      };

      function parseTimeToSeconds(timeStr) {
        var parts = timeStr.split(':');
        return parseInt(parts[0], 10) * 3600 + parseInt(parts[1], 10) * 60 + parseInt(parts[2], 10);
      }

      function formatSecondsToTime(seconds) {
        var hours = Math.floor(seconds / 3600);
        var minutes = Math.floor((seconds % 3600) / 60);
        var min, min1;
        var hours1 = hours;
        if (minutes < 15)
          min = "00", hours1 = hours, min1="30";
        else if (minutes < 30)
          min = "15", hours1 = hours, min1="45";
        else if (minutes < 45)
          min = "30", hours1 = hours+1, min1="00";
        else
          min = "45", hours1 = hours+1, min1="15";
        var seconds = seconds % 60;
        return `${hours}:${min}:00 - ${hours1}:${min1}:00`;
      }

      function getMaxOnExtent(data) {
        var colorMax = -Infinity;
        var symbolSizeMax = -Infinity;
        for (var i = 0; i < data.length; i++) {
          var item = data[i];
          var colorVal = item[fieldIndices[config.color]];
          var symbolSizeVal = item[fieldIndices[config.symbolSize]];
          colorMax = Math.max(colorVal, colorMax);
          symbolSizeMax = Math.max(symbolSizeVal, symbolSizeMax);
        }
        return {
          color: colorMax,
          symbolSize: symbolSizeMax
        };
      }

      fetch('../../data/student_statistics.json')
        .then(response => response.json())
        .then(data => {
          var processedData = Object.keys(data).map(id => {
            var item = data[id];
            return [
              id,
              item.total_answers,
              item.correct_rate,
              parseTimeToSeconds(item.average_time)
            ];
          });

          var max = getMaxOnExtent(processedData);
          console.log(max.color);

          myChart.setOption({
            tooltip: {
              formatter: function (params) {
                // console.log(params);
                return `ID: ${params.value[3]}<br>
                        Total Answers: ${params.value[0]}<br>
                        Correct Rate: ${params.value[1]}<br>
                        Peak Time: ${formatSecondsToTime(params.value[2])}`;
              }
            },
            visualMap: [
              {
                top: 10,
                calculable: true,
                dimension: 1,
                max: max.color,
                inRange: {
                  color: [
                    '#1710c0',
                    '#0b9df0',
                    '#00fea8',
                    '#00ff0d',
                    '#f5f811',
                    '#f09a09',
                    '#fe0300'
                  ]
                },
                textStyle: {
                  color: '#fff'
                }
              },
              {
                bottom: 10,
                calculable: true,
                dimension: 1,
                max: max.symbolSize,
                inRange: {
                  symbolSize: [10, 40]
                },
                textStyle: {
                  color: '#fff'
                }
              }
            ],
            xAxis3D: {
              name: 'Total Answers',
              type: 'value'
            },
            yAxis3D: {
              name: 'Correct Rate',
              type: 'value'
            },
            zAxis3D: {
              name: 'Peak Time',
              type: 'value',
              axisLabel: {
                formatter: function (value) {
                  return formatSecondsToTime(value);
                }
              }
            },
            grid3D: {
              axisLine: {
                lineStyle: {
                  color: '#fff'
                }
              },
              axisPointer: {
                lineStyle: {
                  color: '#ffbd67'
                }
              },
              viewControl: {
                autoRotate: true,
                projection: 'orthographic'
              }
            },
            series: [
              {
                type: 'scatter3D',
                dimensions: [
                  'total_answers',
                  'correct_rate',
                  'average_time',
                  'id' // 添加id到dimensions
                  // 'correct_rate',
                  // 'total_answers'
                ],
                data: processedData.map(function (item) {
                  return [
                    item[fieldIndices['total_answers']],
                    item[fieldIndices['correct_rate']],
                    item[fieldIndices['average_time']],
                    item[fieldIndices['id']] // 添加id到data
                    // item[fieldIndices['correct_rate']],
                    // item[fieldIndices['total_answers']]
                  ];
                }),
                symbolSize: 12,
                itemStyle: {
                  borderWidth: 1,
                  borderColor: 'rgba(255,255,255,0.8)'
                },
                emphasis: {
                  itemStyle: {
                    color: '#fff'
                  }
                }
              }
            ]
          });
        });
    }
  }
}
</script>

<style scoped>
#main {
  height: 100%;
}
</style>
