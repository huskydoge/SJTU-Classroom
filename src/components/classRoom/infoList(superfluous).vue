<template>
  <br>
  <div class="ctt">
    <div class="vr">
      <div class="iframeBox">
        <iframe frameborder="0" src="https://etc.sjtu.edu.cn/vr/s/101/index.html" style="height: 300px;"></iframe>
      </div>
    </div>
  </div>
  <br>
  <el-descriptions title="环境信息">
    <el-descriptions-item label="温度湿度">kooriookami</el-descriptions-item>
    <el-descriptions-item label="CO2浓度">18100000000</el-descriptions-item>
    <el-descriptions-item label="照度">Suzhou</el-descriptions-item>
    <el-descriptions-item label="PM2.5">
      <el-tag size="small">School</el-tag>
    </el-descriptions-item>
    <el-descriptions-item label="Address"
    >No.1188, Wuzhong Avenue, Wuzhong District, Suzhou, Jiangsu
      Province</el-descriptions-item
    >
  </el-descriptions>
  <br>
  <el-descriptions title="教室特色">
    <el-descriptions-item label="温度湿度">kooriookami</el-descriptions-item>
    <el-descriptions-item label="CO2浓度">18100000000</el-descriptions-item>
    <el-descriptions-item label="照度">Suzhou</el-descriptions-item>
    <el-descriptions-item label="PM2.5">
      <el-tag size="small">School</el-tag>
    </el-descriptions-item>
    <el-descriptions-item label="Address"
    >No.1188, Wuzhong Avenue, Wuzhong District, Suzhou, Jiangsu
      Province</el-descriptions-item
    >
  </el-descriptions>

</template>

<script>
export default {
  name: "infoList",
  props:{
    ClassInfo:Object, // 传入参数
  }
}
</script>

<style scoped>
#app > section > main > div:nth-child(1) > div.el-tabs.el-tabs--right > div.el-tabs__content > div.ctt > div > div > iframe{
  width: 800px;
}
</style>