<template>
  <div v-if="!customChoice">
  <div style="position:fixed; left: 50px;top:150px;display: flex;align-items: center">
    <el-avatar src="https://ts1.cn.mm.bing.net/th/id/R-C.8421fec5bae5300b4ddda08f0b475d33?rik=vRDDRWkv0GEV4w&riu=http%3a%2f%2fwww.acgwow.com%2fimages%2fupload%2f2021071913181768.png&ehk=LhH15PpfhR0yqsERwXOBB0EjUTjw1VWfeo0M7TQbGR8%3d&risl=&pid=ImgRaw&r=0"
    >
    </el-avatar>
    <div style="margin-left: 10px;">
      <el-popover
          placement="bottom-start"
          :width="300"
          trigger="hover"
      >
        <template #reference>
          <el-button>
           <span style="padding: 2px">
             ...
        </span>
          </el-button>
        </template>
        <template #default>
          <div
              class="demo-rich-conent"
              style="display: flex; gap: 10px; flex-direction: column;padding: 20px"
          >
            <div style="display: inline-flex;column-gap: 10px">
              <p style="font-size: 20px;font-weight: 800">帮助与提示</p>
              <help :strokeWidth="2" theme="outline" size="30" fill="#333" strokeLinejoin="bevel" strokeLinecap="square"/>
            </div>
            <div>
              <p

                  style="margin: 0; font-weight: 500"
              >
                基本概念
              </p>
              <p
                  class="demo-rich-content__mention"
                  style="margin: 0; font-size: 14px; color: var(--el-color-info)"
              >
                矩形高低表征数据大小.
              </p>
              <br>
              <p

                  style="margin: 0; font-weight: 500"
              >
                交互
              </p>
              <p
                  class="demo-rich-content__mention"
                  style="margin: 0;margin-top: 4px; font-size: 14px; color: var(--el-color-info)"
              >
                1.用鼠标拖动图表可以放大局部信息.
              </p>
              <p
                  class="demo-rich-content__mention"
                  style="margin: 0;margin-top: 4px; font-size: 14px; color: var(--el-color-info)"
              >
                2.鼠标悬浮可以看到对应的数据大小.
              </p>
              <p
                  class="demo-rich-content__mention"
                  style="margin: 0;margin-top: 4px; font-size: 14px; color: var(--el-color-info)"
              >
                3.鼠标单击可以放大对应的信息.
              </p>
              <p
                  class="demo-rich-content__mention"
                  style="margin: 0;margin-top: 4px; font-size: 14px; color: var(--el-color-info)"
              >
                4.鼠标双击可以进入对应的教室界面.
              </p>
              <p
                  class="demo-rich-content__mention"
                  style="margin: 0;margin-top: 4px; font-size: 14px; color: var(--el-color-info)"
              >
                5.点击右侧的标签栏可以切换不同的数据类型.
              </p>

            </div>

            <p class="demo-rich-content__desc" style="margin: 0">
              Navi Group, SJTU
            </p>
          </div>
        </template>
      </el-popover>
    </div>
  </div>
  <nav style="position:fixed;top:100px;right: 200px">
    <el-tabs tab-position="right" v-model="activeName">
      <el-tab-pane label="座位数" name="seats" >
      </el-tab-pane>
      <el-tab-pane label="空位数" name="vacancy" >
      </el-tab-pane>
      <el-tab-pane label="实时人数" name="people">
      </el-tab-pane>
      <el-tab-pane label="CO2浓度" name="co2">
      </el-tab-pane>
      <el-tab-pane label="PM2.5浓度" name="pm25">
      </el-tab-pane>
      <el-tab-pane label="空气湿度" name="humidity"></el-tab-pane>
      <el-tab-pane label="温度" name="temperature"></el-tab-pane>
    </el-tabs>
  </nav>
  <div id="barGraph" style="height: 600px;"></div>
  </div>
  <div v-if="customChoice" style="display: flex;flex-direction: column;align-items: center">
    <nav style="transform: translateX(-40px);">
      <el-tabs tab-position="top" v-model="activeName">
        <el-tab-pane label="座位数" name="seats" >
        </el-tab-pane>
        <el-tab-pane label="空位数" name="vacancy" >
        </el-tab-pane>
        <el-tab-pane label="实时人数" name="people">
        </el-tab-pane>
        <el-tab-pane label="CO2浓度" name="co2">
        </el-tab-pane>
        <el-tab-pane label="PM2.5浓度" name="pm25">
        </el-tab-pane>
        <el-tab-pane label="空气湿度" name="humidity"></el-tab-pane>
        <el-tab-pane label="温度" name="temperature"></el-tab-pane>
      </el-tabs>
    </nav>
    <div id="barGraph" style="height: 600px;"></div>
  </div>
