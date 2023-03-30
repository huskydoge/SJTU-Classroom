let db = require('../db/index')

// 添加账户
exports.addUser = (req, res) => {
    const sql = "INSERT Users (username, avatarUrl)\n" +
        " SELECT ?, ? \n" +
        " WHERE NOT EXISTS (SELECT * FROM Users WHERE username=?)";
    db.query(sql, [req.query.name,req.query.avatarUrl, req.query.name],(err, data) => {
        if(err) {
            return res.send('错误：' + err.message)
        }
        res.send(data)
    });
}

// 获得账户密码, 安全性堪忧啊
exports.getPassword = (req, res) => {
    const sql = "SELECT * from Users WHERE username = ?";
    db.query(sql, [req.query.name],(err, data) => {
        if(err) {
            return res.send('错误：' + err.message)
        }
        res.send(data[0])
    });
}

// 查询账户
exports.findUser = (req, res) => {
    const sql_1 = "select * from Users where username = ?";
    db.query(sql_1, [req.query.name],(err, data) => {
        if(err) {
            return res.send('错误：' + err.message)
        }
        res.send(data)
    });
}

// 专门获得用户的头像和id
exports.getAvatarAndUserId = (req, res) => {
    const sql = "select * from Users where username = ?";
    db.query(sql, [req.body.name],(err, data) => {
        if(err) {
            return res.send('错误：' + err.message)
        }
        res.send(data[0])
    });
}

// 创建账户
exports.signUp = (req, res) => {
    const sql = "INSERT INTO Users (username, password, avatarUrl) Values (?, ?, ?)";
    db.query(sql, [req.body.name, req.body.password, req.body.avatarurl],(err, data) => {
        if(err) {
            return res.send('错误：' + err.message)
        }
        res.send(data)
    });
}

// 登陆账户，在后端进行判断
exports.signIn = (req, res) => {
    const sql = "SELECT * FROM Users WHERE username = ?";
    db.query(sql, [req.body.name],(err, data) => {
        if(err) {
            return res.send('错误：' + err.message)
        }
        // 如果返回长度为0，说明没有注册！
        if(data.length === 0){
            data = {status: 2}
        }
        else if(data[0].password === req.body.password){
            data = {status: 1};
        } else {
            data = {status: 0};
        }
        res.send(data)
    });
}