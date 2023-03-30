<template>
  <div class="typer" >
    <div class="typer-content">
      <p class="typer-dynamic typeStr">
          <span class="cut">
            <span class="word typeStr" v-for="(letter,index) in words" :key="index">{{letter}}</span>
          </span>
        <!-- 模拟光标-->
        <span class="typer-cursor"></span>
      </p>
    </div>
  </div>

  <el-dialog
      v-model="inputAvatarUrl"
      title="Avatars"
      width="30%">
    <input v-model="inputAvatarUrlContext" type="text" placeholder="Your Avatar Url">
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="inputAvatarUrl = false;">Cancel</el-button>
        <el-button type="primary" @click="confirmAvatarUrl">
          Confirm
        </el-button>
      </span>
    </template>
  </el-dialog>
  <el-dialog
      v-model="dialogVisible"
      title="Avatars"
      width="30%"
  >
    <div class="grid-container">
      <div v-for="(item, index) in this.avatarUrlList" :key="index"  @click="chooseAvatar(index)">
        <el-avatar :class="{'chosen': this.chosenIndex == index}" :src="item" :size="'large'"></el-avatar>
      </div>
    </div>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogVisible = false; this.chosenIndex = 0;">Cancel</el-button>
        <el-button type="primary" @click="handleConfirm">
          Confirm
        </el-button>
      </span>
    </template>
  </el-dialog>
  <div v-loading="imitateSignDelay" :class="{container:true,'right-panel-active':this.signIn }" id="container" style="margin: 0 auto">
    <div class="form-container sign-up-container">
      <div class="formClass" >
        <h1>注册</h1>
        <div class="social-container">
          <el-tooltip
              effect="dark"
          content="可以直接上传url哦"
          placement="bottom-start">
          <a href="#" @click="this.inputAvatarUrl = true;">
            <el-avatar src= "https://www.beihaiting.com/uploads/allimg/161010/10723-161010140Z4E8.jpg">
          </el-avatar>
          </a>
          </el-tooltip>
          <el-tooltip
              effect="dark"
              content="点击上传头像"
              placement="bottom-start">
            <a @click="clickHiddenInput">
              <el-avatar :src="avatarUrl">
              </el-avatar>
            </a>
          </el-tooltip>
          <input ref="fileinp" hidden type="file" id="file" @change="add($event)" />
          <el-tooltip content="也可以选择默认头像">
          <a href="#" @click="this.dialogVisible = true">
            <el-avatar src="https://tse3-mm.cn.bing.net/th/id/OIP-C.ivzGyMaIjHLlavqbwGXnpwAAAA?pid=ImgDet&rs=1"></el-avatar>
          </a>
          </el-tooltip>
        </div>
        <span>name yourself</span>
        <input type="text" v-model="username" @focusout="checkUserNameValidity" placeholder="User Name">
        <input type="password" v-model="password" placeholder="Password">
        <button @click="signUpAccount" style="margin-top: 20px" >Sign Up</button>
      </div>
    </div>
    <div class="form-container sign-in-container">
      <div class="formClass">
        <h1>登录</h1>
        <div class="social-container">
          <a href="#"><el-avatar src="https://tse1-mm.cn.bing.net/th/id/OIP-C.iM5exdDydjHccRz4-k27uQHaHa?pid=ImgDet&rs=1"
          ></el-avatar></a>
          <el-tooltip
              effect="dark"
              content="帅气的您"
              placement="bottom-start">
          <a href="#"><el-avatar src= "https://www.beihaiting.com/uploads/allimg/161010/10723-161010140Z4E8.jpg"
          ></el-avatar></a>
          </el-tooltip>
          <a href="#"><el-avatar src="https://tse3-mm.cn.bing.net/th/id/OIP-C.ivzGyMaIjHLlavqbwGXnpwAAAA?pid=ImgDet&rs=1"></el-avatar></a>
        </div>
        <span>or use your account</span>
        <input v-model="username" type="text" placeholder="User Name" />
        <input v-model="password" type="password" placeholder="Password" />
        <a href="#">Forgot your password?</a>
        <button @click="signInAccount">Sign In</button>
      </div>
    </div>
    <div class="overlay-container">
      <div class="overlay">
        <div class="overlay-panel overlay-left">
          <h1>Welcome Back!</h1>
          <p>
            To keep connected with us please login with your personal info
          </p>
          <button class="ghost" @click="handleSignIn" id="signIn">Sign In</button>
        </div>
        <div class="overlay-panel overlay-right">
          <h1>Hello,Friend!</h1>
          <p>Enter your personal details and start journey with us</p>
          <button @click="handleSignUp" class="ghost" id="signUp">Sign Up</button>
        </div>
      </div>
    </div>
  </div>
  <footer>
    <p>
      Created with<i class="fa fa-heart"></i>by
      <a href="https://space.bilibili.com/13833854" target="_blank">Navi</a>
    </p>
  </footer>