</template>

<script>
import {Help} from '@icon-park/vue-next'
import * as echarts from 'echarts';
import axios from "axios";
export default {
  name: "barBelowSearch",
  props:{
    customChoice: Boolean,
    dataFromSearch: Array,
  },
  data(){
    return {
      unit: '个',
      activeTitle:'座位数情况',
      symmetric: true,
      prefix: '座位数：',
      suffix: '',
      classroomData:[],
      classroomDataToSort:[],
      activeName: 'seats',
      xAxis: [],
      dataSet:[],
    }
  },
  components:{
    Help,
  },
  methods:{
    judgeNull(str){
      if(str === 'NONE' || str === 'None' || str === 'NaN' || str === undefined){
        return 0;
      } else {
        return str;
      }
    },
    fetchData(){ // 要先在终端运行 node app.js
      function handleCo2(str='0PPM') {
        if (str == 'None' || str == 'NONE' || str == undefined) {
          return 0;
        }
        let pos = str.lastIndexOf("PPM");
        let num = str.slice(0, pos);
        return num;
      }
      function handlePm25(str='0μg'){
        if(str === 'None'){return 0}
        let pos = str.lastIndexOf("μg");
        let num = str.slice(0,pos);
        return num;
      }
      function handleTemperature(str = '0℃'){
        if(str === 'None'){return 0}
        let pos = str.lastIndexOf("℃");
        let num = str.slice(0,pos);
        return num;
      }
      function handleHumidity(str='0%'){
        if(str === 'None'){return 0}
        let pos = str.lastIndexOf("%");
        let num = str.slice(0,pos);
        return num;
      }
      this.classRoomData = [];
      axios.get('http://127.0.0.1/getAllClassroom').then(res=>{
        let cnt = 1; // index
        let tmp = [];
        for(const i in res.data){
          let obj = {
            depth: 1,
            id: 'classroom.' + res.data[i]['教室名'],
            index: cnt,
            vacancy: this.judgeNull(res.data[i]['座位数'])- this.judgeNull(res.data[i]['实到人数']),
            name: res.data[i]['教室名'],
            seats: this.judgeNull(res.data[i]['座位数']),
            people: this.judgeNull(res.data[i]['实到人数']),
            co2: handleCo2(res.data[i]['CO2浓度']),
            pm25:handlePm25(res.data[i]['PM25浓度']),
            temperature:handleTemperature(res.data[i]['温度']),
            humidity: handleHumidity(res.data[i]['空气湿度']),
          };
          tmp.push(obj);
          ++ cnt;
        }
        this.classroomData = tmp;
      }).catch(err=>{
        console.log("获取数据失败" + err);
      });
    },
    renderBar(){
      if(this.activeName === 'seats'){
        this.renderSeats();
      } else if(this.activeName === 'vacancy'){
        this.renderVacancy();
      } else if(this.activeName === 'people'){
        this.renderPeople();
      } else if(this.activeName === 'co2'){
        this.renderCo2();
      } else if(this.activeName === 'pm25'){
        this.renderPm25();
      } else if(this.activeName === 'humidity'){
        this.renderHumidity();
      } else {
        this.renderTemperature();
      }
      console.log('renderBar');
      console.log(this.dataSet);
      console.log(this.xAxis);
    },
    renderSeats(){
      this.classroomDataToSort = this.classroomData;
      this.classroomDataToSort.sort(function (a,b){
        return b.seats - a.seats;
      })
      this.dataSet = [];
      this.xAxis = [];
      let length = this.classroomDataToSort.length;
      if(this.symmetric) {
        for (let i = 0; i < length; ++i) {
          if (i % 2) {
            this.dataSet.push(this.classroomDataToSort[i].seats);
            this.xAxis.push(this.classroomDataToSort[i].name);
          } else {
            this.dataSet.unshift(this.classroomDataToSort[i].seats);
            this.xAxis.unshift(this.classroomDataToSort[i].name);
          }
        }
      } else {
        for (let i = 0; i < length; ++i) {
          this.dataSet.push(this.classroomDataToSort[i].seats);
          this.xAxis.push(this.classroomDataToSort[i].name);
        }
      }
    },
    renderVacancy(){
      this.classroomDataToSort = this.classroomData;
      this.classroomDataToSort.sort(function (a,b){
        return b.vacancy - a.vacancy;
      })
      this.xAxis = [];this.dataSet = [];
      let length = this.classroomDataToSort.length;
      if(this.symmetric) {
        for (let i = 0; i < length; ++i) {
          if (i % 2) {
            this.dataSet.push(this.classroomDataToSort[i].vacancy);
            this.xAxis.push(this.classroomDataToSort[i].name);
          } else {
            this.dataSet.unshift(this.classroomDataToSort[i].vacancy);
            this.xAxis.unshift(this.classroomDataToSort[i].name);
          }
        }
      } else {
        for (let i = 0; i < length; ++i) {
          this.dataSet.push(this.classroomDataToSort[i].vacancy);
          this.xAxis.push(this.classroomDataToSort[i].name);
        }
      }
    },
    renderPeople(){
      this.classroomDataToSort = this.classroomData;
      this.classroomDataToSort.sort(function (a,b){
        return b.people - a.people;
      })

      this.xAxis = [];this.dataSet = [];
      let length = this.classroomDataToSort.length;
      if(this.symmetric) {
        for (let i = 0; i < length; ++i) {
          if (i % 2) {
            this.dataSet.push(this.classroomDataToSort[i].people);
            this.xAxis.push(this.classroomDataToSort[i].name);
          } else {
            this.dataSet.unshift(this.classroomDataToSort[i].people);
            this.xAxis.unshift(this.classroomDataToSort[i].name);
          }
        }
      } else {
        for (let i = 0; i < length; ++i) {
          this.dataSet.push(this.classroomDataToSort[i].people);
          this.xAxis.push(this.classroomDataToSort[i].name);
        }
      }
    },
    renderCo2(){
      this.classroomDataToSort = this.classroomData;
      this.classroomDataToSort.sort(function (a,b){
        return b.co2 - a.co2;
      })

      this.xAxis = [];this.dataSet = [];
      let length = this.classroomDataToSort.length;
      if(this.symmetric) {
        for (let i = 0; i < length; ++i) {
          if (i % 2) {
            this.dataSet.push(this.classroomDataToSort[i].co2);
            this.xAxis.push(this.classroomDataToSort[i].name);
          } else {
            this.dataSet.unshift(this.classroomDataToSort[i].co2);
            this.xAxis.unshift(this.classroomDataToSort[i].name);
          }
        }
      } else {
        for (let i = 0; i < length; ++i) {
          this.dataSet.push(this.classroomDataToSort[i].co2);
          this.xAxis.push(this.classroomDataToSort[i].name);
        }
      }
    },
    renderPm25(){
      this.classroomDataToSort = this.classroomData;
      this.classroomDataToSort.sort(function (a,b){
        return b.pm25 - a.pm25;
      })
      this.xAxis = [];this.dataSet = [];
      let length = this.classroomDataToSort.length;
      if(this.symmetric) {
        for (let i = 0; i < length; ++i) {
          if (i % 2) {
            this.dataSet.push(this.classroomDataToSort[i].pm25);
            this.xAxis.push(this.classroomDataToSort[i].name);
          } else {
            this.dataSet.unshift(this.classroomDataToSort[i].pm25);
            this.xAxis.unshift(this.classroomDataToSort[i].name);
          }
        }
      } else {
        for (let i = 0; i < length; ++i) {
          this.dataSet.push(this.classroomDataToSort[i].pm25);
          this.xAxis.push(this.classroomDataToSort[i].name);
        }
      }
    },
    renderHumidity(){
      this.classroomDataToSort = this.classroomData;
      this.classroomDataToSort.sort(function (a,b){
        return b.humidity - a.humidity;
      })

      this.xAxis = [];this.dataSet = [];
      let length = this.classroomDataToSort.length;
      if(this.symmetric) {
        for (let i = 0; i < length; ++i) {
          if (i % 2) {
            this.dataSet.push(this.classroomDataToSort[i].humidity);
            this.xAxis.push(this.classroomDataToSort[i].name);
          } else {
            this.dataSet.unshift(this.classroomDataToSort[i].humidity);
            this.xAxis.unshift(this.classroomDataToSort[i].name);
          }
        }
      } else {
        for (let i = 0; i < length; ++i) {
          this.dataSet.push(this.classroomDataToSort[i].humidity);
          this.xAxis.push(this.classroomDataToSort[i].name);
        }
      }
    },
    renderTemperature(){
      this.classroomDataToSort = this.classroomData;
      this.classroomDataToSort.sort(function (a,b){
        return b.temperature - a.temperature;
      })

      this.xAxis = [];this.dataSet = [];
      let length = this.classroomDataToSort.length;
      if(this.symmetric) {
        for (let i = 0; i < length; ++i) {
          if (i % 2) {
            this.dataSet.push(this.classroomDataToSort[i].temperature);
            this.xAxis.push(this.classroomDataToSort[i].name);
          } else {
            this.dataSet.unshift(this.classroomDataToSort[i].temperature);
            this.xAxis.unshift(this.classroomDataToSort[i].name);
          }
        }
      } else {
        for (let i = 0; i < length; ++i) {
          this.dataSet.push(this.classroomDataToSort[i].temperature);
          this.xAxis.push(this.classroomDataToSort[i].name);
        }
      }
    },
    changeString(){
      if(this.activeName == 'seats'){
        this.prefix = '座位数:'
        this.suffix = '';
        this.activeTitle = '座位数情况';
        this.unit='个';
      } else if(this.activeName == 'vacancy'){
        this.prefix = '空位数:'
        this.suffix = '';
        this.activeTitle = '空位数情况';
        this.unit='个';
      }else if(this.activeName == 'people'){
        this.prefix = '当前人数:'
        this.suffix = '';
        this.activeTitle = '人数情况';
        this.unit='人';
      }else if(this.activeName == 'co2'){
        this.prefix = 'co2浓度:'
        this.suffix = 'PPM';
        this.activeTitle = 'CO2浓度';
        this.unit='PPM';
      }else if(this.activeName == 'pm25'){
        this.prefix = 'PM2.5浓度:'
        this.suffix = 'μg'
        this.activeTitle = 'PM2.5浓度';
        this.unit='μg';
      }else if(this.activeName == 'humidity'){
        this.prefix = '湿度:'
        this.suffix = '%'
        this.activeTitle = '湿度情况';
        this.unit='%';
      }else {
        this.prefix = '温度:'
        this.suffix='℃'
        this.activeTitle = '温度情况';
        this.unit='℃';
      }
    },
    initChart(){
      var chartDom = document.getElementById('barGraph');
      var myChart = echarts.init(chartDom);
      var option;
      var prefix = this.prefix;
      var suffix = this.suffix;
      let dataAxis = this.xAxis;
      console.log(dataAxis);
      let data = this.dataSet;
      console.log(data);
      // let yMax = 500;
      // let dataShadow = [];
      // for (let i = 0; i < data.length; i++) {
      //   dataShadow.push(yMax);
      // }
      option = {
        title: {
          text: this.activeTitle,
        },
        tooltip: {
          axisPointer: {
            type: 'shadow'
          },
          formatter: function (params) {
            return prefix + data[params.dataIndex] + suffix;
          }
        },
        xAxis: {
          data: dataAxis,
          axisLabel: {
            rotate: 45
          },
          axisTick: {
            show: false
          },
          axisLine: {
            show: false
          },
          z: 10
        },
        yAxis: {
          axisLine: {
            show: true
          },
          axisTick: {
            show: true
          },
          axisLabel: {
            color: '#999',
            formatter: '{value}' + this.unit,
          }
        },
        dataZoom: [
          {
            type: 'inside'
          }
        ],
        series: [
          {
            type: 'bar',
            showBackground: true,
            itemStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                { offset: 0, color: '#e9c46a' },
                { offset: 0.5, color: '#f4a261' },
                { offset: 1, color: '#e76f51' }
              ])
            },
            emphasis: {
              itemStyle: {
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  { offset: 0, color: '#264653' },
                  { offset: 0.7, color: '#2a9d8f' },
                  { offset: 1, color: '#e9c46a' }
                ]),
              }
            },
            data: data
          }
        ]
      };
