let db = require('../db/index');
// eslint-disable-next-line no-unused-vars
let dynamicInfo = require('../db/dynamic');

// 得到所有教室信息
exports.getAllClassroom =  (req, res) => {
    const sql = "select * from ClassroomInfo";
    db.query(sql,(err, data) => {
        if(err) {
            return res.send('错误：' + err.message)
        }
        res.send(data)
    })
}
// 得到所有教室名
exports.getAllClassroomName =  (req, res) => {
    const sql = "select 教室名 from classroomCharacter";
    db.query(sql,(err, data) => {
        if(err) {
            return res.send('错误：' + err.message)
        }
        res.send(data)
    })
}

// 按照教室名搜索教室
exports.getInfo = (req, res) => {
    const sql = "select * from ClassroomInfo WHERE 教室名=?";
    db.query(sql,[req.query.教室名],(err, data) => {
        if(err) {
            return res.send('错误：' + err.message)
        }
        res.send(data)
    })
}

// 按照教室名搜索教室，获得教室的特色信息
exports.getCharacter = (req, res) => {
    const sql = "select * from classroomCharacter WHERE 教室名=?";
    db.query(sql,[req.query.教室名],(err, data) => {
        if(err) {
            return res.send('错误：' + err.message)
        }
        res.send(data)
    })
}

// 按照教室名获取评论
exports.getComments = (req, res) => {
    const sql = "select * from classroomComments WHERE 教室名=?";
    db.query(sql,[req.query.教室名],(err, data) => {
        if(err) {
            return res.send('错误：' + err.message)
        }
        res.send(data)
    })
}

// 添加根评论
exports.addComment = (req, res) => {
    const sql = "INSERT INTO classroomComments (教室名, username, userId, avatarUrl, favour, date, content, replyInfo) VALUES(?, ?, ?, ? ,? ,? ,?, ?)"
    db.query(sql, [req.query.classroomName, req.query.name ,  req.query.userId, req.query.avatarUrl, req.query.favour, req.query.date, req.query.content, req.query.replyInfo],(err, data) => {
        if(err) {
            return res.send('错误：' + err.message)
        }
        res.send(data)
    });
}

// 删除根评论
exports.deleteComment = (req, res) => {
    const sql = "DELETE FROM classroomComments WHERE _id = ?";
    db.query(sql,[req.query.id],(err, data) => {
        if(err) {
            return res.send('错误：' + err.message)
        }
        res.send(data)
    });
}

// 更新根评论的赞数组
exports.updateFavour = (req, res) => {
    const sql = "UPDATE classroomComments SET favour = ? WHERE _id = ?"
    db.query(sql, [req.query.favour, req.query.id], (err, data) => {
        if (err) {
            return res.send('错误：' + err.message)
        }
        res.send(data)
    });
}

// 获得子评论
exports.getSubComments = (req, res) => {
    const sql = "Select * from classroomComments WHERE _id = ? ";
    db.query(sql, [req.query.id],(err, data) => {
        if(err) {
            return res.send('错误：' + err.message)
        }
        res.send(data[0].replyInfo);
    });
}

// 更新子评论
exports.setSubComments = (req, res) => {
    const sql = "UPDATE classroomComments SET replyInfo = ? WHERE _id = ?"
    db.query(sql, [req.query.replyInfo, req.query.id],(err, data) => {
        if(err) {
            return res.send('错误：' + err.message)
        }
        res.send(data)
    });
}

// Lost
exports.getAllLost = (req, res) => {
    const sql = "SELECT * from lostItem"
    db.query(sql,(err, data) => {
        if(err) {
            return res.send('错误：' + err.message)
        }
        res.send(data)
    });
}

// Found
exports.getAllFound = (req, res) => {
    const sql = "SELECT * from foundItem"
    db.query(sql,(err, data) => {
        if(err) {
            return res.send('错误：' + err.message)
        }
        res.send(data)
    });
}

// 按照教室获取Found
exports.getClassroomFound = (req, res) => {
    const sql = "SELECT * from founditem WHERE classroomname = ?"
    db.query(sql,[req.query.classroom],(err, data) => {
        if(err) {
            return res.send('错误：' + err.message)
        }
        res.send(data)
    });
}

// 按照教室获取Lost
exports.getClassroomLost = (req, res) => {
    const sql = "SELECT * from lostItem WHERE classroomname = ?"
    db.query(sql,[req.query.classroom],(err, data) => {
        if(err) {
            return res.send('错误：' + err.message)
        }
        res.send(data)
    });
}

// 提交物品信息
exports.submitItemInfo = (req, res) => {
    let str = '';
    if(req.query.type === 'Lost'){
        str = 'INSERT INTO lostItem (classroomname, lostitem, context, username, avatarurl, date) VALUES(?, ?, ?, ?, ?, ?) ';
    } else {
        // eslint-disable-next-line no-unused-vars
        str = 'INSERT INTO foundItem (classroomname, lostitem, context, username, avatarurl, date) VALUES(?, ?, ?, ?, ?, ?)';
    }
    let sql = str;
    db.query(sql,[req.query.classroomname, req.query.lostitem, req.query.context, req.query.username, req.query.avatarurl, req.query.date ],(err, data) => {
        if(err) {
            return res.send('错误：' + err.message)
        }
        res.send(data)
    });
}

// 获取VR图
exports.getGraph = (req, res) => {
    const sql = "SELECT * from vrPics WHERE classroom = ?"
    db.query(sql,[req.query.classroom], (err, data) => {
        if(err) {
            return res.send('错误：' + err.message)
        }
        res.send(data)
    });
}

// 得到某个教室的评分
exports.getRate = (req, res) => {
    const sql = "SELECT * from classroomRate  WHERE classroom = ?"
    db.query(sql,[req.body.classroom], (err, data) => {
        if(err) {
            return res.send('错误：' + err.message)
        }
        res.send(data)
    });
}

// 更新某个教室的评分
exports.postRate = (req, res) => {
    const sql = "UPDATE classroomRate SET " + req.body.rate + "=" + "'" + req.body.list + "'" + " WHERE classroom = ?"
    db.query(sql,[req.body.classroom], (err, data) => {
        if(err) {
            return res.send('错误：' + err.message)
        }
        res.send(data)
    });
}
