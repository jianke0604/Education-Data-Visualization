<template>
  <div id="main" style="height: 100%"></div>
</template>

<script>
import * as echarts from 'echarts/core';
import { Scatter3DChart } from 'echarts-gl/charts';
import { TooltipComponent, VisualMapComponent } from 'echarts/components';
import { CanvasRenderer } from 'echarts/renderers';
import { Grid3DComponent } from 'echarts-gl/components';

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
      var myChart = echarts.init(chartDom, 'dark');
      var option;

      var schema = [
        { name: 'id', index: 0 },
        { name: 'total_answers', index: 1 },
        { name: 'correct_rate', index: 2 },
        { name: 'average_time', index: 3 },
        { name: 'most_common_method', index: 4 }
      ];

      var fieldIndices = schema.reduce(function (obj, item) {
        obj[item.name] = item.index;
        return obj;
      }, {});

      var config = {
        xAxis3D: 'total_answers',
        yAxis3D: 'correct_rate',
        zAxis3D: 'average_time_seconds',
        color: 'most_common_method',
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

      // Fetch data and initialize the chart
      fetch('../../data/student_statistics1.json')
        .then(response => response.json())
        .then(data => {
          // Create a set to store unique programming languages
          const programmingLanguagesSet = new Set();

          var processedData = Object.keys(data).map(id => {
            var item = data[id];
            // Add the most_common_method to the set
            programmingLanguagesSet.add(item.most_common_method);
            return [
              id,
              item.total_answers,
              item.correct_rate,
              parseTimeToSeconds(item.average_time),
              item.most_common_method
            ];
          });

          // Convert the set to an array and map colors to each programming language
          const programmingLanguagesArray = Array.from(programmingLanguagesSet);
          const colorPalette = [
            '#1710c0', '#0b9df0', '#00fea8', '#00ff0d', '#f5f811', '#f09a09', '#fe0300',
            '#800080', '#ff1493', '#00ced1', '#8b4513', '#7fffd4', '#228b22', '#daa520'
          ];
          const methodToColor = {};
          programmingLanguagesArray.forEach((method, index) => {
            methodToColor[method] = colorPalette[index % colorPalette.length];
          });

          myChart.setOption({
            tooltip: {
              formatter: function (params) {
                return `ID: ${params.value[3]}<br>
                        Total Answers: ${params.value[0]}<br>
                        Correct Rate: ${params.value[1]}<br>
                        Peak Time: ${formatSecondsToTime(params.value[2])}<br>
                        Programming Language: ${params.value[4]}`;
              }
            },
            visualMap: [
              {
                top: 10,
                calculable: true,
                dimension: 4,
                categories: programmingLanguagesArray,
                inRange: {
                  color: programmingLanguagesArray.map(method => methodToColor[method])
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
                  'id',
                  'most_common_method'
                ],
                data: processedData.map(item => {
                  return [
                    item[fieldIndices['total_answers']],
                    item[fieldIndices['correct_rate']],
                    item[fieldIndices['average_time']],
                    item[fieldIndices['id']],
                    item[fieldIndices['most_common_method']]
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
