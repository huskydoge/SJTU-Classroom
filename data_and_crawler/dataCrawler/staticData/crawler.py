# 获取教室的静态信息

import requests
import json
import pymysql
# from lxml import etree


def get_aff(url, headers, buildId):
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


def get_name(url, headers, roomId):
    data = {
        "roomId": roomId
    }
    responses = requests.post(url, headers=headers, data=data)
    jdata = json.loads(responses.content)
    datas = [jdata['data']['teachBuilding']['name']]
    return datas


def get_data2(url, headers, roomId):
    data = {"roomId": roomId,
            }
    responses = requests.post(url, headers=headers, data=data)
    jdata = json.loads(responses.content)
    datas = [{i['name']: i['value'] for i in jdata['data']['roomAttrList']}]
    for i in datas:
        if '座位数' not in i:
            i['座位数'] = "NONE"
        if '座椅类型' not in i:
            i['座椅类型'] = "NONE"
        if '课桌类型' not in i:
            i['课桌类型'] = "NONE"
        if '讲台类型' not in i:
            i['讲台类型'] = "NONE"
        if '智能中控' not in i:
            i['智能中控'] = "NONE"
        if '智能控制面板' not in i:
            i['智能控制面板'] = "NONE"
        if '电子白板' not in i:
            i['电子白板'] = "NONE"
        if '自习位' not in i:
            i['自习位'] = "NONE"
        if '传感器' not in i:
            i['传感器'] = "NONE"
        if '空调' not in i:
            i['空调'] = "NONE"
        if '新风系统' not in i:
            i['新风系统'] = "NONE"
        if '讲台电脑' not in i:
            i['讲台电脑'] = "NONE"
        if '投影仪' not in i:
            i['投影仪'] = "NONE"
        if '电动幕布' not in i:
            i['电动幕布'] = "NONE"
        if '讲台黑板' not in i:
            i['讲台黑板'] = "NONE"
        if '话筒' not in i:
            i['话筒'] = "NONE"
        if '扩声系统' not in i:
            i['扩声系统'] = "NONE"
        if '激光笔' not in i:
            i['激光笔'] = "NONE"
        if '灯光设备' not in i:
            i['灯光设备'] = "NONE"
        if '考勤机' not in i:
            i['考勤机'] = "NONE"
        if '考位数' not in i:
            i['考位数'] = "NONE"
        return datas


headersID = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42',
    # cookie自己换一下
    'Cookie': '_ga=GA1.3.183396916.1643871094; Qs_lvt_374225=1667464957,1669017559,1669189787,1669364986,1669527441; Qs_pv_374225=4014547470625467400,2597225703320165000,2542070338921005000,4084250698850740000,289474851380865100; buildId=; Hm_lvt_b5e89d165916dae4f0dca6193b9d4f4d=1668939341,1669164057,1669298232,1669706619; schoolArea=3; _gid=GA1.3.1826861872.1669708355; SECKEY_ABVK=EBGgvv5EpwzZMhkCJqkdsz6HOWPffv817xw2t1KAnFU=; JSESSIONID=1531FEBF543EC55F2FDAEDFAD659967E; Hm_lpvt_b5e89d165916dae4f0dca6193b9d4f4d=1669729487',
    'Host': 'ids.sjtu.edu.cn',
    'Origin': 'https://ids.sjtu.edu.cn',
    'Referer': 'https://ids.sjtu.edu.cn/build/goMRoomSearch?param=17df647a22c2261eba9da32cc41786ff'
    }
