// 先导入express，它是一个node框架，能简化代码
const express = require('express')
const app = express()

// 导入bodyParser插件，它帮助我们获取前端post请求传过来的参数
const bodyParser = require('body-parser')
app.use(bodyParser.urlencoded({ extended:false }))

//导入上传文件中间件，能帮助我们实现接收文件的接口
const multer  = require('multer')
//接收到的文件放uploads文件夹
const upload = multer({ dest: 'uploads/' })
//使得让外部通过链接可以访问这个文件夹里文件（ 地址 + 端口 / 文件名 ）便可访问
app.use(express.static('uploads'))
//使用接收文件基本接口模板，可到官网查看更详细的
/* app.post('/profile', uploads.single('avatar'), function (req, res, next) {
  // req.file is the `avatar` file
  // req.body will hold the text fields, if there were any
}) */

//定义服务器端口
const port = 8848

// 导入knex插件，他能帮助我们连接MySQL数据库
const knex = require('knex')({
    client: 'mysql',
    //填入数据库的地址、账号、密码、库名
    connection: {
        host     : 'localhost',
        user     : 'root',
        password : 'Hbh001098hbh',
        database : 'buildingInfo'
    }
})

//下面这个能解决跨域问题
app.all('*', function(req, res, next) {
    console.log(req.method);
    res.header("Access-Control-Allow-Origin", "*");
    res.header('Access-Control-Allow-Headers', 'Content-type');
    res.header("Access-Control-Allow-Methods", "PUT,POST,GET,DELETE,OPTIONS,PATCH");
    res.header('Access-Control-Max-Age',1728000);//预请求缓存20天
    next();
});

//使得express后端能接收前端发送回来的json格式数据
app.use(express.json());

//实现新增（上传图片）接口，post请求，参数为 avatar ！！！
app.post('/avatar/add',upload.single('avatar'),(req,response)=>{
    // req.file得到前端发送回来的文件信息，req.body的到文件文本信息
    // eslint-disable-next-line no-unused-vars
    const {file,body} = req
    //判断是否发送的是空文件回来
    if( file == undefined){
        response.send({code:400,msg:'新增失败,参数缺失'})
    }else{
        //利用kenx在数据库完成新增操作，保存文件名字段
        //相当于 insert into comic （icon）values（file.filename）
        // eslint-disable-next-line no-unused-vars
        knex('Users').insert({username:'asdasda',avatar:file.filename}).then(res=>{
            response.send({code:200,msg:'新增成功',filename:file.filename});
        })
    }
})

app.post('/imgStorage/add',upload.single('avatar'),(req,response)=>{
    // req.file得到前端发送回来的文件信息，req.body的到文件文本信息
    // eslint-disable-next-line no-unused-vars
    const {file,body} = req
    //判断是否发送的是空文件回来
    if( file == undefined){
        response.send({code:400,msg:'新增失败,参数缺失'})
    }else{
        //利用kenx在数据库完成新增操作，保存文件名字段
        //相当于 insert into comic （icon）values（file.filename）
        // eslint-disable-next-line no-unused-vars
        knex('ImgStorage').insert({avatar:file.filename}).then(res=>{
            response.send({code:200,msg:'新增成功',filename:file.filename});
        })
    }
})

//实现查询接口，就是要返回图片给前端显示
app.get('/avatar',(req,response)=>{
    // 相当于 select * from comic
    knex('Users').where('username', req.body.name).select()
        .then(res=>{
            if(res.length === 0){
                response.send({code:200,msg:'暂无数据'})
            }else{
                response.send({code:200,msg:'查询成功',data:res})
            }
        })
})

//监听接口
app.listen(port,()=> console.log('图片上传服务启动成功！'))
