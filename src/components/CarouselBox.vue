<template>
  <div class="block text-center">

    <el-carousel height="600px">
      <el-carousel-item v-for="item in ((respectiveImgList == [])? imgList:respectiveImgList)" :key="item">
        <img :src=item style="width: 100%"/>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>

export default {
  name: 'CarouselBox',
  props:{
    respectiveImgList: Array,
  },
  data(){
    return{
      imgList:['https://img1.qunarzz.com/travel/d8/201404/03/e4a6bc6e68004cd4ddb12cfb.jpg_r_640x423x70_581f32f0.jpg',
        "https://ts1.cn.mm.bing.net/th/id/R-C.03711e2e699ca0432e116d10caab7225?rik=%2bgrelp8ydUfmFw&riu=http%3a%2f%2fpic140.huitu.com%2fpic%2f20200417%2f1656159_20200417161613159070_0.jpg&ehk=O72StrqjVI5mvE8spnNiN36Bi2%2fPnJFn2Tj%2bQZjMJRQ%3d&risl=&pid=ImgRaw&r=0",
        'https://ts1.cn.mm.bing.net/th/id/R-C.d1cc12091978bd8584c251b48d2e30cd?rik=w%2b3eHQeYDM4PtQ&riu=http%3a%2f%2fwww.youxiuhr.com%2fuploads%2f2017%2f09%2f220007377293.jpg&ehk=KQeNJmCUoYYQsM6%2fI5Lph%2b782pHTlhiaET02Booyi9k%3d&risl=&pid=ImgRaw&r=0',
        'https://img1.qunarzz.com/travel/poi/1704/eb/1a2692a8af38b537.jpg_480x360x95_5c07df71.jpg']
    }
  }
}
</script>

<style scoped>
.demonstration {
  color: var(--el-text-color-secondary);
}

.el-carousel__item h3 {
  color: #475669;
  opacity: 0.75;
  line-height: 150px;
  margin: 0;
  text-align: center;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
</style>
