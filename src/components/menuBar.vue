<template>
<!--  TODO 图中计算vacancy的时候应该用character里的座位数来计算比较合理！-->
  <el-menu
      class="el-menu-demo"
      mode="horizontal"
      :default-active="activeIndex"
  >
    <el-menu-item style="font-size: 2rem" index="0" @click="handleClick('Aside')">
      <page class="icon" theme="outline" size="24" fill="#333"/>
      SJTU
    </el-menu-item>
    <div class="flex-grow" />

    <el-menu-item @click="handleClick('personalPage')" index="mine" v-if="this.haveLogin" >
      <el-avatar style="margin-right: 20px" :src="this.$user.avatarUrl"></el-avatar>
      <el-tooltip placement="bottom" content="点击进入个人主页">
      <span class="menuTab">{{$user.userName}}</span>
      </el-tooltip>
    </el-menu-item>

    <el-menu-item index="login" v-if="!haveLogin" @click="this.handleClick('login')">
      <login class="icon" theme="outline" size="24" fill="#333"/>
      <span class="menuTab">登陆</span>
    </el-menu-item>
    <el-menu-item index="classroom" @click="handleClick('Aside')">
      <building-three class="icon" theme="outline" size="24" fill="#333"/>
          <span class="menuTab">教室情况</span>
    </el-menu-item>
    <el-menu-item index="lostAndFound" @click="handleClick('LostAndFound')">
      <bookshelf class="icon" theme="outline" size="24" fill="#333"/>
      <span class="menuTab">
            失物招领
    </span>
    </el-menu-item>

    <el-menu-item index="search" @click="handleClick('Search')">
      <search class="icon" theme="outline" size="24" fill="#333"/>
    <span class="menuTab">
        检索
    </span>
    </el-menu-item>

    <el-menu-item index="us">
        <a class="menuTab" href="http://ice2604-navi.github.io/" title="跳转到GitHub主页">   关于我们</a>
    </el-menu-item>


  </el-menu>

  <login-or-register v-if="activateLogin" @goToMainPage="this.handleLogin"></login-or-register>
  <personal-page @logOut="logOut" v-if="enterPersonalPage"></personal-page>

  <el-container style="height: 900px;">
    <transition name="all">
    <aside-menu v-if="activateAside"></aside-menu>
    </transition>
    <search-class v-if="activateSearch"></search-class>
    <lost-and-found-for-all v-if="activateLostAndFound"></lost-and-found-for-all>
  </el-container>

</template>
<script>
import '@icon-park/vue-next/styles/index.css';
import {Page} from '@icon-park/vue-next'
import {Search} from '@icon-park/vue-next'
import {BuildingThree} from '@icon-park/vue-next'
import asideMenu from "@/components/asideMenu";
import SearchClass from "@/components/searchPage/searchClass";
import {Bookshelf} from "@icon-park/vue-next";
import LostAndFoundForAll from "@/components/lostAndFoundForAll";
import LoginOrRegister from "@/components/user/loginOrRegister";
import PersonalPage from "@/components/user/personalPage";
import {Login} from '@icon-park/vue-next'
export default {
  data(){
    return{
      activeIndex: 'classroom',
      enterPersonalPage: false,
      activateAside: true,
      activateSearch: false,
      activateLostAndFound: false,
      activateLogin: false,
      haveLogin: false,
    }
  },
  components:{
    Page,
    Login,
    PersonalPage,
    LoginOrRegister,
    LostAndFoundForAll,
    SearchClass,
    Bookshelf,
    asideMenu,
    BuildingThree,
    Search,
  },
  methods:{
    clear(){
      this.activateAside = this.activateSearch = this.activateLostAndFound = this.activateLogin = this.enterPersonalPage = false;
    },
    handleClick(str){
      this.clear();
      if(str==='Aside'){
        this.activateAside = true;
      } else if(str === 'LostAndFound') {
        this.activateLostAndFound = true;
      }
        else if(str === 'login'){
          this.activateLogin = true;
      } else if(str === 'personalPage'){
          this.enterPersonalPage = true;
      } else {
        this.activateSearch = true;
      }
    },
    changeLogin(){
      this.haveLogin = !this.haveLogin;
    },
    handleLogin(){
      this.handleClick('Aside'); // 登陆后返回主界面;
      this.changeLogin();
    },
    logOut(){
      this.haveLogin = false;
      this.$user.userName = '';
      this.$user.avatarUrl = '';
      this.$user.userId = -1;
      this.$message.success('已登出')
      this.handleClick('Aside'); // 登陆后返回主界面;
    },
  },
  created() {
  }
}
</script>

<style>
.all-enter{
  animation-duration: 10s;
}
.flex-grow {
  flex-grow: 1;
}

.menuTab{
  font-size: larger;
}

.icon {
  margin-right: 10px;
}
</style>
