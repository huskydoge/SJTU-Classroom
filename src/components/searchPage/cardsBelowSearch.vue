<!--TODO 加入一个数据加载时的动画～ -->
<template>
  <div style="position:fixed; left: 50px;top:150px;display: flex;align-items: center">
    <el-avatar @mouseenter="this.animationIn = true" @mouseleave="this.animationIn = false" :class="{'animation':animationIn}" src="https://pic2.zhimg.com/v2-0c5dc901830ee38c87e691774a4239d9_r.jpg?source=1940ef5c">
    </el-avatar>
    <div style="margin-left: 10px;">
<!--左边提示框-->
      <el-popover
          placement="bottom"
          :width="300"
          trigger="hover"
          content="this is content, this is content, this is content"
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
                每张卡片可以翻页，获得该教室的简略信息.
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
                1.点击卡片可以进入对应的教室界面.
              </p>
              <p
                  class="demo-rich-content__mention"
                  style="margin: 0;margin-top: 4px; font-size: 14px; color: var(--el-color-info)"
              >
                2.切换视图可以呈现不同的图表.
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
  <div style="margin-top: 30px;width: 1300px">
    <div style="display: flex;align-items: center;height: 52px">
      <el-button @click="chooseSort" v-if="!toSort && !toSelect">排序</el-button>
      <el-button @click="chooseSelect" v-if="!toSort && !toSelect">筛选</el-button>
      <el-button @click="recover" v-if="toSort || toSelect">返回</el-button>
      <el-switch v-if="toSort"
                 v-model="multiSort"
                 class="ml-2"
                 style="margin-left:10px;--el-switch-on-color: #13ce66; --el-switch-off-color: #ff4949;animation-duration: 0.5s"
                 active-text="多重排序"
                 inactive-text="普通排序"
                 inline-prompt
      />
      <transition name="sortBtn">
        <el-button-group v-if="toSort" size="default" style="margin:10px auto;animation-duration: 0.5s">
          <el-button class="button-below-search" @click="sortBySeats">按座位数排序
            <up theme="outline" size="21" fill="#333" :strokeWidth="1" strokeLinejoin="bevel" strokeLinecap="square" v-if="bySeats"/>
            <down theme="outline" size="21" fill="#333" :strokeWidth="1" strokeLinejoin="bevel" strokeLinecap="square" v-if="!bySeats"/>
          </el-button>
          <el-button class="button-below-search" @click="sortByVacancy">按空位数排序
            <up theme="outline" size="21" fill="#333" :strokeWidth="1" strokeLinejoin="bevel" strokeLinecap="square" v-if="byVacancy"/>
            <down theme="outline" size="21" fill="#333" :strokeWidth="1" strokeLinejoin="bevel" strokeLinecap="square" v-if="!byVacancy"/>
          </el-button>
          <el-button class="button-below-search" @click="sortByPeople">按人数排序
            <up theme="outline" size="21" fill="#333" :strokeWidth="1" strokeLinejoin="bevel" strokeLinecap="square" v-if="byPeople"/>
            <down theme="outline" size="21" fill="#333" :strokeWidth="1" strokeLinejoin="bevel" strokeLinecap="square" v-if="!byPeople"/>
          </el-button>
          <el-button class="button-below-search" @click="sortByCo2">按CO2浓度排序
            <up theme="outline" size="21" fill="#333" :strokeWidth="1" strokeLinejoin="bevel" strokeLinecap="square" v-if="byCo2"/>
            <down theme="outline" size="21" fill="#333" :strokeWidth="1" strokeLinejoin="bevel" strokeLinecap="square" v-if="!byCo2"/>
          </el-button>
          <el-button class="button-below-search" @click="sortByPm25">按PM2.5浓度排序
            <up theme="outline" size="21" fill="#333" :strokeWidth="1" strokeLinejoin="bevel" strokeLinecap="square" v-if="byPm25"/>
            <down theme="outline" size="21" fill="#333" :strokeWidth="1" strokeLinejoin="bevel" strokeLinecap="square" v-if="!byPm25"/>
          </el-button>
          <el-button class="button-below-search" @click="sortByTemperature">按温度排序
            <up theme="outline" size="21" fill="#333" :strokeWidth="1" strokeLinejoin="bevel" strokeLinecap="square" v-if="byTemperature"/>
            <down theme="outline" size="21" fill="#333" :strokeWidth="1" strokeLinejoin="bevel" strokeLinecap="square" v-if="!byTemperature"/>
          </el-button>
          <el-button class="button-below-search" @click="sortByHumidity">按湿度排序
            <up theme="outline" size="21" fill="#333" :strokeWidth="1" strokeLinejoin="bevel" strokeLinecap="square" v-if="byHumidity"/>
            <down theme="outline" size="21" fill="#333" :strokeWidth="1" strokeLinejoin="bevel" strokeLinecap="square" v-if="!byHumidity"/>
          </el-button>

        </el-button-group>
      </transition>
