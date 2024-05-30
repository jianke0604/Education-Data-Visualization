<template>
  <div style="height: 100%; width: 100%;">
    <div id="submit" style="height: 80%; width: 100%"></div>

  </div>
  
</template>

<script>
import * as echarts from "echarts/core";

export default {
  name: "DateHeatMap",
  data() {
    return {
      data: [],
      knowledge: "total",
      knowledges: [
        "total",
        "r8S3g",
        "r8S3g_l0p5viby",
        "r8S3g_n0m9rsw4",
        "t5V9e",
        "t5V9e_e1k6cixp",
        "m3D1v",
        "m3D1v_r1d7fr3l",
        "m3D1v_v3d9is1x",
        "m3D1v_t0v5ts9h",
        "y9W5d",
        "y9W5d_c0w4mj5h",
        "k4W1c",
        "k4W1c_h5r6nux7",
        "s8Y2f",
        "s8Y2f_v4x8by9j",
        "y9W5d_p8g6dgtv",
        "y9W5d_e2j7p95s",
        "g7R2j",
        "g7R2j_e0v1yls8",
        "g7R2j_j1g8gd3v",
        "b3C9s",
        "b3C9s_l4z6od7y",
        "b3C9s_j0v1yls8"
      ],
    };
  },
  mounted() {
    fetch("../../data/dateheatmap.json")
      .then((response) => response.json())
      .then((data) => {
        this.data = data;
        this.draw('total');
      });
  },
  methods: {
    draw(knowledge) {
      var submitChart = echarts.init(document.getElementById("submit"));

      submitChart.clear();

      var data = [];
      for (let i = 0; i < this.data.length; i++) {
        data.push([this.data[i].date, this.data[i][knowledge]]);
      }

      var start_date = this.data[0].date;
      var end_date = this.data[this.data.length - 1].date;
      var submit_max_value = Math.max.apply(
        Math,
        data.map(function (item) {
          return item[1];
        })
      );

      console.log(
        data.map(function (item) {
          return item[1];
        })
      );

      const option = {
        title: {
          text: "提交次数",
          left: "center",
          top: 0,
          textStyle: {
            color: "white",
            fontSize: 20,
          },
        },
        calendar: {
          top: "20%",
          left: "center",
          range: [start_date, end_date],
          cellSize: [18, 18],
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
            color: "white",
          },
          monthLabel: {
            show: true,
            color: "white",
          },
          yearLabel: {
            show: false,
          },
          itemStyle: {
            color: "rgba(0, 0, 0, 0.0)",
            borderWidth: 5,
            borderColor: "rgba(0, 0, 0, 0.0)",
          },
        },
        visualMap: {
          min: 0,
          max: submit_max_value,
          calculable: true,
          orient: "horizontal",
          left: 'center',
          bottom: 0,
          inRange: {
            color: ["rgba(0, 255, 0, 0.0)", "rgba(0, 255, 0, 0.8)"],
          },
          outOfRange: {
            color: ["rgba(0, 255, 0, 0.0)", "rgba(0, 255, 0, 0.0)"],
          },
          textStyle: {
            color: "white",
          },
        },
        series: {
          type: "heatmap",
          coordinateSystem: "calendar",
          data: data,
          emphasis: {
            itemStyle: {
              shadowBlur: 10,
              shadowColor: "rgba(255, 255, 255, 1)",
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
      };

      option && submitChart.setOption(option);
    },
  },
};
</script>
