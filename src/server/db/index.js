let mysql = require('mysql')

let db = mysql.createPool({
    host: '127.0.0.1',     //数据库IP地址
    user: 'root',          //数据库登录账号
    password: 'Hbh001098hbh',      //数据库登录密码
    database: 'buildingInfo'       //要操作的数据库
})

module.exports = db
