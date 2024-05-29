<template>
  <div style="height: 100%; width: 100%;">
    <div id="submit" style="height: 80%; width: 100%"></div>
    <div>
    <select id="select" v-model="knowledge" style="position: relative; left: 10px;">
      <!-- 去除第一个key -->
      <option v-for="(key, index) in knowledges" :key="key" :value="key">{{ key }}</option>
    </select>
  </div>
  </div>
  
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
    this.submitChart = echarts.init(document.getElementById("submit"));

    fetch("../../data/dateheatmap.json")
      .then((response) => response.json())
      .then((data) => {
        this.data = data;
        this.draw('total');
      });
  },
  watch: {
    knowledge: function(newKnowledge) {
      this.draw(newKnowledge);
    }
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
            color: "white",
            fontSize: 20,
          },
        },
        calendar: {
          top: 40,
          left: 50,
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
          calculable: false,
          orient: "horizontal",
          left: 'center',
          bottom: 0,
          inRange: {
            color: ["rgba(0, 255, 0, 0.0)", "rgba(0, 255, 0, 0.8)"],
          },
          outOfRange: {
            color: ["rgba(0, 0, 0, 0.0)"],
          },
          textStyle: {
            color: "white",
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
      };

      this.submitChart.setOption(this.submitOption);
    },
  },
};
</script>
