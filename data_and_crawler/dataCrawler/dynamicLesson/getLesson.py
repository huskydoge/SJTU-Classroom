# 获得教室的当前课程名，授课教师名，但是网站里没有用上
import requests
import json
import pymysql

def get_aff(url, headers, buildId):
    data = {"buildId": buildId,
            "mobileType": 'mobileFlag',
            "dayinweek": 3
            }
    responses = requests.post(url, headers=headers, data=data)
    jdata = json.loads(responses.content)
    datas = []
    for m in range(len(jdata['data']['floorList'])):
        for i in jdata['data']['floorList'][m]['children']:
            if 'roomCourseList' not in i:
                i['roomCourseList'] = []
            if i['roomCourseList'] != []:
                t = [[k['startSection'], k['endSection']] for k in i['roomCourseList']]
                i['roomCourseList'] = t
        datas.extend(
            [[i['name'], i['freeRoom'], i['roomCourseList']] for i in jdata['data']['floorList'][m]['children']])
    return datas


def get_id(url, headers, buildId):
    data = {"buildId": buildId,
            "roomType": "",
            "zws": "",
            "area": 3,
            "selectParamArrStr": ""
            }
    responses = requests.post(url, headers=headers, data=data)
    jdata = json.loads(responses.content)
    datas = [[i['id'] for i in jdata['data']['roomList']]]
    return datas


def get_data1(url, headers, roomId):
    data = {
        "roomId": roomId
    }
    responses = requests.post(url, headers=headers, data=data)
    jdata = json.loads(responses.content)
    for i in jdata['data']['courseList']:
        if 'courseName' not in i:
            i['courseName'] = "NONE"
        if 'teacherName' not in i:
            i['teacherName'] = "NONE"
        if 'orgName' not in i:
            i['orgName'] = "NONE"
    datas = [[i['courseName'], i['teacherName'], i['orgName']] for i in jdata['data']['courseList']]
    if datas == []:
        datas.append(['NONE', 'NONE', 'NONE'])
    # print(datas)
    return datas


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42',
    # cookie可能要自己换一下不然爬不到
    'Cookie': 'SECKEY_ABVK=FKt8c8eJJ10Ak/QPFJiWf1kSWGGaPuknfrX/eoXoX7Y%3D; _ga=GA1.3.1188746164.1630113667; Hm_lvt_b5e89d165916dae4f0dca6193b9d4f4d=1668519128; Hm_lvt_ce40ae2cbb7d37938c7a90c8dd0660b5=1668519135; buildId=; SECKEY_ABVK=FKt8c8eJJ10Ak/QPFJiWf+fE5zoNSmDcHml50EBNJvk%3D; JSESSIONID=3AA6E5B670A635643736C12C40D8281E; Hm_lpvt_ce40ae2cbb7d37938c7a90c8dd0660b5=1668851821; Hm_lpvt_b5e89d165916dae4f0dca6193b9d4f4d=1668853344',
    'Host': 'ids.sjtu.edu.cn',
    'Origin': 'https://ids.sjtu.edu.cn',
    'Referer': 'https://ids.sjtu.edu.cn/build/goMFreeRoom?param=17df647a22c2261eba9da32cc41786ff'
    }
headersID = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42',
    # cookie自己换一下
    'Cookie': 'schoolArea=0; SECKEY_ABVK=FKt8c8eJJ10Ak/QPFJiWf5ZPgUhdhZLMlVSUBTANFrY%3D; _ga=GA1.3.1188746164.1630113667; SECKEY_ABVK=FKt8c8eJJ10Ak/QPFJiWf+299igm03vqLpw03ys0gUE%3D; schoolArea=3; JSESSIONID=B1DED2E044B9D6DCAC3C1518670A40DF; Hm_lvt_b5e89d165916dae4f0dca6193b9d4f4d=1668519128,1669093246; Hm_lvt_ce40ae2cbb7d37938c7a90c8dd0660b5=1668519135,1669093291; Hm_lpvt_b5e89d165916dae4f0dca6193b9d4f4d=1669093851; Hm_lpvt_ce40ae2cbb7d37938c7a90c8dd0660b5=1669093855',
    'Host': 'ids.sjtu.edu.cn',
    'Origin': 'https://ids.sjtu.edu.cn',
    'Referer': 'https://ids.sjtu.edu.cn/build/goMRoomSearch?param=17df647a22c2261eba9da32cc41786ff'
    }

