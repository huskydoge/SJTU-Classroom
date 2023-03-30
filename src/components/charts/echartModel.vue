<template>
<div id = "Yourchart"></div>
<!--  id 用于选择图表加载的容器-->
</template>

<script>
import * as echarts from "echarts";
export default {
  name: "echartModel",
  data(){
    return{
      写变量
    }
  },
  mounted() {
    // 页面加载时执行的函数
    this.initChart()
  },
  methods:{
    // 写函数，函数如果要用到data里的变量格式为：this.varname
    initChart(){}
  }
}
</script>

<style scoped>

</style>