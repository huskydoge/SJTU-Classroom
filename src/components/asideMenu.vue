<template>
 <el-aside  width="230px" style="margin-right: 30px">
      <el-menu
          class="el-menu-vertical-demo"
          router
          :collapse=false
          default-active="/home/">

        <el-menu-item index="/home/intro">
          <template #title>
            <home-two theme="outline" size="20px" style="margin-right: 10px" fill="#333"/>
            <span class="asideTab">介绍</span>
          </template>
        </el-menu-item>
        <el-menu-item index="/home/dynamic">
          <template #title>
            <api-app class="icon" theme="outline" size="24" fill="#333"/>
            <span class="asideTab">实时动态</span>
          </template>
        </el-menu-item>

        <el-menu-item index="/home/dongshang">
          <template #title>
            <school theme="outline"  size="20px" fill="#333" style="margin-right: 10px"/>
            <span class="asideTab" style="font-size: large">东上院</span>
          </template>
        </el-menu-item>
        <el-menu-item index="/home/dongzhong">
          <school theme="outline"  size="20px" fill="#333" style="margin-right: 10px"/>
          <span class="asideTab">东中院</span>
        </el-menu-item>
        <el-menu-item index="/home/dongxia">
          <school theme="outline"  size="20px" fill="#333" style="margin-right: 10px"/>
          <span class="asideTab">东下院</span>
        </el-menu-item>
        <el-menu-item index="/home/shangyuan">
          <engineering-brand class="icon" theme="outline" size="24" fill="#333"/>
          <span class="asideTab">上院</span>
        </el-menu-item>
        <el-menu-item index="/home/zhongyuan">
          <engineering-brand class="icon" theme="outline" size="24" fill="#333"/>
          <span class="asideTab">中院</span>
        </el-menu-item>
        <el-menu-item index="/home/xiayuan">
          <engineering-brand class="icon" theme="outline" size="24" fill="#333"/>
          <span class="asideTab">下院</span>
        </el-menu-item>
        <el-menu-item index="/home/chenruiqiu">
          <building-four class="icon" theme="outline" size="24" fill="#333"/>
          <span class="asideTab">陈瑞球楼</span>
        </el-menu-item>
      </el-menu>
 </el-aside>
  <div class="content"  style="display: flex;">
    <router-view></router-view>
  </div>
</template>

<script>
import '@icon-park/vue-next/styles/index.css';
import {EngineeringBrand} from '@icon-park/vue-next'
import {BuildingFour} from '@icon-park/vue-next'
import {School} from '@icon-park/vue-next';
import {HomeTwo} from '@icon-park/vue-next';
import {ApiApp} from '@icon-park/vue-next';
export default{
components:{
  School,
  HomeTwo,
  BuildingFour,
  EngineeringBrand,
  ApiApp
}
}

</script>

<style scoped>
.content::-webkit-scrollbar {
  width: 0;
}
.icon{
  size: 20px;
  margin-right: 10px;
}
.asideTab{
  font-size: large;
}
/*.el-aside {*/
/*  height: calc(100vh - 70px);*/
/*}*/

/*.el-main {*/
/*  padding: 0;*/
/*  height: calc(100vh - 70px);*/
/*}*/


</style>