</template>

<script>
import axios from "axios";

export default {
  name: "loginOrRegister",
  data(){
    return{
      words:[],               //字母数组push，pop的载体
      str:"By Navi",          //str初始化
      letters:[],             //str分解后的字母数组
      order:1,                //表示当前是第几句话
      typewriter: '',
      i: 0,
      timer: 0,
      userId: -1,
      userNameOccupied: false,
      imitateSignDelay: false,
      inputAvatarUrl: false,
      inputAvatarUrlContext: '',
      dialogVisible: false,
      chosenIndex: 0,
      avatarUrlList:
          [
            "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
            'https://tse2-mm.cn.bing.net/th/id/OIP-C.vNn5RXHfCzUZGcdtzYG92AHaHa?w=161&h=180&c=7&r=0&o=5&dpr=2&pid=1.7',
            "https://tse2-mm.cn.bing.net/th/id/OIP-C.UsavMQ7MV08TtUiCaEKTAAAAAA?w=198&h=198&c=7&r=0&o=5&dpr=2&pid=1.7",
            "https://tse3-mm.cn.bing.net/th/id/OIP-C.-SW2Zx4d18IXG3GqeoaBYgHaHa?w=206&h=207&c=7&r=0&o=5&dpr=2&pid=1.7",
            "https://pic1.zhimg.com/v2-b832e983b07e5a56cb08106e45cbedc1_r.jpg?source=1940ef5c",
            "https://www.beihaiting.com/uploads/allimg/170522/10723-1F522142304A6.jpg",
            "https://pic2.zhimg.com/v2-0c5dc901830ee38c87e691774a4239d9_r.jpg?source=1940ef5c",
            "https://tse1-mm.cn.bing.net/th/id/OIP-C.iM5exdDydjHccRz4-k27uQHaHa?pid=ImgDet&rs=1",
            "https://www.beihaiting.com/uploads/allimg/161010/10723-161010140Z4E8.jpg",
            "https://ts1.cn.mm.bing.net/th/id/R-C.8421fec5bae5300b4ddda08f0b475d33?rik=vRDDRWkv0GEV4w&riu=http%3a%2f%2fwww.acgwow.com%2fimages%2fupload%2f2021071913181768.png&ehk=LhH15PpfhR0yqsERwXOBB0EjUTjw1VWfeo0M7TQbGR8%3d&risl=&pid=ImgRaw&r=0",
            "https://tse3-mm.cn.bing.net/th/id/OIP-C.ivzGyMaIjHLlavqbwGXnpwAAAA?pid=ImgDet&rs=1",
            "https://img.zcool.cn/community/01a5655d528cbba80120695cd78819.jpg@2o.jpg",
            "https://ts1.cn.mm.bing.net/th/id/R-C.2f0bf39a1525331307fa77da4104c50b?rik=IPiRE327Dtghpg&riu=http%3a%2f%2ftva3.sinaimg.cn%2flarge%2f006yt1Omgy1grcdi199vbj30u00tmnpd.jpg&ehk=hsqxxbCktnIp%2fckZr9whtjyyUyQmN4tqXZMCawc23bI%3d&risl=&pid=ImgRaw&r=0",
            "https://tse2-mm.cn.bing.net/th/id/OIP-C.l440iacD-fbdgHBFK58lHAHaJi?pid=ImgDet&rs=1",
            "https://pic1.zhimg.com/v2-3eed23b842ba9744cec6a2cba1def428_b.jpg",
            "https://ts1.cn.mm.bing.net/th/id/R-C.3737b40703e92d0636ab33c0f854954e?rik=ycEskn5cezWJtw&riu=http%3a%2f%2fn.sinaimg.cn%2fsinakd20210103ac%2f133%2fw1453h1080%2f20210103%2fc189-kherpxx2987953.jpg&ehk=Gi14Za0bY5y9LGmgeNFvwi4N7kWzYARFFWutzfitAc4%3d&risl=&pid=ImgRaw&r=0",
          ],
      username: '',
      password:'',
      signIn:false,
      avatarUrl: "https://tse1-mm.cn.bing.net/th/id/OIP-C.iM5exdDydjHccRz4-k27uQHaHa?pid=ImgDet&rs=1",
    }
  },
  methods:{
    //开始输入的效果动画
    begin(){
      this.letters=this.str.split("")
      for(var i=0;i<this.letters.length;i++){
        setTimeout(this.write(i),i*50);
      }
    },
    //开始删除的效果动画
    back(){
      let L=this.letters.length;
      for(var i=0;i<L;i++){
        setTimeout(this.wipe(i),10 * i);
      }
    },
    //输入字母
    write(i){
      return ()=>{
        let L=this.letters.length;
        this.words.push(this.letters[i]);
        let that=this;
        /*如果输入完毕，在2s后开始删除*/
        if(i==L-1){
          setTimeout(function(){
            that.back();
          },2000);

        }
      }
    },
    //擦掉(删除)字母
    wipe(i){
      return ()=>{
        this.words.pop(this.letters[i]);
        /*如果删除完毕，在300ms后开始输入*/
        if(this.words.length==0){
          this.order++;
          let that=this;
          setTimeout(function(){
            that.begin();
          },100);

        }
      }
    },
    chooseAvatar(index){
      this.chosenIndex = index;
    },
    handleConfirm(){
      this.avatarUrl = this.avatarUrlList[this.chosenIndex];
      this.chosenIndex = 0;
      this.dialogVisible = false;
    },
    confirmAvatarUrl(){
      this.avatarUrl = this.inputAvatarUrlContext;
      this.inputAvatarUrl = false;
    },
    checkUserNameValidity(){
      axios.get('http://127.0.0.1/findUser',
          {
            params: {
              name: this.username
            }
          }).then(res=>{
            if(res.data.length > 0){
              this.userNameOccupied = true;
              return;
            } else {
              this.userNameOccupied = false;
            }
      }).catch(err=>{
        console.log("获取数据失败" + err);
      });
    },
    signUpAccount(){
      if(this.username === '' || this.password === '') {
        this.$message.warning("请输入完整注册信息");
        return;
      } else if(this.userNameOccupied){
        if(this.username === ''){
          this.$message.warning("请输入完整注册信息");
          return;
        }
        this.$message.warning('用户名已被占用，请更换用户名');
        return;
      }
      axios.post('http://127.0.0.1/signUp',
          {
            name: this.username,
            password: this.password,
            avatarurl: this.avatarUrl,
          }).then(res=>{
        axios.post('http://127.0.0.1/getAvatarAndUserId',
            {
              name: this.username
            }).then(res=>{
          // console.log(res.data);
          this.imitateSignDelay = true;
          setTimeout(()=>{
            this.changeImitateSign();
            this.$user.userName = this.username;
            this.$user.avatarUrl = res.data.avatarUrl;
            this.$user.userId = res.data.userId;
            this.username = this.password = '';
            this.$message.success('注册成功！');
            this.goToMainPage();
          },1500);
        }).catch(err=>{
          console.log("获取数据失败" + err);
        });
        console.log(res.data);
      }).catch(err=>{
        console.log("获取数据失败" + err);
      });
    },
    signInAccount(){
      if(this.username === '' && this.password === ''){
        this.$message.warning("请输入账户信息");
        return;
      } else if(this.username === ''){
        this.$message.warning('用户名不能为空');
        return;
      } else if(this.password === ''){
        this.$message.warning('密码不能为空');
        return;
      }
      axios.post('http://127.0.0.1/signIn',
          {
            name: this.username,
            password: this.password,
          }).then(res=>{
            if(res.data.status === 1){
              axios.post('http://127.0.0.1/getAvatarAndUserId',
                  {
                    name: this.username
                  }).then(res=>{
                // console.log(res.data);
                this.avatarUrl = res.data.avatarUrl;
                this.userId = res.data.userId;
                this.imitateSignDelay = true;
                setTimeout(()=>{
                  this.changeImitateSign();
                  this.$message.success('登陆成功！');
                  this.password = '';
                  this.$user.userId = this.userId;
                  this.$user.userName = this.username;
                  this.$user.avatarUrl = this.avatarUrl;
                  this.goToMainPage();
                },1500);
              }).catch(err=>{
                console.log("获取数据失败" + err);
              });
            } else if(res.data.status === 0) {
              this.imitateSignDelay = true;
              setTimeout(()=>{
                this.changeImitateSign();
                this.$message.warning('用户名或密码错误！');
                this.username = '';
                this.password = ''
                },1500);
              return;
            } else {
                this.$message.warning('您还未注册哦～');
                this.username = '';
                this.password = ''
            }
      }).catch(err=>{
        console.log("获取数据失败" + err);
      });
    },
    clickHiddenInput(){
      this.$refs.fileinp.click();
    },
    // 这些是动画控制，和实际无关！
    handleSignUp(){
      this.signIn = true;
    },
    handleSignIn(){
      this.signIn = false;
    },
    add(e) {
      //获取到第一个文件
      var file = e.target.files[0];
      //可打印看看
      console.log(e.target.files);
      //新建一个 FormData 对象
      var param = new FormData();
      // 把文件添加到 FormData对象里
      param.append("avatar", file);
      //可以打印看看
      console.log(param.get("file"));
      //利用axios发送post请求
      axios
          .post("http://localhost:8848/imgStorage/add", param, {
            headers: { "Content-Type": "multipart/form-data" },
          })
          // eslint-disable-next-line no-unused-vars
          .then((res) => {
            console.log(res);
            this.avatarUrl = 'http://localhost:8848/' + res.data.filename;
            //调用查询方法
          });
    },
    changeImitateSign(){
      this.imitateSignDelay = !this.imitateSignDelay;
    },
    goToMainPage(){
      this.$emit('goToMainPage');
    }
  },
  mounted() {
    this.begin();
  },
  watch:{                     //监听order值的变化，改变str的内容
    // eslint-disable-next-line no-unused-vars
    order(old,newV){
      if(this.order%4==1){
        this.str="Hello My Friend!"
      }
      else if(this.order%4==2){
        this.str="Login in or Sign up Your Account~"
      }
      else if(this.order%4==3){
        this.str="Hope You can Enjoy the Journey with us!"
      }
      else{
        this.str="Welcome!"
      }
    },
    username(){
      this.checkUserNameValidity();
    }
  },
}
</script>

