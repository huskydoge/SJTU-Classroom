<template>
  <!--  <input type="button" @click="up">-->
 <div v-if="check">
   <div  id="calendar" :style="{ width: '100%', height: '200px' }"></div>
 </div>
</template>

<script>
// 要往组件里传数据
import * as echarts from "echarts";
export default {
  name: "calendarMap",
  props:{
    displayHeatMap:Boolean,
  },
  data(){
    return{
      option : {
        title: {
          top: 30,
          left: 'center',
          text: '每日人流量热力图' // 标题
        },
        tooltip: {},
        visualMap: {
          min: 0,
          max: 10000,
          type: 'piecewise',
          orient: 'horizontal',
          left: 'center',
          top: 65
        },
        calendar: {
          top: 120,
          left: 30,
          right: 30,
          cellSize: ['auto', 13],
          range: '2016',
          itemStyle: {
            borderWidth: 0.5
          },
          yearLabel: { show: false }
        },
        series: {
          type: 'heatmap',
          coordinateSystem: 'calendar',
          data: this.getVirtulData('2016')
        }
      },
      init: this.initChart(),
      check: this.displayHeatMap,
    }
  },
  mounted(){
    this.initChart()
  },
  methods:{
    getVirtulData(year) {
      year = year || '2017';
      var date = +echarts.number.parseDate(year + '-01-01');
      var end = +echarts.number.parseDate(+year + 1 + '-01-01');
      var dayTime = 3600 * 24 * 1000;
      var data = [];
      for (var time = date; time < end; time += dayTime) {
        data.push([
          echarts.format.formatTime('yyyy-MM-dd', time),
          Math.floor(Math.random() * 10000)
        ]);
      }
      return data;
    },
    initChart(){
      this.$nextTick(()=>
      {
        var chartDom = document.getElementById("calendar");
        var myChart = echarts.init(chartDom);
        this.getVirtulData();
        this.option && myChart.setOption(this.option,true);

      })
    },
    up(){
      this.initChart();
    }
  },
  watch: {
    displayHeatMap(val){
      this.check = val;
      this.up();
    },
    immediate: true,
  }
}
</script>
