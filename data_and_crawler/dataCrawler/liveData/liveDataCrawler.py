# 每隔30分钟爬取教室的数据。事实上，信息来源的更新速度本身就不是实时的，据观察刷新时间应该在半个小时到一个小时之间。

import requests
import json
import pymysql
import getDynamicCookie
import schedule
import time
import random


def get_aff(url, headers, buildId):
    data = {"buildId": buildId}
    responses = requests.post(url, headers=headers, data=data)
    jdata = json.loads(responses.content)
    for i in jdata['data']['roomList']:
        if 'name' not in i:
            i['name'] = 'None'
        if 'zws' not in i:
            i['zws'] = 'None'
        if 'actualStuNum' not in i:
            i['actualStuNum'] = 'None'
        if 'sensorCo2' not in i:
            i['sensorCo2'] = 'None'
        else:
            i['sensorCo2'] = str(i['sensorCo2']) + 'PPM'
        if 'sensorHum' not in i:
            i['sensorHum'] = 'None'
        else:
            i['sensorHum'] = str(i['sensorHum']) + '%'
        if 'sensorPm25' not in i:
            i['sensorPm25'] = 'None'
        else:
            i['sensorPm25'] = str(i['sensorPm25']) + 'μg'
        if 'sensorTemp' not in i:
            i['sensorTemp'] = 'None'
        else:
            i['sensorTemp'] = str(i['sensorTemp']) + "℃"
        i['zws'] = str(i['zws'])
        i['actualStuNum'] = str(i['actualStuNum'])
    datas = [[i['name'], i['zws'], i['actualStuNum'], i['sensorCo2'],
              i['sensorHum'], i['sensorPm25'], i['sensorTemp']] for i in jdata['data']['roomList']]
    return datas


def crawler():
    Cookie = getDynamicCookie.getCookie()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42',
        # cookie自己换一下
        'Cookie': Cookie,
        'Host': 'ids.sjtu.edu.cn',
        'Origin': 'https://ids.sjtu.edu.cn',
        'Referer': 'https://ids.sjtu.edu.cn/build/goMRealtimeDynamic?param=cd6b63cb06a935de3050b73a4c68c87fe52d1d57b3e35ffff151ec8a27e9de7da12b83afef264445b2ff8e1a7a0f3914'
    }

    datas = []
    datas.extend(get_aff('https://ids.sjtu.edu.cn/classroomUse/findSchoolCourseInfo', headers, 126))
    datas.extend(get_aff('https://ids.sjtu.edu.cn/classroomUse/findSchoolCourseInfo', headers, 128))
    datas.extend(get_aff('https://ids.sjtu.edu.cn/classroomUse/findSchoolCourseInfo', headers, 127))
    datas.extend(get_aff('https://ids.sjtu.edu.cn/classroomUse/findSchoolCourseInfo', headers, 122))
    datas.extend(get_aff('https://ids.sjtu.edu.cn/classroomUse/findSchoolCourseInfo', headers, 564))

    datas.extend(get_aff('https://ids.sjtu.edu.cn/classroomUse/findSchoolCourseInfo', headers, 124))
    datas.extend(get_aff('https://ids.sjtu.edu.cn/classroomUse/findSchoolCourseInfo', headers, 125))
    print(datas)
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='Hbh001098hbh',
        # database需要自己创建，表不需要
        database='buildingInfo',
        charset='utf8mb4',
    )
    # sql = "CREATE TABLE classroomInfo (`教室名` VARCHAR (10) NOT NULL, `座位数` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (10) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;"
    cur = conn.cursor()
    # cur.execute(sql)
    deletesql = 'DELETE FROM classroomInfo'
    cur.execute(deletesql)
    cur.executemany(
        'INSERT INTO classroomInfo (教室名,座位数,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s,%s)',
        datas)
    # 纠正座位数的错误
    seatsSql = 'UPDATE classroomInfo SET 座位数 = (SELECT 座位数 FROM classRoomCharacter WHERE classRoomCharacter.教室名 = classroomInfo.教室名)'
    cur.execute(seatsSql)
    conn.commit()
    # conn.close()


# 每30分钟拉取一次
schedule.every(30).minutes.do(crawler)

while True:
    schedule.run_pending()
    x = random.randint(-3, 3)
    y = random.randint(-3, 3)
    # 在设置范围内移动
    # pyautogui.moveTo(1300 + x, 100 + y)
    time.sleep(2)  # 别设置太小
    print(x)
