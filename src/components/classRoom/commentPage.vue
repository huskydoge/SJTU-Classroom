<template>
  <word-cloud :words="this.wordsData"></word-cloud>
  <h2> 你留下的足迹  👣.....</h2>
  <div class="comment" style="margin-top: 2rem">
    <div class="comment-body" v-for="(item, index) in comments" :key="item._id + '' + index">
      <!-- 一级评论 -->
      <div class="first-comment">
        <el-avatar :size="40" :src="item.avatarUrl"></el-avatar>
        <div class="content">
          <!-- 一级评论用户昵称 -->
          <h3>{{ item.username }}</h3>
          <!-- 一级评论发布时间 -->
          <span>{{ item.date }}</span>
          <!-- 一级评论评论内容 -->
          <p>{{ item.content }}</p>
          <!-- 一级评论评论点赞 -->
          <div class="comment-right">
            <i
                class="el-icon-trophy"
                @click="giveALike(item, index)"
                :class="item.favour.includes(this.$user.userId) ? 'active' : ''"
            >👍</i>
            <!-- 显示点赞个数-->
            {{ item.favour.length || 0 }}
            <!-- 展示这个评论下的回复 -->
            <i
                class="el-icon-chat-dot-round"
                @click="isShowSecReply(item._id)"
            >回复</i>
            <i
                class="el-icon-delete"
                @click="deleteComment(item, index)"
                v-show="this.$user.userId === item.userId"
            >
              删除</i>
          </div>
          <!-- 回复一级评论 -->
          <div class="reply-comment" v-show="isShowSec === item._id">
            <el-input
                :placeholder="placeholderText"
                class="input"
                v-model="replyContext"
                :maxlength="contentLength"
                show-word-limit
            ></el-input>
            <el-button
                type="info"
                size="mini"
                class="reply-button"
                @click="replyTheComment(item._id, item.username)"
            >回复</el-button>
          </div>
          <!-- 次级评论 -->
          <div
              class="second-comment"
              v-for="(reply, index) in item.replyInfo"
              :key="reply._id + '' + index"
          >
            <!-- 次级评论头像,该用户没有头像则显示默认头像 -->
            <el-avatar :size="40" :src="reply.avatarUrl"></el-avatar>
            <div class="content">
              <!-- 次级评论用户昵称 -->
              <h3>{{ reply.username }}</h3>
              <!-- 次级评论评论时间 -->
              <span style="margin-right:10px ">{{ reply.date }}</span>
              <span class="to_reply">{{ reply.username }}</span>
              回复
              <span class="to_reply">{{ reply.replyName }}</span>:
              <p>{{ reply.content }}</p>
              <!-- 次级评论评论点赞 -->
              <div class="comment-right">
                <i
                    class="el-icon-trophy"
                    @click="giveALike(reply, index)"
                    :class="reply.favour.includes(this.$user.userId) ? 'active' : ''"
                >👍</i>
                <!--处理favourList为空的问题-->
                {{ reply.favour == '[]' ? reply.favour.length - 2 :  reply.favour.length}}
                <i
                    class="el-icon-chat-dot-round"
                    @click="isShowThirdReply(item._id, index)"
                >回复</i>
                <i
                    class="el-icon-delete"
                    @click="deleteComment(reply, index)"
                    v-show="this.$user.userId === reply.userId"
                >删除</i>
              </div>
              <!--回复二级评论 -->
              <div class="reply-comment" v-show="(isShowRoot === reply.rootId) && (isShowThird === index)">
                <!-- v-model.trim用于删去首尾的空格 -->
                <el-input
                    :placeholder="placeholderText"
                    class="input"
                    v-model="replyContext"
                    :maxlength="contentLength"
                    show-word-limit
                ></el-input>
                <el-button
                    type="info"
                    size="mini"
                    class="reply-button"
                    @click="replyTheComment(item._id, reply.username)"
                >回复</el-button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- 暂无评论的空状态 -->
    <el-empty :description="emptyText" v-show="comments.length === 0"></el-empty>
  </div>
  <div id="comments">
    <div id="valine" class="comment v" data-class="v">
      <div class="vpanel">
        <div class="vwrap">
          <div class="vheader item3" style="display: flex;justify-content: space-between">
              <div style="display:inline-flex;justify-content: center;align-items: center">
                <el-avatar :src="this.$user.avatarUrl? this.$user.avatarUrl: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'" :size="40" style="margin-right: 15px"></el-avatar>
                <span>{{this.$user.userName}}</span>
              </div>
            <input class="vnick vinput" value="发表您的评论" type="button" @click="tryToReply">
          </div>
          <!--登陆后展示-->
          <div v-show="this.alreadyLogin">
          <div  class="vedit">
        <!--点击输入框的时候默认收起回复框   -->
            <textarea :maxlength="contentLength + 100"  @focus="isShowSecReply(undefined)" v-model="context" id="veditor" class="veditor vinput" placeholder="Your comment (no more than 250 words)" style="height: 138px;">
            </textarea>
            <div style="text-align:right">
              <span id="span_Font_Length" style="font-size: 18px;">{{this.context.length}}</span>
              <span style="font-size: 14px;">/</span>
              <span style="font-size: 14px;">250</span>
            </div>
          </div>
          <div class="vrow">
            <div class="vcol vcol-30">
                <svg class="markdown" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true">
                  <path fill-rule="evenodd" d="M14.85 3H1.15C.52 3 0 3.52 0 4.15v7.69C0 12.48.52 13 1.15 13h13.69c.64 0 1.15-.52 1.15-1.15v-7.7C16 3.52 15.48 3 14.85 3zM9 11H7V8L5.5 9.92 4 8v3H2V5h2l1.5 2L7 5h2v6zm2.99.5L9.5 8H11V5h2v3h1.5l-2.51 3.5z">
                  </path>
                </svg>
            </div>
            <div class="vcol vcol-70 text-right">
              <button type="button" title="Cmd|Ctrl+Enter" @click="submitComment" class="vsubmit vbtn">Submit</button>
            </div>
          </div>
          </div>
        </div>
      </div>
    </div>
  </div>
