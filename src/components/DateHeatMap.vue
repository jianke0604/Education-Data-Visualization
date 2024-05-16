<template>
  <div id="submit" style="height: 200px; width: 100%"></div>
  <div id="correct" style="height: 200px; width: 100%"></div>
  <select id="select" v-model="knowledge"></select>
</template>

<script>
import * as echarts from "echarts";

export default {
  name: "DateHeatMap",
  data() {
    return {
      submitChart: null,
      submitOption: null,
      data: [],
      knowledge: "total",
    };
  },
  mounted() {
    this.submitChart = echarts.init(document.getElementById("submit"));

    document.getElementById("select").addEventListener("change", (event) => {
      this.draw(event.target.value);
    });

    fetch("../../data/dateheatmap.json")
      .then((response) => response.json())
      .then((data) => {
        this.data = data;
        this.draw('total');
        for (let key in data[0]) {
          if (key === 'date') continue;
          var option = document.createElement("option");
          option.text = key;
          option.value = key;
          document.getElementById("select").appendChild(option);
        }
      });
  },
  methods: {
    draw(knowledge) {

      var data = [];
      for (let i = 0; i < this.data.length; i++) {
        data.push([this.data[i].date, this.data[i][knowledge]]);
      }

      var start_date = this.data[0].date;
      var end_date = this.data[this.data.length - 1].date;
      var submit_max_value = Math.max.apply(
        null,
        this.data.map(function (item) {
          return item[knowledge];
        })
      );

      console.log(
        data.map(function (item) {
          return item[1];
        })
      );

      this.submitOption = {
        title: {
          text: "提交次数",
          left: "center",
          top: 0,
          textStyle: {
            color: "black",
            fontSize: 20,
          },
        },
        visualMap: {
          show: false,
          min: 0,
          max: submit_max_value,
          inRange: {
            color: ["white", "green"],
          },
        },
        calendar: {
          top: 40,
          left: 100,
          range: [start_date, end_date],
          cellSize: [20, 20],
          splitLine: {
            show: true,
            lineStyle: {
              color: "green",
              width: 1,
              type: "solid",
            },
          },
          dayLabel: {
            nameMap: ["", "Mon", "", "Wen", "", "Fri", ""],
          },
          yearLabel: {
            show: false,
          },
          itemStyle: {
            borderWidth: 5,
            borderColor: "rgba(0, 0, 0, 0)",
          },
        },
        series: {
          type: "heatmap",
          coordinateSystem: "calendar",
          data: data.map(function (item) {
            return [item[0], item[1]];
          }),
          emphasis: {
            itemStyle: {
              shadowBlur: 10,
              shadowColor: "rgba(0, 0, 0, 0.5)",
            },
          },
        },
        tooltip: {
          position: "top",
          formatter: function (params) {
            return (
              "日期: " +
              params.value[0] +
              "<br>" +
              "提交次数: " +
              params.value[1]
            );
          },
        },
        visualMap: {
          min: 0,
          max: submit_max_value,
          calculable: true,
          orient: "vertical",
          left: 0,
          top: 40,
          inRange: {
            color: ["white", "green"],
          },
        },
      };

      this.submitOption && this.submitChart.setOption(this.submitOption);
    },
  },
};
</script>
