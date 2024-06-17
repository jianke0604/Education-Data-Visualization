<template>
    <div class="header">
        <div class="bg-header">
            <div class="t-title">
            教育数据可视化平台
            </div>
        </div>
    </div>
</template>

<script>
export default {

}
</script>


<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
.header {
    width: 100%;
    height: 80px;
    padding: 0 20px;
}
.bg-header {
    width: 100%;
    height: 80px;
    background: url(src/assets/title.png) no-repeat;
    background-size: 100% 100%;
}
.t-title {
    width: 100%;
    height: 100%;
    text-align: center;
    font-size: 3em;
    line-height: 80px;
    color: #fff;
}
</style>