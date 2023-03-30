<template>
  <div class="personalPage" style="margin: 20px auto">
    <div style="margin-top: 30px">
      <form action="">
        <div class="social-container">
          <el-tooltip
              effect="dark"
              content="帅气的您"
              placement="bottom-start">
            <a href="#"><el-avatar size="large" :src= "this.$user.avatarUrl"
            ></el-avatar></a>
          </el-tooltip>
        </div>
        <span style="font-size: 3rem">{{ this.$user.userName}}</span>
        <a href="#">Change your password?</a>
        <button>Confirm</button>
      </form>
    </div>
    <div class="overlay-container">
      <div class="overlay">
        <div class="overlay-panel overlay-right">
          <h1>Want To Leave?</h1>
          <p>farewell my friend</p>
          <button @click="logOut" class="ghost" id="signUp">
            <div style="display: flex;align-items: center;column-gap: 10px">
            <logout theme="outline" size="21" fill="#333" strokeLinejoin="bevel" strokeLinecap="square"/>
            <span>Log Out</span>
            </div>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {Logout} from "@icon-park/vue-next";
export default {
  components:{
    Logout,
  },
  name: "personalPage",
  methods:{
    logOut(){
      this.$emit('logOut');
    }
  }
}
</script>

<style scoped>
/*@import url(https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,200;1,100&display=swap)*/

* {
  box-sizing: border-box;
}

body {
  background: #f6f5f7;
  font-family: 'Montserrat', sans-serif;
  height: 100vh;
  margin: -20px 0 50px;
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

form {
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

.personalPage{
  row-gap: 100px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22);
  position: relative;
  overflow: hidden;
  width: 800px;
  height: 800px;
  max-width: 100%;
  min-height: 480px;
}

.container.right-panel-active .sign-in-container{
  transform: translateX(100%);
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
  height: 20%;
  transition: transform 0.6s ease-in-out;
  z-index: 100;
}
.right-panel-active .overlay-container{
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
  position: absolute;
  left: -100%;
  margin-top: 25%;
  height: 30%;
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
</style>