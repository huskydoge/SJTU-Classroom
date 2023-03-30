<template>
  <div class="scroll-content" style="width:1000px;height:800px;overflow-x: hidden;overflow-y: auto;" v-if="!showPage">
    <!--    通过v-if控制不同组件的展示 -->
    <page-header v-bind:classroomName="this.currentClassroomInfo.classroomName" v-if="!showPage" :fatherMethod="showPageChart"></page-header>
    <tab-page :classroom-name=this.currentClassroomInfo.classroomName v-if="!showPage"></tab-page>
    <!--    <div id="bubble" v-if="showBubble" style="width: 1100px;height:1100px;"></div>-->
  </div>
  <div v-if="showPage" style="display: flex">
    <div
        class="scroll-content"
        @scroll="onScroll"
        :style="
        'overflow-x: hidden; overflow-y: auto;width: 1300px;height:' + contentStyleObj.height
      "
    >
      <h1 style="font-size: 3.5rem"> 上院 </h1>
      <!-- 教学楼图片 -->
      <div :ref="tabs[0].refName" class="scroll-item">
        <h1 id="教学楼图片" style="font-size: 3rem">教学楼图片</h1>
        <div style="width: 75%">
          <carousel-box :respective-img-list="imgList" ></carousel-box>
          <br>
          <hr>
        </div>
      </div>
      <!-- 教学楼信息 -->
      <div :ref="tabs[1].refName" class="scroll-item">
        <h1 id="教学楼信息" style="font-size: 3rem">教学楼信息</h1>
        <div style="width: 75%">
          <p style="display: block;width: 100%;font-size: 1rem">清末发源
            1896年，清政府刑部左侍郎李端棻上奏《推广学校》一折，建议自
            南洋公学
            南洋公学(2张)

            京师以及各省府州县皆设学堂。10月，盛宣怀向清朝政府正式上奏《条陈自强大计折》，附奏《请设学堂片》，禀明两江总督刘坤一，拟在上海捐地开办南洋公学，经费由轮电两局捐输，聘请何嗣焜出任总理。12月得到光绪皇帝准允。至此，标志南洋公学正式创立。因学堂地处南洋（当时称江、浙、闽、广等地为南洋），参考西方学堂经费“半由商民所捐，半由官助者为公学”，故定名为南洋公学。南洋公学初建时以培养高端法政人才为办学目标，先设师范院、外院、中院、上院四院，继设铁路班、特班、政治班、译书院、东文学堂等。

            1897年，盛宣怀呈奏《筹建南洋公学及达成馆舍》一折，提出南洋公学及达成馆均可由轮电两局集捐筹办。聘请张焕纶为中文总教习，福开森为监院。在上海徐家汇赁屋办学。首批招考师范生30名，于4月8日开学，按五层格进行培养。11月9日外院开办，由师范生担任教习。师范生自编《蒙学课本》，风行中国国内。何嗣焜拟订公学第一份办学章程——《南洋公学章程》。招商局认捐规银6万两，电报局认捐规银4万两，作为办学经费。

            1905年，学校改隶商部，改校名为商部上海高等实业学堂，始以培养高级工程技术与管理人才为目标。

            1906年秋，学校工科之始——铁路工程班成立。
          </p>
          <hr>
        </div>
      </div>
      <!-- 教学楼位置 -->
      <div
          :ref="tabs[2].refName"
          class="scroll-item"
          style="padding-top: 1rem; top: 5px"
      >
        <h1 id="教学楼位置" style="font-size: 3rem">教学楼位置</h1>
        <el-button style="width: fit-content;margin-left: auto" @click="returnLocation">回到原来位置</el-button>
        <baidu-map v-if="map" :points="[121.437395,31.025958]"></baidu-map>
      </div>
      <!-- 教学楼自习教室 -->
      <div
          :ref="tabs[3].refName"
          class="scroll-item"
          style="padding-top: 1rem; top: 5px"
      >
        <h1 id="教学楼自习教室" style="font-size: 3rem">教学楼自习教室</h1>
        <layer-view :classRoomList="this.classRooms" @fatherMethod="showClassPage"></layer-view>
      </div>
      <div
          :ref="tabs[4].refName"
          class="scroll-item"
          style="padding-top: 1rem; top: 5px"
      >
        <h1 id="更多服务" style="font-size: 3rem">更多服务</h1>
        <div style="width: 75%;display: grid;grid-template-columns: 1fr 1fr;column-gap: 20px;row-gap: 18px">
          <el-card shadow="hover" :body-style="{ padding: '10px' }">
            <h2>联系电话</h2>
            上院：34203956
          </el-card>
        </div>
      </div>
      <h1 style="font-size: 2rem;margin-top: 20px">更多精彩有待拓展.......</h1>
    </div>
    <nav style="position:fixed;right:100px;top:100px;">
      <el-tabs
          @tab-click="jump"
          v-model="tabName"
          tab-position="right"
      >
        <el-tab-pane
            v-for="(tab, index) in tabs"
            :name="tab.refName"
            :key="index"
            :label="tab.name"
        ></el-tab-pane>
      </el-tabs>
    </nav>
  </div>