<style scoped lang="less">
/*@import url(https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,200;1,100&display=swap)*/

.typing{
  font-weight: 200;
  margin: 0  auto;
}
* {
  box-sizing: border-box;
}
body {
  background: #f6f5f7;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  font-family: 'Montserrat', sans-serif;
  height: 100vh;
  margin: -20px 0 50px;
}
.grid-container {
   display: grid;
   grid-template-columns: auto auto auto auto;
   grid-gap: 10px;
   padding: 20px;
 }
h1 {
  font-weight: bold;
  margin: 0;
}
h2 {
  text-align: center;
}
p {
  font-size: 14px;
  font-weight: 100;
  line-height: 20px;
  letter-spacing: 0.5px;
  margin: 20px 0 30px;
}
span {
  font-size: 12px;
}
a {
  color: #333;
  font-size: 14px;
  text-decoration: none;
  margin: 15px 0;
}
button {
  border-radius: 20px;
  border: 1px solid #58c7e0;
  background-color: #0ec9ea;
  color: #ffffff;
  font-size: 12px;
  font-weight: bold;
  padding: 12px 45px;
  letter-spacing: 1px;
  text-transform: uppercase;
  transition: transform 80ms ease-in;
}
button:active {
  transform: scale(0.95);
}
button:focus {
  outline: none;
}
button.ghost {
  background-color: transparent;
  border-color: #ffffff;
}
.formClass {
  background-color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 0 50px;
  height: 100%;
  text-align: center;
}
input {
  background-color: #eee;
  border: none;
  padding: 12px 15px;
  margin: 8px 0;
  width: 100%;
}
.container {
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22);
  position: relative;
  overflow: hidden;
  width: 1000px;
  max-width: 100%;
  min-height: 480px;
}
.form-container{
  position: absolute;
  top: 0;
  height: 100%;
  transition: all 0.6s ease-in-out;
}
.sign-in-container{
  left: 0;
  width: 50%;
  z-index: 2;
}
.container.right-panel-active .sign-in-container{
  transform: translateX(100%);
}
.sign-up-container{
  left: 0;
  width: 50%;
  opacity: 0;
  z-index: 1;
}
.container.right-panel-active .sign-up-container{
  transform: translateX(100%);
  opacity: 1;
  z-index: 5;
  animation: show 0.6s;
}
@keyframes show {
  0%,49.99%{
    opacity: 0;
    z-index: 1;
  }
  50%,100%{
    opacity: 1;
    z-index: 5;
  }
}
.overlay-container{
  position: absolute;
  top: 0;
  left: 50%;
  width: 50%;
  height: 100%;
  overflow: hidden;
  transition: transform 0.6s ease-in-out;
  z-index: 100;
}
.container.right-panel-active .overlay-container{
  transform: translateX(-100%);
}
.overlay{
  background: #18c0de;
  background: -webkit-linear-gradient(to right, #18c0de, #18c0de);
  background: linear-gradient(to right, #73d6e8, #73d6e8);
  background-repeat: no-repeat;
  background-size: cover;
  background-position: 0 0;
  color: #ffffff;
  position: relative;
  left: -100%;
  height: 100%;
  width: 200%;
  transform: translateX(0);
  transition: transform 0.6s ease-in-out;
}
.container.right-panel-active .overlay{
  transform: translateX(50%);
}
.overlay-panel{
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  text-align: center;
  top: 0;
  height: 100%;
  width: 50%;
  transform: translateX(0);
  transition: transform 0.6s ease-in-out;
}
.overlay-left{
  transform: translateX(-20%);
}
.container.right-panel-active .overlay-left{
  transform: translateX(0);
}
.overlay-right{
  right: 0;
  transform: translateX(0);
}
.container.right-panel-active .overlay-right{
  transform: translateX(20%);
}
.social-container{
  margin: 20px 0;
}
.social-container a{
  border: 1px solid #dddddd;
  border-radius: 50%;
  display: inline-flex;
  justify-content: center;
  align-items: center;
  margin: 0 5px ;
  height: 50px ;
  width: 50px ;
}
.chosen {
  border: 1px solid blue;
}

footer{
  background-color: #dfe2e3;
  font-weight: 100;
  color: #000000;
  font-size: 14px ;
  bottom: 0;
  position: fixed;
  left: 0;
  right: 0;
  text-align: center;
  z-index: 999;
}
footer p{
  margin: 10px 0;

}
footer i{
  color: red;
}
footer a{
  color: #3c97bf;
  text-decoration: none;
}

@thePink: #000000;

.typer{
  height: 5rem;
}
.typer-content{
  margin: 20px auto;
  font-size: 2rem;
  font-weight: bolder;
  display: flex;
  flex-direction: row;
  letter-spacing: 2px
}
.typer-dynamic{
  margin: 0 auto;
  font-size: 2rem;
  font-weight: bolder;
  position: relative;
}
.cut{
  color: @thePink;
}
.typer-cursor{
  position: absolute;
  height: 100%;
  width: 3px;
  top: 0;
  right: -10px;
  background-color: @thePink;
  animation: flash 1.5s linear infinite; //闪烁
}

.typeStr{
  font-size: 2rem;
  font-weight: bolder;
}
</style>