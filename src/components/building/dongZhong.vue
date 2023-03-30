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
      <h1 style="font-size: 3.5rem"> 东中院 </h1>
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
        <baidu-map v-if="map" :points="[121.443979,31.029662]"></baidu-map>
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
            34204418
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
            "教室名": "东中院1-104",
            "座位数": "24",
            "实到人数": "0",
            "CO2浓度": "420.0PPM",
            "空气湿度": "56.8%",
            "PM25浓度": "4μg",
            "温度": "21.7℃"
          },
          {
            "教室名": "东中院1-105",
            "座位数": "28",
            "实到人数": "0",
            "CO2浓度": "443.0PPM",
            "空气湿度": "55.9%",
            "PM25浓度": "6μg",
            "温度": "22.7℃"
          },
          {
            "教室名": "东中院1-106",
            "座位数": "194",
            "实到人数": "0",
            "CO2浓度": "423.0PPM",
            "空气湿度": "58.7%",
            "PM25浓度": "6μg",
            "温度": "21.9℃"
          },
          {
            "教室名": "东中院1-107",
            "座位数": "125",
            "实到人数": "0",
            "CO2浓度": "461.0PPM",
            "空气湿度": "59.0%",
            "PM25浓度": "8μg",
            "温度": "22.1℃"
          },
          {
            "教室名": "东中院1-108",
            "座位数": "90",
            "实到人数": "2",
            "CO2浓度": "422.0PPM",
            "空气湿度": "61.3%",
            "PM25浓度": "7μg",
            "温度": "21.0℃"
          },
          {
            "教室名": "东中院1-109",
            "座位数": "78",
            "实到人数": "37",
            "CO2浓度": "681.0PPM",
            "空气湿度": "56.8%",
            "PM25浓度": "7μg",
            "温度": "23.3℃"
          },
          {
            "教室名": "东中院1-201",
            "座位数": "45",
            "实到人数": "0",
            "CO2浓度": "456.0PPM",
            "空气湿度": "52.1%",
            "PM25浓度": "7μg",
            "温度": "24.2℃"
          },
          {
            "教室名": "东中院1-202",
            "座位数": "45",
            "实到人数": "0",
            "CO2浓度": "468.0PPM",
            "空气湿度": "53.2%",
            "PM25浓度": "6μg",
            "温度": "24.0℃"
          },
          {
            "教室名": "东中院1-203",
            "座位数": "24",
            "实到人数": "0",
            "CO2浓度": "427.0PPM",
            "空气湿度": "51.6%",
            "PM25浓度": "7μg",
            "温度": "23.9℃"
          },
          {
            "教室名": "东中院1-204",
            "座位数": "24",
            "实到人数": "0",
            "CO2浓度": "424.0PPM",
            "空气湿度": "52.3%",
            "PM25浓度": "9μg",
            "温度": "23.5℃"
          },
          {
            "教室名": "东中院1-301",
            "座位数": "45",
            "实到人数": "0",
            "CO2浓度": "414.0PPM",
            "空气湿度": "51.4%",
            "PM25浓度": "7μg",
            "温度": "23.8℃"
          },
          {
            "教室名": "东中院1-302",
            "座位数": "45",
            "实到人数": "0",
            "CO2浓度": "432.0PPM",
            "空气湿度": "52.0%",
            "PM25浓度": "8μg",
            "温度": "23.8℃"
          },
          {
            "教室名": "东中院1-303",
            "座位数": "24",
            "实到人数": "0",
            "CO2浓度": "421.0PPM",
            "空气湿度": "51.2%",
            "PM25浓度": "7μg",
            "温度": "23.7℃"
          },
          {
            "教室名": "东中院1-304",
            "座位数": "24",
            "实到人数": "2",
            "CO2浓度": "440.0PPM",
            "空气湿度": "51.4%",
            "PM25浓度": "6μg",
            "温度": "23.7℃"
          }
        ],
        [
          {
            "教室名": "东中院2-101",
            "座位数": "24",
            "实到人数": "0",
            "CO2浓度": "472.0PPM",
            "空气湿度": "57.7%",
            "PM25浓度": "7μg",
            "温度": "23.2℃"
          },
          {
            "教室名": "东中院2-102",
            "座位数": "24",
            "实到人数": "0",
            "CO2浓度": "636.0PPM",
            "空气湿度": "56.8%",
            "PM25浓度": "8μg",
            "温度": "24.0℃"
          },
          {
            "教室名": "东中院2-103",
            "座位数": "72",
            "实到人数": "0",
            "CO2浓度": "439.0PPM",
            "空气湿度": "57.6%",
            "PM25浓度": "8μg",
            "温度": "22.4℃"
          },
          {
            "教室名": "东中院2-106",
            "座位数": "130",
            "实到人数": "1",
            "CO2浓度": "425.0PPM",
            "空气湿度": "54.2%",
            "PM25浓度": "7μg",
            "温度": "24.0℃"
          },
          {
            "教室名": "东中院2-201",
            "座位数": "24",
            "实到人数": "0",
            "CO2浓度": "1626.0PPM",
            "空气湿度": "58.0%",
            "PM25浓度": "5μg",
            "温度": "24.3℃"
          },
          {
            "教室名": "东中院2-202",
            "座位数": "24",
            "实到人数": "10",
            "CO2浓度": "757.0PPM",
            "空气湿度": "57.2%",
            "PM25浓度": "8μg",
            "温度": "23.8℃"
          },
          {
            "教室名": "东中院2-203",
            "座位数": "72",
            "实到人数": "0",
            "CO2浓度": "414.0PPM",
            "空气湿度": "55.1%",
            "PM25浓度": "6μg",
            "温度": "22.6℃"
          },
          {
            "教室名": "东中院2-206",
            "座位数": "130",
            "实到人数": "0",
            "CO2浓度": "472.0PPM",
            "空气湿度": "51.9%",
            "PM25浓度": "6μg",
            "温度": "24.0℃"
          },
          {
            "教室名": "东中院2-301",
            "座位数": "24",
            "实到人数": "0",
            "CO2浓度": "423.0PPM",
            "空气湿度": "55.5%",
            "PM25浓度": "8μg",
            "温度": "23.0℃"
          },
          {
            "教室名": "东中院2-302",
            "座位数": "24",
            "实到人数": "0",
            "CO2浓度": "528.0PPM",
            "空气湿度": "57.9%",
            "PM25浓度": "8μg",
            "温度": "22.5℃"
          },
          {
            "教室名": "东中院2-303",
            "座位数": "72",
            "实到人数": "0",
            "CO2浓度": "443.0PPM",
            "空气湿度": "55.4%",
            "PM25浓度": "7μg",
            "温度": "22.9℃"
          },
          {
            "教室名": "东中院2-305",
            "座位数": "20",
            "实到人数": "0",
            "CO2浓度": "480.0PPM",
            "空气湿度": "51.1%",
            "PM25浓度": "6μg",
            "温度": "25.0℃"
          },
          {
            "教室名": "东中院2-306",
            "座位数": "130",
            "实到人数": "16",
            "CO2浓度": "469.0PPM",
            "空气湿度": "54.5%",
            "PM25浓度": "6μg",
            "温度": "22.8℃"
          },
          {
            "教室名": "东中院2-401",
            "座位数": "24",
            "实到人数": "0",
            "CO2浓度": "420.0PPM",
            "空气湿度": "56.3%",
            "PM25浓度": "7μg",
            "温度": "22.7℃"
          },
          {
            "教室名": "东中院2-402",
            "座位数": "24",
            "实到人数": "0",
            "CO2浓度": "469.0PPM",
            "空气湿度": "56.8%",
            "PM25浓度": "5μg",
            "温度": "22.1℃"
          },
          {
            "教室名": "东中院2-403",
            "座位数": "72",
            "实到人数": "0",
            "CO2浓度": "431.0PPM",
            "空气湿度": "55.0%",
            "PM25浓度": "6μg",
            "温度": "22.6℃"
          },
          {
            "教室名": "东中院2-405",
            "座位数": "20",
            "实到人数": "0",
            "CO2浓度": "463.0PPM",
            "空气湿度": "52.6%",
            "PM25浓度": "6μg",
            "温度": "23.9℃"
          },
          {
            "教室名": "东中院2-406",
            "座位数": "20",
            "实到人数": "0",
            "CO2浓度": "443.0PPM",
            "空气湿度": "49.5%",
            "PM25浓度": "7μg",
            "温度": "24.1℃"
          }
        ],
        [
          {
            "教室名": "东中院3-102",
            "座位数": "51",
            "实到人数": "13",
            "CO2浓度": "479.0PPM",
            "空气湿度": "54.8%",
            "PM25浓度": "9μg",
            "温度": "23.8℃"
          },
          {
            "教室名": "东中院3-104",
            "座位数": "58",
            "实到人数": "0",
            "CO2浓度": "468.0PPM",
            "空气湿度": "56.5%",
            "PM25浓度": "8μg",
            "温度": "22.9℃"
          },
          {
            "教室名": "东中院3-105",
            "座位数": "58",
            "实到人数": "0",
            "CO2浓度": "560.0PPM",
            "空气湿度": "58.0%",
            "PM25浓度": "9μg",
            "温度": "22.6℃"
          },
          {
            "教室名": "东中院3-106",
            "座位数": "73",
            "实到人数": "5",
            "CO2浓度": "431.0PPM",
            "空气湿度": "53.4%",
            "PM25浓度": "6μg",
            "温度": "24.1℃"
          },
          {
            "教室名": "东中院3-202",
            "座位数": "51",
            "实到人数": "0",
            "CO2浓度": "422.0PPM",
            "空气湿度": "54.3%",
            "PM25浓度": "7μg",
            "温度": "23.4℃"
          },
          {
            "教室名": "东中院3-204",
            "座位数": "62",
            "实到人数": "0",
            "CO2浓度": "415.0PPM",
            "空气湿度": "52.6%",
            "PM25浓度": "6μg",
            "温度": "23.9℃"
          },
          {
            "教室名": "东中院3-205",
            "座位数": "58",
            "实到人数": "0",
            "CO2浓度": "428.0PPM",
            "空气湿度": "55.5%",
            "PM25浓度": "7μg",
            "温度": "23.0℃"
          },
          {
            "教室名": "东中院3-206",
            "座位数": "73",
            "实到人数": "5",
            "CO2浓度": "452.0PPM",
            "空气湿度": "51.7%",
            "PM25浓度": "6μg",
            "温度": "24.3℃"
          },
          {
            "教室名": "东中院3-302",
            "座位数": "51",
            "实到人数": "0",
            "CO2浓度": "445.0PPM",
            "空气湿度": "50.8%",
            "PM25浓度": "7μg",
            "温度": "24.6℃"
          },
          {
            "教室名": "东中院3-304",
            "座位数": "58",
            "实到人数": "7",
            "CO2浓度": "576.0PPM",
            "空气湿度": "55.9%",
            "PM25浓度": "7μg",
            "温度": "22.9℃"
          },
          {
            "教室名": "东中院3-305",
            "座位数": "58",
            "实到人数": "0",
            "CO2浓度": "436.0PPM",
            "空气湿度": "51.8%",
            "PM25浓度": "8μg",
            "温度": "23.3℃"
          },
          {
            "教室名": "东中院3-306",
            "座位数": "73",
            "实到人数": "44",
            "CO2浓度": "847.0PPM",
            "空气湿度": "54.3%",
            "PM25浓度": "5μg",
            "温度": "24.9℃"
          },
          {
            "教室名": "东中院3-402",
            "座位数": "51",
            "实到人数": "0",
            "CO2浓度": "421.0PPM",
            "空气湿度": "52.5%",
            "PM25浓度": "6μg",
            "温度": "23.7℃"
          },
          {
            "教室名": "东中院3-404",
            "座位数": "58",
            "实到人数": "0",
            "CO2浓度": "433.0PPM",
            "空气湿度": "57.0%",
            "PM25浓度": "7μg",
            "温度": "22.4℃"
          },
          {
            "教室名": "东中院3-405",
            "座位数": "58",
            "实到人数": "0",
            "CO2浓度": "434.0PPM",
            "空气湿度": "53.9%",
            "PM25浓度": "6μg",
            "温度": "23.0℃"
          },
          {
            "教室名": "东中院3-406",
            "座位数": "73",
            "实到人数": "11",
            "CO2浓度": "417.0PPM",
            "空气湿度": "52.7%",
            "PM25浓度": "5μg",
            "温度": "23.5℃"
          }
        ],
        [
          {
            "教室名": "东中院4-101",
            "座位数": "63",
            "实到人数": "0",
            "CO2浓度": "440.0PPM",
            "空气湿度": "54.1%",
            "PM25浓度": "8μg",
            "温度": "23.8℃"
          },
          {
            "教室名": "东中院4-102",
            "座位数": "40",
            "实到人数": "18",
            "CO2浓度": "439.0PPM",
            "空气湿度": "54.0%",
            "PM25浓度": "8μg",
            "温度": "23.9℃"
          },
          {
            "教室名": "东中院4-103",
            "座位数": "48",
            "实到人数": "0",
            "CO2浓度": "418.0PPM",
            "空气湿度": "53.3%",
            "PM25浓度": "9μg",
            "温度": "23.5℃"
          },
          {
            "教室名": "东中院4-104",
            "座位数": "40",
            "实到人数": "1",
            "CO2浓度": "459.0PPM",
            "空气湿度": "54.4%",
            "PM25浓度": "9μg",
            "温度": "23.9℃"
          },
          {
            "教室名": "东中院4-106",
            "座位数": "45",
            "实到人数": "0",
            "CO2浓度": "885.0PPM",
            "空气湿度": "50.9%",
            "PM25浓度": "8μg",
            "温度": "26.0℃"
          },
          {
            "教室名": "东中院4-201",
            "座位数": "63",
            "实到人数": "18",
            "CO2浓度": "599.0PPM",
            "空气湿度": "52.8%",
            "PM25浓度": "6μg",
            "温度": "24.3℃"
          },
          {
            "教室名": "东中院4-202",
            "座位数": "40",
            "实到人数": "0",
            "CO2浓度": "447.0PPM",
            "空气湿度": "50.6%",
            "PM25浓度": "5μg",
            "温度": "24.8℃"
          },
          {
            "教室名": "东中院4-203",
            "座位数": "48",
            "实到人数": "18",
            "CO2浓度": "453.0PPM",
            "空气湿度": "50.4%",
            "PM25浓度": "6μg",
            "温度": "24.6℃"
          },
          {
            "教室名": "东中院4-204",
            "座位数": "40",
            "实到人数": "0",
            "CO2浓度": "482.0PPM",
            "空气湿度": "50.5%",
            "PM25浓度": "7μg",
            "温度": "24.9℃"
          },
          {
            "教室名": "东中院4-206",
            "座位数": "45",
            "实到人数": "9",
            "CO2浓度": "502.0PPM",
            "空气湿度": "46.1%",
            "PM25浓度": "6μg",
            "温度": "26.2℃"
          },
          {
            "教室名": "东中院4-301",
            "座位数": "63",
            "实到人数": "0",
            "CO2浓度": "430.0PPM",
            "空气湿度": "49.2%",
            "PM25浓度": "5μg",
            "温度": "25.1℃"
          },
          {
            "教室名": "东中院4-302",
            "座位数": "40",
            "实到人数": "16",
            "CO2浓度": "565.0PPM",
            "空气湿度": "52.1%",
            "PM25浓度": "7μg",
            "温度": "24.2℃"
          },
          {
            "教室名": "东中院4-303",
            "座位数": "48",
            "实到人数": "0",
            "CO2浓度": "423.0PPM",
            "空气湿度": "50.5%",
            "PM25浓度": "6μg",
            "温度": "24.1℃"
          },
          {
            "教室名": "东中院4-304",
            "座位数": "40",
            "实到人数": "8",
            "CO2浓度": "438.0PPM",
            "空气湿度": "50.4%",
            "PM25浓度": "6μg",
            "温度": "24.6℃"
          },
          {
            "教室名": "东中院4-306",
            "座位数": "45",
            "实到人数": "0",
            "CO2浓度": "415.0PPM",
            "空气湿度": "50.7%",
            "PM25浓度": "6μg",
            "温度": "24.0℃"
          },
          {
            "教室名": "东中院4-401",
            "座位数": "63",
            "实到人数": "10",
            "CO2浓度": "531.0PPM",
            "空气湿度": "51.7%",
            "PM25浓度": "5μg",
            "温度": "24.3℃"
          },
          {
            "教室名": "东中院4-402",
            "座位数": "40",
            "实到人数": "0",
            "CO2浓度": "530.0PPM",
            "空气湿度": "52.3%",
            "PM25浓度": "6μg",
            "温度": "24.1℃"
          },
          {
            "教室名": "东中院4-403",
            "座位数": "48",
            "实到人数": "42",
            "CO2浓度": "905.0PPM",
            "空气湿度": "53.4%",
            "PM25浓度": "7μg",
            "温度": "24.8℃"
          },
          {
            "教室名": "东中院4-404",
            "座位数": "40",
            "实到人数": "0",
            "CO2浓度": "511.0PPM",
            "空气湿度": "51.0%",
            "PM25浓度": "6μg",
            "温度": "24.4℃"
          },
          {
            "教室名": "东中院4-406",
            "座位数": "45",
            "实到人数": "6",
            "CO2浓度": "444.0PPM",
            "空气湿度": "50.0%",
            "PM25浓度": "7μg",
            "温度": "24.4℃"
          },
          {
            "教室名": "东中院4-501",
            "座位数": "63",
            "实到人数": "0",
            "CO2浓度": "450.0PPM",
            "空气湿度": "53.7%",
            "PM25浓度": "6μg",
            "温度": "22.9℃"
          },
          {
            "教室名": "东中院4-502",
            "座位数": "40",
            "实到人数": "4",
            "CO2浓度": "450.0PPM",
            "空气湿度": "52.7%",
            "PM25浓度": "5μg",
            "温度": "23.3℃"
          },
          {
            "教室名": "东中院4-503",
            "座位数": "48",
            "实到人数": "0",
            "CO2浓度": "453.0PPM",
            "空气湿度": "53.1%",
            "PM25浓度": "6μg",
            "温度": "23.4℃"
          },
          {
            "教室名": "东中院4-504",
            "座位数": "40",
            "实到人数": "2",
            "CO2浓度": "438.0PPM",
            "空气湿度": "51.5%",
            "PM25浓度": "6μg",
            "温度": "23.9℃"
          },
          {
            "教室名": "东中院4-506",
            "座位数": "45",
            "实到人数": "0",
            "CO2浓度": "459.0PPM",
            "空气湿度": "51.9%",
            "PM25浓度": "8μg",
            "温度": "23.6℃"
          }
        ]
      ],
      first:[],
      second:[],
      third:[],
      four:[],
      five:[],
      imgList:['static/pictures/dongzhong/dongzhong.jpg','static/pictures/dongzhong/dongzhong1.jpg','static/pictures/dongzhong/dongzhong2.jpg','static/pictures/dongzhong/dongzhong3.jpg'],
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
      axios.post('http://127.0.0.1/getBuildingLayer',
      {
        building: '东中院',
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


