<template>
<!--  上菜单栏-->
  <get-classroom-info v-if="false"></get-classroom-info>
    <el-header>
       <menu-bar></menu-bar>
    </el-header>
</template>

<script>


// import asideMenu from "@/components/asideMenu";
import menuBar from "@/components/menuBar.vue"
import getClassroomInfo from "@/components/dataBase/getClassroomInfo";
export default {
  name:'App',
  data(){
    return{
      showDynamicBubble: true,
    }
  },
  components:{
    getClassroomInfo,
    menuBar,
    // asideMenu,
  },
  methods:{
  }
}

</script>

<style>
.el-header {
  height: 70px;
}

</style>
