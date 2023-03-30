let db = require('../db/index')

exports.getBuildingLayer = (req, res) => {
    let result = [];
    let flag = false;
    for(let i = 1; i < 6; ++ i){
        if(flag){break;}
        let sql = "SELECT * FROM classroomInfo WHERE 教室名 like '" + req.body.building + i + "%" + "'";
        db.query(sql, (err, data) => {
            if (err) {
                return res.send('错误：' + err.message)
            }
            if(data.length !== 0){
                result.push(data);
            } else {
                return res.send(result);
            }
        })
    }
}

exports.getDongzhongBuildingLayer = (req, res) => {
    let result = [];
    let flag = false;
    for(let i = 1; i < 7; ++ i){
        if(flag){break;}
        let sql = "SELECT * FROM classroomInfo WHERE 教室名 like '" + '东中院' + i + "-" + "%" + "'";
        db.query(sql, (err, data) => {
            if (err) {
                return res.send('错误：' + err.message)
            }
            if(data.length !== 0){
                result.push(data);
            } else {
                return res.send(result);
            }
        })
    }
}