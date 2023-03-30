<template>
  <div id="app">
    <!-- 上传文件按钮，绑定change事件 -->
    <div class="upload">
      <input type="file" id="file" @change="add($event)" />
    </div>
    <!-- 显示图片的盒子 -->
    <div class="container">
      <!-- 假如变量imgs为接口返回的图片数组，循环显示 -->
      <div v-for="(item, index) in imgs" :key="index">
        <!-- 服务端地址 + 数据库里的 icon字段 便可以显示一张图片 -->
        <img :src="'http://localhost:8848/' + item.icon" alt="" />
      </div>
    </div>
  </div>

</template>

<script>
import axios from "axios";
export default {
  name: "avatarUpload",
  data() {
    return {
      imgs: [],
    };
  },
  methods: {
    //上传图片
    add(e) {
      //获取到第一个文件
      var file = e.target.files[0];
      //可打印看看
      console.log(e.target.files);
      //新建一个 FormData 对象
      var param = new FormData();
      // 把文件添加到 FormData对象里
      param.append("icon", file);
      //可以打印看看
      console.log(param.get("file"));
      //利用axios发送post请求
      axios
          .post("http://localhost:8848/comic/add", param, {
            headers: { "Content-Type": "multipart/form-data" },
          })
          // eslint-disable-next-line no-unused-vars
          .then((res) => {
            //调用查询方法
            this.qy();
          });
    },
    //查询
    qy() {
      axios({
        url: "http://localhost:8848/comic/all",
        method: "get",
      }).then((res) => {
        //把后端返回数据赋值给imgs
        this.imgs = res.data.data;
      });
    },
  },
  created() {
    this.qy();
  },
};

</script>

<style>
#app > header > section{
}
body {
  text-align: center;
}
.container {
  width: 60%;
  box-shadow: 0 0 5px rgb(190, 190, 190);
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}
.container img {
  width: 250px;
  height: 150px;
  object-fit: cover;
  margin: 30px;
}
.upload {
  margin: 30px auto;
  width: 80px;
  height: 20px;
  background-color: rgba(135, 206, 235, 0.2);
  border: 1px dashed black;
  border-radius: 5px;
  position: relative;
}
.upload:hover {
  background-color: rgba(135, 206, 235, 1);
}
.upload::before {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  content: "上传图片";
  font-size: 13px;
  text-align: center;
  font-family: "fangsong";
  line-height: 20px;
  user-select: none;
}
#file {
  width: 100%;
  height: 100%;
  opacity: 0;
}

</style>