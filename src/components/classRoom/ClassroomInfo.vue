<template>
  <!--陈瑞球楼存在问题，姑且先把数据删了！！！！！-->
  <div>
  <br>
    <!--  TODO VR图地址换了，而且大小还需要调整-->
  <div class="ctt">
    <div class="vr">
      <div class="iframeBox">
        <iframe frameborder="0" :src="this.picLink" style="height: 300px;"></iframe>
      </div>
    </div>
  </div>
  <br>
<!--    <el-descriptions title="课程信息" >-->
<!--      <el-descriptions-item label="课程名">{{ this.fill(classCharacters['课程名']) }}</el-descriptions-item>-->
<!--      <el-descriptions-item label="教师姓名">{{ this.fill(classCharacters['教师姓名']) }}</el-descriptions-item>-->
<!--      <el-descriptions-item label="开设学院">{{ this.fill(classCharacters['开设学院']) }}</el-descriptions-item>-->
<!--    </el-descriptions>-->
<!--    <br>-->
  <el-descriptions title="环境信息">
    <el-descriptions-item label="温度">{{ this.fill(classInfo['温度']) }}</el-descriptions-item>
    <el-descriptions-item label="空气湿度">{{ this.fill(classInfo['空气湿度']) }}</el-descriptions-item>
    <el-descriptions-item label="CO2浓度">{{ this.fill(classInfo['CO2浓度']) }}</el-descriptions-item>
    <el-descriptions-item label="PM2.5">{{ this.fill(classInfo['PM25浓度']) }}</el-descriptions-item>
    <el-descriptions-item label="座位数">{{ this.fill(classInfo['座位数']) }}</el-descriptions-item>
    <el-descriptions-item label="实到人数">{{ this.fill(classInfo['实到人数']) }}</el-descriptions-item>
  </el-descriptions>
  <br>
    <el-descriptions title="教室特色">
      <el-descriptions-item label="自习位"> {{ this.fill(classCharacters['自习位'])}} </el-descriptions-item>
      <el-descriptions-item label="座椅类型"> {{ this.fill(classCharacters['座椅类型'])}} </el-descriptions-item>
      <el-descriptions-item label="电子白板">{{ this.fill(classCharacters['电子白板'])}}</el-descriptions-item>
      <el-descriptions-item label="传感器">{{ this.fill(classCharacters['传感器'])}}</el-descriptions-item>
      <el-descriptions-item label="空调">{{ this.fill(classCharacters['空调'])}}</el-descriptions-item>
      <el-descriptions-item label="投影仪">{{ this.fill(classCharacters['投影仪'])}}</el-descriptions-item>
      <el-descriptions-item label="电动幕布">{{ this.fill(classCharacters['电动幕布'])}}</el-descriptions-item>
      <el-descriptions-item label="讲台黑板">{{ this.fill(classCharacters['讲台黑板'])}}</el-descriptions-item>
    </el-descriptions>
<!--    这里还得加一些元素-->
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ClassroomInfo",
  data(){
    return {
      picLink: '',
    }
  },
  props:{
    classroom: String,
    classInfo: Object, // 传入参数
    classCharacters: Object, // 传入参数
  },
  methods:{
    fetchGraph(){
      axios.get('http://127.0.0.1/getGraph',{
        params:{
          classroom: this.classroom,
        }
      }).then(res=>{
        this.picLink = res.data[0].picLink;
      }).catch(err=>{
        console.log("获取数据失败" + err);
      });
    },
    test(){
      // console.log(this.classInfo);
      console.log("here");
      // console.log(!('课程名' in this.classCharacters));
    },
    // 格式化展示信息
    fill(str){
      if(str == '' || str == 'None' || str == undefined){
        return '暂无信息';
      } else {
        return str;
      }
    },
  },
  mounted() {
    this.test();
  },
  created() {
    this.fetchGraph();
  },
  watch:{
    classCharacters(){
      console.log(!('课程名' in this.classCharacters));
    }
  }
}
</script>

<style scoped>

#app > header > section > div > div:nth-child(1) > div:nth-child(4) > div.ctt > div > div > iframe{
  width: 100%;
}

</style>