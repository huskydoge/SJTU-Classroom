import mainPage from "@/components/classRoom/mainPage"
// import everyClassInfoPage from "@/components/everyClassInfoPage";
import { createRouter, createWebHashHistory } from 'vue-router'
import chenRuiQiu from "@/components/building/chenRuiQiu";
import xiaYuan from "@/components/building/xiaYuan";
import zhongYuan from "@/components/building/zhongYuan";
import shangYuan from "@/components/building/shangYuan";
import dongXia from "@/components/building/dongXia";
import dongZhong from "@/components/building/dongZhong";
import dongShang from "@/components/building/dongShang";
import introPart from "@/components/introPart";
import searchClass from "@/components/searchPage/searchClass";
const routes = [

    //一级路由
    {
        path: '/',
        name: 'root',
        redirect: '/home/dynamic'
        //路由嵌套
    },
    {
        path: '/search',
        name: 'search',
        component: searchClass
        //路由嵌套
    },
    {
        path: '/home',
        name: 'home',
        //路由嵌套
        children:[
            {
                path: 'dynamic',
                name: 'dynamic',
                component: mainPage,
                //路由嵌套
            },
            {
                path: 'intro',
                name: 'intro',
                component: introPart,
            },
            {
                path: 'dongshang',
                name: 'dongshang',
                component: dongShang,
            },
            {
                path: '/home/dongzhong',
                name: 'dongzhong',
                component: dongZhong,
            },
            {
                path: '/home/dongxia',
                name: 'dongxia',
                component: dongXia,
            },
            {
                path: '/home/shangyuan',
                name: 'shangyuan',
                component: shangYuan,
            },
            {
                path: '/home/zhongyuan',
                name: 'zhongyuan',
                component: zhongYuan,
            },
            {
                path: '/home/xiayuan',
                name: 'xiayuan',
                component: xiaYuan,
            },
            {
                path: '/home/chenruiqiu',
                name: 'chenruiqiu',
                component: chenRuiQiu,
            },
        ]
    },



]

const router = createRouter({
    mode: 'history',
    history: createWebHashHistory(),
    routes
})

export default router;
