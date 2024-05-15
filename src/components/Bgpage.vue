<template>
    <!-- <div class="bgpage">
        <Header></Header>
        <div>
            <div class="container">
                <div class="box">
                    <Viewbox
                        :title="subTitle"
                        :boxb="true"
                    />
                </div>
                <div class="box">
                    <Viewbox
                        :title="subTitle"
                        :boxb="true"
                    />
                </div>
                <div class="box">
                    <Viewbox
                        :title="subTitle"
                        :boxb="true"
                    >
                    </Viewbox>
                </div>
            </div>
            <div class="container">
                <div class="box">
                    <Viewbox
                        title="测试子标题"
                        :boxb="true"
                    />
                </div>
                <div class="box">
                    <Viewbox
                        title="测试子标题"
                        :boxb="true"
                    />
                </div>
            </div>
            
        </div>
    </div> -->

    <div>
        <zoom2D />
    </div>
    <div style="width: 100%; height: 600px;">
    <ECharts3D />
    </div>
    <div>
    <DateHeatMap />
    </div>
</template>

<script>
import ECharts3D from './ECharts3D.vue';
import zoom2D from './zoom2D.vue';
import Header from './Header.vue'
import Viewbox from './viewbox/Viewbox.vue'
import DateHeatMap from './DateHeatMap.vue';
export default {
    components: {
    Header,
    Viewbox,
    ECharts3D,
    zoom2D,
    DateHeatMap
},
    data() {
        return {
            subTitle: "子标题"
        }
    }, 
    mounted() {
        
    },
    methods: {
        
    }

}
</script>


<style>
.bgpage{
    background: url(src/assets/true.png);
    height: 90vh;
    width: 100vw;
}
.container {
    display: flex; /* 将容器设置为 flex 容器 */
}
.box {
    flex: 1; /* 每个子元素占据相等的空间 */
    height: 300px;
    margin: 10px;
}

</style>