<template>
    <div id="jizhongdutu"></div>
    <h3 style="color:rgb(204, 255, 255); margin-left: 10%;">注：同一知识点的各题目做题时间越接近，集中度越高</h3>
  </template>
  
  <script>
  import axios from 'axios';
  import * as echarts from 'echarts';
  
  export default {
    name: 'JZD',
    mounted(){
      this.initChart();
    },
    methods: {
        async initChart() {
            try {
                // 获取数据
                const [inconsistentQuestionsResponse, studentStatisticsResponse,studentFirstTimeResponse] = await Promise.all([
                    axios.get('../../data/students_inconsistent_questions.json'),
                    axios.get('../../data/student_statistics.json'),
                    axios.get('../../data/students_jizhongdu.json')
                ]);
                var chartDom = document.getElementById('jizhongdutu');
                var myChart = echarts.init(chartDom);
                const inconsistentQuestions = inconsistentQuestionsResponse.data;
                const studentStatistics = studentStatisticsResponse.data;
                const studentFirstTime = studentFirstTimeResponse.data;
                // 处理数据
                let data = [];
                let minCorrectRatePerCount = {};

                // 找出每个count的最小correct_rate
                for (let id in inconsistentQuestions) {
                    if (studentStatistics[id]) {
                        let count = inconsistentQuestions[id].count;
                        let correctRate = studentStatistics[id].correct_rate;

                        if (!(count in minCorrectRatePerCount) || correctRate < minCorrectRatePerCount[count].correctRate) {
                            minCorrectRatePerCount[count] = { correctRate: correctRate, id: id };
                        }
                    }
                }

                // 生成数据点
                for (let id in inconsistentQuestions) {
                    if (studentStatistics[id]) {
                        let count = inconsistentQuestions[id].count;
                        let correctRate = studentStatistics[id].correct_rate;
                        let color = 'rgba(0, 102, 204, 0.8)';
                        //检查当前点是否满足平均初次通过时间小于特定值
                       // if(studentFirstTime[id]<threshold){
                            //color = 'orange'
                        //}
                        
                        
                        // 检查当前点是否是该count的最小correct_rate
                       // if (minCorrectRatePerCount[count].id === id) {
                            //color = 'red';
                        //}

                        data.push({
                            value: [studentFirstTime[id], correctRate],
                            itemStyle: {
                                color: color
                            },
                            id: id
                        });
                    }
                }

                // 设置图表的选项
                var option = {
                    title: {
                        text: '',
                    },
                    tooltip: {
                        trigger: 'item',
                        formatter: function (params) {
                            return 'ID: ' + params.data.id + '<br/>Count: ' + params.data.value[0] + '<br/>Correct Rate: ' + params.data.value[1];
                        }
                    },
                    xAxis: {
                        name: '集中度',
                        nameTextStyle: {
                            color: 'white'
                        },
                        type: 'value',
                        axisLabel: {
                            textStyle: {
                                color: 'white'
                            }
                        }
                    },
                    yAxis: {
                        name: '正确率',
                        nameTextStyle: {
                            color: 'white'
                        },
                        type: 'value',
                        axisLabel: {
                            textStyle: {
                                color: 'white'
                            }
                        }
                    },
                    series: [{
                        symbolSize: 10,
                        data: data,
                        type: 'scatter',
                    }]
                };

                // 使用指定的配置项和数据显示图表
                myChart.setOption(option);

            } catch (error) {
                console.error('Error fetching or processing data:', error);
            }
        }
    }
  }
  </script>
  
  <style scoped>
  #jizhongdutu {
    width: 100%;
    height: 80%;
  }
  </style>
  