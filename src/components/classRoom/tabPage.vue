<template>

  <nav style="position:fixed;top:100px;right: 200px">
    <el-tabs tab-position="right" v-model="activeName" @tab-change="handleClick">
      <el-tab-pane label="教室信息" name="info" >
      </el-tab-pane>
      <el-tab-pane label="折线图" name="plot" >
      </el-tab-pane>
      <el-tab-pane label="热力图" name="heatmap">
      </el-tab-pane>
      <el-tab-pane label="柱状图" name="bar">
      </el-tab-pane>
      <el-tab-pane label="饼图" name="ratePage">
      </el-tab-pane>
      <el-tab-pane label="评论区" name="comment">
    </el-tab-pane>
      <el-tab-pane label="失物招领" name="lostAndFound">
      </el-tab-pane>
    </el-tabs>
  </nav>

<!--  用v-if控制不同组件的展示-->
  <div class="tabContent" style="width: 1500px;margin-top: 30px"></div>
  <ClassroomInfo :classroom="this.classroomName" style="margin-left: 20px" :class-info="this.classInformation" :class-characters="this.classCharacters" v-if="activeName === 'info' "></ClassroomInfo>
  <week-calendar :name="this.classroomName" v-if="activeName === 'heatmap'"></week-calendar>
  <calendar :display-heat-map="activeName === 'heatmap'"></calendar>
  <multi-plot-chart :classname="classroomName" v-if="activeName === 'plot'"> </multi-plot-chart>
  <rate-page :classname="classroomName" v-if="activeName === 'ratePage'"></rate-page>
  <comment-box :classroom-name="this.classroomName" v-if="activeName === 'comment' "></comment-box>
  <lost-and-found :classroom-specified="this.classInformation['教室名']" v-if="activeName === 'lostAndFound'"></lost-and-found>
  <bar-below-search :custom-choice="true" v-if="activeName === 'bar'"></bar-below-search>
</template>
<script>
import axios from "axios"
import CommentBox from "@/components/classRoom/commentPage";
import ClassroomInfo from "@/components/classRoom/ClassroomInfo";
import calendar from "@/components/classRoom/calendar";
import LostAndFound from "@/components/classRoom/lostAndFound";
import weekCalendar from "@/components/charts/weekCalendar";
import ratePage from "@/components/classRoom/ratePage";
import BarBelowSearch from "@/components/searchPage/barBelowSearch";
import multiPlotChart from "@/components/classRoom/multiPlotChart";
// 日历图组件
export default {
  name: "tabPage",
  props:{
    classroomName: String,
  },
  data() {
    return {
      activeName: "info",
      classInformation:Object,
      classCharacters: Object,
    }
  },
  methods: {
    handleClick() {
    },
    getClassroomInfo() {
      axios.get('http://127.0.0.1/classroomInfo',
          {
            params: {
              教室名: this.classroomName
            }
          }).then(res=>{
        this.classInformation = res.data[0];
        // alert(this.classInformation['教室名']);
      }).catch(err=>{
        console.log("获取数据失败" + err);
      });
    },
    getClassroomCharacter() {
      axios.get('http://127.0.0.1/classroomCharacter',
          {
            params: {
              教室名: this.classroomName
            }
          }).then(res=>{
        this.classCharacters = res.data[0];
        // alert(this.classCharacters['自习位']);
      }).catch(err=>{

        console.log("获取数据失败" + err);
      });
    },
  },
  created() {
    // 获取相关数据
    this.getClassroomInfo();
    this.getClassroomCharacter();
  },
  computed: {
  },
  components:{
    multiPlotChart,
    BarBelowSearch,
    ratePage,
    weekCalendar,
    LostAndFound,
    ClassroomInfo,
    calendar,
    CommentBox,
  },
}
</script>

<style>
element.style {
  width: 1154px;
  height: 1000px;
}
</style>