import pymysql
from datetime import datetime

days = ['Mon', 'Tue', 'Wedn', 'Thur', 'Fri', 'Sat', 'Sun']
dataList = ['实到人数', 'CO2浓度', 'PM25浓度', '温度', '空气湿度']

def getPlotData(classname):
    averageData = dict()
    dailyData = []
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
        oneDay = dict()
        daily = [dict() for i in range(16)]
        for datatype in dataList:
            total = 0
            if j != day:
                for i in range(8, 24):
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

                    daily[i - 8][datatype] = num
                    if num == 'Non':
                        num = '0'
                    total += eval(num)
                average = round(total / 16, 2)
                oneDay[datatype] = average
            else:
                for i in range(8, hour + 1):
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

                    daily[i - 8][datatype] = num
                    if num == 'Non':
                        num = '0'
                    total += eval(num)
                average = round(total / (hour - 7), 2)
                oneDay[datatype] = average
        averageData[j] = oneDay
        dailyData.append(daily)
    return averageData, dailyData