<!--      选择按钮-->
      <div style="display: flex;margin: 0 auto;width:1900px;align-items: center;justify-content: space-evenly" v-if="toSelect">
        <span style="display: flex;align-items: center">
          <span style="padding-left:10px;padding-right:10px">
          座位数大于
          </span>
          <el-select v-model="seats" placeholder="" style="width: 90px;padding-right:10px">
        <el-option
            v-for="item in seatList"
            :key="item.value"
            :label="item.label"
            :value="item.value"
        />
         </el-select>
        </span>
        <span style="display: flex;align-items: center">
          <span style="padding-left:10px;padding-right:10px">
          空位数大于
          </span>
          <el-select v-model="vacancy" placeholder="" style="width: 90px;padding-right:10px">
        <el-option
            v-for="item in vacancyList"
            :key="item.value"
            :label="item.label"
            :value="item.value"
        />
         </el-select>
        </span>
        <span style="display: flex;align-items: center">
          <span style="padding-left:10px;padding-right:10px">
          人数小于
          </span>
          <el-select v-model="people" placeholder="" style="width: 90px;padding-right:10px">
        <el-option
            v-for="item in peopleList"
            :key="item.value"
            :label="item.label"
            :value="item.value"
        />
         </el-select>
        </span>
        <span style="display: flex;align-items: center">
          <span style="padding-left:10px;padding-right:10px">
          CO2浓度
          </span>
          <el-select v-model="co2" placeholder="" style="width: 90px;padding-right:10px">
        <el-option
            v-for="item in co2List"
            :key="item.value"
            :label="item.label"
            :value="item.value"
        />
         </el-select>
        </span>
        <span style="display: flex;align-items: center">
          <span style="padding-left:10px;padding-right:10px">
          PM2.5浓度
          </span>
          <el-select v-model="pm25" placeholder="" style="width: 90px;padding-right:10px">
        <el-option
            v-for="item in pm25List"
            :key="item.value"
            :label="item.label"
            :value="item.value"
        />
         </el-select>
        </span>
        <span style="display: flex;align-items: center">
          <span style="padding-left:10px;padding-right:10px">
          温度
          </span>
          <el-select v-model="temperature" placeholder="" style="width: 90px;padding-right:10px">
        <el-option
            v-for="item in temperatureList"
            :key="item.value"
            :label="item.label"
            :value="item.value"
        />
         </el-select>
        </span>
        <el-tooltip content="勾选则显示对应值缺失的教室，'任意'选项下设置为显示">
        <el-checkbox style="padding-left:5px;" v-model="displayNone">NONE</el-checkbox>
        </el-tooltip>
      </div>
      <el-button  @click="reset">reset</el-button>
    </div>

    <el-empty style="padding-top: 200px" v-if="isEmpty"></el-empty>

    <transition-group name="cardAnimation" v-if="!isEmpty">
      <div  v-if="animate" style="display: grid;grid-template-columns: 1fr 1fr 1fr;gap:30px; margin-bottom: 2rem;height: 37vw" v-loading="this.loadingAllData">
        <el-card  :body-style="{ padding: '0px'}"
                  v-for="(item,index) in this.ClassRoomDataForCards.slice((currentPage - 1) * pageSize, currentPage * pageSize)" @click="this.showClassInfo(item.name)"
                  :key=index
                  :class="{'card-item':true,'card-container':true}">
          <div>
            <div class="back">
              <div style="padding-top:30px">
                <div class="back-content">
                  <span style="margin-right: 10px">座位：{{ this.fill(item.seats) }}</span>
                  <span>空位：{{ this.fill(item.vacancy) }}</span>
                  <span>人数：{{ this.fill(item.people) }}</span>
                </div>
                <div class="back-content">
                  <span style="margin-right: 10px">室内温度：{{ item.temperature}}</span>
                  <span style="margin-right: 10px">空气湿度：{{ item.humidity}}</span>
                  <span style="margin-right: 10px">PM25浓度：{{ item.pm25 }}</span>
                </div>
                <span class="back-content" style="margin-right: 10px">CO2浓度：{{(item.co2)}}</span>
              </div>
            </div>
            <div class="cover">
              <img style="width: 100%" src="https://ts1.cn.mm.bing.net/th/id/R-C.87a6dd9de4d83ab4d17fbcebeb93d934?rik=XHOq1qyGAIWY0A&riu=http%3a%2f%2flife.sjtu.edu.cn%2fteacher%2fAssets%2fimages%2fdefault%2f3.jpg&ehk=5nJAQ5%2fNi%2bTnd24JyF82QQH9smX%2f3PRd9Qi22uwqeA0%3d&risl=&pid=ImgRaw&r=0">
              <div>
                <h1 style="margin-left: 10px;margin-top: 10px">{{ item.name }}</h1>
              </div>
            </div>
          </div>
        </el-card>
      </div>
    </transition-group>
    <el-pagination
        v-if="!isEmpty"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-sizes="[6, 12, 18, 24]"
        :page-size="pageSize"
        layout="prev, pager, next, total"
        :total="ClassRoomDataForCards.length">
    </el-pagination>
  </div>
