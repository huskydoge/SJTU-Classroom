<template>
  <div><Calendar
      :months="months"
      :begin="begin"
      :end="end"
      :value="value"
      @next="next"
      @prev="prev"
      :events="events"
      :lunar="lunar"
      clean
      @select="select"
      ref="calendar"
      @selectMonth="selectMonth"
      @selectYear="selectYear"
      style="margin-bottom: 30px;padding-bottom: 30px"
  />
    <button @click="setToday">返回今日</button>
  </div>
</template>

<script>
import Calendar from 'mpvue-calendar'

import lunar from 'mpvue-calendar/dist/lunar'
// import {ref} from'vue'
export default {
  name:'CalendarBox',
  data () {
    return {
      lunar:lunar,
      months: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
      disabledarr: ['2018-6-27','2018-6-25'],
      value: '2022-12-20',
      begin: '2019-1-1',
      end: '2023-1-1',
      events: {'2018-6-7':'今日备注', '2018-6-8':'一条很长的明日备注'},
    }
  },
  components: {
    Calendar
  },
  methods: {
    selectMonth(month,year){
      this.$refs.month = month;
      console.log(year,month)
    },
    prev(month){
      console.log(month)
    },
    next(month){
      console.log(month)
    },
    selectYear(year){
      console.log(year)
    },
    // eslint-disable-next-line no-unused-vars
    setToday(val,val1,val2) {
      this.$refs.calendar.setToday();
      console.log(this.$refs.calendar)
    },
    select(val, val2) {
      console.log(val)
      console.log(val2)
    }
  }
}
</script>