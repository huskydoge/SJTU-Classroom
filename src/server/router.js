let express = require('express')
let router = express.Router()
let classroom = require('./API/classroom')
let user = require('./API/user')
let building = require('./API/building')
// TODO 优化命名
// 通过数据库拿数据
router.get('/getAllClassroom', classroom.getAllClassroom)
router.get('/classroomInfo', classroom.getInfo)
router.get('/classroomCharacter', classroom.getCharacter)

// 获取某个教室的评论区
router.get('/classroomComments', classroom.getComments)

// 注册账户
router.get('/addUser', user.addUser)

// 获得密码
router.post('/getPassword', user.getPassword)

// 找用户
router.get('/findUser', user.findUser)

// 获得用户头像和Id
router.post('/getAvatarAndUserId',user.getAvatarAndUserId)

// 注册
router.post('/signUp', user.signUp)

// 登陆
router.post('/signIn',user.signIn)

// 添加评论
router.get('/addComments', classroom.addComment)

// 删除评论
router.get('/deleteComment', classroom.deleteComment)

// 找子评论
router.get('/getSubComments', classroom.getSubComments)

// 更新子评论
router.get('/setSubComments', classroom.setSubComments)

// 更新根评论的赞数
router.get('/updateFavour',classroom.updateFavour)

// 获取所有Lost
router.get('/getAllLost', classroom.getAllLost)

// 获取所有Found
router.get('/getAllFound', classroom.getAllFound)

// 按照教室获取Lost
router.get('/getClassroomLost', classroom.getClassroomLost)

// 按照教室获取Found
router.get('/getClassroomFound', classroom.getClassroomFound)

// 提交一条失物启示
router.get('/submitItemInfo', classroom.submitItemInfo)

// 获取全景图
router.get('/getGraph',classroom.getGraph)

// 获得评分
router.post('/getRate', classroom.getRate)

// 更新评分
router.post('/postRate', classroom.postRate)

// 获取某个楼栋的数据
router.post('/getBuildingLayer', building.getBuildingLayer)

router.post('/getDongzhongBuildingLayer', building.getDongzhongBuildingLayer)

// 获取所有教室名
router.get('/getAllClassroomName', classroom.getAllClassroomName)

module.exports = router