<!--  <input type="button" @click="getCommentList">-->
</template>
<script>
// import { ElMessage, ElMessageBox } from 'element-plus'
import axios from "axios";
import WordCloud from "@/components/charts/wordCloud";
export default {
  components: {WordCloud},
  props: {
    classroomName: String,
    emptyText: {
      // 评论为空的时候显示的文字
      type: String,
      default: "期待你的评论！"
    },
    buttonText: {
      // 下方评论按钮文字
      type: String,
      default: "评论"
    },
    contentLength: {
      // 评论长度
      type: Number,
      default: 150
    },
    placeholderText: {
      // 默认显示文字
      type: String,
      default: "请输入最多150字的评论..."
    }
  },
  data() {
    return {
      update: false,
      wordsData:[],
      inputAvatarUrl: '',
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
      // 其实应该从外参数传入，先放着
      alreadyLogin: false,
      comments: [
      ], // 获取得到的评论
      context: "", // 评论内容
      replyContext: "", //一级评论回复
      isShowSec: "", //是否显示次级回复框
      isClickId: "", //记录点击回复的评论id

      isShowThird: "", //是否显示回复二级评论的回复框
      isClickIndex: "", // 记录点击回复的二级评论的index
      isShowRoot: "",
      isClickRoot: "",
      firstIdx: 1,
      secIdx: 1,
      avatarUrl:
          "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
    };
  },
  created() {
    // 获取评论数据
    this.getCommentList();
    this.getCommentCloudData();
  },
  methods: {
    getCommentCloudData(){
      axios.get('http://127.0.0.1:8000/getCommentCloudByCLassroom',
          {
            params:{
              classroom: this.classroomName,
            }
          }).then(res=>{
        // console.log(res);
        let tmp = [];
        for (let i in res.data){
          let obj = {
            name: i,
            value : res.data[i],
          }
          tmp.push(obj);
        }
        this.wordsData = tmp;
      }).catch(err=>{
        console.log("获取数据失败" + err);
      });
    },
    TextareaFontLength() {
      let strTeatArea = this.context.length;
      $("[id$='span_Font_Length']").text(strTeatArea);
    },
      tryToReply(){
        if(this.$user.userName === ''){
          this.$message.warning('您还未登陆！');
          return;
        } else {
          this.alreadyLogin = true;
        }
      },
      replyTheComment(rootId, replyName){
        if(this.replyContext === ''){
          this.$message.warning("回复内容不能为空哦！");
          return;
        }
        let tmp = {
          rootId: rootId,
          replyName: replyName, // 回复哪个用户
          date: this.dateFormat(),
          username: this.$user.userName,
          userId: this.$user.userId,
          avatarUrl: this.$user.avatarUrl,
          content: this.replyContext,
          favour: '[]',
        };
        console.log(tmp);
        axios.get('http://127.0.0.1/getSubComments',
            {
              params:{
                id: rootId,
              }
            }).then(res=>{
          console.log("divide")
          let reply = res.data;
          reply.replyList.push(tmp);
          console.log("divide")
          reply = JSON.stringify(reply);
          // console.log(reply);
          axios.get('http://127.0.0.1/setSubComments',
              {
                params: {
                  replyInfo: reply,
                  id: rootId
                }
              }).then(res=>{
            console.log(res);
            // Clear
            this.isClickId = this.isShowSec = "";
            this.isShowThird = this.isClickIndex = this.isClickRoot = this.isShowRoot = "";
            this.replyContext = '';
            this.getCommentList();
          }).catch(err=>{
            console.log("添加数据失败" + err);
          });
        }).catch(err=>{
          console.log("添加数据失败" + err);
        });
      },
      // 获取所有评论
      getCommentList(){
        axios.get('http://127.0.0.1/classroomComments',
            {
          params:{
            教室名: this.classroomName,
          }
        }).then(res=>{
          // console.log(res);
          this.comments = [];
          let tmp = {};
          let data = res.data;
          for(let i = 0; i < data.length; ++ i){
            tmp ={
              _id: data[i]._id,
              date: data[i].date, //创建日期
              username: data[i].username, //评论人
              userId: data[i].userId,
              avatarUrl: data[i].avatarUrl,
              favour: eval(' (' + data[i].favour + ')'), //点赞的用户id
              content: data[i].content, //评论内容
              replyInfo: eval(' (' + data[i].replyInfo + ')').replyList
            }
            this.comments.push(tmp);
          }
          this.getCommentCloudData();
        }).catch(err=>{
          console.log("获取数据失败" + err);
        });
      },
      //添加根评论
      addComment(){
        let date = this.dateFormat();
        axios.get('http://127.0.0.1/addComments',
            {
              params:{
                classroomName: this.classroomName,
                name: this.$user.userName,
                userId: this.$user.userId,
                avatarUrl: this.$user.avatarUrl,
                favour: '[]',
                date: date,
                content: this.context,
                replyInfo: JSON.stringify({replyList:[]}) // 留到有回复的时候进行格式处理好了
              }
            }).then(res=>{
          console.log(res);
          this.context = '';
          this.getCommentList(); // 刷新当前的comments
        }).catch(err=>{
          console.log("添加数据失败" + err);
        });

      },
      // 点击submit按钮后，创建用户和提交评论的集成
      submitComment() {
        if (!this.context) {
          this.$message.warning("评论或留言不能为空哦！");
          return;
        }
        this.addComment();
      },
      // 时间格式化
      dateFormat () {
        var date = new Date()
        var year = date.getFullYear()
        var month = date.getMonth() + 1 < 10 ? '0' + (date.getMonth() + 1) : date.getMonth() + 1
        var day = date.getDate() < 10 ? '0' + date.getDate() : date.getDate()
        var hours = date.getHours() < 10 ? '0' + date.getHours() : date.getHours()
        var minutes = date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes()
        var seconds = date.getSeconds() < 10 ? '0' + date.getSeconds() : date.getSeconds()
        let week = date.getDay() // 星期
        let weekArr = [ '星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六' ]
        // 拼接 时间格式处理
        return year + '年' + month + '月' + day + '日 ' + hours + ':' + minutes + ':' + seconds + ' ' + weekArr[week]
},
      dealWithAvatar(e) {
      // const maxSize = 2 * 1024 * 1024;
      const file = Array.prototype.slice.call(e.target.files)[0];
      console.log(file);
},
    // 评论点赞
  giveALike(item, index) {
  if(this.$user.userName === ''){
    this.$message.warning("没有登陆不能点赞哦～");
    return;
  }
// 不允许同一个人重复点赞
if (item.favour?.includes(this.$user.userId)) {
  this.$message.info("您已经点过赞啦！");
  return;
}
//判断是给一级评论点赞还是二级评论，只有二级评论会有replyName
if (item.replyName) {
  // 给二级评论点赞，向后台提交数据
  axios.get('http://127.0.0.1/getSubComments',
      {
        params:{
          id: item.rootId,
        }
      }).then(res=>{
    let reply = res.data;
    let favourList = eval(reply.replyList[index].favour);
    favourList.push(this.$user.userId);
    reply.replyList[index].favour = favourList;
    reply = JSON.stringify(reply);
    // console.log(reply);
    axios.get('http://127.0.0.1/setSubComments',
        {
          params: {
            replyInfo: reply,
            id: item.rootId
          }
        }).then(res=>{
      console.log(res);
      this.getCommentList(); // 刷新
    }).catch(err=>{
      console.log("添加数据失败" + err);
    });
  }).catch(err=>{
    console.log("添加数据失败" + err);
  });} else {
  // 一级评论点赞，向后台提交数据
  let favourList = item.favour;
  favourList.push(this.$user.userId);
  favourList = JSON.stringify(favourList);
  axios.get('http://127.0.0.1/updateFavour',
      {
        params:{
          favour: favourList,
          id: item._id,
        }
      }).then(res=>{
    console.log(res);
    this.getCommentList(); // 刷新当前的comments
  }).catch(err=>{
    console.log("添加数据失败" + err);
  });
}
},

  isShowSecReply(id) {
      if(this.$user.userName === ''){
        this.$message.warning('您还未登陆！');
        return;
      }
      this.isShowThird = this.isClickIndex = this.isClickRoot = this.isShowRoot = "";
      if (id) {
        this.isShowSec = id;
        // 如果点了一次，那么就复原
        if (this.isClickId === this.isShowSec) {
          this.isShowSec = "";
        } else {
          this.isShowSec = id;
        }
        this.isClickId = this.isShowSec;
      }
      else {
        this.isShowSec = this.isClickId = "";
      }
  },
  isShowThirdReply(rootId, index){
    if(this.$user.userName === ''){
      this.$message.warning('您还未登陆');
      return;
    }
        this.isShowSec = this.isClickId = "";
        if(rootId) {
          this.isShowThird = index;
          this.isShowRoot = rootId;
          if((this.isClickIndex === this.isShowThird) && (this.isClickRoot === this.isShowRoot) ){
            this.isShowThird = "";
            this.isShowRoot = "";
          } else {
            this.isShowThird = index;
            this.isShowRoot = rootId;
          }
          this.isClickRoot = this.isShowRoot;
          this.isClickIndex = this.isShowThird;
    } else {
          this.isShowThird = this.isClickIndex = this.isClickRoot = this.isShowRoot = "";
        }
  },
    // 如果这条是你的，可以删除，这就需要设置密码了
  deleteComment(item, index) {
    if (item.rootId) {
      // 删除二级评论，提交请求到后端
      axios.get('http://127.0.0.1/getSubComments',
          {
            params:{
              id: item.rootId,
            }
          }).then(res=>{
        let reply = res.data;
        reply.replyList.splice(index, 1);
        reply = JSON.stringify(reply);
        console.log(reply);
        axios.get('http://127.0.0.1/setSubComments',
            {
              params: {
                replyInfo: reply,
                id: item.rootId
              }
            }).then(res=>{
          console.log(res);
          this.getCommentList(); // 刷新
        }).catch(err=>{
          console.log("添加数据失败" + err);
        });
      }).catch(err=>{
        console.log("添加数据失败" + err);
      });
    } else {
      // 删除一级评论，提交请求到后端
      axios.get('http://127.0.0.1/deleteComment',
          {
            params:{
              id: item._id,
            }
          }).then(res=>{
        console.log(res);
        this.getCommentList();
      }).catch(err=>{
        console.log("获取数据失败" + err);
      });
    }
    },
    toArray(favour){
      return eval(' (' + favour + ')');
    }
} // methods

};
</script>

