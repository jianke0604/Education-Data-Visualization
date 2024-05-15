<template>
    
    <div id="sb_outer">
        <div id="line1_main"></div>
        <div id="sb_main"></div>
        <div id="line2_main"></div>  
    </div>
     
    
</template>

<script>
import * as echarts from 'echarts';
import Papa from 'papaparse';

export default {
    data(){
        return {
            y_m:["23/11","23/12","24/01","24/02","24/03"],
            zt_cnt:[0,0,0,0,0],
            bt_cnt:[0,0,0,0,0],
            //存储了所有知识点,对应的子知识点,及子知识点对应题目
            knowledges:{},
            //title info文件载入的数据
            titles:[],
            
            nametable:{},
            drawData:[],
            //
            otherData:[],
            myChart1:[],
            myChart2:[]
        }
    },
    mounted(){
        this.loadData();
    },

    methods: {
        
        loadData(){
            const titlePath='../../data/Data_TitleInfo.csv';
            fetch(titlePath)
            .then(response=>response.text())
            .then(data=>{
                this.titles=Papa.parse(data, {header:true,dynamicTyping:true,skipEmptyLines:true}).data;
                //保存题目知识点数据
                for(let i=0;i<this.titles.length;i++){
                    let knowledge=this.titles[i].knowledge;
                    let sub_knowledge=this.titles[i].sub_knowledge;
                    let title_ID=this.titles[i].title_ID;
                    if(knowledge in this.knowledges){
                        
                    }
                    else{
                        this.knowledges[knowledge]={};
                        
                    }
                    
                    if(sub_knowledge in this.knowledges[knowledge]){
                        this.knowledges[knowledge][sub_knowledge].push(title_ID);
                    }
                    else{
                        this.knowledges[knowledge][sub_knowledge]=[title_ID]
                    }
                    

                }
                //准备画图数据
               for(let knowledge in this.knowledges){
                    let childrens=[];
                    for(let sub_knowledge in this.knowledges[knowledge]){
                        childrens.push({
                            name:"子知识点"+(knowledge[0].toUpperCase())+(sub_knowledge.replace(knowledge+"_","")[0].toUpperCase())+":共"+this.knowledges[knowledge][sub_knowledge].length+"题",
                            value:this.knowledges[knowledge][sub_knowledge].length,
                            old_name:sub_knowledge
                        })
                    }
                    this.drawData.push({
                        name:"知识点"+(knowledge[0].toUpperCase()),
                        children:childrens,
                        old_name:knowledge
                    })
               } 
               
               this.drawSunGraph();
               
            })
            console.log(this.drawData);
            //const fileContents=fs.readFileSync(titlePath, 'utf8');
            //const result=Papa.parse(fileContents, {header:true,dynamicTyping:true,skipEmptyLines:true});
            //console.log(result.data);
            

            
        },

        drawSunGraph(){
            this.loadOtherData();
            var myChart = echarts.init(document.getElementById('sb_main'));
            var option = {
                
                series: {
                    type: 'sunburst',
                    // emphasis: {
                    //     focus: 'ancestor'
                    // },
                    data: this.drawData,
                    radius: [0, '80%'],
                    emphasis: {
                    focus: 'ancestor'
                    },
                    levels: [
                    {},
                    {
                        r0: '15%',
                        r: '45%',
                        itemStyle: {
                        borderWidth: 2
                        },
                        label:{
                            align: 'right',
                            fontSize:10,
                            fontWeight: 'bold'
                        }
                    },
                    
                    {
                        r0: '45%',
                        r: '62%',
                        label: {
                            position: 'outside',
                            padding: 3,
                            silent: false,
                            fontSize:10,
                        },
                        itemStyle: {
                        borderWidth: 3
                        }
                    }
                    ]
                }

            }
            myChart.setOption(option);
            
            myChart.on('click',(params)=>{
                if(params.data.children==undefined){
                    console.log(params.data.old_name);
                    let subknowledge=params.data.old_name;
                    let knowledge=subknowledge.split("_")[0];
                    console.log("knowledge")
                    this.changeLineGraphs(knowledge,subknowledge);
                }
            })
        },
        changeLineGraphs(knowledge,subknowledge){
            
            let option1={
                title:{
                    text: "子知识点"+(knowledge[0].toUpperCase())+(subknowledge.replace(knowledge+"_","")[0].toUpperCase())+"各月答题人数"
                },
                tooltip: {
                    trigger: 'axis'
                },
                legend: {
                    data: ['参与人数']
                },
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                
                xAxis: {
                    type: 'category',
                    boundaryGap: false,
                    data: ['2023-9', '2023-10', '2023-11', '2023-12', '2024-1']
                },
                yAxis: {
                    type: 'value'
                },
                series:
                    [
                    {
                    name: "子知识点"+(knowledge[0].toUpperCase())+(subknowledge.replace(knowledge+"_","")[0].toUpperCase()),
                    type: 'line',
                    stack: 'Total',
                    data: this.otherData["knowledges"][knowledge]["sub_knowledges"][subknowledge]["participants"]
                    }
                ]
                
            }

            let option2 = {
                title: {
                    text: '准确率'
                },
                tooltip: {
                    trigger: 'axis'
                },
                legend: {
                    data: ['全部题目', "子知识点"+(knowledge[0].toUpperCase())+(subknowledge.replace(knowledge+"_","")[0].toUpperCase()), "知识点"+(knowledge[0].toUpperCase())]
                },
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                
                xAxis: {
                    type: 'category',
                    boundaryGap: false,
                    data: ['2023-9', '2023-10', '2023-11', '2023-12', '2024-1']
                },
                yAxis: {
                    type: 'value'
                },
                series: [
                    {
                    name: '全部题目',
                    type: 'line',
                    
                    data: this.otherData["data"]
                    },
                    {
                    name: "子知识点"+(knowledge[0].toUpperCase())+(subknowledge.replace(knowledge+"_","")[0].toUpperCase()),
                    type: 'line',
                    
                    data: this.otherData["knowledges"][knowledge]["sub_knowledges"][subknowledge]["data"]
                    },
                    {
                    name: "知识点"+(knowledge[0].toUpperCase()),
                    type: 'line',
                    
                    data: this.otherData["knowledges"][knowledge]["data"]
                    },
                ]
                };
            this.myChart1.setOption(option1)
            this.myChart2.setOption(option2)
            console.log(this.otherData.data)
            console.log(this.otherData["knowledges"][knowledge]["sub_knowledges"][subknowledge]["participants"])
        },
        loadOtherData(){
            fetch('../../data/forSB.json')
            .then(response=>response.json())
            .then(data=>{
                this.otherData=data;
                console.log(data)
                this.drawLineGraphs()
            })
        },

        drawLineGraphs(){
            this.myChart1 = echarts.init(document.getElementById('line1_main'));
            this.myChart2 = echarts.init(document.getElementById('line2_main'));
            let option1 = {
                title: {
                    text: '点击旭日图外圈以显示具体数据'
                },
                tooltip: {
                    trigger: 'axis'
                },
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                
                xAxis: {
                    type: 'category',
                    boundaryGap: false,
                    data: ['2023-9', '2023-10', '2023-11', '2023-12', '2024-1']
                },
                yAxis: {
                    type: 'value'
                },
                series: [
                    {
                    name: 'Nothing',
                    type: 'line',
                    stack: 'Total',
                    data: []
                    }
                ]
                }
                let option2 = {
                    title: {
                        text: '点击旭日图外圈以显示数据'
                    },
                    tooltip: {
                        trigger: 'axis'
                    },
                    legend: {
                        data: ['全部题目']
                    },
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    
                    xAxis: {
                        type: 'category',
                        boundaryGap: false,
                        data: ['2023-9', '2023-10', '2023-11', '2023-12', '2024-1']
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                        {
                        name: '全部题目',
                        type: 'line',
                        stack: 'Total',
                        data: this.otherData['data']
                        },
                        
                        
                    ]
                };
            this.myChart1.setOption(option1);
            this.myChart2.setOption(option2);
            
        },
        
    }
    

}
    
</script>

<style>

#sb_main{
    margin-top: 10px;
    width: 30%;
    height: 90%;
}   
#line1_main{
    margin-top: 10px;
    width: 30%;
    height: 90%;
}   
#line2_main{
    margin-top: 10px;
    width: 30%;
    height: 90%;
}

#sb_outer{
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    width: 100%;
    height: 100%;
}
</style>