</template>


<script>
// import InfiniteScrollList from "@/components/searchPage/infiniteScrollList";
import axios from "axios";
import {Up} from '@icon-park/vue-next'
import {Down} from '@icon-park/vue-next'
import {Help} from '@icon-park/vue-next'

export default {
  props:{
    dataFromSearch: Array,
    choices: Object,
  },
  data(){
    return{
      displayNone: true,
      isEmpty: false,
      animate: true,
      animationIn: true,
      animationOut: false,
      peopleList:[
        {
          label:'任意',
          value: -1,
        },
        {
          label:'10',
          value: 10,
        },
        {
          label:'30',
          value: 30,
        },
        {
          label:'60',
          value: 60,
        },
        {
          label:'120',
          value: 120,
        }
      ],
      vacancyList:[
        {
          label:'任意',
          value: -1,
        },
        {
          label:'50',
          value: 50,
        },
        {
          label:'100',
          value: 100,
        },
        {
          label:'200',
          value: 200,
        },
        {
          label:'300',
          value: 300,
        }
      ],
      seatList:[
        {
          label:'任意',
          value: -1,
        },
        {
          label:'50',
          value: 50,
        },
        {
          label:'100',
          value: 100,
        },
        {
          label:'200',
          value: 200,
        },
        {
          label:'300',
          value: 300,
        }
      ],
      // https://www.sohu.com/a/288858682_472588 co2标准
      co2List:[
        {
          label:'任意',
          value: -1,
        },
        {
          label:'低',
          value: 500,
        },
        {
          label:'中',
          value: 1000,
        },
        {
          label:'高',
          value: 5000,
        },
        {
          label:'过高',
          value: 5001,
        },
      ],
      pm25List:[
        {
          label:'任意',
          value: -1,
        },
        {
          label:'低',
          value: 15,
        },
        {
          label:'中',
          value: 35,
        },
        {
          label:'高',
          value: 75,
        },
        {
          label:'过高',
          value: 100,
        },
      ],
      temperatureList:[
        {
          label:'任意',
          value: -1,
        },
        {
          label:'低',
          value: 20,
        },
        {
          label:'中',
          value: 25,
        },
        {
          label:'高',
          value: 35,
        },
      ],

      seats: this.choices.seats,
      people: this.choices.people,
      vacancy: this.choices.vacancy,
      co2: this.choices.co2,
      pm25: this.choices.pm25,
      temperature: this.choices.temperature,

      multiSort: this.choices.multiSort,
      toSelect: this.choices.toSelect,
      toSort: this.choices.toSort,

      backup: [],


      bySeats: false,
      byVacancy: false,
      byPeople: false,
      byCo2: false,
      byPm25: false,
      byTemperature: false,
      byHumidity: false,


      loadingAllData: true,
      currentPage: 1, //初始页
      pageSize: 6, //    每页的数据
      classData:[],
      show:true,
      ClassRoomDataForCards: [] , // 教室信息 !
    }
  },
  components:{
    Up,
    Down,
    Help,
  },
  name: "cardsBelowSearch",
  // components: {InfiniteScrollList}
  created(){
    this.fetchData();
  },
  methods:{
    reset(){
      if(this.toSort){
        this.bySeats = false;
        this.byVacancy= false;
        this.byPeople = false;
        this.byCo2 = false;
        this.byPm25 = false;
        this.byTemperature = false;
        this.byHumidity = false;
      } else {
        this.seats =  '任意';
        this.people = '任意';
        this.vacancy = '任意';
        this.co2 = '任意';
        this.pm25 = '任意';
        this.temperature = '任意';
      }
    },
    handlePm25(str){
      if(str === 'None'){return 0}
      let pos = str.lastIndexOf("μg");
      let num = str.slice(0,pos);
      return num;
    },
    handleCo2(str){
      if(str === 'None'){return 0}
      let pos = str.lastIndexOf("PPM");
      let num = str.slice(0,pos);
      return num;
    },
    handleTemperature(str){
      if(str === 'None'){return 0}
      let pos = str.lastIndexOf("℃");
      let num = str.slice(0,pos);
      return num;
    },
    clearSort(str){
      if(str === 'seat') {
        this.byVacancy = this.byPeople = this.byHumidity = this.byTemperature = this.byPm25 = this.byCo2 = false;
      } else if(str === 'vacancy'){
        this.bySeats = this.byPeople = this.byHumidity = this.byTemperature = this.byPm25 = this.byCo2 = false;
      } else if(str === 'people'){
        this.bySeats = this.byVacancy = this.byHumidity = this.byTemperature = this.byPm25 = this.byCo2 = false;
      } else if(str === 'humidity'){
        this.bySeats = this.byVacancy = this.byPeople = this.byTemperature = this.byPm25 = this.byCo2 = false;
      } else if(str === 'temperature'){
        this.bySeats = this.byVacancy = this.byPeople = this.byHumidity = this.byPm25 = this.byCo2 = false;
      } else if(str === 'pm25'){
        this.bySeats = this.byVacancy = this.byPeople = this.byHumidity = this.byTemperature = this.byCo2 = false;
      } else {
        this.bySeats = this.byVacancy = this.byPeople = this.byHumidity = this.byTemperature = this.byPm25 = false;
      }
    },
    recover(){
      this.toSelect = this.toSort = false;
      this.sortFadeIn = true;
      this.selectFadeIn = true;
    },
    chooseSort(){
      this.toSort = true;
    },
    chooseSelect(){
      this.toSelect = true;
    },
    // 这里可以改成随数组长度而变化的循环
    selectSeats(){
      let tmp = [];
      let seats = this.seats;
      let classData = this.ClassRoomDataForCards;
      if(seats === -1){
        return
      }
      else if(seats === this.seatList[1].value){
        for(let i = 0; i < classData.length; ++ i){
          if(classData[i].seats >= this.seatList[1].value){
            tmp.push(classData[i]);
          }
        }
        classData = tmp;
      } else if(seats === this.seatList[2].value){
        for(let i = 0; i < classData.length; ++ i){
          if(classData[i].seats >= this.seatList[2].value){
            tmp.push(classData[i]);
          }
        }
        classData = tmp;
      } else if(seats === this.seatList[3].value){
        for(let i = 0; i < classData.length; ++ i){
          if(classData[i].seats >= this.seatList[3].value){
            tmp.push(classData[i]);
          }
        }
        classData = tmp;
      } else if(seats === this.seatList[4].value){
        for(let i = 0; i < classData.length; ++ i){
          if(classData[i].seats >= this.seatList[4].value){
            tmp.push(classData[i]);
          }
        }
        classData = tmp;
      }
      this.ClassRoomDataForCards = classData;
    },
    selectVacancy(){
      let tmp = [];
      let vacancy = this.vacancy;
      let classData = this.ClassRoomDataForCards;
      if(vacancy === -1){
        return
      } else if(vacancy === this.seatList[1].value){
        for(let i = 0; i < classData.length; ++ i){
          if(classData[i].vacancy >= this.seatList[1].value){
            tmp.push(classData[i]);
          }
        }
        classData = tmp;
      } else if(vacancy === this.seatList[2].value){
        for(let i = 0; i < classData.length; ++ i){
          if(classData[i].vacancy >= this.seatList[2].value){
            tmp.push(classData[i]);
          }
        }
        classData = tmp;
      } else if(vacancy === this.seatList[3].value){
        for(let i = 0; i < classData.length; ++ i){
          if(classData[i].vacancy >= this.seatList[3].value){
            tmp.push(classData[i]);
          }
        }
        classData = tmp;
      } else if(vacancy === this.seatList[4].value){
        for(let i = 0; i < classData.length; ++ i){
          if(classData[i].vacancy >= this.seatList[4].value){
            tmp.push(classData[i]);
          }
        }
        classData = tmp;
      }
      this.ClassRoomDataForCards = classData;
    },
    selectPeople(){
      let tmp = [];
      let people = this.people;
      let classData = this.ClassRoomDataForCards;
      if(people === -1){
        return
      } else if(people === this.peopleList[1].value){
        for(let i = 0; i < classData.length; ++ i){
          if(classData[i].people <= this.peopleList[1].value && !(!this.displayNone && (this.judgeValid(classData[i].people)))){
            tmp.push(classData[i]);
          }
        }
        classData = tmp;
      } else if(people === this.peopleList[2].value){
        for(let i = 0; i < classData.length; ++ i){
          if(classData[i].people <= this.peopleList[2].value){
            tmp.push(classData[i]);
          }
        }
        classData = tmp;
      } else if(people === this.peopleList[3].value){
        for(let i = 0; i < classData.length; ++ i){
          if(classData[i].people <= this.peopleList[3].value){
            tmp.push(classData[i]);
          }
        }
        classData = tmp;
      } else if(people === this.peopleList[4].value){
        for(let i = 0; i < classData.length; ++ i){
          if(classData[i].people <= this.peopleList[4].value){
            tmp.push(classData[i]);
          }
        }
        classData = tmp;
      }
      this.ClassRoomDataForCards = classData;
    },
    selectCo2(){
      let handleCo2 = this.handleCo2;
      let tmp = [];
      let co2 = this.co2;
      let classData = this.ClassRoomDataForCards;
      if(co2 === -1){
        return
      } else if(co2 === this.co2List[1].value){
        for(let i = 0; i < classData.length; ++ i){
          if((handleCo2(classData[i].co2) >= this.co2List[0].value) && (handleCo2(classData[i].co2) < this.co2List[1].value)
          && !(!this.displayNone && (handleCo2(classData[i].co2) === 0))){
            tmp.push(classData[i]);
          }
        }
        classData = tmp;
      } else if(co2 === this.co2List[2].value){
        for(let i = 0; i < classData.length; ++ i){
          if((handleCo2(classData[i].co2) >= this.co2List[1].value) && (handleCo2(classData[i].co2) < this.co2List[2].value)){
            tmp.push(classData[i]);
          }
        }
        classData = tmp;
      } else if(co2 === this.co2List[3].value){
        for(let i = 0; i < classData.length; ++ i){
          if((handleCo2(classData[i].co2) >= this.co2List[2].value) && (handleCo2(classData[i].co2) < this.co2List[3].value)){
            tmp.push(classData[i]);
          }
        }
        classData = tmp;
      } else if(co2 === this.co2List[4].value) {
        for(let i = 0; i < classData.length; ++ i){
          if((handleCo2(classData[i].co2) >= this.co2List[4].value)){
            tmp.push(classData[i]);
          }
        }
        classData = tmp;
      }
      this.ClassRoomDataForCards = classData;
    },
    selectPm25(){
      let handlePm25 = this.handlePm25;
      let tmp = [];
      let pm25 = this.pm25;
      let classData = this.ClassRoomDataForCards;
      if(pm25 === -1){
        return
      } else if(pm25 === this.pm25List[1].value){
        for(let i = 0; i < classData.length; ++ i){
          if((handlePm25(classData[i].pm25) >= this.pm25List[0].value) && (handlePm25(classData[i].pm25) < this.pm25List[1].value)
          && !(!this.displayNone && (handlePm25(classData[i].pm25) === 0))){
            tmp.push(classData[i]);
          }
        }
        classData = tmp;
      } else if(pm25 === this.pm25List[2].value){
        for(let i = 0; i < classData.length; ++ i){
          if((handlePm25(classData[i].pm25) >= this.pm25List[1].value) && (handlePm25(classData[i].pm25) < this.pm25List[2].value)){
            tmp.push(classData[i]);
          }
        }
        classData = tmp;
      } else if(pm25 === this.pm25List[3].value){
        for(let i = 0; i < classData.length; ++ i){
          if((handlePm25(classData[i].pm25) >= this.pm25List[2].value) && (handlePm25(classData[i].pm25) < this.pm25List[3].value)){
            tmp.push(classData[i]);
          }
        }
        classData = tmp;
      }
      this.ClassRoomDataForCards = classData;
    },
    selectTemperature(){
      let handleT = this.handleTemperature;
      let tmp = [];
      let temperature = this.temperature;
      let classData = this.ClassRoomDataForCards;
      if(temperature === -1){
        return
      } else if(temperature === this.temperatureList[1].value){
        for(let i = 0; i < classData.length; ++ i){
          if(handleT(classData[i].temperature) >= this.temperatureList[0].value && handleT(classData[i].temperature) < this.temperatureList[1].value
              && !(!this.displayNone && (handleT(classData[i].temperature) === 0))){
            tmp.push(classData[i]);
          }
        }
        classData = tmp;
      } else if(temperature === this.temperatureList[2].value){
        for(let i = 0; i < classData.length; ++ i){
          if(handleT(classData[i].temperature) >= this.temperatureList[1].value && handleT(classData[i].temperature) < this.temperatureList[2].value){
            tmp.push(classData[i]);
          }
        }
        classData = tmp;
      } else if(temperature === this.temperatureList[3].value){
        for(let i = 0; i < classData.length; ++ i){
          if(handleT(classData[i].temperature) >= this.temperatureList[2].value && handleT(classData[i].temperature) < this.temperatureList[3].value){
            tmp.push(classData[i]);
          }
        }
        classData = tmp;
      } else {
        for(let i = 0; i < classData.length; ++ i){
          if(handleT(classData[i].temperature) >= this.temperatureList[3].value){
            tmp.push(classData[i]);
          }
        }
      }
      this.ClassRoomDataForCards = classData;
    },
    executeSelect(){
      this.ClassRoomDataForCards = this.backup;
      this.selectSeats();
      this.selectVacancy();
      this.selectPeople();
      this.selectCo2();
      this.selectPm25();
      this.selectTemperature();
    },
    handleSizeChange (size) {
      console.log(size,'size');
      this.pagesize = size;
      console.log(this.pagesize); //每页下拉显示数据
    },
    animateTrue(){
      this.animate = true;
    },
    handleCurrentChange (currentPage) {
      this.animate = false;
      setTimeout(this.animateTrue,200);
      console.log(currentPage,'currentPage');
      this.currentPage = currentPage;
      console.log(this.currentPage); //点击第几页
    },
    // 初始数据为无搜索条件的返回结果
    fetchData(){ // 要先在终端运行 node app.js
      this.backup = [];
      this.loadingAllData = true;
      axios.get('http://127.0.0.1/getAllClassroom').then(res=>{
        console.log(res.data[1])
        let cnt = 1; // index
        for(const i in res.data){
          let obj = {
            depth: 1,
            id: 'classroom.' + res.data[i]['教室名'],
            index: cnt,
            vacancy: this.handleNan(res.data[i]['座位数'] - res.data[i]['实到人数']),
            name: res.data[i]['教室名'],
            seats: this.handleNan(res.data[i]['座位数'] - '0'),
            people: this.handleNan(res.data[i]['实到人数']),
            co2: res.data[i]['CO2浓度'],
            pm25:res.data[i]['PM25浓度'],
            temperature:res.data[i]['温度'],
            humidity: res.data[i]['空气湿度'],
          };
          this.backup.push(obj);
          ++ cnt;
        }
        // 按照空余位置排序
        this.backup.sort(function(a,b){
          return b.seats - a.seats;
        });
        this.ClassRoomDataForCards= this.backup;
        this.executeSelect();
        this.loadingAllData = false;
      }).catch(err=>{
        console.log("获取数据失败" + err);
      });
    },
    handleNan (number){
      if(isNaN(number)){
        return 0;
      } else {
        return number;
      }
    },
    // 点击条目后，像父组件返回教室名
    showClassInfo(className){
      let obj = {
        seats: this.seats,
        people: this.people,
        vacancy: this.vacancy,
        co2: this.co2,
        pm25: this.pm25,
        temperature: this.temperature,
        multiSort: this.multiSort,
        toSelect: this.toSelect,
        toSort: this.toSort,
        data: this.ClassRoomDataForCards
      }
      this.$emit("showClassInfo",className, obj);
    },
    sortBySeats(){
      if(!this.multiSort) {
        this.clearSort('seat');
        this.ClassRoomDataForCards = this.backup;
      }
      if(this.bySeats) {
        this.ClassRoomDataForCards.sort(function (a, b) {
          return b.seats - a.seats;
        });
      } else {
        this.ClassRoomDataForCards.sort(function (a, b) {
          return a.seats - b.seats;
        });
      }
      this.bySeats = !this.bySeats;
      console.log(this.ClassRoomDataForCards)
    },
    sortByVacancy(){
      if(!this.multiSort) {
        this.clearSort('vacancy');
        this.ClassRoomDataForCards = this.backup;
      }
      if(this.byVacancy) {
        this.ClassRoomDataForCards.sort(function (a, b) {
          return b.vacancy - a.vacancy;
        });
      } else {
        this.ClassRoomDataForCards.sort(function (a, b) {
          return a.vacancy - b.vacancy;
        });
      }
      this.byVacancy = !this.byVacancy;
      console.log(this.ClassRoomDataForCards)
    },
    sortByPeople(){
      if(!this.multiSort) {
        this.clearSort('people');
        this.ClassRoomDataForCards = this.backup;
      }
      if(this.byPeople) {
        this.ClassRoomDataForCards.sort(function (a, b) {
          return b.people - a.people;
        });
      } else {
        this.ClassRoomDataForCards.sort(function (a, b) {
          return a.people - b.people;
        });
      }
      this.byPeople = !this.byPeople;
    },
    sortByCo2(){
      let handleCo2 = this.handleCo2;
      if(!this.multiSort) {
        this.clearSort('');
        this.ClassRoomDataForCards = this.backup;
      }
      if(this.byCo2) {
        this.ClassRoomDataForCards.sort(function (a, b) {
          return handleCo2(b.co2) - handleCo2(a.co2);
        });
      } else {
        this.ClassRoomDataForCards.sort(function (a, b) {
          return  handleCo2(a.co2) - handleCo2(b.co2);
        });
      }
      this.byCo2 = !this.byCo2;
    },
    sortByPm25(){
      let handlePm25 = this.handlePm25;
      if(!this.multiSort) {
        this.clearSort('pm25');
        this.ClassRoomDataForCards = this.backup;
      }
      if(this.byPm25) {
        this.ClassRoomDataForCards.sort(function (a, b) {
          return handlePm25(b.pm25) - handlePm25(a.pm25);
        });
      } else {
        this.ClassRoomDataForCards.sort(function (a, b) {
          return handlePm25(a.pm25) - handlePm25(b.pm25);
        });
      }
      this.byPm25 = !this.byPm25;
    },
    sortByTemperature(){
      let handleTemperature = this.handleTemperature;
      if(!this.multiSort) {
        this.clearSort('temperature');
        this.ClassRoomDataForCards = this.backup;
      }
      if(this.byTemperature) {
        this.ClassRoomDataForCards.sort(function (a, b) {
          return handleTemperature(b.temperature) - handleTemperature(a.temperature);
        });
      } else {
        this.ClassRoomDataForCards.sort(function (a, b) {
          return handleTemperature(a.temperature) - handleTemperature(b.temperature);
        });
      }
      this.byTemperature = !this.byTemperature;
    },
    sortByHumidity(){
      function handleHumidity(str){
        if(str === 'None'){return 0}
        let pos = str.lastIndexOf("%");
        let num = str.slice(0,pos);
        return num;
      }
      if(!this.multiSort) {
        this.clearSort('humidity');
        this.ClassRoomDataForCards = this.backup;
      }
      if(this.byHumidity) {
        this.ClassRoomDataForCards.sort(function (a, b) {
          return handleHumidity(b.humidity) - handleHumidity(a.humidity);
        });
      } else {
        this.ClassRoomDataForCards.sort(function (a, b) {
          return handleHumidity(a.humidity) - handleHumidity(b.humidity);
        });
      }
      this.byHumidity = !this.byHumidity;
    },
    fill(str){
      if(str == '' || str == 'None' || str == undefined || str == "NONE" || isNaN(str)){
        return '暂无信息';
      } else {
        return str;
      }
    },
    judgeValid(str){
      if(str == '' || str == 'None' || str == undefined || str == "NONE" || isNaN(str)){
        return false;
      } else {
        return true;
      }
    }
  },
  watch:{
    seats(){
      this.executeSelect();
    },
    vacancy(){
      this.executeSelect();
    },
    people(){
      this.executeSelect();
    },
    co2(){
      this.executeSelect();
    },
    pm25(){
      this.executeSelect();
    },
    temperature(){
      this.executeSelect();
    },
    displayNone(){
      this.executeSelect();
    },
    dataFromSearch(){
      this.ClassRoomDataForCards = [];
      this.ClassRoomDataForCards = this.dataFromSearch;
    },
    ClassRoomDataForCards(){
      if(this.ClassRoomDataForCards.length === 0){
        this.isEmpty = true;
      } else {
        this.isEmpty = false;
      }
    },
    multiSort(){
      this.ClassRoomDataForCards = this.backup;
    }
  }
}

