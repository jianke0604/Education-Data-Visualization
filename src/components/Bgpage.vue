<template>
    <div class="bgpage">
        <Header></Header>
        <div>
            <div class="container">
                <div class="box" style="width:40%;">
                    <Viewbox
                        title="提交次数日期热力图"
                        :boxb="true"
                    >
                        <DateHeatMap ref="dateHeatMap"/>
                    </Viewbox>
                </div>
                <div class="box" style="width:60%;">
                    <Viewbox
                        title="各知识点正确率与人数分布"
                        :boxb="true"
                    >
                        <SunBurst @changeDateHeatMap="changeDateHeatMap"/>
                    </Viewbox>
                </div>
                
            </div>
            <div class="container">
                <div class="box" style="width:40%">
                    <Viewbox
                        title="题目难度与正确率"
                        :boxb="true"
                    >
                    <Diff />
                </Viewbox>
                </div>
                <div class="box" style="width:60%">
                    <Viewbox
                        title="学生通过题目与正确率明细"
                        :boxb="true"
                    >
                    <TGL />
                    </Viewbox>
                </div>
            </div>
            <div class="container">
                <div class="box" style="width:40%">
                    <Viewbox
                        title="三维学生画像"
                        :boxb="true"
                    >
                    <ECharts3D />
                </Viewbox>
                </div>
                <div class="box" style="width:60%;">
                    <Viewbox
                        title="学生提交频率与通过率"
                        :boxb="true"
                    >
                    <zoom2D />
                </Viewbox>
                </div>
            </div>
            <div class="container">
                <div class="box" style="width:50%">
                    <Viewbox
                        title="学生复习题目数量与正确率"
                        :boxb="true"
                    >
                    <EChartsScatterPlot />
                </Viewbox>
                </div>
                <div class="box" style="width:50%">
                    <Viewbox
                        title="学习集中度与正确率关系"
                        :boxb="true"
                    >
                    <JZD />
                </Viewbox>
                </div>
            </div>
        </div>
    </div>

    <!-- <div>
       
    </div>
    <div style="width: 100%; height: 600px;">
    <ECharts3D />
    </div> -->
    <!-- <div>
    </div>
    <div id="sb_container" style="width: 100%; height: 600px;">
        <SunBurst/>
    </div>
    <div>
    </div>
    <div>
        <Error />
    </div> -->
</template>

<script>
import ECharts3D from './ECharts3D.vue';
import zoom2D from './zoom2D.vue';
import Header from './Header.vue'
import Viewbox from './viewbox/Viewbox.vue'
import DateHeatMap from './DateHeatMap.vue';
import SunBurst from './SunBurst.vue';
import Diff from './question_difficulty.vue';
import Error from './t4_error.vue';
import EChartsScatterPlot from './EChartsScatterPlot.vue';
import JZD from './jizhongdu.vue';
import TGL from './TGL.vue';
export default {
    components: {
    Header,
    Viewbox,
    ECharts3D,
    zoom2D,
    DateHeatMap,
    SunBurst,
    Diff,
    Error,
    EChartsScatterPlot,
    JZD,
    TGL
},
    data() {
        return {
            subTitle: "子标题"
        }
    }, 
    mounted() {
        
    },
    methods: {
        changeDateHeatMap(knowledge) {
            this.$refs.dateHeatMap.draw(knowledge);
        }
    }

}
</script>


<style>
.bgpage{
    background: url(src/assets/true.png);
    height: 100%;
    width: 100%;
}
.container {
    display: flex; /* 将容器设置为 flex 容器 */
}
.box {
     /* 每个子元素占据相等的空间 */
    height: 350px;
    margin: 10px;
}



</style>