import pymysql
from datetime import datetime
import numpy as np

days = ['Mon', 'Tue', 'Wedn', 'Thur', 'Fri', 'Sat', 'Sun']

def getHeatMapData(classname, datatype):
    day = datetime.today().weekday()  # 下标0
    hour = datetime.now().hour
    dataMap = []
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='Hbh001098hbh',
        db='classDynamicInfo',
        charset='utf8',
    )
    cur = conn.cursor()
    for j in range(0, day + 1):
        if day == j:
            for i in range(8, hour + 1):
                # print(i, j)
                sql = "SELECT " + datatype + ' FROM myTable' + days[j] + str(i) + ' WHERE 教室名 = ' + "'" + classname + "'"
                cur.execute(sql)
                num = cur.fetchone()[0]
                if datatype == 'CO2浓度':
                    num = num[:num.find('P')]
                elif datatype == 'PM25浓度':
                    num = num[:num.find('μ')]
                elif datatype == '空气湿度':
                    num = num[:num.find('%')]
                elif datatype == '温度':
                    num = num[:num.find('℃')]
                point = [i - 8, j, num]
                dataMap.append(point)
        else:
            for i in range(8, 24):
                # print(i, j)
                sql = "SELECT " + datatype + ' FROM myTable' + days[j] + str(
                    i) + ' WHERE 教室名 = ' + "'" + classname + "'"
                cur.execute(sql)
                num = cur.fetchone()[0]
                if datatype == 'CO2浓度':
                    num = num[:num.find('P')]
                elif datatype == 'PM25浓度':
                    num = num[:num.find('μ')]
                elif datatype == '空气湿度':
                    num = num[:num.find('%')]
                elif datatype == '温度':
                    num = num[:num.find('℃')]
                point = [i - 8, j, num]
                dataMap.append(point)
    return dataMap


