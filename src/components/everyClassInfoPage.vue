<template>
  <div style="width:1000px;height:1000px;">
  <page-header classroom-name="asda" :father-method="goToBubble"></page-header>
  <tab-page></tab-page>
  </div>
</template>

<script>
import pageHeader from "@/components/pageHeader";
import TabPage from "@/components/classRoom/tabPage";
import router from "@/router";
export default {
  name: "everyClassInfo",
  props:{
    ClassInfo:Object, // 传入参数
  },
  components: {
    TabPage,
    pageHeader
  },
  methods:{
    goToBubble(){
      router.push('/index');
    }
  }
}
</script>

<style scoped>
#app > section > main > div > div.el-tabs__content > div.ctt > div > div > iframe {
  width: 800px;
}
</style>