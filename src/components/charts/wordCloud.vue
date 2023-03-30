<template>
  <div id="wordCloud" class="wordCloud">
  </div>
</template>


<script>
import * as echarts from 'echarts';
import "echarts-wordcloud/dist/echarts-wordcloud";
import "echarts-wordcloud/dist/echarts-wordcloud.min";
import {DatasetComponent, TooltipComponent, VisualMapComponent} from "echarts/components";
import {CustomChart} from "echarts/charts";
import {CanvasRenderer} from "echarts/renderers";
echarts.use([
  DatasetComponent,
  TooltipComponent,
  VisualMapComponent,
  CustomChart,
  CanvasRenderer
]);
export default {
  props:{
    words: Array,
  },
  data() {
    return {
      wordList:[
        {
          name: "正在加载",
          value: 15000
        },
        {
          name: "正在加载",
          value: 10081
        },
        {
          name: "正在加载",
          value: 9386
        },
        {
          name: "正在加载",
          value: 7500
        },
        {
          name: "别急",
          value: 7500
        },
        {
          name: "赶来路上",
          value: 6500
        },
        {
          name: "别急",
          value: 6500
        },
        {
          name: "来啦",
          value: 6000
        },
        {
          name: "来啦",
          value: 4500
        },
        {
          name: "别急",
          value: 3800
        },
        {
          name: "急也没用",
          value: 3000
        },
        {
          name: "急也没用",
          value: 2500
        },
        {
          name: "急也没用",
          value: 2300
        },
        {
          name: "快好啦",
          value: 2000
        },
        {
          name: "快好啦",
          value: 1900
        },
        {
          name: "马上好",
          value: 1800
        },
      ]
    }
  },
  mounted(){

    this.initChart();
  },
  methods:{
    initChart(){
      var chartDom = document.getElementById('wordCloud');
      var myChart = echarts.init(chartDom);
      myChart.setOption({
        tooltip: {
          show: true,
        }, // 决定鼠标悬浮是否显示信息,
        series: [
          {
            type: "wordCloud",
            //用来调整词之间的距离
            gridSize: 10,
            //用来调整字的大小范围
            // Text size range which the value in data will be mapped to.
            // Default to have minimum 12px and maximum 60px size.
            sizeRange: [14, 60],
            // Text rotation range and step in degree. Text will be rotated randomly in range [-90,                                                                             90] by rotationStep 45
            //用来调整词的旋转方向，，[0,0]--代表着没有角度，也就是词为水平方向，需要设置角度参考注释内容
            // rotationRange: [-45, 0, 45, 90],
            // rotationRange: [ 0,90],
            rotationRange: [0, 0],
            //随机生成字体颜色
            // maskImage: maskImage,
            textStyle: {
              normal: {
                color: function() {
                  return (
                      "rgb(" +
                      Math.round(Math.random() * 255) +
                      ", " +
                      Math.round(Math.random() * 255) +
                      ", " +
                      Math.round(Math.random() * 255) +
                      ")"
                  );
                }
              }
            },
            //位置相关设置
            // Folllowing left/top/width/height/right/bottom are used for positioning the word cloud
            // Default to be put in the center and has 75% x 80% size.
            left: "center",
            top: "center",
            right: null,
            bottom: null,
            width: "200%",
            height: "200%",
            //数据
            data: this.wordList
          }
        ]
      });
      // myChart.on('click',function (params){
      //   // console.log(params.data.name);
      //   console.log(params.data.value);
      // })
    }
  },
  watch:{
    words(){
      this.wordList = this.words;
      setTimeout( this.initChart, 1000 )
    }
  }
}
</script>

<style scoped>
.wordCloud{
  width:100%;
  height:300px;
  margin:auto 0;
}
</style>

<style scoped>

</style>