headers1 = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52",
    'Cookie': "_ga=GA1.3.1188746164.1630113667; SECKEY_ABVK=FKt8c8eJJ10Ak/QPFJiWf+299igm03vqLpw03ys0gUE%3D; schoolArea=3; JSESSIONID=B1DED2E044B9D6DCAC3C1518670A40DF; Hm_lvt_b5e89d165916dae4f0dca6193b9d4f4d=1668519128,1669093246; Hm_lvt_ce40ae2cbb7d37938c7a90c8dd0660b5=1668519135,1669093291; Hm_lpvt_ce40ae2cbb7d37938c7a90c8dd0660b5=1669093855; Hm_lpvt_b5e89d165916dae4f0dca6193b9d4f4d=1669093864",
    'Host': 'ids.sjtu.edu.cn',
    'Origin': 'https://ids.sjtu.edu.cn',
    'Referer': 'https://ids.sjtu.edu.cn/build/goM3DClassroom?param=a8b2323b21614d6d864d2dd018196eaf'
}
datasID = []
datasID.extend(get_id('https://ids.sjtu.edu.cn/build/findRoomList', headersID, 126))
datasID.extend(get_id('https://ids.sjtu.edu.cn/build/findRoomList', headersID, 128))
datasID.extend(get_id('https://ids.sjtu.edu.cn/build/findRoomList', headersID, 127))
datasID.extend(get_id('https://ids.sjtu.edu.cn/build/findRoomList', headersID, 122))
datasID.extend(get_id('https://ids.sjtu.edu.cn/build/findRoomList', headersID, 564))
datasID.extend(get_id('https://ids.sjtu.edu.cn/build/findRoomList', headersID, 124))
datasID.extend(get_id('https://ids.sjtu.edu.cn/build/findRoomList', headersID, 125))
datas = []
datas.extend(get_aff('https://ids.sjtu.edu.cn/build/findBuildRoomType', headers, 126))
datas.extend(get_aff('https://ids.sjtu.edu.cn/build/findBuildRoomType', headers, 128))
datas.extend(get_aff('https://ids.sjtu.edu.cn/build/findBuildRoomType', headers, 127))
datas.extend(get_aff('https://ids.sjtu.edu.cn/build/findBuildRoomType', headers, 122))
datas.extend(get_aff('https://ids.sjtu.edu.cn/build/findBuildRoomType', headers, 564))
datas.extend(get_aff('https://ids.sjtu.edu.cn/build/findBuildRoomType', headers, 124))
datas.extend(get_aff('https://ids.sjtu.edu.cn/build/findBuildRoomType', headers, 125))
finalDatas = []
for i in datas:
    test = [i[0]]
    if i[1] == '0':
        for j in range(14):
            test.append('空')
    else:
        for j in range(14):
            test.append('自')
    for k in i[2]:
        for i in range(k[0], k[1] + 1):
            test[i] = '课'
    finalDatas.append(test)
datas2 = []
for i in datasID:
    for j in i:
        datas2.extend(get_data1('https://ids.sjtu.edu.cn/course/findCourseToRoom', headers1, j))
# print(len(finalDatas))
for i in range(len(finalDatas)):
    finalDatas[i].extend(datas2[i])
# print(finalDatas)

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='Hbh001098hbh',
    # database需要自己创建，表不需要
    database='buildingInfo',
    charset='utf8mb4',
)
sql = "CREATE TABLE lesson (`教室名` VARCHAR (10) NOT NULL, `课时1` VARCHAR (5) NOT NULL, `课时2` VARCHAR (5) NOT NULL, `课时3` VARCHAR (5) NOT NULL, `课时4` VARCHAR (5) NOT NULL, `课时5` VARCHAR (5) NOT NULL, `课时6` VARCHAR (5) NOT NULL, `课时7` VARCHAR (5) NOT NULL, `课时8` VARCHAR (5) NOT NULL, `课时9` VARCHAR (5) NOT NULL, `课时10` VARCHAR (5) NOT NULL, `课时11` VARCHAR (5) NOT NULL, `课时12` VARCHAR (5) NOT NULL, `课时13` VARCHAR (5) NOT NULL, `课时14` VARCHAR (5) NOT NULL, `课程名` VARCHAR (50) NOT NULL, `教师姓名` VARCHAR (100) NOT NULL, `开设学院` VARCHAR (20) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;"
cur = conn.cursor()
cur.execute(sql)
cur.executemany(
    'INSERT INTO lesson(教室名,课时1,课时2,课时3,课时4,课时5,课时6,课时7,课时8,课时9,课时10,课时11,课时12,课时13,课时14,课程名,教师姓名,开设学院) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
    finalDatas)
conn.commit()
conn.close()
