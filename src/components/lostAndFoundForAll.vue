<template>
  <div v-if="!showClassInfo" style="margin:0 auto;padding-top: 8px;display: block;position: relative">
    <div style="position:fixed; left: 20px;top:90px;display: flex;align-items: center">
      <el-avatar src="https://tse3-mm.cn.bing.net/th/id/OIP-C.-SW2Zx4d18IXG3GqeoaBYgHaHa?w=206&h=207&c=7&r=0&o=5&dpr=2&pid=1.7">
      </el-avatar>
      <div style="margin-left: 10px;">
      <el-button @click="handleSubmitClick">
           <span style="padding: 10px">
             想要提交信息？
        </span>
      </el-button>
        <el-dialog :append-to-body='true' v-model="tableVisible" title="填写信息" width="40%" center>
          <el-form :model="form">
            <div style="display: flex;margin-bottom: 2rem">
            <el-form-item label="物品名称：" :label-width="formLabelWidth">
              <input v-model="form.item" style="padding-left: 10px">
            </el-form-item>
            <el-form-item label="教室名:" :label-width="formLabelWidth">
              <el-tooltip content="格式: 东上院101,东中院请写清楼栋: 东中院4-404">
              <input placeholder="注意格式哦～" v-model="form.classroom" autocomplete="off" style="padding-left: 10px" />
              </el-tooltip>
            </el-form-item>
            </div>
            <el-form-item label="说明:" :label-width="formLabelWidth">
              <textarea placeholder="别忘了留下联系方式" style="width: 80%;padding-left: 10px" v-model="form.context" autocomplete="off" type="textarea" />
            </el-form-item>
            <el-form-item label="信息类型:" :label-width="formLabelWidth" style="margin-top: 1rem">
              <el-radio-group v-model="form.type">
                <el-radio label="Lost" style="margin-right: 20px" />
                <el-radio label="Found" />
              </el-radio-group>
            </el-form-item>
          </el-form>
          <template #footer>
      <span class="dialog-footer">
        <el-button @click="tableVisible= false" style="padding: 20px">
          取消
        </el-button>
        <el-button style="padding: 20px" type="primary" @click="this.submitItemInfo">
          提交
        </el-button>
      </span>
          </template>
        </el-dialog>
      </div>
    </div>
  <h1 style="text-align: center;font-size: 2.5rem;margin-bottom: 1rem">
    Lost And Found
  </h1>
    <div style="width: 500px;margin: 0 auto 20px; display: flex; justify-items: center;justify-content: center" >
    <input
        v-model="inputContext"
        placeholder="Type something"
        @keyup.enter="searchEnter"
        style="width: 1000px;padding-left: 10px;margin-right: 10px"
    />
      <el-button @click="changeOrder">
        <span style="padding: 10px">
        {{ buttonString }}
        </span>
      </el-button>
      <el-button @click="changeContext">
        <span style="padding: 10px;width: 100px">
               {{ contextString }}
        </span>
      </el-button>
    </div>
<!--    vh实现底部栏目居中-->
    <transition-group name="cardAnimation">
    <div v-if="animate" style="display: grid;grid-template-columns: 1fr 1fr 1fr;gap:30px;height: 37vw">
        <el-card v-for="(item, index) in this.infoCards.slice((currentPage - 1) * pageSize, currentPage * pageSize)" :key="index" class="box-card">
          <template #header >
            <div style="display: flex;align-items: center">
              <div>
            <el-avatar size="large" :src="item.avatarurl" style="margin-right: 2.5rem">
            </el-avatar>
                <p style="text-align: center;margin-right:2.5rem;font-size: 1px">{{ item.username }}</p>
              </div>
              <h1>{{ item.lostitem }}</h1>
            </div>
          </template>
          <div class="text item">
            <p>{{ item.context }}</p>
          </div>
          <div style="position: relative">
          <h3 class="className" @click="gotoClass(item.classroomname)"  style="text-align: right;text-align: end;cursor: pointer">{{ item.classroomname }}</h3>
          <p style="text-align: right">{{ this.dateFormat(item.date) }}</p>
            <el-tag style="padding: 5px;position: absolute;bottom: -30px;right: -5px">{{this.lostOrFound? 'lost': 'found'}}</el-tag>
          </div>
        </el-card>
    </div>
    </transition-group>

    <el-pagination
        style="width:55%;position: fixed;bottom:0;text-align:center;"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-sizes="[6, 12, 18, 24]"
        :page-size="pageSize"
        layout="prev, pager, next, total"
        :total="infoCards.length">
    </el-pagination>
  </div>
  <class-info-displayer v-if="showClassInfo" :classroom-name="this.selectedClassName" @return="this.returnLostAndFound"></class-info-displayer>
