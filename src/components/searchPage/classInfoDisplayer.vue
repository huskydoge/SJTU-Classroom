<template>
<!--  TODO 各种信息前可以加上logo-->
  <!--  TODO 各种信息其实可以通过一个函数设置如果有的话就显示，没有就不显示-->

  <el-backtop target=".middle"></el-backtop>
  <div class="container" >
    <div class="left"></div>
    <div class="middle">
      <div style="margin-left: 10px;margin-right: 10px;margin-top: 10px">
      <div id="header" style="display: flex;justify-content: space-between">
        <h1> {{ this.classInformation['教室名'] }} </h1>
        <el-button @click="this.returnSearching">return</el-button>
      </div>
        <el-tabs  class="el-tabs" tab-position="top" v-model="activeName" @tab-change="handleClick">
          <el-tab-pane  label="教室信息" name="info" >
          </el-tab-pane>
          <el-tab-pane label="折线图" name="plot" >
          </el-tab-pane>
          <el-tab-pane label="热力图" name="heatmap">
          </el-tab-pane>
          <el-tab-pane label="饼图" name="rate">
          </el-tab-pane>
          <el-tab-pane label="评论区" name="comment">
          </el-tab-pane>
          <el-tab-pane label="失物招领" name="lostAndFound">
          </el-tab-pane>
        </el-tabs>
      <div>
        <br>
        <!--  TODO VR图地址换了，而且大小还需要调整-->
        <br>
        <div class="tabContent" style="width: 1000px;"></div>
        <ClassroomInfo :classroom="this.classroomName" :class-info="this.classInformation" :class-characters="this.classCharacters" v-if="activeName === 'info' "></ClassroomInfo>
        <week-calendar v-if="activeName === 'heatmap'" :name="classroomName"></week-calendar>
        <calendar :display-heat-map="activeName === 'heatmap'"></calendar>
        <multi-plot-chart v-if="activeName === 'plot'" :classname="classroomName"></multi-plot-chart>
        <rate-page :classname="classroomName" v-if="activeName === 'rate'"></rate-page>
        <comment-box :classroom-name="this.classroomName" v-if="activeName === 'comment' "></comment-box>
        <lost-and-found :classroom-specified="this.classInformation['教室名']" v-if="activeName === 'lostAndFound'"></lost-and-found>
      </div>
      </div>
    </div>


    <div class="right">
    </div>

  </div>
</template>

<script>
import axios from "axios";
import CommentBox from "@/components/classRoom/commentPage";
import ClassroomInfo from "@/components/classRoom/ClassroomInfo";
import calendar from "@/components/classRoom/calendar";
import LostAndFound from "@/components/classRoom/lostAndFound";
import multiPlotChart from "@/components/classRoom/multiPlotChart";
import ratePage from "@/components/classRoom/ratePage";
import WeekCalendar from "@/components/charts/weekCalendar";
export default {
  name: "classInfoDisplayer",
  props:{
    classroomName:String,
  },
  data(){
    return {
      activeName: 'info',
      classInformation: Object,
      classCharacters: Object,
    }
  },
  methods:{
    handleClick() {
    },
    // 返回搜索界面
    returnSearching(){
      this.$emit("return");
    },
    fill(str){
      if(str == '' || str == 'None' || str == undefined || str == "NONE"){
        return '暂无信息';
      } else {
        return str;
      }
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
        // console.log(res)
        // alert(this.classCharacters['教师姓名']);
      }).catch(err=>{
        console.log("获取数据失败" + err);
      });
    },
  },
  components:{
    WeekCalendar,
    multiPlotChart,
    LostAndFound,
    ClassroomInfo,
    calendar,
    CommentBox,
    ratePage,
  },
  created() {
    // 获取相关数据
    this.getClassroomCharacter();
    this.getClassroomInfo();
  },
}
</script>

<style>

.el-tabs{
  display: flex;
  margin: 0 auto;
  justify-self: center;
  justify-items: center;
}

.el-tabs__header{
  margin: 0 auto;
}

.container {
  margin-top: 10px;
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
}
.left, .right, .middle {
  height: 100%;
}
.left {
}
.right {
}
.middle::-webkit-scrollbar{
  width: 0;
}
.middle {
  width: 1000px;
  overflow-y: auto;
  margin-top: 1rem;
  padding-left: 1rem;
  padding-right: 1rem;
  padding-bottom: 2rem;
  border-left: 1px solid red;
  border-right: 1px solid red;
  background: #FDFDFD;
}
#app > header > section > div > div.middle > div > div:nth-child(3) > div:nth-child(4) > div.ctt > div > div > iframe{
  width: 100%;
}

</style>