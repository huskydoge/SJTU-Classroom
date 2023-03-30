<!-- 气泡图界面直接作为次级主界面，整合侧边栏所有内容 -->
<!--suppress ALL -->
<template>
<!--  <div style="position:fixed; left: 50px;top:150px;display: flex;align-items: center">-->
<!--    <el-avatar src="https://tse3-mm.cn.bing.net/th/id/OIP-C.-SW2Zx4d18IXG3GqeoaBYgHaHa?w=206&h=207&c=7&r=0&o=5&dpr=2&pid=1.7">-->
<!--    </el-avatar>-->
<!--    <div style="margin-left: 10px;">-->
<!--      <el-popover-->
<!--          placement="bottom-start"-->
<!--          :width="300"-->
<!--          trigger="hover"-->
<!--          content="this is content, this is content, this is content"-->
<!--      >-->
<!--        <template #reference>-->
<!--          <el-button>-->
<!--           <span style="padding: 2px">-->
<!--             ...-->
<!--        </span>-->
<!--          </el-button>-->
<!--        </template>-->
<!--        <template #default>-->
<!--          <div-->
<!--              class="demo-rich-conent"-->
<!--              style="display: flex; gap: 10px; flex-direction: column;padding: 20px"-->
<!--          >-->
<!--            <div style="display: inline-flex;column-gap: 10px">-->
<!--              <p style="font-size: 20px;font-weight: 800">帮助与提示</p>-->
<!--              <help :strokeWidth="2" theme="outline" size="30" fill="#333" strokeLinejoin="bevel" strokeLinecap="square"/>-->
<!--            </div>-->
<!--            <div>-->
<!--              <p-->

<!--                  style="margin: 0; font-weight: 500"-->
<!--              >-->
<!--                基本概念-->
<!--              </p>-->
<!--              <p-->
<!--                  class="demo-rich-content__mention"-->
<!--                  style="margin: 0; font-size: 14px; color: var(&#45;&#45;el-color-info)"-->
<!--              >-->
<!--                气泡的大小表征数据的大小.-->
<!--              </p>-->
<!--              <br>-->
<!--              <p-->

<!--                  style="margin: 0; font-weight: 500"-->
<!--              >-->
<!--                交互-->
<!--              </p>-->
<!--              <p-->
<!--                  class="demo-rich-content__mention"-->
<!--                  style="margin: 0;margin-top: 4px; font-size: 14px; color: var(&#45;&#45;el-color-info)"-->
<!--              >-->
<!--                1.拉动左侧的滑动条可以控制展示气泡数目的多少.-->
<!--              </p>-->
<!--              <p-->
<!--                  class="demo-rich-content__mention"-->
<!--                  style="margin: 0;margin-top: 4px; font-size: 14px; color: var(&#45;&#45;el-color-info)"-->
<!--              >-->
<!--                2.鼠标悬浮气泡上可以看到对应的具体数据.-->
<!--              </p>-->
<!--              <p-->
<!--                  class="demo-rich-content__mention"-->
<!--                  style="margin: 0;margin-top: 4px; font-size: 14px; color: var(&#45;&#45;el-color-info)"-->
<!--              >-->
<!--                3.点击气泡可以进入对应的教室界面.-->
<!--              </p>-->
<!--              <p-->
<!--                  class="demo-rich-content__mention"-->
<!--                  style="margin: 0;margin-top: 4px; font-size: 14px; color: var(&#45;&#45;el-color-info)"-->
<!--              >-->
<!--                4.点击右侧的标签栏可以切换不同的数据类型.-->
<!--              </p>-->
<!--            </div>-->

<!--            <p class="demo-rich-content__desc" style="margin: 0">-->
<!--              Navi Group, SJTU-->
<!--            </p>-->
<!--          </div>-->
<!--        </template>-->
<!--      </el-popover>-->
<!--    </div>-->
<!--  </div>-->
  <nav style="position:fixed;top:100px;right: 700px">
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
  <div style="height: 800px;display: flex;align-items: center">
    <el-slider  size="small" vertical=vertical v-model="bubbleNumbers" height="400px" :max="this.dataLength" />
    <div id="bubble" v-if="showBubble" style="width: 800px;height:700px;overflow: clip;"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts/core';
