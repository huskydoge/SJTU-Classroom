<!--找教室的搜索引擎,
1.要开启fastAPI project：'classroomAPI' 的端口服务
2.开启es和ki
3.激活数据库
4.打开node.js
-->
<template>
  <!--  展示classInfo，则所有数据不可见-->
  <div v-if="!showClassInfo" id="search">
<!--    <div class="top-img"></div>-->
    <div class="top-search" >
      <div class="search-box">
        <div style="width: 800px;display: flex;align-items: center">
        <input type="text" autocomplete="off" v-model="this.classname" id="searchInputBox" class="search-left">
        <el-button class="search-right view btn" type="button" @mouseenter="this.selectView = true;" >切换视图</el-button>
        </div>
        <transition name="view">
        <div  @mouseleave="this.selectView = false" v-if="selectView"  style="display: inline-flex;align-items: center;position: absolute;right: 3%;top: 130%">
          <el-tooltip
              content="以卡片形式展开"
              placement="bottom"
              >
          <button class="viewBtn btn" type="button" @click="changeView('card')">卡片</button>
          </el-tooltip>
          <el-tooltip
              content="以气泡图形式呈现，气泡大小表征数据大小"
              placement="bottom"
          >
          <button class="viewBtn btn" type="button" @click="changeView('bubble');">气泡图</button>
          </el-tooltip>
          <el-tooltip
              content="以柱状图形式呈现数据，支持放大和拖动"
              placement="bottom"
          >
          <button class="viewBtn btn" type="button" @click="changeView('bar')">柱状图</button>
          </el-tooltip>
        </div>
        </transition>
      </div>
    </div>
<!--    像bubbleChart组件中传入外部数据  -->
    <div style="display: flex;justify-content: center">
    <bubble-below-search :custom-choice="false" v-if="!this.resultIsEmpty && this.active === 'bubble'" :data-from-search="this.classroomData" @showClassInfo="this.displayClassInfo"></bubble-below-search>
    <cards-below-search :choices="choiceObj" style="padding-top: 10px" v-if="!this.resultIsEmpty && this.active === 'card'" :data-from-search="this.classroomData" @showClassInfo="this.displayClassInfoAndStoreChoice"></cards-below-search>
      <el-empty style="margin-top: 100px" v-if="this.resultIsEmpty" description="没有搜索结果哦～" />
      <bar-below-search  v-if="!this.resultIsEmpty && this.active === 'bar'" :data-from-search="this.classroomData"  @showClassInfo="this.displayClassInfo"></bar-below-search>
    </div>
  </div>
  <class-info-displayer v-if="showClassInfo" :classroom-name="this.selectedClassName" @return="this.returnSearching">
  </class-info-displayer>
</template>

