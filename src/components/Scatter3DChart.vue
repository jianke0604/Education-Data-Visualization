<template>
  <div ref="chart" style="width: 100%; height: 100%;"></div>
</template>

<script>
import * as echarts from 'echarts';
import axios from 'axios';

export default {
  name: 'Scatter3DChart',
  data() {
    return {
      chart: null,
      config: {
        xAxis3D: 'average_time',
        yAxis3D: 'total_answers',
        zAxis3D: 'correct_rate',
        color: 'correct_rate',
        symbolSize: 'total_answers',
      },
      fieldIndices: {},
    };
  },
  methods: {
    getMaxOnExtent(data) {
      console.log('Data in getMaxOnExtent:', data);
      let colorMax = -Infinity;
      let symbolSizeMax = -Infinity;
      data.forEach((item) => {
        const colorVal = item[this.fieldIndices[this.config.color]];
        const symbolSizeVal = item[this.fieldIndices[this.config.symbolSize]];
        colorMax = Math.max(colorVal, colorMax);
        symbolSizeMax = Math.max(symbolSizeVal, symbolSizeMax);
      });
      return { color: colorMax, symbolSize: symbolSizeMax };
    },
    async fetchData() {
      try {
        const response = await axios.get('../../data/student_statistics.json');
        let data = response.data;

        // Convert the object to an array
        data = Object.values(data);

        // Log data type and content
        console.log('Fetched data:', data);
        console.log('Data type:', typeof data);
        console.log('Is Array:', Array.isArray(data));

        if (!Array.isArray(data)) {
          throw new Error('Data is not an array');
        }

        // Assuming data is an array of objects
        const schema = [
          { name: 'total_answers', index: 0 },
          { name: 'correct_rate', index: 1 },
          { name: 'average_time', index: 2 },
        ];

        // Generate fieldIndices based on schema
        this.fieldIndices = schema.reduce((obj, item) => {
          obj[item.name] = item.index;
          return obj;
        }, {});

        // Convert time strings to hours (0-24 format)
        data = data.map((item) => {
          const [hours, minutes, seconds] = item.average_time.split(':').map(Number);
          item.average_time = hours + minutes / 60 + seconds / 3600;
          return item;
        });

        const max = this.getMaxOnExtent(data);

        this.chart.setOption({
          tooltip: {},
          visualMap: [
            {
              top: 10,
              calculable: true,
              dimension: 3,
              max: max.color / 2,
              inRange: {
                color: [
                  '#1710c0',
                  '#0b9df0',
                  '#00fea8',
                  '#00ff0d',
                  '#f5f811',
                  '#f09a09',
                  '#fe0300',
                ],
              },
              textStyle: { color: '#fff' },
            },
            {
              bottom: 10,
              calculable: true,
              dimension: 4,
              max: max.symbolSize / 2,
              inRange: {
                symbolSize: [10, 40],
              },
              textStyle: { color: '#fff' },
            },
          ],
          xAxis3D: { name: this.config.xAxis3D, type: 'value' },
          yAxis3D: { name: this.config.yAxis3D, type: 'value' },
          zAxis3D: { name: this.config.zAxis3D, type: 'value' },
          grid3D: {
            axisLine: { lineStyle: { color: '#fff' } },
            axisPointer: { lineStyle: { color: '#ffbd67' } },
          },
          series: [
            {
              type: 'scatter3D',
              dimensions: [
                this.config.xAxis3D,
                this.config.yAxis3D,
                this.config.zAxis3D,
                this.config.color,
                this.config.symbolSize,
              ],
              data: data.map((item, idx) => [
                item[this.fieldIndices[this.config.xAxis3D]],
                item[this.fieldIndices[this.config.yAxis3D]],
                item[this.fieldIndices[this.config.zAxis3D]],
                item[this.fieldIndices[this.config.color]],
                item[this.fieldIndices[this.config.symbolSize]],
                idx,
              ]),
              symbolSize: 12,
              itemStyle: {
                borderWidth: 1,
                borderColor: 'rgba(255,255,255,0.8)',
              },
              emphasis: {
                itemStyle: { color: '#fff' },
              },
            },
          ],
        });
      } catch (error) {
        console.error('Failed to fetch data:', error);
      }
    },
    initChart() {
      this.chart = echarts.init(this.$refs.chart);
      this.fetchData();
    },
  },
  mounted() {
    this.initChart();
  },
};
</script>

<style>
html,
body,
#app {
  height: 100%;
}
</style>
