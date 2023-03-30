<!-- 气泡图界面直接作为次级主界面，整合侧边栏所有内容 -->
<!--suppress ALL -->
<template>

  <div class="mainContent" style="width:1000px;overflow-x: hidden;overflow-y: auto;">
    <!--    通过v-if控制不同组件的展示 -->
    <page-header v-bind:classroomName="this.currentClassroomInfo.classroomName" v-if="!showBubble" :fatherMethod="showBubbleChart"></page-header>
    <tab-page :classroom-name=this.currentClassroomInfo.classroomName v-if="!showBubble"></tab-page>
<!--    <div id="bubble" v-if="showBubble" style="width: 1100px;height:1100px;"></div>-->
    <div v-if="showBubble">
    <div style="margin-bottom:20px;display: inline-flex;align-items: center;">
      <button class="viewBtn btn" type="button" @click="changeView('bubble');">气泡图</button>
      <button class="viewBtn btn" type="button" @click="changeView('bar')">柱状图</button>
    </div>
    <bubble-below-search v-if="activeName === 'bubble'" :custom-choice="true"></bubble-below-search>
      <bar-below-search :custom-choice="true" @showClassInfo="this.changeCurrentClass" v-if="activeName === 'bar'"></bar-below-search>
    </div>
  </div>
  <div>
    <h1 style="text-align: left;font-size: 2rem" v-if="showBubble" >实时动态</h1>
    <echart-clock v-if="showBubble"></echart-clock>
    <CalendarBox v-if="showBubble" style="height: 700px"></CalendarBox>
  </div>
  <el-backtop target=".mainContent" :visibility-height=10></el-backtop>


</template>

