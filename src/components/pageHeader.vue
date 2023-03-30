<template>
  <el-page-header :icon="icon" @click="goBack">

    <template #content>
      <span class="text-large font-600 mr-3"> {{ classroomName }} </span>
    </template>

  </el-page-header>
</template>

<script>
import { ArrowLeft } from '@element-plus/icons-vue'
export default {
  props:{
    fatherMethod: {
      type: Function,
    },
    classroomName: String
  },
  data(){
    return{
      icon: ArrowLeft
    }
  },
  methods:{
    goBack(){
      this.fatherMethod();
    }
  }
}
</script>