datasID = []
datasID.extend(get_aff('https://ids.sjtu.edu.cn/build/findRoomList', headersID, 126))
datasID.extend(get_aff('https://ids.sjtu.edu.cn/build/findRoomList', headersID, 128))
datasID.extend(get_aff('https://ids.sjtu.edu.cn/build/findRoomList', headersID, 127))
datasID.extend(get_aff('https://ids.sjtu.edu.cn/build/findRoomList', headersID, 122))
datasID.extend(get_aff('https://ids.sjtu.edu.cn/build/findRoomList', headersID, 564))
datasID.extend(get_aff('https://ids.sjtu.edu.cn/build/findRoomList', headersID, 124))
datasID.extend(get_aff('https://ids.sjtu.edu.cn/build/findRoomList', headersID, 125))
# print(datasID)
headersName = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52",
    'Cookie': '_ga=GA1.3.183396916.1643871094; Qs_lvt_374225=1667464957,1669017559,1669189787,1669364986,1669527441; Qs_pv_374225=4014547470625467400,2597225703320165000,2542070338921005000,4084250698850740000,289474851380865100; buildId=; Hm_lvt_b5e89d165916dae4f0dca6193b9d4f4d=1668939341,1669164057,1669298232,1669706619; schoolArea=3; _gid=GA1.3.1826861872.1669708355; SECKEY_ABVK=EBGgvv5EpwzZMhkCJqkdsz6HOWPffv817xw2t1KAnFU=; JSESSIONID=1531FEBF543EC55F2FDAEDFAD659967E; Hm_lpvt_b5e89d165916dae4f0dca6193b9d4f4d=1669729616',
    'Host': 'ids.sjtu.edu.cn',
    'Origin': 'https://ids.sjtu.edu.cn',
    'Referer': 'https://ids.sjtu.edu.cn/build/goM3DClassroom?param=cc236aa1c3f82b7c54358231a4002b9b'
}
headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52',
    'Cookie': '_ga=GA1.3.183396916.1643871094; Qs_lvt_374225=1667464957,1669017559,1669189787,1669364986,1669527441; Qs_pv_374225=4014547470625467400,2597225703320165000,2542070338921005000,4084250698850740000,289474851380865100; buildId=; Hm_lvt_b5e89d165916dae4f0dca6193b9d4f4d=1668939341,1669164057,1669298232,1669706619; schoolArea=3; _gid=GA1.3.1826861872.1669708355; SECKEY_ABVK=EBGgvv5EpwzZMhkCJqkdsz6HOWPffv817xw2t1KAnFU=; JSESSIONID=1698ABE53D682ABDEAF0D53A98D0138C; Hm_lpvt_b5e89d165916dae4f0dca6193b9d4f4d=1669733170',
    'Host': 'ids.sjtu.edu.cn',
    'Origin': 'https://ids.sjtu.edu.cn',
    'Referer': 'https://ids.sjtu.edu.cn/build/goM3DClassroom?param=a8b2323b21614d6d864d2dd018196eaf'

}
datas = []
for i in datasID:
    for j in i:
        datas.append(get_name('https://ids.sjtu.edu.cn/build/findById', headersName, j))
dataToAdd = []
for i in datasID:
    for j in i:
        dataToAdd.extend(get_data2('https://ids.sjtu.edu.cn/roomAttr/findRoomAttrValue', headers2, j))
print(datas)
print(dataToAdd)
for i in range(len(datas)):
    datas[i].append(dataToAdd[i]['座位数'])
    datas[i].append(dataToAdd[i]['座椅类型'])
    datas[i].append(dataToAdd[i]['课桌类型'])
    datas[i].append(dataToAdd[i]['讲台类型'])
    datas[i].append(dataToAdd[i]['智能中控'])
    datas[i].append(dataToAdd[i]['智能控制面板'])
    datas[i].append(dataToAdd[i]['电子白板'])
    datas[i].append(dataToAdd[i]['传感器'])
    datas[i].append(dataToAdd[i]['空调'])
    datas[i].append(dataToAdd[i]['新风系统'])
    datas[i].append(dataToAdd[i]['讲台电脑'])
    datas[i].append(dataToAdd[i]['投影仪'])
    datas[i].append(dataToAdd[i]['电动幕布'])
    datas[i].append(dataToAdd[i]['讲台黑板'])
    datas[i].append(dataToAdd[i]['话筒'])
    datas[i].append(dataToAdd[i]['扩声系统'])
    datas[i].append(dataToAdd[i]['激光笔'])
    datas[i].append(dataToAdd[i]['灯光设备'])
    datas[i].append(dataToAdd[i]['考勤机'])
    datas[i].append(dataToAdd[i]['自习位'])
    datas[i].append(dataToAdd[i]['考位数'])
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
sql = "CREATE TABLE classRoomCharacter (`教室名` VARCHAR (10) NOT NULL, `座位数` VARCHAR (10) NOT NULL, `座椅类型` VARCHAR (10) NOT NULL, `课桌类型` VARCHAR (10) NOT NULL, `讲台类型` VARCHAR (10) NOT NULL, `智能中控` VARCHAR (20) NOT NULL, `智能控制面板` VARCHAR (20) NOT NULL, `电子白板` VARCHAR (10) NOT NULL, `传感器` VARCHAR (20) NOT NULL, `空调` VARCHAR (20) NOT NULL, `新风系统` VARCHAR (20) NOT NULL, `讲台电脑` VARCHAR (30) NOT NULL, `投影仪` VARCHAR (20) NOT NULL, `电动幕布` VARCHAR (20) NOT NULL, `讲台黑板` VARCHAR (10) NOT NULL, `话筒` VARCHAR (15) NOT NULL, `扩声系统` VARCHAR (20) NOT NULL, `激光笔` VARCHAR (5) NOT NULL, `灯光设备` VARCHAR (15) NOT NULL, `考勤机` VARCHAR (10) NOT NULL, `自习位` VARCHAR (10) NOT NULL, `考位数` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;"
cur = conn.cursor()
cur.execute(sql)
cur.executemany(
    'INSERT INTO classRoomCharacter(教室名,座位数,座椅类型,课桌类型,讲台类型,智能中控,智能控制面板,电子白板,传感器,空调,新风系统,讲台电脑,投影仪,电动幕布,讲台黑板,话筒,扩声系统,激光笔,灯光设备,考勤机,自习位,考位数) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
    datas)
conn.commit()
conn.close()
