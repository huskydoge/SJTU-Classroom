<template>
  <div style="display: grid; grid-template-columns: 1fr 1fr">
  <div id="people" style="height: 300px; width:100%"></div>
  <div id="co2" style="height: 300px; width: 100%"></div>
  <div id="pm25" style="height: 300px; width: 100%"></div>
  <div id="humidity" style="height: 300px; width: 100%"></div>
  </div>
  <div id="temperature" style="height: 300px; width: 100%"></div>
  <div style="margin-bottom: 50px"></div>
</template>

<script>
import * as echarts from 'echarts';
import axios from "axios";
export default {
  name: "stackedAreaChart",
  props:{
    classname: String,
  },
  data(){
    return{
      themes:{
        "color": [
          "#c12e34",
          "#e6b600",
          "#0098d9",
          "#2b821d",
          "#005eaa",
          "#339ca8",
          "#cda819",
          "#32a487"
        ],
        "backgroundColor": "rgba(0,0,0,0)",
        "textStyle": {},
        "title": {
          "textStyle": {
            "color": "#333333"
          },
          "subtextStyle": {
            "color": "#aaaaaa"
          }
        },
        "line": {
          "itemStyle": {
            "borderWidth": 1
          },
          "lineStyle": {
            "width": 2
          },
          "symbolSize": 4,
          "symbol": "emptyCircle",
          "smooth": false
        },
        "radar": {
          "itemStyle": {
            "borderWidth": 1
          },
          "lineStyle": {
            "width": 2
          },
          "symbolSize": 4,
          "symbol": "emptyCircle",
          "smooth": false
        },
        "bar": {
          "itemStyle": {
            "barBorderWidth": 0,
            "barBorderColor": "#ccc"
          }
        },
        "pie": {
          "itemStyle": {
            "borderWidth": 0,
            "borderColor": "#ccc"
          }
        },
        "scatter": {
          "itemStyle": {
            "borderWidth": 0,
            "borderColor": "#ccc"
          }
        },
        "boxplot": {
          "itemStyle": {
            "borderWidth": 0,
            "borderColor": "#ccc"
          }
        },
        "parallel": {
          "itemStyle": {
            "borderWidth": 0,
            "borderColor": "#ccc"
          }
        },
        "sankey": {
          "itemStyle": {
            "borderWidth": 0,
            "borderColor": "#ccc"
          }
        },
        "funnel": {
          "itemStyle": {
            "borderWidth": 0,
            "borderColor": "#ccc"
          }
        },
        "gauge": {
          "itemStyle": {
            "borderWidth": 0,
            "borderColor": "#ccc"
          }
        },
        "candlestick": {
          "itemStyle": {
            "color": "#c12e34",
            "color0": "#2b821d",
            "borderColor": "#c12e34",
            "borderColor0": "#2b821d",
            "borderWidth": 1
          }
        },
        "graph": {
          "itemStyle": {
            "borderWidth": 0,
            "borderColor": "#ccc"
          },
          "lineStyle": {
            "width": 1,
            "color": "#aaa"
          },
          "symbolSize": 4,
          "symbol": "emptyCircle",
          "smooth": false,
          "color": [
            "#c12e34",
            "#e6b600",
            "#0098d9",
            "#2b821d",
            "#005eaa",
            "#339ca8",
            "#cda819",
            "#32a487"
          ],
          "label": {
            "color": "#eee"
          }
        },
        "map": {
          "itemStyle": {
            "areaColor": "#ddd",
            "borderColor": "#eee",
            "borderWidth": 0.5
          },
          "label": {
            "color": "#c12e34"
          },
          "emphasis": {
            "itemStyle": {
              "areaColor": "#e6b600",
              "borderColor": "#ddd",
              "borderWidth": 1
            },
            "label": {
              "color": "#c12e34"
            }
          }
        },
        "geo": {
          "itemStyle": {
            "areaColor": "#ddd",
            "borderColor": "#eee",
            "borderWidth": 0.5
          },
          "label": {
            "color": "#c12e34"
          },
          "emphasis": {
            "itemStyle": {
              "areaColor": "#e6b600",
              "borderColor": "#ddd",
              "borderWidth": 1
            },
            "label": {
              "color": "#c12e34"
            }
          }
        },
        "categoryAxis": {
          "axisLine": {
            "show": true,
            "lineStyle": {
              "color": "#333"
            }
          },
          "axisTick": {
            "show": true,
            "lineStyle": {
              "color": "#333"
            }
          },
          "axisLabel": {
            "show": true,
            "color": "#333"
          },
          "splitLine": {
            "show": false,
            "lineStyle": {
              "color": [
                "#ccc"
              ]
            }
          },
          "splitArea": {
            "show": false,
            "areaStyle": {
              "color": [
                "rgba(250,250,250,0.3)",
                "rgba(200,200,200,0.3)"
              ]
            }
          }
        },
        "valueAxis": {
          "axisLine": {
            "show": true,
            "lineStyle": {
              "color": "#333"
            }
          },
          "axisTick": {
            "show": true,
            "lineStyle": {
              "color": "#333"
            }
          },
          "axisLabel": {
            "show": true,
            "color": "#333"
          },
          "splitLine": {
            "show": true,
            "lineStyle": {
              "color": [
                "#ccc"
              ]
            }
          },
          "splitArea": {
            "show": false,
            "areaStyle": {
              "color": [
                "rgba(250,250,250,0.3)",
                "rgba(200,200,200,0.3)"
              ]
            }
          }
        },
        "logAxis": {
          "axisLine": {
            "show": true,
            "lineStyle": {
              "color": "#333"
            }
          },
          "axisTick": {
            "show": true,
            "lineStyle": {
              "color": "#333"
            }
          },
          "axisLabel": {
            "show": true,
            "color": "#333"
          },
          "splitLine": {
            "show": true,
            "lineStyle": {
              "color": [
                "#ccc"
              ]
            }
          },
          "splitArea": {
            "show": false,
            "areaStyle": {
              "color": [
                "rgba(250,250,250,0.3)",
                "rgba(200,200,200,0.3)"
              ]
            }
          }
        },
        "timeAxis": {
          "axisLine": {
            "show": true,
            "lineStyle": {
              "color": "#333"
            }
          },
          "axisTick": {
            "show": true,
            "lineStyle": {
              "color": "#333"
            }
          },
          "axisLabel": {
            "show": true,
            "color": "#333"
          },
          "splitLine": {
            "show": true,
            "lineStyle": {
              "color": [
                "#ccc"
              ]
            }
          },
          "splitArea": {
            "show": false,
            "areaStyle": {
              "color": [
                "rgba(250,250,250,0.3)",
                "rgba(200,200,200,0.3)"
              ]
            }
          }
        },
        "toolbox": {
          "iconStyle": {
            "borderColor": "#06467c"
          },
          "emphasis": {
            "iconStyle": {
              "borderColor": "#4187c2"
            }
          }
        },
        "legend": {
          "textStyle": {
            "color": "#333333"
          }
        },
        "tooltip": {
          "axisPointer": {
            "lineStyle": {
              "color": "#cccccc",
              "width": 1
            },
            "crossStyle": {
              "color": "#cccccc",
              "width": 1
            }
          }
        },
        "timeline": {
          "lineStyle": {
            "color": "#005eaa",
            "width": 1
          },
          "itemStyle": {
            "color": "#005eaa",
            "borderWidth": 1
          },
          "controlStyle": {
            "color": "#005eaa",
            "borderColor": "#005eaa",
            "borderWidth": 0.5
          },
          "checkpointStyle": {
            "color": "#005eaa",
            "borderColor": "#316bc2"
          },
          "label": {
            "color": "#005eaa"
          },
          "emphasis": {
            "itemStyle": {
              "color": "#005eaa"
            },
            "controlStyle": {
              "color": "#005eaa",
              "borderColor": "#005eaa",
              "borderWidth": 0.5
            },
            "label": {
              "color": "#005eaa"
            }
          }
        },
        "visualMap": {
          "color": [
            "#1790cf",
            "#a2d4e6"
          ]
        },
        "dataZoom": {
          "backgroundColor": "rgba(47,69,84,0)",
          "dataBackgroundColor": "rgba(47,69,84,0.3)",
          "fillerColor": "rgba(167,183,204,0.4)",
          "handleColor": "#a7b7cc",
          "handleSize": "100%",
          "textStyle": {
            "color": "#333333"
          }
        },
        "markPoint": {
          "label": {
            "color": "#eee"
          },
          "emphasis": {
            "label": {
              "color": "#eee"
            }
          }
        }
      }
      ,
      days : ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun'],
      hours: ['8a', '9a', '10a', '11a', '12a', '1p', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p', '10p', '11p'],
      translation: {Mon: '周一', Tue: '周二', Wed: '周三', Thur: '周四', Fri :'周五', Sat: '周六', Sun: '周日'},
      // 人数
      peopleFlag: false,
      peopleTitle: '一周人数变化图',
      peopleDailyData: [],
      peopleWeekData: [["Mon", 116], ["Tue", 129], ["Wed", 135], ["Thur", 86], ["Fri", 73], ["Sat", 85], ["Sun", 73]],
      peopleData: [["Mon", 116], ["Tue", 129], ["Wed", 135], ["Thur", 86], ["Fri", 73], ["Sat", 85], ["Sun", 73]],

      // CO2
      co2Flag: false,
      co2Title: '一周CO2浓度变化图',
      co2DailyData: [],
      co2WeekData: [["Mon", 116], ["Tue", 129], ["Wed", 135], ["Thur", 86], ["Fri", 73], ["Sat", 85], ["Sun", 73]],
      co2Data: [["Mon", 116], ["Tue", 129], ["Wed", 135], ["Thur", 86], ["Fri", 73], ["Sat", 85], ["Sun", 73]],

      // PM25
      pm25Flag: false,
      pm25Title: '一周PM2.5浓度变化图',
      pm25DailyData: [],
      pm25WeekData: [["Mon", 116], ["Tue", 129], ["Wed", 135], ["Thur", 86], ["Fri", 73], ["Sat", 85], ["Sun", 73]],
      pm25Data: [["Mon", 116], ["Tue", 129], ["Wed", 135], ["Thur", 86], ["Fri", 73], ["Sat", 85], ["Sun", 73]],

      // temperature
      temperatureFlag: false,
      temperatureTitle: '一周教室温度变化图',
      temperatureDailyData: [],
      temperatureWeekData: [["Mon", 116], ["Tue", 129], ["Wed", 135], ["Thur", 86], ["Fri", 73], ["Sat", 85], ["Sun", 73]],
      temperatureData: [["Mon", 116], ["Tue", 129], ["Wed", 135], ["Thur", 86], ["Fri", 73], ["Sat", 85], ["Sun", 73]],

      // humidity
      humidityFlag: false,
      humidityTitle: '一周空气湿度变化图',
      humidityDailyData: [],
      humidityWeekData: [["Mon", 116], ["Tue", 129], ["Wed", 135], ["Thur", 86], ["Fri", 73], ["Sat", 85], ["Sun", 73]],
      humidityData: [["Mon", 116], ["Tue", 129], ["Wed", 135], ["Thur", 86], ["Fri", 73], ["Sat", 85], ["Sun", 73]],
    }
  },
  methods:{
    handleCo2(str='0PPM') {
  if (str == 'None') {
    return 0;
  }
  let pos = str.lastIndexOf("PPM");
  let num = str.slice(0, pos);
  return num;
},
    handlePm25(str='0μg'){
  if(str === 'None'){return 0}
  let pos = str.lastIndexOf("μg");
  let num = str.slice(0,pos);
  return num;
},
    handleTemperature(str = '0℃'){
  if(str === 'None'){return 0}
  let pos = str.lastIndexOf("℃");
  let num = str.slice(0,pos);
  return num;
},
    handleHumidity(str='0%'){
  if(str === 'None'){return 0}
  let pos = str.lastIndexOf("%");
  let num = str.slice(0,pos);
  return num;
},
    fetchData(){
      let that = this;
      axios.get('http://127.0.0.1:8000/getPlotData', {
        params:{
          classname: this.classname
        }
      }).then(res=>{
        let day = new Date().getDay(); // 1 开头
        let hour = new Date().getHours();
        // eslint-disable-next-line no-unused-vars
        let average = res.data[0];
        let daily = res.data[1];
        console.log(daily);
        let peopleTmp1 = [];
        let co2Tmp1 = [];
        let pm25Tmp1 = [];
        let temperatureTmp1 = [];
        let humidityTmp1 = [];


        for(let i = 0; i < day; ++ i){
          let peopleTmp2 = [];
          let co2Tmp2 = [];
          let pm25Tmp2 = [];
          let temperatureTmp2 = [];
          let humidityTmp2 = [];
          peopleTmp1.push([that.days[i], average[i]['实到人数']]);
          co2Tmp1.push([that.days[i], average[i]['CO2浓度']]);
          pm25Tmp1.push([that.days[i], average[i]['PM25浓度']]);
          temperatureTmp1.push([that.days[i], average[i]['温度']]);
          humidityTmp1.push([that.days[i], average[i]['空气湿度']]);
          if(i === day - 1) {
            for (let j = 8; j < hour + 1; ++j) {
              peopleTmp2.push([that.hours[j - 8], daily[i][j - 8]['实到人数']]);
              co2Tmp2.push([that.hours[j - 8], daily[i][j - 8]['CO2浓度']]);
              temperatureTmp2.push([that.hours[j - 8], daily[i][j - 8]['温度']]);
              humidityTmp2.push([that.hours[j - 8], daily[i][j - 8]['空气湿度']]);
              pm25Tmp2.push([that.hours[j - 8], daily[i][j - 8]['PM25浓度']])
            }
          } else {
            for (let j = 8; j < 24; ++j) {
              peopleTmp2.push([that.hours[j - 8], daily[i][j - 8]['实到人数']]);
              co2Tmp2.push([that.hours[j - 8], daily[i][j - 8]['CO2浓度']]);
              temperatureTmp2.push([that.hours[j - 8], daily[i][j - 8]['温度']]);
              humidityTmp2.push([that.hours[j - 8], daily[i][j - 8]['空气湿度']]);
              pm25Tmp2.push([that.hours[j - 8], daily[i][j - 8]['PM25浓度']])
            }
          }
          that.peopleDailyData[that.days[i]] = peopleTmp2;
          that.co2DailyData[that.days[i]] = co2Tmp2;
          that.pm25DailyData[that.days[i]] = pm25Tmp2;
          that.humidityDailyData[that.days[i]] = humidityTmp2;
          that.temperatureDailyData[that.days[i]] = temperatureTmp2;
        }

        this.peopleWeekData = peopleTmp1;
        this.peopleData = this.peopleWeekData;

        this.co2WeekData = co2Tmp1;
        this.co2Data = this.co2WeekData;

        this.pm25WeekData = pm25Tmp1;
        this.pm25Data = this.pm25WeekData;

        this.humidityWeekData = humidityTmp1;
        this.humidityData = this.humidityWeekData;

        this.temperatureWeekData = temperatureTmp1;
        this.temperatureData = this.temperatureWeekData;

        console.log(this.peopleData)

        this.initPeopleChart();
        this.initCO2Chart();
        this.initPM25Chart();
        this.initTemperatureChart();
        this.initHumidityChart()
      }).catch(err=>{
        console.log("获取数据失败" + err);
      });
    },
    initPeopleChart(){
      var that = this;
      echarts.init(document.getElementById('people')).dispose();
      var chartDom = document.getElementById('people');
      var myChart = echarts.init(chartDom, 'shine');
      var option;
      const dateList = that.peopleData.map(function (item) {
        return item[0];
      });
      const valueList = that.peopleData.map(function (item) {
        return item[1];
      });
      // var colors = ['#4587E7','#35AB33','#F5AD1D','#ff7f50','#da70d6','#32cd32','#6495ed'];
      option = {
        // Make gradient line here
        toolbox: {
          top:0,
          feature: {
            //点击图表可直接将柱形图与折线图进行切换
            magicType: {show: true, type: ['line', 'bar']},
            saveAsImage: {},
          }
        },
        visualMap: [
          {
            show: false,
            type: 'continuous',
            seriesIndex: 0,
            min: 0,
            max: 400
          },
        ],
        title: [
          {
            left: 'center',
            text: that.peopleTitle,
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
        series: [
          {
            type: 'bar',
            showSymbol: true,
            data: valueList
          },
        ],
    };
      // eslint-disable-next-line no-unused-vars
      myChart.on('click', function (params) {
        if(that.peopleFlag) {
          that.peopleData = that.peopleWeekData;
          that.peopleFlag = false;
          console.log(params.name)
          that.peopleTitle = '一周平均人数变化图';
        } else {
          that.peopleData = that.peopleDailyData[params.name];
          that.peopleFlag = true;
          that.peopleTitle = that.translation[params.name] + '人数变化图'
        }
      });
      option && myChart.setOption(option,true);
    },
    initCO2Chart(){
      var that = this;
      echarts.init(document.getElementById('co2')).dispose();
      var chartDom = document.getElementById('co2');
      var myChart = echarts.init(chartDom, 'shine');
      var option;
      const dateList = that.co2Data.map(function (item) {
        return item[0];
      });
      const valueList = that.co2Data.map(function (item) {
        return item[1];
      });
      option = {
        // Make gradient line here
        toolbox: {
          top:0,
          feature: {
            //点击图表可直接将柱形图与折线图进行切换
            magicType: {show: true, type: ['line', 'bar']},
            saveAsImage: {},
          }
        },
        visualMap: [
          {
            show: false,
            type: 'continuous',
            seriesIndex: 0,
            min: 0,
            max: 400
          },
        ],
        title: [
          {
            left: 'center',
            text: that.co2Title,
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
        series: [
          {
            type: 'bar',
            showSymbol: true,
            data: valueList,
            itemStyle: {
              normal: {
                label: {
                  show: false
                },
              }
            },
          },
        ],
        emphasis: {
          itemStyle: {
            // 高亮时点的颜色。
            color:  '#1ab9d3',
          },
        }
      };
      // eslint-disable-next-line no-unused-vars
      myChart.on('click', function (params) {
        if(that.co2Flag) {
          that.co2Data = that.co2WeekData;
          that.co2Flag = false;
          console.log(params.name)
          that.co2Title = '一周平均CO2浓度变化图';
        } else {
          that.co2Data = that.co2DailyData[params.name];
          that.co2Flag = true;
          that.co2Title = that.translation[params.name] + 'CO2浓度变化图'
        }
      });
      option && myChart.setOption(option,true);
    },
    initPM25Chart(){
      var that = this;
      echarts.init(document.getElementById('pm25')).dispose();
      var chartDom = document.getElementById('pm25');
      var myChart = echarts.init(chartDom, 'shine');
      var option;
      const dateList = that.pm25Data.map(function (item) {
        return item[0];
      });
      const valueList = that.pm25Data.map(function (item) {
        return item[1];
      });
      option = {
        // Make gradient line here
        toolbox: {
          top:0,
          feature: {
            //点击图表可直接将柱形图与折线图进行切换
            magicType: {show: true, type: ['line', 'bar']},
            saveAsImage: {},
          }
        },
        visualMap: [
          {
            show: false,
            type: 'continuous',
            seriesIndex: 0,
            min: 0,
            max: 400
          },
        ],
        title: [
          {
            left: 'center',
            text: that.pm25Title,
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
        series: [
          {
            type: 'bar',
            showSymbol: false,
            data: valueList
          },
        ],
        emphasis: {
          itemStyle: {
            // 高亮时点的颜色。
            color:  '#1ab9d3',
          },
        }
      };
      // eslint-disable-next-line no-unused-vars
      myChart.on('click', function (params) {
        if(that.pm25Flag) {
          that.pm25Data = that.pm25WeekData;
          that.pm25Flag = false;
          console.log(params.name)
          that.pm25Title = '一周平均pm25浓度变化图';
        } else {
          that.pm25Data = that.pm25DailyData[params.name];
          that.pm25Flag = true;
          that.pm25Title = that.translation[params.name] + 'pm25浓度变化图'
        }
      });
      option && myChart.setOption(option,true);
    },
    initTemperatureChart(){
      var that = this;
      echarts.init(document.getElementById('temperature')).dispose();
      var chartDom = document.getElementById('temperature');
      var myChart = echarts.init(chartDom, 'shine');
      var option;
      const dateList = that.temperatureData.map(function (item) {
        return item[0];
      });
      const valueList = that.temperatureData.map(function (item) {
        return item[1];
      });
      option = {
        // Make gradient line here
        toolbox: {
          top:0,
          feature: {
            //点击图表可直接将柱形图与折线图进行切换
            magicType: {show: true, type: ['line', 'bar']},
            saveAsImage: {},
            dataView: {},
          }
        },
        visualMap: [
          {
            show: false,
            type: 'continuous',
            seriesIndex: 0,
            min: 0,
            max: 400
          },
        ],
        title: [
          {
            left: 'center',
            text: that.temperatureTitle,
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
        series: [
          {
            type: 'bar',
            showSymbol: true,
            data: valueList,
            itemStyle: {
              normal: {
                label: {
                  show: true
                },
              }
            },
          },

        ],
        emphasis: {
          itemStyle: {
            // 高亮时点的颜色。
            color:  '#1ab9d3',
          },
        }
      };
      // eslint-disable-next-line no-unused-vars
      myChart.on('click', function (params) {
        if(that.temperatureFlag) {
          that.temperatureData = that.temperatureWeekData;
          that.temperatureFlag = false;
          console.log(params.name)
          that.temperatureTitle = '一周平均教室温度变化图';
        } else {
          that.temperatureData = that.temperatureDailyData[params.name];
          that.temperatureFlag = true;
          that.temperatureTitle = that.translation[params.name] + '教室温度变化图'
        }
      });
      option && myChart.setOption(option,true);
    },
    initHumidityChart(){
      var that = this;
      echarts.init(document.getElementById('humidity')).dispose();
      var chartDom = document.getElementById('humidity');
      var myChart = echarts.init(chartDom, 'shine');
      var option;
      const dateList = that.humidityData.map(function (item) {
        return item[0];
      });
      const valueList = that.humidityData.map(function (item) {
        return item[1];
      });
      option = {
        // Make gradient line here
        toolbox: {
          top:0,
          feature: {
            //点击图表可直接将柱形图与折线图进行切换
            magicType: {show: true, type: ['line', 'bar']},
            saveAsImage: {},
          }
        },
        visualMap: [
          {
            show: false,
            type: 'continuous',
            seriesIndex: 0,
            min: 0,
            max: 400
          },
        ],
        title: [
          {
            left: 'center',
            text: that.humidityTitle,
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
        series: [
          {
            type: 'bar',
            showSymbol: false,
            data: valueList
          },
        ],
        emphasis: {
          itemStyle: {
            // 高亮时点的颜色。
            color:  '#1ab9d3',
          },
        }
      };
      // eslint-disable-next-line no-unused-vars
      myChart.on('click', function (params) {
        if(that.humidityFlag) {
          that.humidityData = that.humidityWeekData;
          that.humidityFlag = false;
          console.log(params.name)
          that.humidityTitle = '一周平均空气湿度变化图';
        } else {
          that.humidityData = that.humidityDailyData[params.name];
          that.humidityFlag = true;
          that.humidityTitle = that.translation[params.name] + '空气湿度变化图'
        }
      });
      option && myChart.setOption(option,true);
    },
  },
  mounted() {
    echarts.registerTheme('shine', this.themes)
    this.fetchData();
  },
  watch:{
    peopleData(){
      this.initPeopleChart();
    },
    co2Data(){
      this.initCO2Chart();
    },
    pm25Data(){
      this.initPM25Chart();
    },
    humidityData(){
      this.initHumidityChart();
    },
    temperatureData(){
      this.initTemperatureChart();
    }
  }
}
</script>

<style scoped>


</style>