<script>
import * as echarts from 'echarts/core';
import echartClock from "@/components/charts/clock";
import pageHeader from "@/components/pageHeader.vue"
import tabPage from "@/components/classRoom/tabPage"
import CalendarBox from "@/components/CalendarBox"
import {
  DatasetComponent,
  TooltipComponent,
  VisualMapComponent
} from 'echarts/components';
import { CustomChart } from 'echarts/charts';
import { CanvasRenderer } from 'echarts/renderers';
echarts.use([
  DatasetComponent,
  TooltipComponent,
  VisualMapComponent,
  CustomChart,
  CanvasRenderer
]);
import * as d3 from 'd3';
import axios from "axios";
import BubbleBelowSearch from "@/components/searchPage/bubbleBelowSearch";
import BarBelowSearch from "@/components/searchPage/barBelowSearch";
export default {
  name:"bubbleChart",
  data() {
    return {
      activeName:'bubble',
      dataFetched: Object,
      classData:[],
      classRoomData: [
        // 父亲节点
        {
          depth: 0,
          id: 'classroom',
          index: 0,
          vacancy: 0,
          name: '',
        },
        {
          depth: 1,
          id: 'classroom.东上院101',
          index: 1,
          vacancy: 100,
          name: '东上院101',
          url:"https://www.runoob.com/jsref/jsref-tutorial.html"
        },
        {
          depth: 1,
          id: 'classroom.下院305',
          name: '下院106',
          index: 1,
          vacancy: 92,
          url:"https://www.runoob.com/jsref/jsref-tutorial.html"
        },
        {
          depth: 1,
          name: '教室404',
          id: 'classroom.dataZoom-inside',
          index: 3,
          vacancy: 30
        },
        {
          depth: 1,
          id: 'classroom.dataZoom1',
          index: 4,
          vacancy: 40
        },
        {
          depth: 1,
          id: 'classroom.dataZoom2',
          index: 5,
          vacancy: 50
        },
        {
          depth: 1,
          id: 'classroom.dataZoom3',
          index: 5,
          vacancy: 60
        },
        {
          depth: 1,
          id: 'classroom.dataZoom4',
          index: 5,
          vacancy: 70
        },
        {
          depth: 1,
          id: 'classroom.dataZoom5',
          index: 5,
          vacancy: 80
        }
      ] , // 教室信息 !
      showBubble: true,
      option: {},
      colorList: ['#5470c6', '#91cc75', '#fac858', '#ee6666', '#73c0de', '#3ba272', '#fc8452', '#9a60b4', '#ea7ccc'],
      // 存储当前教室信息
      currentClassroomInfo: {
        classroomName:"NULL"
      },
    };
  },
  components: {
    BarBelowSearch,
    BubbleBelowSearch,
    tabPage, // 标签页
    echartClock, // 时钟
    pageHeader, // 页头
    CalendarBox, // 日历图
  },
  mounted() {
    // !在窗口注册函数
    // window.test= this.test;
    this.fetchData();
    window.disableBubble = this.eraseBubbleChart;
    window.setClassroomInfo = this.setClassroomInfo;
    let that = this
    let seriesData = this.classRoomData;
    let displayRoot = stratify1();
    function stratify1() {
      return d3
          .stratify()
          .parentId(function (d) {
            return d.id.substring(0, d.id.lastIndexOf('.'));
          })(seriesData)
          .sum(function (d) {
            return d.vacancy || 0;
          })
          .sort(function (a, b) {
            return b.vacancy - a.vacancy;
          });
    }
    function overallLayout(params, api) {
      let context = params.context;
      d3
          .pack()
          .size([api.getWidth() - 2, api.getHeight() - 2])
          .padding(0)(displayRoot);
      context.nodes = {}; // 把节点加入字典

      displayRoot.descendants().forEach(function (node) {

        context.nodes[node.id] = node;
      });
    }
    // renderItem引用overallLayout
    function renderItem(params, api) {
      // context: // {Object} 一个可供开发者暂存东西的对象。生命周期只为：当前次的渲染。 dataIndex: // {number} 数据项的 index。
      let context = params.context;
      let idx = params.dataIndex;
      // console.log(params);

      // Only do that layout once in each time `setOption` called.
      // 每次调用“setOption”时，只能进行一次布局。
      if (!context.layout) {
        context.layout = true;
        overallLayout(params, api);
      }

      let nodePath = api.value('id'); // 例如 classroom.dataZoom
      let nodeName = nodePath // 这里用了正则表达式来从节点路径得到名字，其实可以自定义
          .slice(nodePath.lastIndexOf('.') + 1)
          .split(/(?=[A-Z][^A-Z])/g)
          .join('')
      let node = context.nodes[nodePath];
      if (node.id === 'classroom') {
        node.r = 0 // 大圆不显示
      }
      if (!node) {
        // Render nothing.
        return;
      }
      if(node.data.name){
        nodeName = node.data.name;
        // nodeName = node.name;
      }

      let z2 = api.value('depth') * 2;
      return {
        type: 'circle',
        shape: {
          cx: node.x,
          cy: node.y,
          r: node.r
        },
        // transition: ['shape'],
        z2: z2,
        textContent: {
          type: 'text',
          style: {
            // transition: isLeaf ? 'fontSize' : null,
            text: nodeName, // 圆圈内部的文字
            fill: '#fff',
            fontFamily: 'Arial',
            width: node.r * 1.3,
            overflow: 'truncate',
            fontSize: node.r / 3
          },
          emphasis: {
            style: {
              overflow: null,
              fontSize: Math.max(node.r / 3, 12)
            }
          }
        },
        textConfig: {
          position: 'inside'
        },
        style: {
          fill: that.colorList[idx % that.colorList.length]
        },
        emphasis: {
          style: {
            fontFamily: 'Arial',
            fontSize: 12,
            shadowBlur: 20,
            shadowOffsetX: 3,
            shadowOffsetY: 5,
            shadowColor: 'rgba(0,0,0,0.3)'
          }
        }
      };
    }
    // option用到renderItem
    this.option = {
      dataset: {
        source: seriesData
      },
      tooltip: {
        formatter(params) {
            return (
                params.data.name +
                "的剩余位置：" +
                    params.data.vacancy // 这里注意要先进入data，否则会找不到！https://blog.csdn.net/metooyoume/article/details/108726385
            );
        },

      }, // 决定鼠标悬浮是否显示信息
      hoverLayerThreshold: Infinity,
      series: [{
        type: 'custom',
        colorBy: 'data',
        renderItem: renderItem, // 自定义custom需要这个函数
        progressive: 0,
        coordinateSystem: 'none',
        encode: {
          // tooltip: ['name','vacancy'],
          // itemName: 'id'
        }
      }]
    }
    // init用到option
    this.initEcharts()
  },

  methods: {
    changeView(str){
      this.activeName = str;
    },
    setClassroomInfo(info){
      this.currentClassroomInfo.classroomName = info.name;
    },
    showBubbleChart(){
      this.showBubble = true;
    },
    eraseBubbleChart(){
      this.showBubble = false;
    },
    initEcharts() {
      // nextTick解决图表不加载问题
      this.$nextTick(()=>
          {
      let myChart = echarts.init(document.getElementById('bubble'))
      myChart.setOption(this.option)
            myChart.on('click',function (params){
              window.setClassroomInfo(params.data)
              window.disableBubble(); // 隐藏bubble图
              // alert(params.data.name) // 如何传参？
            })
          })
    },
    fetchData(){
      axios.get('http://127.0.0.1/getAllClassroom').then(res=>{
        this.dataFetched = res.data;
        // console.log(this.dataFetched)
        let cnt = 1;
        for(const i in this.dataFetched){
          let obj = {
            depth: 1,
            id: 'classroom.' + this.dataFetched[i]['教室名'],
            index: cnt,
            vacancy: this.dataFetched[i]['座位数'] - this.dataFetched[i]['实到人数'],
            name: this.dataFetched[i]['教室名'],
          };
          this.classData.push(obj);
          ++ cnt;
        }
        // 按照空余位置排序
        this.classData.sort(function(a,b){
          return b.vacancy - a.vacancy;
        });
        let tmp = [
          {
            depth: 0,
            id: 'classroom',
            index: 0,
            vacancy: 0,
            name: '',
          },
        ];
        // 设置展示的数目
        for(let i = 0; i < 10; ++ i){
          tmp.push(this.classData[i]);
        }
        this.classRoomData = tmp
      }).catch(err=>{
        console.log("获取数据失败" + err);
      });

    },
    // 接收组件传来的教室名
    changeCurrentClass(name){
      this.currentClassroomInfo.classroomName = name;
      this.showBubble = false;
    }
  },
  // 监听data和props的数据变化，及时更新数据
  watch:{
    showBubble(){
      this.initEcharts();
},
    classRoomData(){
      let that = this
      let seriesData = this.classRoomData;
      let displayRoot = stratify1();
      function stratify1() {
        return d3
            .stratify()
            .parentId(function (d) {
              return d.id.substring(0, d.id.lastIndexOf('.'));
            })(seriesData)
            .sum(function (d) {
              return d.vacancy || 0;
            })
            .sort(function (a, b) {
              return b.vacancy - a.vacancy;
            });
      }
      function overallLayout(params, api) {
        let context = params.context;
        d3
            .pack()
            .size([api.getWidth() - 2, api.getHeight() - 2])
            .padding(0)(displayRoot);
        context.nodes = {}; // 把节点加入字典

        displayRoot.descendants().forEach(function (node) {

          context.nodes[node.id] = node;
        });
      }
      function renderItem(params, api) {
        // context: // {Object} 一个可供开发者暂存东西的对象。生命周期只为：当前次的渲染。 dataIndex: // {number} 数据项的 index。
        let context = params.context;
        let idx = params.dataIndex;
        // console.log(params);

        // Only do that layout once in each time `setOption` called.
        // 每次调用“setOption”时，只能进行一次布局。
        if (!context.layout) {
          context.layout = true;
          overallLayout(params, api);
        }

        let nodePath = api.value('id'); // 例如 classroom.dataZoom
        let nodeName = nodePath // 这里用了正则表达式来从节点路径得到名字，其实可以自定义
            .slice(nodePath.lastIndexOf('.') + 1)
            .split(/(?=[A-Z][^A-Z])/g)
            .join('')
        let node = context.nodes[nodePath];
        if (node.id === 'classroom') {
          node.r = 0 // 大圆不显示
        }
        if (!node) {
          // Render nothing.
          return;
        }
        if(node.data.name){
          nodeName = node.data.name;
          // nodeName = node.name;
        }

        let z2 = api.value('depth') * 2;
        return {
          type: 'circle',
          shape: {
            cx: node.x,
            cy: node.y,
            r: node.r
          },
          // transition: ['shape'],
          z2: z2,
          textContent: {
            type: 'text',
            style: {
              // transition: isLeaf ? 'fontSize' : null,
              text: nodeName, // 圆圈内部的文字
              fill: '#fff',
              fontFamily: 'Arial',
              width: node.r * 1.3,
              overflow: 'truncate',
              fontSize: node.r / 3
            },
            emphasis: {
              style: {
                overflow: null,
                fontSize: Math.max(node.r / 3, 12)
              }
            }
          },
          textConfig: {
            position: 'inside'
          },
          style: {
            fill: that.colorList[idx % that.colorList.length]
          },
          emphasis: {
            style: {
              fontFamily: 'Arial',
              fontSize: 12,
              shadowBlur: 20,
              shadowOffsetX: 3,
              shadowOffsetY: 5,
              shadowColor: 'rgba(0,0,0,0.3)'
            }
          }
        };
      }
      this.option = {
        dataset: {
          source: seriesData
        },
        tooltip: {
          formatter(params) {
            return (
                params.data.name +
                "的剩余位置：" +
                params.data.vacancy // 这里注意要先进入data，否则会找不到！https://blog.csdn.net/metooyoume/article/details/108726385
            );
          },

        }, // 决定鼠标悬浮是否显示信息
        hoverLayerThreshold: Infinity,
        series: [{
          type: 'custom',
          colorBy: 'data',
          renderItem: renderItem, // 自定义custom需要这个函数
          progressive: 0,
          coordinateSystem: 'none',
          encode: {
            // tooltip: ['name','vacancy'],
            // itemName: 'id'
          }
        }]
      }
      this.initEcharts()
    },
    immediate: true,

  },
}

</script>

<style>
#bubble > div:nth-child(1) > canvas{
  left: -78px;
}

.mainContent::-webkit-scrollbar{
  width: 0;
}


.viewBtn{
  cursor: pointer;
  color: #fff;
  font-size: 11px;
  width: 80px;
  height: 25px;
  border: 0;
  background-color: rgb(242, 78, 122);
}

/*按钮当鼠标悬浮时的状态：*/
.btn:hover{
  transform: translateY(3px);
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
