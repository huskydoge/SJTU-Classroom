<template>
  <el-container>
    <el-container >
      <aside-menu ></aside-menu>
    </el-container>
  </el-container>
</template>

<script>


import asideMenu from "@/components/asideMenu";
export default {
  name:'App',
  data(){
    return{
      showDynamicBubble: true,
    }
  },
  components:{
    asideMenu
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
