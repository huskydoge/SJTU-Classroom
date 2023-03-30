<template>
  <div class="collapse" style="margin-top: 20px;padding-bottom: 20px">
    <div style="border-bottom: #ECEEF5 solid;">
    <h1 style="font-size: 3rem">Lost</h1>
      <el-empty v-if="this.lostList.length === 0"></el-empty>
    <el-collapse v-model="activeName" accordion>
      <el-collapse-item v-for="(item, index) in this.lostList" :name="index" :key="index">
        <template #title>
          <div id="headerInfo">
            <h1 id="lostItem"> {{item.lostitem }}</h1>
            <span id="lostTime" style="text-align: right">{{this.dateFormat(item.date)}}</span>
          </div>
        </template>
        <div id="detailedInfo">
          <el-avatar :src=item.avatarurl></el-avatar>
          <div>
            <h1 id="userName">{{item.username}}</h1>
            <p id="content">
              {{item.context}}
            </p>
        </div>
        </div>
      </el-collapse-item>
    </el-collapse>
    </div>


    <div>
    <h1 style="font-size: 3rem">Found</h1>
      <el-empty v-if="this.foundList.length ===0"></el-empty>
    <el-collapse v-model="activeName" accordion>
      <el-collapse-item v-for="(item, index) in this.foundList" :name="index + this.lostList.length" :key="index">
        <template #title>
          <div id="headerInfo">
            <h1 id="lostItem"> {{item.lostitem }}</h1>
            <span id="lostTime" style="text-align: right">{{this.dateFormat(item.date)}}</span>
          </div>
        </template>
        <div id="detailedInfo">
          <el-avatar :src=item.avatarurl></el-avatar>
          <div>
            <h1 id="userName">{{item.username}}</h1>
            <p id="content">
              {{item.context}}
            </p>
          </div>
        </div>
      </el-collapse-item>
    </el-collapse>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props:{
    classroomSpecified: String,
  },
  data(){
    return {
      foundList: [],
      lostList: [],
      activeName: String,
    }
  },
  methods:{
    // 时间格式化
    dateFormat (str) {
      var date = new Date(str)
      var year = date.getFullYear()
      var month = date.getMonth() + 1 < 10 ? '0' + (date.getMonth() + 1) : date.getMonth() + 1
      var day = date.getDate() < 10 ? '0' + date.getDate() : date.getDate()
      let week = date.getDay() // 星期
      let weekArr = [ '星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六' ]
      // 拼接 时间格式处理
      return year + '年' + month + '月' + day + '日 ' + weekArr[week]
    },
    getFoundItem(){
      console.log(this.classroomSpecified);
      axios.get('http://127.0.0.1/getClassroomFound',{
        params:{
          classroom: this.classroomSpecified,
        }
      }).then(res=>{
        console.log(res.data)
        this.foundList = res.data;
      }).catch(err=>{
        console.log("获取数据失败" + err);
      });
    },
    getLostItem(){
      axios.get('http://127.0.0.1/getClassroomLost',{
        params:{
          classroom: this.classroomSpecified,
        }
      }).then(res=>{
        console.log(res.data);
        this.lostList = res.data;
      }).catch(err=>{
        console.log("获取数据失败" + err);
      });
    },
  },
  created() {
    this.getFoundItem();
    this.getLostItem();
  }
}
</script>

<style scoped>

*{
  margin: 0;
  padding: 0;
}
#detailedInfo {
  margin-top: 20px;
  display: flex;
}

#headerInfo{
  display: flex;
}

#userName{
  margin-left: 20px;
  margin-bottom: 10px;
}

#avatar{
  margin-right: 10px;
}

#content{
  margin-bottom: 20px;
  font-size: 1rem;
}

#lostItem{
  width: 700px;
  padding-right: 10px;
}

#lostTime{
  padding-left:10px ;
  margin-left: 30px;
}
</style>