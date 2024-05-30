<template>
  <div id="diff" style="height: 80%; width: 100%%"></div>
</template>

<script>
import * as echarts from "echarts";

export default {
  name: "Diff",
  data() {
    return {
      difficultyChart: null,
      difficultyOption: null,
      knowledges: {},
      subknowledges: {},
      data: {},
      features: {},
    };
  },
  mounted() {
    this.difficultyChart = echarts.init(document.getElementById("diff"));
    fetch("../../data/Data_Titleinfo.csv")
      .then(response => response.text())
      .then(data => {
        this.csv2json(data);
      })
      .then(
        fetch("../../data/submit_features.json")
          .then((response) => response.json())
          .then((data) => {
            this.features = data;
          })
      )
      .then(
        fetch("../../data/question_pass_rate.json")
          .then((response) => response.json())
          .then((data) => {
            this.data = this.parseData(data);
            console.log(this.data);
            this.draw();
          })
      );
  },
  methods: {
    csv2json(csv) {
      var lines = csv.split("\n");
      var result = [];
      var headers = lines[0].split(",");
      for (var i = 1; i < lines.length; i++) {
        var items = lines[i].split(",");
        var title = items[1];
        var knowledge = items[3];
        var subknowledge = items[4];
        if (knowledge in this.knowledges) {
          this.knowledges[knowledge].push(title);
        } else {
          this.knowledges[knowledge] = [title];
        }
        if (subknowledge in this.subknowledges) {
          this.subknowledges[subknowledge].push(title);
        } else {
          this.subknowledges[subknowledge] = [title];
        }
      }
      return result;
    },

    parseData(data) {
      var result = {};
      var knowledges = Object.keys(this.knowledges);
      knowledges.forEach((knowledge) => {
        result[knowledge] = {};
        for (var j = 0; j < this.knowledges[knowledge].length; j++) {
          var title = this.knowledges[knowledge][j];
          result[knowledge][title] = data[title];
        }
      });
      return result;
    },

    draw() {
      var self = this;
      // 单轴散点图
      var data = this.data;
      var title = [];
      var singleAxis = [];
      var series = [];

      var knowledge_names = Object.keys(this.knowledges);
      knowledge_names.forEach((name, idx) => {
        title.push({
          textBaseline: "middle",
          top: (idx + 0.5) * 100 / knowledge_names.length + "%",
          text: name,
          textStyle: {
            fontSize: 13,
            color: "white",
          },
        });
        singleAxis.push({
          left: "20%",
          type: "value",
          boundaryGap: false,
          min: 0,
          max: 1,
          top: (idx * 100) / knowledge_names.length + 3 + "%",
          height: (100 / knowledge_names.length - 10) + "%",
          axisLabel: {
            interval: 0,
          },
        });
        series.push({
          singleAxisIndex: idx,
          coordinateSystem: "singleAxis",
          type: "scatter",
          data: this.knowledges[name].map((title) => {
            return [data[name][title], title];
          }),
          symbolSize: function (dataItem) {
            return self.features[dataItem[1]]["total"] / 500;
          },
        });
      });

      this.difficultyOption = {
        title: title,
        tooltip: {
          position: "top",
          formatter: function (params) {
            return (
              "题目: " +
              params.value[1] +
              "<br>知识点: " +
              params.seriesName +
              "<br>提交次数: " +
              self.features[params.value[1]]["total"] +
              "<br>准确率: " +
              params.value[0]
            );
          },
        },
        singleAxis: singleAxis,
        series: series,
      };

      this.difficultyChart.setOption(this.difficultyOption);
    },
  },
};
</script>