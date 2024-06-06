<template>
    <form @submit.prevent="handleSubmit">
        <label for="firstSelect" style="color: white; margin: 2%;">班级:</label>
        <select id="firstSelect" v-model="selectedCategory" @change="updateSubcategories">
            <option v-for="(name, key) in classes" :key="key" :value="key">
                {{ key }}
            </option>
        </select>

        <label for="secondSelect" style="color: white; margin: 2%;">学生:</label>
        <select id="secondSelect" v-model="selectedSubcategory" :disabled="!selectedCategory">
            <option v-for="(name, index) in classes[selectedCategory]" :key="name" :value="name">
                {{ name }}
            </option>
        </select>

        <input type="submit" value="查询" style="
                margin: 2%; 
                padding: 3px; 
                background-color: rgba(0, 153, 204, 0.8); 
                color: white; 
                border-color: transparent;
                border-radius: 3px;
                ">
    </form>
    <div id="pics">
        <div id="pic1"></div>
        <div id="pic2"></div>
    </div>
</template>
  
  <script>
  import axios from 'axios';
  import * as echarts from 'echarts';
  
  export default {
    name: 'TGL',
    data(){
        return{
            selectedCategory:'',
            selectedSubcategory:'',
            tgl:[],
            zql:[],
            classes:{}
        }
    },
    mounted(){
      this.prepareData();
    },
    methods: {
        updateSubcategories() {
                    this.selectedSubcategory = '';
        },
        handleSubmit() {
               console.log('你选择了: ' + this.selectedCategory + ' - ' + this.selectedSubcategory);

            let student=this.selectedSubcategory;
            let s_tgl=this.tgl[student];
            let s_zql=this.zql[student];
            const keys=Object.keys(s_tgl);
            s_tgl=Object.values(s_tgl);
            s_zql=Object.values(s_zql);
            var pic1=echarts.init(document.getElementById('pic1'));
            var pic2=echarts.init(document.getElementById('pic2'));
            const option1 = {
                title: {
                    text: '通过率',
                    textStyle: {
                        color: "white"
                    }
                },
                tooltip: {
                    trigger: 'axis'
                },
                xAxis: {
                    type: 'category',
                    data: keys,
                    axisLabel: {
                        textStyle: {
                            color: 'white'
                        }
                    }
                },
                yAxis: {
                    type: 'value',
                    axisLabel: {
                        textStyle: {
                            color: 'white'
                        }
                    }
                },
                series: [{
                    data: s_tgl,
                    type: 'line',
                    itemStyle: {
                        color: 'rgba(0, 153, 153, 0.8)'
                    },
                    areaStyle: {
                        color: {
                            type: 'linear',
                            x: 0,
                            y: 0,
                            x2: 0,
                            y2: 1,
                            colorStops: [{
                                offset: 0,
                                color: 'rgba(0, 153, 153, 0.8)' // 0% 处的颜色
                            }, {
                                offset: 1,
                                color: 'rgba(0, 153, 153, 0.0)' // 100% 处的颜色
                            }],
                            global: false // 缺省为 false
                        }
                    }
                        }]
            };

            // 设置选项并渲染图表
            pic1.setOption(option1);
            const option2 = {
                title: {
                    text: '正确率',
                    textStyle: {
                        color: "white"
                    }
                },
                tooltip: {
                    trigger: 'axis'
                },
                xAxis: {
                    type: 'category',
                    data: keys,
                    axisLabel: {
                        textStyle: {
                            color: 'white'
                        }
                    }
                },
                yAxis: {
                    type: 'value',
                    axisLabel: {
                        textStyle: {
                            color: 'white'
                        }
                    }
                },
                series: [{
                    data: s_zql,
                    type: 'line',
                    itemStyle: {
                        color: 'rgba(0, 102, 204, 0.8)'
                    },
                    areaStyle: {
                        color: {
                            type: 'linear',
                            x: 0,
                            y: 0,
                            x2: 0,
                            y2: 1,
                            colorStops: [{
                                offset: 0,
                                color: 'rgba(0, 102, 204, 0.8)' // 0% 处的颜色
                            }, {
                                offset: 1,
                                color: 'rgba(0, 102, 204, 0.0)' // 100% 处的颜色
                            }],
                            global: false // 缺省为 false
                        }
                    }
                }]
            };

            // 设置选项并渲染图表
            pic2.setOption(option2);
        },
        async prepareData() {
                // 获取数据
                
                this.tgl=await axios.get('../../data/time_series_pass_rate_per_question.json');
                this.zql=await axios.get('../../data/time_series_pass_rate_per_student.json');
                this.classes=await axios.get('../../data/Classes_students.json');
                this.tgl=this.tgl.data;
                this.zql=this.zql.data;
                this.classes=this.classes.data;
                console.log(this.tgl);
        
        }
    }
  }
  </script>
  
  <style scoped>
  select {
    position: relative;
    z-index: 6666;
  }
  input {
    position: relative;
    z-index: 6666;
  }
    form {
        display: flex;
        flex-direction: row;
        justify-content: flex-end;
        align-items: center;
        width: 100%;
        height: 10%;
        position: absolute;
        top: 0;
    }
  #pics {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    width: 100%;
    height: 90%;
    margin-top: 2%;
  }

  #pic1,#pic2{
    width:45%;
    height: 100%;
  }
  </style>
  