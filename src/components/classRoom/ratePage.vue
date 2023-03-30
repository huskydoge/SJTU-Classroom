<template>
<!--  TODO 颜色可以改一改-->
  <div>
  <div style="display:flex;justify-items: center;align-items:center;flex-direction: column">
    <el-avatar style="width: 4rem;height: 4rem" :src=this.handleAvatar(this.$user.avatarUrl)></el-avatar>
    <p  v-if="this.flag"
       style="margin: 0; font-size: 14px; color: var(--el-color-info)"
    >
      您上次的打分是
    </p>
    <p  v-if="!this.flag"
        style="margin: 0; font-size: 14px; color: var(--el-color-info)"
    >
      您还没评分哦 😊
    </p>
    <el-rate
        size="large"
        v-model="value"
        text-color="#ff9900"
        show-score
        score-template="{value} 分"
    />
    <el-tooltip content="点击评分" >
    <p @click="this.confirmRate"
        style="margin: 0; font-size: 14px; color: var(--el-color-info)"
    >
      {{this.texts[this.value - 1]}}
    </p>
    </el-tooltip>
  </div>

  <div id="pieChart" style="margin:0 auto;width: 800px;height: 600px"></div>
  </div>
</template>
<script>
import * as echarts from 'echarts';
import axios from "axios";
export default {
  name: "ratePage",
  props:{
    classname: String,
  },
  data(){
    return{
      user: '',
      flag: 0,
      rateAffine: ['zero', 'one', 'two', 'three', 'four', 'five'],
      classRateData: [
        [
          69
        ],
        [
          70
        ],
        [
          59
        ],
        [
          2,
          58
        ],
        [
          1,
          56,
          57
        ]
      ],
      value: 1,
      texts:['别来！','凑合凑合','不错的教室～','下课就冲！','直接住这儿！'],
      starTexts:['One Star', 'Two Star', 'Three Star', 'Four Star', 'Five Star'],
    }
  },
  methods:{
    confirmRate(){
      this.postData();
    },
    handleAvatar(){
      if(this.$user.avatarUrl === ''){
        return 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png';
      } else {
        return this.$user.avatarUrl;
      }
    },
    initChart(){
      var chartDom = document.getElementById('pieChart');
      var myChart = echarts.init(chartDom);
      var option;
      var starTexts = this.starTexts;
      var classRateData = this.classRateData;
      option = {
        tooltip: {
          trigger: 'item'
        },
        legend: {
          top: '5%',
          left: 'center'
        },
        series: [
          {
            name: 'Access From',
            type: 'pie',
            radius: ['40%', '70%'],
            avoidLabelOverlap: false,
            itemStyle: {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: '40',
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            data: [
              { value: classRateData[4].length, name: starTexts[4] },
              { value: classRateData[3].length, name: starTexts[3] },
              { value: classRateData[2].length, name: starTexts[2] },
              { value: classRateData[1].length, name: starTexts[1] },
              { value: classRateData[0].length, name: starTexts[0] }
            ]
          }
        ]
      };
      option && myChart.setOption(option);

    },
    fetchData(){
      function handleNull(arr){
        if(arr == null){
          return [];
        } else {
          return arr;
        }
      }
      axios.post('http://127.0.0.1/getRate',
          {
            classroom: this.classname,
          }).then(res => {
              let tmp = [];
              tmp.push(handleNull(eval(res.data[0]['one'])));
              tmp.push(handleNull(eval(res.data[0]['two'])));
              tmp.push(handleNull(eval(res.data[0]['three'])));
              tmp.push(handleNull(eval(res.data[0]['four'])));
              tmp.push(handleNull(eval(res.data[0]['five'])));
              this.classRateData = tmp;
              this.checkRated();
              if(this.flag !== 0){
                this.value = this.flag;
              } else {
                this.value = 3; // 默认值
              }
          }
      ).catch(err => {
        console.log("获取数据失败" + err);
      });
    },
    // 做到禁止刷分
    postData(){
      if(this.$user.userName == ''){
        this.$message.warning('您还未登陆哦！');
        return;
      }
      // 没有打过分
      if(this.flag === 0){
        // console.log(newArray);
        let newArray = this.classRateData[this.value - 1];
        newArray.push(this.$user.userId);
        axios.post('http://127.0.0.1/postRate',
            {
              rate: this.rateAffine[this.value],
              classroom: this.classname,
              list: '[' + String(newArray) + ']',
            }).then(res => {
              console.log(res);
              this.flag = this.value;
              this.$message.success('评分成功！');
              this.fetchData();
            }
        ).catch(err => {
          console.log("获取数据失败" + err);
        });
      } else {
        let deleteArray = this.classRateData[this.flag - 1];
        for(let j = 0; j < deleteArray.length; ++ j){
          if(deleteArray[j] === this.$user.userId){
            deleteArray.splice(j, 1); //删除该元素
            this.classRateData[this.flag - 1] = deleteArray;
          }
        }
        //删除到数据库
        axios.post('http://127.0.0.1/postRate',
            {
              rate: this.rateAffine[this.flag],
              classroom: this.classname,
              list: '[' + String(deleteArray) + ']',
            }).then(res => {
              // 删除完了
          let newArray = this.classRateData[this.value - 1];
          newArray.push(this.$user.userId);
          axios.post('http://127.0.0.1/postRate',
              {
                rate: this.rateAffine[this.value],
                classroom: this.classname,
                list: '[' + String(newArray) + ']',
              }).then(res => {
                console.log(res);
                this.flag = this.value;
                this.fetchData();
                this.$message.success('更新评分成功！')
              }
          ).catch(err => {
            console.log("获取数据失败" + err);
          });
              console.log(res);
            }
        ).catch(err => {
          console.log("获取数据失败" + err);
        });
      }
    },
    checkRated(){
      for(let i = 0; i < 5; ++ i){
        if(this.classRateData[i].includes(this.$user.userId)){
          this.flag =  i + 1; // 返回1，2，3，4，5
          return;
        }
      }
      this.flag = 0;
      return;
    }
  },
  created(){
    this.fetchData();
  },
  mounted() {
    this.user = this.$user.userName;
    this.initChart();
  },
  watch:{
    classRateData(){
      this.initChart();
    },
    user(){
    }
  }
}
</script>

<style scoped>

</style>