// Enable data zoom when user click bar.
      const zoomSize = 6;
      var timeId;
      var times = 0;
      myChart.on('click', function (params) {
        clearTimeout(timeId);
        timeId = setTimeout(function () {
          myChart.dispatchAction({
            type: 'dataZoom',
            startValue: dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)],
            endValue:
                dataAxis[Math.min(params.dataIndex + zoomSize / 2, data.length - 1)]
          });
        }, 200)
      });
      myChart.on('dblclick',function (params) {
        clearTimeout(timeId);
        if(!times) {
          times = 1;
          window.displayInfo(dataAxis[params.dataIndex]);
        } else {
          times = 0;
        }
      })

      option && myChart.setOption(option);

    },
    showClassInfoFromBar(name){
      this.$emit("showClassInfo",name);
    },
  },
  created() {
    window.displayInfo = this.showClassInfoFromBar; // 和另一个bubble图做区分
  },
  mounted() {
    this.initChart();
    this.fetchData();
  },
  watch:{
    activeName(){
      this.changeString();
      this.renderBar();
      this.initChart();
    },
    classroomData(){
      this.renderBar();
      this.initChart();
    },
    dataFromSearch(){
      function handleCo2(str='0PPM') {
        if (str == 0 || str == 'None' || str == 'NONE' || str == undefined) {
          return 0;
        }
        let pos = str.lastIndexOf("PPM");
        let num = str.slice(0, pos);
        return num;
      }
      function handlePm25(str='0μg'){
        if(str == 0 ||str === 'None'){return 0}
        let pos = str.lastIndexOf("μg");
        let num = str.slice(0,pos);
        return num;
      }
      function handleTemperature(str = '0℃'){
        if(str == 0 ||str === 'None'){return 0}
        let pos = str.lastIndexOf("℃");
        let num = str.slice(0,pos);
        return num;
      }
      function handleHumidity(str='0%'){
        if(str == 0 || str === 'None'){return 0}
        let pos = str.lastIndexOf("%");
        let num = str.slice(0,pos);
        return num;
      }
      let search = this.dataFromSearch;
      let tmp = [];
      for(let i in this.dataFromSearch){
        let obj = {
          vacancy: this.judgeNull(search[i].vacancy),
          name: search[i].name,
          seats: this.judgeNull(search[i].seats),
          people: this.judgeNull(search[i].people),
          co2: handleCo2(search[i].co2),
          pm25:handlePm25(search[i].pm25),
          temperature:handleTemperature(search[i].temperature),
          humidity: handleHumidity(search[i].humidity),
        };
        tmp.push(obj);
      }
      this.classroomData = tmp;
      this.renderBar();
      this.initChart();
    },
  }
}
</script>

<style scoped>
#barGraph{
  width: 1000px;
  height: 800px;
  margin-top: 70px;
}
</style>