<style lang="less" scoped>
.grid-container {
  display: grid;
  grid-template-columns: auto auto auto auto;
  grid-gap: 10px;
  padding: 20px;
}

.chosen {
  border: 1px solid blue;
}
.comment {
  min-height: 26vh;
  border-radius: 5px;
  margin-top: 2px;
  .active {
    color: rgb(202, 4, 4);
  }
  .comment-header {
    position: relative;
    height: 60px;
    padding: 10px 5px;
    display: flex;
    align-items: center;

    .input {
      margin-left: 10px;
      margin-right: 20px;
      flex: 1;
      /deep/.el-input__inner:focus {
        border-color: #dcdfe6;
      }
    }
  }

  .comment-body {
    min-height: 70px;
    padding: 10px 20px;
    font-size: 14px;
    .first-comment {
      display: flex;
      .input {
        /deep/.el-input__inner:focus {
          border-color: #dcdfe6;
        }
      }
      i {
        margin-right: 5px;
        margin-left: 1vw;
        cursor: pointer;

        &:nth-child(3) {
          color: rgb(202, 4, 4);
        }
      }

      .content {
        margin-left: 10px;
        position: relative;
        flex: 1;

        & > span {
          font-size: 12px;
          color: rgb(130, 129, 129);
        }

        .comment-right {
          position: absolute;
          right: 0;
          top: 0;
        }

        .reply-comment {
          height: 60px;
          display: flex;
          align-items: center;

          .reply-button {
            margin-left: 20px;
            height: 35px;
          }
        }

        .second-comment {
          display: flex;
          padding: 10px 0 10px 5px;
          border-radius: 20px;
          background: #ffffff;
          .to_reply {
            color: rgb(126, 127, 128);
          }
        }
      }
    }
  }
}
</style>
