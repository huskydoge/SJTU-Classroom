import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/antd.css';
import App from './App.vue'
import router from "@/router";
import Calendar from 'mpvue-calendar'
import animated from 'animate.css'
import vuetyped from 'vue3typed'
const app = createApp(App)
//引入样式
app.config.globalProperties.$user = {
    userId: -1,
    userName: '',
    avatarUrl: '',
}
app.use(vuetyped)
app.use(animated)
app.use(ElementPlus)
app.use(router)
app.use(Antd)
app.use(Calendar)
app.mount('#app')