</template>

<script>
import axios from "axios";
import classInfoDisplayer from "@/components/searchPage/classInfoDisplayer";
export default {
  name: "lostAndFoundForAll",
  components:{
    classInfoDisplayer,
  },
  data(){
    return{
      animate: true,
      allClassName: [],
      form: {
        username: '',
        avatarurl: '',
        classroom: '',
        item: '',
        date: this.getDate(),
        type: 'Lost',
        context: '',
      },
      showClassInfo: false,
      selectedClassName: "东上院101", // 记录选中的教室名
      formLabelWidth: "140px",
      tableVisible: false,
      buttonString: '时间升序',
      contextString: 'goto Found',
      currentPage: 1, //初始页
      pageSize: 6, //    每页的数据
      infoCards: [],
      inputContext: "",
      lostOrFound: true, // true for lost, false for found
    }
  },
  mounted() {
    this.getAllName();
  },
  methods:{
    animateTrue(){
      this.animate = true;
    },
    returnLostAndFound(){
      this.showClassInfo = false;
    },
    gotoClass(name){
      this.selectedClassName = name;
      this.showClassInfo = true;
    },
    changeOrder(){
      if(this.buttonString == '时间升序'){
        this.buttonString = '时间降序';
        this.infoCards.sort(this.sortByTimeInverted);
      } else {
        this.buttonString = '时间升序';
        this.infoCards.sort(this.sortByTime);
      }
    },
    changeContext(){
      this.inputContext = '';
      if(this.lostOrFound){
        this.lostOrFound = false;
        this.contextString = 'goto Lost';
        this.getAllFound();
      } else {
        this.lostOrFound = true;
        this.contextString = 'goto Found';
        this.getAllLost();
      }
    },
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
    // 初始页currentPage、初始每页数据数pagesize和数据data
    getDate(){
      // 获取当前日期
      var date = new Date();
      var nowMonth = date.getMonth() + 1;
      var strDate = date.getDate();
      var seperator = "-";
      if (nowMonth >= 1 && nowMonth <= 9) {
        nowMonth = "0" + nowMonth;
      }
      if (strDate >= 0 && strDate <= 9) {
        strDate = "0" + strDate;
      }
      var nowDate = date.getFullYear() + seperator + nowMonth + seperator + strDate;
      return nowDate;
    },
    handleSizeChange (size) {
      console.log(size,'size');
      this.pagesize = size;
      console.log(this.pagesize); //每页下拉显示数据
    },
    handleCurrentChange (currentPage) {
      this.animate = false;
      setTimeout(this.animateTrue,200);
      console.log(currentPage,'currentPage');
      this.currentPage = currentPage;
      console.log(this.currentPage); //点击第几页
    },
    getAllLost(){
      axios.get('http://127.0.0.1/getAllLost').then(res=>{
        // console.log(res.data)
        console.log(res);
        this.infoCards = res.data;
        this.infoCards.sort(this.sortByTime);
      }).catch(err=>{
        console.log("获取数据失败" + err);
      });
    },
    getAllName(){
      axios.get('http://127.0.0.1/getAllClassroomName').then(res=>{
        // console.log(res.data)
        for(let i in res.data){
          this.allClassName.push(res.data[i]['教室名'])
        }
        console.log(this.allClassName)
      }).catch(err=>{
        console.log("获取数据失败" + err);
      });
    },
    searchLostItem(){
      // noinspection SpellCheckingInspection
      axios.get('http://127.0.0.1:8000/getLostItem',{
        params:{
          context: this.inputContext,
        }
      }).then(res=>{
        // console.log(res.data)
        console.log(res);
        this.infoCards = [];
        for(let i = 0; i < res.data.length; ++ i){
          this.infoCards.push(res.data[i]['_source']);
        }
        this.infoCards.sort(this.sortByTime);
        console.log(this.infoCards)
      }).catch(err=>{
        console.log("获取数据失败" + err);
      });
    },
    getAllFound(){
      axios.get('http://127.0.0.1/getAllFound').then(res=>{
        // console.log(res.data)
        console.log(res);
        this.infoCards = res.data;
        this.infoCards.sort(this.sortByTime);
      }).catch(err=>{
        console.log("获取数据失败" + err);
      });
    },
    searchFoundItem(){
      // noinspection SpellCheckingInspection
      axios.get('http://127.0.0.1:8000/getFoundItem',{
        params:{
          context: this.inputContext,
        }
      }).then(res=>{
        // console.log(res.data)
        console.log(res);
        this.infoCards = [];
        for(let i = 0; i < res.data.length; ++ i){
          this.infoCards.push(res.data[i]['_source']);
        }
        this.infoCards.sort(this.sortByTime);
        // console.log(this.infoCards)
      }).catch(err=>{
        console.log("获取数据失败" + err);
      });
    },
    handleSubmitClick(){
      if(this.$user.userName === ''){
        this.$message.warning("您还未登陆！");
        return;
      }
      this.tableVisible = !this.tableVisible;
    },
    submitItemInfo(){
      if(this.form.item === '' || this.form.context === '' || this.form.classroom === ''){
        this.tableVisible = false;
        this.$message.warning("三个内容均为必填哦！");
        return;
      }
      // console.log(this.allClassName)
      if(!(this.allClassName.includes(this.form.classroom))){
        this.tableVisible = false;
        this.$message.warning("您输入的教室不存在哦～");
        return;
      }
      this.tableVisible = false;
      // console.log(this.form);
      // noinspection SpellCheckingInspection
      axios.get('http://127.0.0.1/submitItemInfo',{
        params:{
          type: this.form.type,
          classroomname: this.form.classroom,
          lostitem: this.form.item,
          context: this.form.context,
          username: this.$user.userName,
          avatarurl: this.$user.avatarUrl,
          date: this.form.date,
        }
      }).then(res=>{
        // console.log(res.data)
        console.log(res);
        if(this.form.type === 'Found'){
          this.getAllFound();
          this.lostOrFound = false;
          this.contextString = 'goto Lost';
        } else {
          this.getAllLost();
          this.lostOrFound = true;
          this.contextString = 'goto Found';
        }
        this.form = {
          username: '',
          avatarurl: '',
          classroom: '',
          item: '',
          date: this.getDate(),
          type: 'Lost',
          context: '',
        };
        // console.log(this.infoCards)
      }).catch(err=>{
        console.log("获取数据失败" + err);
      });
    },
    sortByTime(a,b){
      return Date.parse (a.date) - Date.parse (b.date); // 时间正序
    },
    sortByTimeInverted(a,b){
      return Date.parse (b.date) - Date.parse (a.date);
    },
    searchEnter(e) {
      var keyCode = window.event ? e.keyCode : e.which;
      if (keyCode == 13) {
        if(!(this.inputContext == '')) {
          if(this.lostOrFound) {
            this.searchLostItem(); //搜索按钮的回调
          } else {
            this.searchFoundItem();
          }
        } else  {
          if(this.lostOrFound) {
            this.getAllLost();
          } else {
            this.getAllFound();
          }
        }
      }
    },
  },
  created() {
    this.getAllLost();
  },
  watch:{
    inputContext(){
      if(!(this.inputContext == '')) {
        if(this.lostOrFound) {
          this.searchLostItem(); //搜索按钮的回调
        } else {
          this.searchFoundItem();
        }
      } else  {
        if(this.lostOrFound) {
          this.getAllLost();
        } else {
          this.getAllFound();
        }
      }
    }
  }
}
</script>

<style scoped>

*{
  margin: 0;
  padding: 0;
}

.el-pagination{
  margin-top: 1rem;
  margin-bottom: 1rem;
  justify-content: center;
}

.form{
  display: grid;
  grid-template-columns: 1fr 1fr;
}

.el-dialog.el-dialog--center {
  border-radius: 20px;
}

.box-card{
  padding: 20px;
  width: 300px;
  height: 33vh;
  /*position: relative;*/
}
.className:hover{
  font-size: 2rem;
  color: #3fc3ee;
  text-decoration: underline;
}
.cardAnimation-enter-active{
  animation-duration: .7s;
  animation-name: fadeIn;  /*animate.css库*/
}

.cardAnimation-leave-active{
  animation-duration: .7s;
  animation-name: fadeOut;
}
</style>