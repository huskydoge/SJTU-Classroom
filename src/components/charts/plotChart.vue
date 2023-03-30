<template>
<div style="margin-bottom:20px;display: inline-flex;align-items: center;">
    <button class="viewBtn btn" type="button" @click="changeView('bubble');">今天</button>
    <button class="viewBtn btn" type="button" @click="changeView('bar')">昨天</button>
  <button class="viewBtn btn" type="button" @click="changeView('bar')">前天</button>
  </div>
<div id="stackedArea" style="height: 500px"></div>
</template>

<script>
import * as echarts from 'echarts';
export default {
  name: "stackedAreaChart",
  methods:{
    initChart(){
      var chartDom = document.getElementById('stackedArea');
      var myChart = echarts.init(chartDom);
      var option;
      const data = [["2000-06-05", 116], ["2000-06-06", 129], ["2000-06-07", 135], ["2000-06-08", 86], ["2000-06-09", 73], ["2000-06-10", 85], ["2000-06-11", 73], ["2000-06-12", 68], ["2000-06-13", 92], ["2000-06-14", 130], ["2000-06-15", 245], ["2000-06-16", 139], ["2000-06-17", 115], ["2000-06-18", 111], ["2000-06-19", 309], ["2000-06-20", 206], ["2000-06-21", 137], ["2000-06-22", 128], ["2000-06-23", 85], ["2000-06-24", 94], ["2000-06-25", 71], ["2000-06-26", 106], ["2000-06-27", 84], ["2000-06-28", 93], ["2000-06-29", 85], ["2000-06-30", 73], ["2000-07-01", 83], ["2000-07-02", 125], ["2000-07-03", 107], ["2000-07-04", 82], ["2000-07-05", 44], ["2000-07-06", 72], ["2000-07-07", 106], ["2000-07-08", 107], ["2000-07-09", 66], ["2000-07-10", 91], ["2000-07-11", 92], ["2000-07-12", 113], ["2000-07-13", 107], ["2000-07-14", 131], ["2000-07-15", 111], ["2000-07-16", 64], ["2000-07-17", 69], ["2000-07-18", 88], ["2000-07-19", 77], ["2000-07-20", 83], ["2000-07-21", 111], ["2000-07-22", 57], ["2000-07-23", 55], ["2000-07-24", 60]];
      const dateList = data.map(function (item) {
        return item[0];
      });
      const valueList = data.map(function (item) {
        return item[1];
      });
      option = {
        // Make gradient line here
        visualMap: [
          {
            show: false,
            type: 'continuous',
            seriesIndex: 0,
            min: 0,
            max: 400
          },
          {
            show: false,
            type: 'continuous',
            seriesIndex: 1,
            dimension: 0,
            min: 0,
            max: dateList.length - 1
          }
        ],
        title: [
          {
            left: 'center',
            text: 'Gradient along the y axis'
          },
        ],
        tooltip: {
          trigger: 'axis'
        },
        xAxis: [
          {
            data: dateList
          },
        ],
        yAxis: [
          {},
        ],
        grid: [
          {
            bottom: '60%'
          },
        ],
        series: [
          {
            type: 'line',
            showSymbol: false,
            data: valueList
          },
        ]
      };
      option && myChart.setOption(option);
    },
  },
  mounted() {
    this.initChart()
  }
}
</script>

<style scoped>
.viewBtn{
  color: #fff;
  font-size: 11px;
  width: 80px;
  height: 25px;
  border: 0;
  background-color: rgb(242, 78, 122);
  cursor: pointer;
}

/*按钮当鼠标悬浮时的状态：*/
.btn:hover{
  transform: translateY(-3px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.2);
}

/*当按钮点击时的状态：*/
.btn:active{
  transform: translateY(-1px);
  box-shadow: 0 5px 10px rgba(0,0,0,0.2);
}

.btn:visited{
  text-transform: uppercase;
  text-decoration: none;
  padding: 15px 40px;
  display: inline-block;
  margin-top: 30px;
  transition: all .2s;
  position: relative;
  animation: moveInBottom 1s 0.75s;
  animation-fill-mode: backwards;
}
</style>