</script>

<style>

.cardAnimation-enter-active{
  animation-duration: .7s;
  animation-name: fadeIn;
}

.cardAnimation-leave-active{
  animation-duration: .7s;
  animation-name: fadeOut;
}

.scrollbar-demo-item{
  width: 600px;
}

.el-card__header {
  padding: 0 !important;
}

.animation:hover{
  animation-duration: 1s;
  animation-name: heartBeat;
}

.card-item {
  width: 400px;
  height: 300px;
  border-radius: 10px;
  background: var(--el-color-primary-light-9);
  color: var(--el-color-primary);
  position: relative;
}

.sortBtn-enter-active{
  animation-duration: 1s;
  animation-name: fadeInRight;
}

.sortBtn-leave-active{
  animation-duration: 1s;
  animation-name: fadeOutRight;
}

.cover, .back {
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  transition: transform .25s ease-in-out;
  border-radius: .4rem;
  position: absolute;
}

.cover {
  transform: rotatey(0deg);
}

.sortBtn:hover{
  animation-duration: 1s;
  animation-name: bounce;
}

.chooseBtn:hover{
  animation-duration: 1s;
  animation-name: bounce;
}

.card-container:hover .cover {
  transform: rotatey(180deg);
}

.back {
  transform: rotatey(-180deg);
}

.back-content{
  display: grid;
  grid-template-columns: 1fr 1fr;
  padding: 15px 30px;
  width: 100%;
  font-size: 1rem;
  gap:10px;
}

.card-container:hover .back {
  transform: rotatey(0deg)
}



.button-below-search{
  padding: 10px 2px 10px 15px;
}

.el-pagination{
  margin-top: 1rem;
  margin-bottom: 1rem;
  justify-content: center;
}
</style>