import {Help} from '@icon-park/vue-next'
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
export default {
  emits: ['showClassInfo'],
  props:{
    dataFromSearch: Array,
    customChoice: Boolean,
  },
  data() {
    return {
      activeName:'vacancy',

      dataLength: 377, // 最多377
      bubbleNumbers: 10, // 显示多少个泡泡
      bubbleString: '的空位数:',
      classData:[], // classRoomData的中间储存
      // 默认值, 变化就要重新加载
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
      ] , // 教室初始信息,不要删除！
      showBubble: true,
      option: {},
      colorList: ['#5470c6', '#91cc75', '#fac858', '#ee6666', '#73c0de', '#3ba272', '#fc8452', '#9a60b4', '#ea7ccc'],
      // 存储当前教室信息
      className: String,
    };
  },
  components: {
    Help,
  },
  mounted() {
    window.activeName = this.activeName;
    window.bubbleString = this.bubbleString;
    window.setClassroomDisplayInfo = this.setClassroomInfoInSearch; // 和另一个bubble图做区分
    this.renderBubbleChart(this.stratifyByVacancy);
  },

  methods: {
    stratifyByVacancy(seriesData) {
      function handleCo2(str='0PPM') {
        if (str == 'None') {
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
      if(window.activeName == 'seats'){
        return d3
            .stratify()
            .parentId(function (d) {
              return d.id.substring(0, d.id.lastIndexOf('.'));
            })(seriesData)
            .sum(function (d) {
              return d.seats || 0;
            })
            .sort(function (a, b) {
              return b.seats - a.seats;
            });
      } else if(window.activeName == 'vacancy'){
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
      } else if(window.activeName == 'people') {
        return d3
            .stratify()
            .parentId(function (d) {
              return d.id.substring(0, d.id.lastIndexOf('.'));
            })(seriesData)
            .sum(function (d) {
              return d.people || 0;
            })
            .sort(function (a, b) {
              return b.people - a.people;
            });
      }else if(window.activeName == 'co2') {
        return d3
            .stratify()
            .parentId(function (d) {
              return d.id.substring(0, d.id.lastIndexOf('.'));
            })(seriesData)
            .sum(function (d) {
              return handleCo2(d.co2);
            })
            .sort(function (a, b) {
              return handleCo2(b.co2) - handleCo2(a.co2);
            });
      }else if(window.activeName == 'pm25') {
        return d3
            .stratify()
            .parentId(function (d) {
              return d.id.substring(0, d.id.lastIndexOf('.'));
            })(seriesData)
            .sum(function (d) {
              return handlePm25(d.pm25);
            })
            .sort(function (a, b) {
              return handlePm25(b.pm25) - handlePm25(a.pm25);
            });
      }else if(window.activeName == 'humidity'){
        return d3
            .stratify()
            .parentId(function (d) {
              return d.id.substring(0, d.id.lastIndexOf('.'));
            })(seriesData)
            .sum(function (d) {
              return (handleHumidity(d.humidity) - 70) * 10;
            })
            .sort(function (a, b) {
              return handleHumidity(b.humidity) - handleHumidity(a.humidity);
            });
      } else {
        return d3
            .stratify()
            .parentId(function (d) {
              return d.id.substring(0, d.id.lastIndexOf('.'));
            })(seriesData)
            .sum(function (d) {
              return (handleTemperature(d.temperature) - 21) * 10;
            })
            .sort(function (a, b) {
              return handleTemperature(b.temperature) - handleTemperature(a.temperature);
            });
      }
    },
    changeBubbleString(){
      window.activeName = this.activeName;
      if(window.activeName == 'seats'){
        window.bubbleString = '的座位数:'
      } else if(window.activeName == 'vacancy'){
        window.bubbleString = '的空位数:'
      }else if(window.activeName == 'people'){
        window.bubbleString = '的当前人数:'
      }else if(window.activeName == 'co2'){
        window.bubbleString = '的co2浓度:'
      }else if(window.activeName == 'pm25'){
        window.bubbleString = '的PM2.5浓度:'
      }else if(window.activeName == 'humidity'){
        window.bubbleString = '的湿度:'
      }else {
        window.bubbleString = '的温度:'
      }},
    renderBubbleChart(stratify){
      let seriesData = this.classRoomData.slice(0, this.bubbleNumbers);
      this.fetchData();
      let that = this
      let displayRoot = stratify(seriesData);
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
              fontSize: node.r / 4
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
                this.bubbleString +
                params.data[window.activeName] // 这里注意要先进入data，否则会找不到！https://blog.csdn.net/metooyoume/article/details/108726385
            );
          },

        }, // 决定鼠标悬浮是否显示信息
        hoverLayerThreshold: Infinity,
        series: [{
          type: 'custom',
          colorBy: 'data',
          renderItem: renderItem, // 自定义custom需要这个函数
          progressive: 10,
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
    renderBubbleChartNoFetchData(stratify){
      let seriesData = this.classRoomData.slice(0, this.bubbleNumbers);
      let that = this
      let displayRoot = stratify(seriesData);
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
              fontSize: node.r / 4
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
                window.bubbleString +
                params.data[window.activeName] // 这里注意要先进入data，否则会找不到！https://blog.csdn.net/metooyoume/article/details/108726385
            );
          },

        }, // 决定鼠标悬浮是否显示信息
        hoverLayerThreshold: Infinity,
        series: [{
          type: 'custom',
          colorBy: 'data',
          renderItem: renderItem, // 自定义custom需要这个函数
          progressive: 10,
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
    // 点击chart展示对应的classroom
    showClassInfo(className){
      this.$emit("showClassInfo",className);
    },
    setClassroomInfoInSearch(name){
      this.className = name;
      this.showClassInfo(this.className);
    },
    initEcharts() {
      let setClass = this.setClassroomInfoInSearch; // 和另一个bubble图做区分
      // nextTick解决图表不加载问题
      this.$nextTick(()=>
      {
        let myChart = echarts.init(document.getElementById('bubble'))
        myChart.setOption(this.option)
        myChart.on('click',function (params){
          // console.log(params.data.name);
          setClass(params.data.name)
        })
      })
    },
    fetchData(){ // 要先在终端运行 node app.js
      axios.get('http://127.0.0.1/getAllClassroom').then(res=>{
        // console.log(res.data)
        this.classData = [];
        let tmp =
            {
              depth: 0,
              id: 'classroom',
              index: 0,
              vacancy: 0,
              name: '',
              seats: 0, //没问题
              people: 0,
              co2: '0PPM',
              pm25: '0μg',
              temperature: '0℃',
              humidity: '0%',
            };
        this.classData.push(tmp)
        let cnt = 1; // index
        for(const i in res.data){
          let obj = {
            depth: 1,
            id: 'classroom.' + res.data[i]['教室名'],
            index: cnt,
            vacancy: res.data[i]['座位数'] - res.data[i]['实到人数'], //目前没问题
            name: res.data[i]['教室名'],
            seats: (res.data[i]['座位数'] == 'NONE') ? 0: res.data[i]['座位数'] - '0', //没问题
            people: (res.data[i]['实到人数'] == 'None')? 0:res.data[i]['实到人数'] , //要处理下
            co2: res.data[i]['CO2浓度'],
            pm25:res.data[i]['PM25浓度'],
            temperature:res.data[i]['温度'],
            humidity: res.data[i]['空气湿度'],
          };
          this.classData.push(obj);
          ++ cnt;
        }
        // 设置展示的数目, 这里设置展示数目
        this.classRoomData = this.classData;
      }).catch(err=>{
        console.log("获取数据失败" + err);
      });

    }
  },
  // 监听data和props的数据变化，及时更新数据
  watch:{
    activeName(){
      this.changeBubbleString();
      this.renderBubbleChartNoFetchData(this.stratifyByVacancy);
    },
    classRoomData(){
      this.dataLength = this.classRoomData.length;
      this.renderBubbleChartNoFetchData(this.stratifyByVacancy);
    },
    bubbleNumbers(){
      console.log(this.bubbleNumbers);
      this.renderBubbleChartNoFetchData(this.stratifyByVacancy);
    },
    dataFromSearch(){
      let head =
          {
            depth: 0,
            id: 'classroom',
            index: 0,
            vacancy: 0,
            name: '',
            seats: 0, //没问题
            people: 0,
            co2: '0PPM',
            pm25: '0μg',
            temperature: '0℃',
            humidity: '0%',
          };
      this.classRoomData=this.dataFromSearch;
      this.classRoomData.unshift(head);
      this.bubbleNumbers = 10;
    },
  },
}

</script>

<style>
#bubble > div:nth-child(1) > canvas{
  left: -78px;
}
</style>
