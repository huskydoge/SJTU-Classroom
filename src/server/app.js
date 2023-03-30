let express = require('express')
let app = express()
let cors = require('cors')
let bodyParser = require('body-parser')
let router = require('./router')

app.use(bodyParser.json());  //配置解析，用于解析json和urlencoded格式的数据
app.use(bodyParser.urlencoded({extended: true})); //设置为true用于接受post请求
app.use(cors())              //配置跨域
app.use(router)              //配置路由

app.listen(80, () => {
    console.log('主服务器启动成功！');
})