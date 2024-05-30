<template>
  <div id="scatter"></div>
</template>

<script>
import axios from 'axios';
import * as echarts from 'echarts';

export default {
  name: 'EChartsScatterPlot',
  mounted() {
    this.initChart();
  },
  methods: {
    async initChart() {
      var chartDom = document.getElementById('scatter');
      var myChart = echarts.init(chartDom);
      var option;

      try {
        const [inconsistentQuestionsResponse, studentStatisticsResponse] = await Promise.all([
          axios.get('../../data/students_inconsistent_questions.json'),
          axios.get('../../data/student_statistics.json')
        ]);

        const inconsistentQuestions = inconsistentQuestionsResponse.data;
        const studentStatistics = studentStatisticsResponse.data;

        let data = [];
        let minCorrectRatePerCount = {};

        for (let id in inconsistentQuestions) {
          if (studentStatistics[id]) {
            let count = inconsistentQuestions[id].count;
            let correctRate = studentStatistics[id].correct_rate;

            if (!(count in minCorrectRatePerCount) || correctRate < minCorrectRatePerCount[count].correctRate) {
              minCorrectRatePerCount[count] = { correctRate: correctRate, id: id };
            }
          }
        }

        for (let id in inconsistentQuestions) {
          if (studentStatistics[id]) {
            let count = inconsistentQuestions[id].count;
            let correctRate = studentStatistics[id].correct_rate;
            let color = 'blue';

            if (minCorrectRatePerCount[count].id === id) {
              color = 'red';
            }

            data.push({
              value: [count, correctRate],
              itemStyle: {
                color: color
              },
              id: id
            });
          }
        }

        option = {
          title: {
            text: 'Scatter Plot of Count vs Correct Rate',
          },
          tooltip: {
            trigger: 'item',
            formatter: function (params) {
              return 'ID: ' + params.data.id + '<br/>Count: ' + params.data.value[0] + '<br/>Correct Rate: ' + params.data.value[1];
            }
          },
          xAxis: {
            name: 'Count',
            type: 'value'
          },
          yAxis: {
            name: 'Correct Rate',
            type: 'value'
          },
          series: [{
            symbolSize: 10,
            data: data,
            type: 'scatter'
          }]
        };

        myChart.setOption(option);

      } catch (error) {
        console.error('Error fetching or processing data:', error);
      }
    }
  }
}
</script>

<style scoped>
#scatter {
  width: 100%;
  height: 100%;
}
</style>