</template>

<script>
import baiduMap from "@/components/classRoom/baiduMap";
import CarouselBox from "@/components/CarouselBox";
import LayerView from "@/components/building/layerView";
import axios from "axios";
import PageHeader from "@/components/pageHeader";
import tabPage from "@/components/classRoom/tabPage";
export default {
  props: {},
  components: {PageHeader, LayerView, baiduMap,CarouselBox, tabPage},
  data() {
    return {
      map :true,
      currentClassroomInfo: {
        classroomName:"NULL"
      },
      showPage: true,
      classRooms:[
        [
          {
            "教室名": "上院100",
            "座位数": "432",
            "实到人数": "93",
            "CO2浓度": "506.0PPM",
            "空气湿度": "None",
            "PM25浓度": "None",
            "温度": "None"
          },
          {
            "教室名": "上院101",
            "座位数": "87",
            "实到人数": "0",
            "CO2浓度": "502.0PPM",
            "空气湿度": "95.0%",
            "PM25浓度": "13μg",
            "温度": "26.2℃"
          },
          {
            "教室名": "上院102",
            "座位数": "87",
            "实到人数": "16",
            "CO2浓度": "398.0PPM",
            "空气湿度": "95.0%",
            "PM25浓度": "13μg",
            "温度": "23.6℃"
          },
          {
            "教室名": "上院103",
            "座位数": "87",
            "实到人数": "0",
            "CO2浓度": "488.0PPM",
            "空气湿度": "95.0%",
            "PM25浓度": "12μg",
            "温度": "23.7℃"
          },
          {
            "教室名": "上院104",
            "座位数": "87",
            "实到人数": "26",
            "CO2浓度": "None",
            "空气湿度": "None",
            "PM25浓度": "None",
            "温度": "None"
          },
          {
            "教室名": "上院105",
            "座位数": "100",
            "实到人数": "15",
            "CO2浓度": "1928.0PPM",
            "空气湿度": "93.0%",
            "PM25浓度": "28μg",
            "温度": "21.4℃"
          },
          {
            "教室名": "上院107",
            "座位数": "67",
            "实到人数": "0",
            "CO2浓度": "410.0PPM",
            "空气湿度": "95.0%",
            "PM25浓度": "1000μg",
            "温度": "22.9℃"
          },
          {
            "教室名": "上院108",
            "座位数": "67",
            "实到人数": "10",
            "CO2浓度": "None",
            "空气湿度": "94.0%",
            "PM25浓度": "16384μg",
            "温度": "21.7℃"
          },
          {
            "教室名": "上院110",
            "座位数": "100",
            "实到人数": "0",
            "CO2浓度": "422.0PPM",
            "空气湿度": "54.0%",
            "PM25浓度": "9μg",
            "温度": "24.5℃"
          },
          {
            "教室名": "上院111",
            "座位数": "122",
            "实到人数": "42",
            "CO2浓度": "1818.0PPM",
            "空气湿度": "95.0%",
            "PM25浓度": "11μg",
            "温度": "23.9℃"
          },
          {
            "教室名": "上院112",
            "座位数": "122",
            "实到人数": "12",
            "CO2浓度": "1180.0PPM",
            "空气湿度": "95.0%",
            "PM25浓度": "11μg",
            "温度": "23.8℃"
          },
          {
            "教室名": "上院115",
            "座位数": "169",
            "实到人数": "2",
            "CO2浓度": "None",
            "空气湿度": "50.0%",
            "PM25浓度": "5μg",
            "温度": "24.8℃"
          }
        ],
        [
          {
            "教室名": "上院201",
            "座位数": "87",
            "实到人数": "22",
            "CO2浓度": "452.0PPM",
            "空气湿度": "95.0%",
            "PM25浓度": "13μg",
            "温度": "23.4℃"
          },
          {
            "教室名": "上院202",
            "座位数": "87",
            "实到人数": "0",
            "CO2浓度": "500.0PPM",
            "空气湿度": "95.0%",
            "PM25浓度": "12μg",
            "温度": "25.7℃"
          },
          {
            "教室名": "上院203",
            "座位数": "87",
            "实到人数": "26",
            "CO2浓度": "424.0PPM",
            "空气湿度": "57.0%",
            "PM25浓度": "11μg",
            "温度": "22.9℃"
          },
          {
            "教室名": "上院204",
            "座位数": "87",
            "实到人数": "0",
            "CO2浓度": "454.0PPM",
            "空气湿度": "95.0%",
            "PM25浓度": "11μg",
            "温度": "23.2℃"
          },
          {
            "教室名": "上院205",
            "座位数": "87",
            "实到人数": "24",
            "CO2浓度": "506.0PPM",
            "空气湿度": "60.0%",
            "PM25浓度": "15μg",
            "温度": "22.1℃"
          },
          {
            "教室名": "上院207",
            "座位数": "67",
            "实到人数": "0",
            "CO2浓度": "554.0PPM",
            "空气湿度": "95.0%",
            "PM25浓度": "15μg",
            "温度": "23.5℃"
          },
          {
            "教室名": "上院210",
            "座位数": "87",
            "实到人数": "6",
            "CO2浓度": "None",
            "空气湿度": "86.0%",
            "PM25浓度": "3μg",
            "温度": "23.2℃"
          },
          {
            "教室名": "上院211",
            "座位数": "122",
            "实到人数": "0",
            "CO2浓度": "470.0PPM",
            "空气湿度": "87.0%",
            "PM25浓度": "1000μg",
            "温度": "24.1℃"
          },
          {
            "教室名": "上院212",
            "座位数": "122",
            "实到人数": "27",
            "CO2浓度": "702.0PPM",
            "空气湿度": "95.0%",
            "PM25浓度": "12μg",
            "温度": "26.4℃"
          },
          {
            "教室名": "上院213",
            "座位数": "122",
            "实到人数": "45",
            "CO2浓度": "702.0PPM",
            "空气湿度": "95.0%",
            "PM25浓度": "567μg",
            "温度": "24.8℃"
          },
          {
            "教室名": "上院215",
            "座位数": "178",
            "实到人数": "2",
            "CO2浓度": "1230.0PPM",
            "空气湿度": "82.0%",
            "PM25浓度": "8μg",
            "温度": "25.1℃"
          }
        ],
        [
          {
            "教室名": "上院301",
            "座位数": "30",
            "实到人数": "0",
            "CO2浓度": "402.0PPM",
            "空气湿度": "63.0%",
            "PM25浓度": "10μg",
            "温度": "22.8℃"
          },
          {
            "教室名": "上院302",
            "座位数": "30",
            "实到人数": "1",
            "CO2浓度": "494.0PPM",
            "空气湿度": "95.0%",
            "PM25浓度": "12μg",
            "温度": "23.7℃"
          },
          {
            "教室名": "上院303",
            "座位数": "30",
            "实到人数": "0",
            "CO2浓度": "566.0PPM",
            "空气湿度": "95.0%",
            "PM25浓度": "13μg",
            "温度": "23.1℃"
          },
          {
            "教室名": "上院304",
            "座位数": "30",
            "实到人数": "2",
            "CO2浓度": "452.0PPM",
            "空气湿度": "95.0%",
            "PM25浓度": "8μg",
            "温度": "24.6℃"
          },
          {
            "教室名": "上院305",
            "座位数": "30",
            "实到人数": "0",
            "CO2浓度": "820.0PPM",
            "空气湿度": "95.0%",
            "PM25浓度": "13μg",
            "温度": "25.3℃"
          },
          {
            "教室名": "上院306",
            "座位数": "30",
            "实到人数": "0",
            "CO2浓度": "450.0PPM",
            "空气湿度": "69.0%",
            "PM25浓度": "8μg",
            "温度": "22.9℃"
          },
          {
            "教室名": "上院307",
            "座位数": "30",
            "实到人数": "0",
            "CO2浓度": "928.0PPM",
            "空气湿度": "95.0%",
            "PM25浓度": "7μg",
            "温度": "22.7℃"
          },
          {
            "教室名": "上院308",
            "座位数": "30",
            "实到人数": "1",
            "CO2浓度": "552.0PPM",
            "空气湿度": "75.0%",
            "PM25浓度": "9μg",
            "温度": "22.2℃"
          },
          {
            "教室名": "上院309",
            "座位数": "30",
            "实到人数": "0",
            "CO2浓度": "None",
            "空气湿度": "94.0%",
            "PM25浓度": "11μg",
            "温度": "21.9℃"
          },
          {
            "教室名": "上院310",
            "座位数": "67",
            "实到人数": "1",
            "CO2浓度": "402.0PPM",
            "空气湿度": "88.0%",
            "PM25浓度": "8μg",
            "温度": "25.1℃"
          },
          {
            "教室名": "上院311",
            "座位数": "30",
            "实到人数": "0",
            "CO2浓度": "None",
            "空气湿度": "93.0%",
            "PM25浓度": "3μg",
            "温度": "20.0℃"
          },
          {
            "教室名": "上院312",
            "座位数": "30",
            "实到人数": "0",
            "CO2浓度": "880.0PPM",
            "空气湿度": "88.0%",
            "PM25浓度": "12μg",
            "温度": "22.5℃"
          },
          {
            "教室名": "上院313",
            "座位数": "67",
            "实到人数": "0",
            "CO2浓度": "49505.0PPM",
            "空气湿度": "94.0%",
            "PM25浓度": "13330μg",
            "温度": "21.6℃"
          },
          {
            "教室名": "上院314",
            "座位数": "30",
            "实到人数": "0",
            "CO2浓度": "438.0PPM",
            "空气湿度": "54.0%",
            "PM25浓度": "8μg",
            "温度": "25.3℃"
          },
          {
            "教室名": "上院315",
            "座位数": "161",
            "实到人数": "0",
            "CO2浓度": "1410.0PPM",
            "空气湿度": "95.0%",
            "PM25浓度": "9μg",
            "温度": "26.0℃"
          },
          {
            "教室名": "上院317",
            "座位数": "122",
            "实到人数": "23",
            "CO2浓度": "1024.0PPM",
            "空气湿度": "95.0%",
            "PM25浓度": "14μg",
            "温度": "24.1℃"
          },
          {
            "教室名": "上院318",
            "座位数": "122",
            "实到人数": "42",
            "CO2浓度": "578.0PPM",
            "空气湿度": "95.0%",
            "PM25浓度": "10μg",
            "温度": "25.3℃"
          },
          {
            "教室名": "上院319",
            "座位数": "122",
            "实到人数": "43",
            "CO2浓度": "688.0PPM",
            "空气湿度": "90.0%",
            "PM25浓度": "9μg",
            "温度": "25.3℃"
          }
        ],
        [
          {
            "教室名": "上院405",
            "座位数": "32",
            "实到人数": "None",
            "CO2浓度": "None",
            "空气湿度": "None",
            "PM25浓度": "None",
            "温度": "None"
          },
          {
            "教室名": "上院407",
            "座位数": "32",
            "实到人数": "None",
            "CO2浓度": "None",
            "空气湿度": "None",
            "PM25浓度": "None",
            "温度": "None"
          },
          {
            "教室名": "上院408",
            "座位数": "40",
            "实到人数": "None",
            "CO2浓度": "464.0PPM",
            "空气湿度": "48.0%",
            "PM25浓度": "5μg",
            "温度": "28.1℃"
          },
          {
            "教室名": "上院409",
            "座位数": "57",
            "实到人数": "None",
            "CO2浓度": "None",
            "空气湿度": "None",
            "PM25浓度": "None",
            "温度": "None"
          },
          {
            "教室名": "上院410",
            "座位数": "30",
            "实到人数": "0",
            "CO2浓度": "418.0PPM",
            "空气湿度": "46.0%",
            "PM25浓度": "10μg",
            "温度": "27.1℃"
          }
        ],
        [
          {
            "教室名": "上院515",
            "座位数": "178",
            "实到人数": "0",
            "CO2浓度": "472.0PPM",
            "空气湿度": "76.0%",
            "PM25浓度": "8μg",
            "温度": "28.3℃"
          }
        ]
      ],
      first:[],
      second:[],
      third:[],
      four:[],
      five:[],
      imgList:['static/pictures/shangyuan/shangyuan.jpg','static/pictures/shangyuan/shangyuan2.jpg'],
      navList:['教学楼图片','教学楼信息','教学楼位置','教学楼自习教室','更多服务'],
      tabIndex: '0',
      contentStyleObj: {
        height: '100px',
      },
      tabName: 'setOneRef',
      tabs: [
        {
          name: '教学楼图片',
          refName: 'setOneRef',
        },
        {
          name: '教学楼信息',
          refName: 'setTwoRef',
        },
        {
          name: '教学楼位置',
          refName: 'setThreeRef',
        },
        {
          name: '教学楼自习教室',
          refName: 'setFourRef',
        },
        {
          name: '更多服务',
          refName: 'setFiveRef',
        },
      ],
    }
  },
  computed: {},
  watch: {},
  created() {
    this.getHight()
    // this.fetchRooms();
    window.addEventListener('resize', this.getHight)
  },
  unmounted() {
    window.removeEventListener('resize', this.getHight)
  },
  methods: {
    returnLocation(){
      this.map = false;
      this.$nextTick(
          () => {
            this.map = true
          }
      )
    },
    handleClick(str){
      this.currentClassroomInfo.classroomName = str;
    },
    showPageChart(){
      this.showPage = true;
    },
    showClassPage(name){
      this.showPage = false;
      this.currentClassroomInfo.classroomName = name;
    },
    // tab click
    jump(tab) {
      let target = document.querySelector('.scroll-content')
      let scrollItems = document.querySelectorAll('.scroll-item')
      // 判断滚动条是否滚动到底部
      if (target.scrollHeight <= target.scrollTop + target.clientHeight) {
        this.tabIndex = tab.index.toString()
      }
      let totalY = scrollItems[tab.index].offsetTop - scrollItems[0].offsetTop // 锚点元素距离其offsetParent(这里是body)顶部的距离(待滚动的距离)
      let distance = document.querySelector('.scroll-content').scrollTop // 滚动条距离滚动区域顶部的距离
      // let distance = document.body.scrollTop || document.documentElement.scrollTop || window.pageYOffset // 滚动条距离滚动区域顶部的距离(滚动区域为窗口)
      // 滚动动画实现, 使用setTimeout的递归实现平滑滚动，将距离细分为50小段，10ms滚动一次
      // 计算每一小段的距离
      let step = totalY / 50
      if (totalY > distance) {
        smoothDown(document.querySelector('.scroll-content'))
      } else {
        let newTotal = distance - totalY
        step = newTotal / 50
        smoothUp(document.querySelector('.scroll-content'))
      }

      // 参数element为滚动区域
      function smoothDown(element) {
        if (distance < totalY) {
          distance += step
          element.scrollTop = distance
          setTimeout(smoothDown.bind(this, element), 10)
        } else {
          element.scrollTop = totalY
        }
      }

      // 参数element为滚动区域
      function smoothUp(element) {
        if (distance > totalY) {
          distance -= step
          element.scrollTop = distance
          setTimeout(smoothUp.bind(this, element), 10)
        } else {
          element.scrollTop = totalY
        }
      }
    },
    // 滚动条滚动
    onScroll(e) {
      let scrollItems = document.querySelectorAll('.scroll-item')
      for (let i = scrollItems.length - 1; i >= 0; i--) {
        // 判断滚动条滚动距离是否大于当前滚动项可滚动距离
        let judge =
            e.target.scrollTop >=
            scrollItems[i].offsetTop - scrollItems[0].offsetTop - 400
        if (judge) {
          this.tabIndex = i.toString()
          // 找对应的tab-name值
          this.tabName = this.tabs[this.tabIndex].refName
          break
        }
      }
    },
    getHight() {
      this.contentStyleObj.height = window.innerHeight - 190 + 'px'
    },
    fetchRooms(){
      axios.post('http://127.0.0.1/getBuildingLayer',{
        building: '上院',
      }).then(res=>{
        this.classRooms = res.data;
        console.log(this.classRooms);
      }).catch(err=>{
        console.log("获取数据失败" + err);
      });
    }
  },
}
</script>


<style lang="scss" scoped>
.scroll-content::-webkit-scrollbar{
  width: 0;
}
* {
  overflow-x: hidden;
}
::v-deep.customer-tab {
  width: 100%;
  height: 50px;
  background-color:#f5f7fa;
  padding: 4px;
}
::v-deep.el-tabs--card > .el-tabs__header {
  border-bottom: none;
  margin: 0;
  .el-tabs__nav {
    width: 100%;
    display: flex;
    justify-content: space-around;
    border: none;
    .el-tabs__item {
      width: 25%;
      text-align: center;
      border: none;
    }
    .is-active {
      border-radius: 4px;
      background-color: #005BD9;
      color: #fff;
    }
  }
}
</style>


