import json
import pymysql


# 1. 连接数据库，
def getAllComments():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='Hbh001098hbh',
        db='buildingInfo',
        charset='utf8',
    )
    # ****python, 必须有一个游标对象， 用来给数据库发送sql语句， 并执行的.
    # 2. 创建游标对象，
    cur = conn.cursor()

    sqli = "select * from classroomComments;"
    cur.execute(sqli)  # 默认不返回查询结果集， 返回数据记录数。
    results = cur.fetchall()
    allComments = []
    allString = ''
    for row in results:
        allComments.append(row[6])
        childComments = json.loads(row[7])['replyList']
        for item in childComments:
            allComments.append(item['content'])
        print(len(allComments))

    for comment in allComments:
        allString += comment

    # 4. 关闭游标
    cur.close()
    # 5. 关闭连接
    conn.close()
    return allString


def getCommentsByClassRoom(classroom):
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='Hbh001098hbh',
        db='buildingInfo',
        charset='utf8',
    )
    # ****python, 必须有一个游标对象， 用来给数据库发送sql语句， 并执行的.
    # 2. 创建游标对象，
    cur = conn.cursor()

    sqli = "select * from classroomComments where 教室名 = '" + classroom + "'"
    cur.execute(sqli)  # 默认不返回查询结果集， 返回数据记录数。
    results = cur.fetchall()
    allComments = []
    allString = ''
    for row in results:
        allComments.append(row[6])
        childComments = json.loads(row[7])['replyList']
        for item in childComments:
            allComments.append(item['content'])
        print(allComments)

    for comment in allComments:
        allString += comment

    # 4. 关闭游标
    cur.close()
    # 5. 关闭连接
    conn.close()
    return allString