<script>
import axios from "axios";
import bubbleBelowSearch from "@/components/searchPage/bubbleBelowSearch";
import cardsBelowSearch from "@/components/searchPage/cardsBelowSearch";
import ClassInfoDisplayer from "@/components/searchPage/classInfoDisplayer";
import BarBelowSearch from "@/components/searchPage/barBelowSearch";
export default {
  data(){
    return{
      choiceObj:{
        seats: '任意',
        people: '任意',
        vacancy: '任意',
        co2: '任意',
        pm25: '任意',
        temperature: '任意',
        multiSort: false,
        toSelect: false,
        toSort: false,
        data: [],
      },
      active: 'card',
      selectView: false,
      value: '',
      options: [
        {
          value: 'Option1',
          label: 'Option1',
        },
        {
          value: 'Option2',
          label: 'Option2',
        },
        {
          value: 'Option3',
          label: 'Option3',
        },
        {
          value: 'Option4',
          label: 'Option4',
        },
        {
          value: 'Option5',
          label: 'Option5',
        },
      ],
      condition: String,
      classData: [],
      selectedClassName: "东上院101", // 记录选中的教室名
      classname : '', // 记录搜索框内容
      classroomData: [],
      showClassInfo: false,
      resultIsEmpty: false,
    }
  },
  components:{
    BarBelowSearch,
    ClassInfoDisplayer,
    cardsBelowSearch,
    bubbleBelowSearch,
  },
  methods: {
    changeView(str){ // 改变搜索结果的展示方式
      if(!(this.classname.length === 0)){
        this.fetchData();
      } else {
        this.fetchAllData(); // 如果搜索框为空，则展示默认的数据
      }
      this.active = str;
    },
    fetchData() {
      // FastAPI方法
      // 通过get请求获得与当前搜索的教室名相符合的搜索结果
      axios.get('http://127.0.0.1:8000/classroomInfo',
          {
            params:{
              classname: this.classname,
      }
          }).then(res => {
            // this.classrooms = res;
            let tmp = [];
            // console.log(res.data[0]['_source']);
            let cnt = 1 // index
            for(const i in res.data){
              let obj = {
                  depth: 1,
                  id: 'classroom.' + res.data[i]['_source']['教室名'],
                  index: cnt,
                  vacancy: res.data[i]['_source']['座位数'] - res.data[i]['_source']['实到人数'],
                  seats: res.data[i]['_source']['座位数'],
                  people: res.data[i]['_source']['实到人数'],
                  name: res.data[i]['_source']['教室名'],
                  co2: res.data[i]['_source']['co2浓度'],
                  pm25:res.data[i]['_source']['pm25浓度'],
                  temperature:res.data[i]['_source']['温度'],
                  humidity: res.data[i]['_source']['空气湿度'],
              };
              tmp.push(obj);
              cnt ++
            }
            // 将搜索结果返回给data
            if(tmp.length==0){this.resultIsEmpty = true;}
            else {
              this.classroomData = tmp;
              // console.log(this.classroomData);
              this.resultIsEmpty = false;
            }
        // console.log('fromsearch');
        console.log(this.classroomData.length);
          }
      ).catch(err => {
        console.log("获取数据失败" + err);
      });
    },
    fetchAllData(){ // 要先在终端运行 node app.js
      this.classData = [];
      axios.get('http://127.0.0.1/getAllClassroom').then(res=>{
        let cnt = 1; // index
        for(const i in res.data){
          let obj = {
            depth: 1,
            id: 'classroom.' + res.data[i]['教室名'],
            index: cnt,
            vacancy: res.data[i]['座位数'] - res.data[i]['实到人数'],
            seats: res.data[i]['座位数'],
            people: res.data[i]['实到人数'],
            name: res.data[i]['教室名'],
            co2: res.data[i]['CO2浓度'],
            pm25:res.data[i]['PM25浓度'],
            temperature:res.data[i]['温度'],
            humidity: res.data[i]['空气湿度'],
          };
          this.classData.push(obj);
          ++ cnt;
        }
        // 按照空余位置排序
        this.classData.sort(function(a,b){
          return b.vacancy - a.vacancy;
        });

        this.classroomData = this.classData;
        this.resultIsEmpty = false;
        console.log(this.classData);
      }).catch(err=>{
        console.log("获取数据失败" + err);
      });
    },
    handleSearch(){
      if(this.classname.length === 0){
        this.fetchAllData();
      } else {
        this.fetchData();
      }
    },
    displayClassInfo(params){
      this.showClassInfo = true;
      this.selectedClassName = params;
      // console.log(this.selectedClassName);
    },
    displayClassInfoAndStoreChoice(params, obj){
      this.showClassInfo = true;
      this.selectedClassName = params;
      this.choiceObj = obj;
    },
    returnSearching(){
      this.showClassInfo = false;
      this.classname = '';
    }
  },
  watch:{
    classname(){
      this.handleSearch();
    }
  }
}

</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}

#search{
  margin: 0 auto;
}

#searchInputBox{
  padding-left: 12px;
}

.top-search {
  width: 680px;
  height: 45px;
  margin: 10px auto;
}

.search-box {
  position: relative;
}

.search-left {
  width: 545px;
  height: 45px;
  border: 2px solid rgb(196, 199, 206);
  border-bottom-left-radius: 10px;
  border-top-left-radius: 10px;
  outline-color: rgb(78, 110, 242);
}

.view{
  border-bottom-right-radius: 10px;
  border-top-right-radius: 10px;
}

.icon-xiangji {
  position: absolute;
  right: 150px;
  top: 12px;
  font-size: 24px;
  color: rgb(196, 199, 206);
}

.search-right {
  color: #fff;
  font-size: 18px;
  width: 110px;
  height: 45px;
  border: 0;
  background-color: rgb(242, 78, 122);
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
.btn-white{
  background-color:#fff;
  color:#777;
}

/*按钮当鼠标悬浮时的状态：*/
.btn:hover{
     transform: translateY(-3px);
     box-shadow: 0 10px 20px rgba(0,0,0,0.2);
   }

/*当按钮点击时的状态：*/
.btn:active{
     transform: translateY(-1px);
     box-shadow: 0 5px 10px rgba(0,0,0,0.2);
   }

.btn::after{
     content: '';
     display: inline-block;
     height: 100%;
     width: 100%;
     position: absolute;
     top: 0;
     left: 0;
     z-index: -1;
     transition: all .4s ;
   }
.btn-white::after{
  background:#fff;
}
.btn:hover::after{
  transform: scaleX(1.4) scaleY(1.6);
  opacity: 0;
}

.view-enter-active{
  animation-duration: 0.5s;
  animation-name:fadeInUp ;
}

@keyframes moveInBottom{
     0%{
       opacity: 0;
       transform: translateY(100px);
     }
     100%{
       opacity: 1;
       transform: translate(0);
     }
   }
</style>
