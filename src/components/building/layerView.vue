<template>
<el-collapse style="width: 78%" v-model="activeName" accordion>
<el-collapse-item v-for="(item,index) in this.classRoomList" :key="index" :name="index">
  <template #title>
    <div style="display: grid;grid-template-columns: 1fr 1fr;align-items: center;">
    <up-and-down theme="outline" size="34" fill="#333" :strokeWidth="2" strokeLinejoin="bevel" strokeLinecap="square"/>
    <p style="font-size: 23px;font-weight: 800;margin-top: 25px">{{ this.layerList[index]}}</p>
    </div>
  </template>
  <div style="display: grid;grid-template-columns: 1fr 1fr 1fr">
  <el-card @click="handleClick(i['教室名'])" v-for="(i, id) in item" :key="id + 10" shadow="hover" body-style="padding:30px;">
    <div style="display:flex;justify-content:space-between;">
    <span style="font-weight: 500;font-size: 20px">
      {{i['教室名']}}
    </span>
    <classroom style="margin-right: 5px" theme="outline" size="33" fill="#333" :strokeWidth="2" strokeLinejoin="bevel" strokeLinecap="square"/>
    </div>
  </el-card>
  </div>
</el-collapse-item>
</el-collapse>
</template>
<script>
import {UpAndDown} from "@icon-park/vue-next";
import {Classroom} from "@icon-park/vue-next";

export default {
  props:{
    classRoomList: Object,
  },
  data() {
    return {
      layerList:['一楼','二楼','三楼','四楼','五楼','六楼','七楼'],
      activeName: '1'
    };
  },
  components:{
    UpAndDown,
    Classroom
  },
  created() {
    console.log(this.classRoomList);
  },
  methods:{
    handleClick(str){
      this.$emit('fatherMethod', str);
    }
  }
}
</script>