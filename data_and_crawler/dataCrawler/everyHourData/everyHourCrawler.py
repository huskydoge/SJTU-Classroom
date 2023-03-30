# 自动爬取8点到23点每小时的教室各项数据

import requests
import json
import pymysql
import schedule
import time
import random
import datetime
import getDynamicCookie
import pyautogui

date = datetime.date.today()
dateLst = str(date).split('-', 2)
# 得到当前是星期几
d = datetime.date(int(dateLst[0]), int(dateLst[1]), int(dateLst[2])).isoweekday()
print(d)
sql = [
    'CREATE TABLE myTableMon8 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableMon9 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableMon10 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableMon11 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableMon12 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableMon13 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableMon14 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableMon15(`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableMon16 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableMon17 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableMon18 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableMon19 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableMon20 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableMon21 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableMon22 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableMon23 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableTue8 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableTue9 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableTue10 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableTue11 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableTue12 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableTue13 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableTue14 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableTue15(`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableTue16 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableTue17 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableTue18 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableTue19 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableTue20 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableTue21 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableTue22 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableTue23 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableWedn8 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableWedn9 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableWedn10 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableWedn11 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableWedn12 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableWedn13 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableWedn14 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableWedn15(`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableWedn16 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableWedn17 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableWedn18 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableWedn19 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableWedn20 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableWedn21 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableWedn22 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableWedn23 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableThur8 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableThur9 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableThur10 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableThur11 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableThur12 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableThur13 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableThur14 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableThur15(`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableThur16 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableThur17 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableThur18 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableThur19 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableThur20 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableThur21 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableThur22 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableThur23 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableFri8 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableFri9 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableFri10 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableFri11 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableFri12 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableFri13 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableFri14 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableFri15(`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableFri16 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableFri17 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableFri18 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableFri19 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableFri20 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableFri21 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableFri22 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableFri23 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSat8 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSat9 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSat10 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSat11 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSat12 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSat13 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSat14 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSat15(`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSat16 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSat17 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSat18 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSat19 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSat20 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSat21 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSat22 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSat23 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSun8 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSun9 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSun10 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSun11 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSun12 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSun13 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSun14 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSun15(`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSun16 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSun17 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSun18 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSun19 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSun20 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSun21 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSun22 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;',
    'CREATE TABLE myTableSun23 (`教室名` VARCHAR (10) NOT NULL, `实到人数` VARCHAR (5) NOT NULL, `CO2浓度` VARCHAR (10) NOT NULL, `空气湿度` VARCHAR (10) NOT NULL, `PM25浓度` VARCHAR (10) NOT NULL, `温度` VARCHAR (10) NOT NULL, primary key (`教室名`))CHARSET=utf8mb4 collate utf8mb4_general_ci;']
conn1 = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='Hbh001098hbh',
    database='classDynamicInfo',
    charset='utf8mb4',
)
cur = conn1.cursor()

# Cookie = "_ga=GA1.3.183396916.1643871094; Qs_lvt_374225=1669017559,1669189787,1669364986,1669527441,1669777509; Qs_pv_374225=4084250698850740000,289474851380865100,336714975456755460,1162725617322055200,1048580809875088000; buildId=; Hm_lvt_b5e89d165916dae4f0dca6193b9d4f4d=1671214216;JSESSIONID=3BC26B58C5F69D5FE6E374F9224AD06C; schoolArea=3; _gid=GA1.3.364948003.1671212658; Hm_lpvt_b5e89d165916dae4f0dca6193b9d4f4d=1671214216; SECKEY_ABVK=Ms9ILOs5wWcRy11y42oEAy8FguELiX58iZl5cc8bQL4%3D"
def get_aff(url, headers, buildId):
    data = {"buildId": buildId}
    responses = requests.post(url, headers=headers, data=data)
    jdata = json.loads(responses.content)
    for i in jdata['data']['roomList']:
        if 'name' not in i:
            i['name'] = 'None'
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
        i['actualStuNum'] = str(i['actualStuNum'])
    datas = [[i['name'], i['actualStuNum'], i['sensorCo2'],
              i['sensorHum'], i['sensorPm25'], i['sensorTemp']] for i in jdata['data']['roomList']]
    return datas

def crawler(t):
    Cookie = getDynamicCookie.getCookie()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46',
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
    # print(datas)
    # for i in range(len(sql)):
    #     cur.execute(sql[i])
    insertsql = ['INSERT INTO myTableMon8(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableMon9(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableMon10(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableMon11(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableMon12(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableMon13(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableMon14(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableMon15(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableMon16(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableMon17(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableMon18(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableMon19(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableMon20(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableMon21(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableMon22(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableMon23(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableTue8(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableTue9(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableTue10(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableTue11(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableTue12(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableTue13(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableTue14(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableTue15(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableTue16(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableTue17(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableTue18(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableTue19(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableTue20(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableTue21(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableTue22(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableTue23(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableWedn8(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableWedn9(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableWedn10(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableWedn11(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableWedn12(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableWedn13(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableWedn14(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableWedn15(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableWedn16(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableWedn17(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableWedn18(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableWedn19(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableWedn20(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableWedn21(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableWedn22(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableWedn23(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableThur8(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableThur9(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableThur10(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableThur11(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableThur12(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableThur13(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableThur14(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableThur15(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableThur16(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableThur17(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableThur18(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableThur19(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableThur20(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableThur21(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableThur22(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableThur23(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableFri8(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableFri9(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableFri10(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableFri11(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableFri12(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableFri13(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableFri14(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableFri15(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableFri16(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableFri17(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableFri18(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableFri19(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableFri20(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableFri21(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableFri22(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableFri23(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSat8(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSat9(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSat10(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSat11(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSat12(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSat13(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSat14(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSat15(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSat16(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSat17(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSat18(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSat19(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSat20(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSat21(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSat22(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSat23(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSun8(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSun9(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSun10(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSun11(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSun12(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSun13(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSun14(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSun15(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSun16(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSun17(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSun18(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSun19(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSun20(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSun21(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSun22(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)',
                 'INSERT INTO myTableSun23(教室名,实到人数,CO2浓度,空气湿度,PM25浓度,温度) VALUES(%s,%s,%s,%s,%s,%s)']
    deletesql = ['DELETE FROM myTableMon8', 'DELETE FROM myTableMon9', 'DELETE FROM myTableMon10',
                 'DELETE FROM myTableMon11', 'DELETE FROM myTableMon12', 'DELETE FROM myTableMon13',
                 'DELETE FROM myTableMon14', 'DELETE FROM myTableMon15', 'DELETE FROM myTableMon16',
                 'DELETE FROM myTableMon17', 'DELETE FROM myTableMon18', 'DELETE FROM myTableMon19',
                 'DELETE FROM myTableMon20', 'DELETE FROM myTableMon21', 'DELETE FROM myTableMon22',
                 'DELETE FROM myTableMon23', 'DELETE FROM myTableTue8', 'DELETE FROM myTableTue9',
                 'DELETE FROM myTableTue10', 'DELETE FROM myTableTue11', 'DELETE FROM myTableTue12',
                 'DELETE FROM myTableTue13', 'DELETE FROM myTableTue14', 'DELETE FROM myTableTue15',
                 'DELETE FROM myTableTue16', 'DELETE FROM myTableTue17', 'DELETE FROM myTableTue18',
                 'DELETE FROM myTableTue19', 'DELETE FROM myTableTue20', 'DELETE FROM myTableTue21',
                 'DELETE FROM myTableTue22', 'DELETE FROM myTableTue23', 'DELETE FROM myTableWedn8',
                 'DELETE FROM myTableWedn9', 'DELETE FROM myTableWedn10', 'DELETE FROM myTableWedn11',
                 'DELETE FROM myTableWedn12', 'DELETE FROM myTableWedn13', 'DELETE FROM myTableWedn14',
                 'DELETE FROM myTableWedn15', 'DELETE FROM myTableWedn16', 'DELETE FROM myTableWedn17',
                 'DELETE FROM myTableWedn18', 'DELETE FROM myTableWedn19', 'DELETE FROM myTableWedn20',
                 'DELETE FROM myTableWedn21', 'DELETE FROM myTableWedn22', 'DELETE FROM myTableWedn23',
                 'DELETE FROM myTableThur8', 'DELETE FROM myTableThur9', 'DELETE FROM myTableThur10',
                 'DELETE FROM myTableThur11', 'DELETE FROM myTableThur12', 'DELETE FROM myTableThur13',
                 'DELETE FROM myTableThur14', 'DELETE FROM myTableThur15', 'DELETE FROM myTableThur16',
                 'DELETE FROM myTableThur17', 'DELETE FROM myTableThur18', 'DELETE FROM myTableThur19',
                 'DELETE FROM myTableThur20', 'DELETE FROM myTableThur21', 'DELETE FROM myTableThur22',
                 'DELETE FROM myTableThur23', 'DELETE FROM myTableFri8', 'DELETE FROM myTableFri9',
                 'DELETE FROM myTableFri10', 'DELETE FROM myTableFri11', 'DELETE FROM myTableFri12',
                 'DELETE FROM myTableFri13', 'DELETE FROM myTableFri14', 'DELETE FROM myTableFri15',
                 'DELETE FROM myTableFri16', 'DELETE FROM myTableFri17', 'DELETE FROM myTableFri18',
                 'DELETE FROM myTableFri19', 'DELETE FROM myTableFri20', 'DELETE FROM myTableFri21',
                 'DELETE FROM myTableFri22', 'DELETE FROM myTableFri23', 'DELETE FROM myTableSat8',
                 'DELETE FROM myTableSat9', 'DELETE FROM myTableSat10', 'DELETE FROM myTableSat11',
                 'DELETE FROM myTableSat12', 'DELETE FROM myTableSat13', 'DELETE FROM myTableSat14',
                 'DELETE FROM myTableSat15', 'DELETE FROM myTableSat16', 'DELETE FROM myTableSat17',
                 'DELETE FROM myTableSat18', 'DELETE FROM myTableSat19', 'DELETE FROM myTableSat20',
                 'DELETE FROM myTableSat21', 'DELETE FROM myTableSat22', 'DELETE FROM myTableSat23',
                 'DELETE FROM myTableSun8', 'DELETE FROM myTableSun9', 'DELETE FROM myTableSun10',
                 'DELETE FROM myTableSun11', 'DELETE FROM myTableSun12', 'DELETE FROM myTableSun13',
                 'DELETE FROM myTableSun14', 'DELETE FROM myTableSun15', 'DELETE FROM myTableSun16',
                 'DELETE FROM myTableSun17', 'DELETE FROM myTableSun18', 'DELETE FROM myTableSun19',
                 'DELETE FROM myTableSun20', 'DELETE FROM myTableSun21', 'DELETE FROM myTableSun22',
                 'DELETE FROM myTableSun23']
    cur.execute(deletesql[(d - 1) * 16 + t - 8])
    cur.executemany(insertsql[(d - 1) * 16 + t - 8], datas)
    conn1.commit()
    print("the hour is {}".format(t))


schedule.every().day.at("08:30").do(crawler, 8)
schedule.every().day.at("09:05").do(crawler, 9)
schedule.every().day.at("10:05").do(crawler, 10)
schedule.every().day.at("11:19").do(crawler, 11)
schedule.every().day.at("12:00").do(crawler, 12)
schedule.every().day.at("13:00").do(crawler, 13)
schedule.every().day.at("14:00").do(crawler, 14)
schedule.every().day.at("15:00").do(crawler, 15)
schedule.every().day.at("16:00").do(crawler, 16)
schedule.every().day.at("17:00").do(crawler, 17)
schedule.every().day.at("18:00").do(crawler, 18)
schedule.every().day.at("19:00").do(crawler, 19)
schedule.every().day.at("20:00").do(crawler, 20)
schedule.every().day.at("21:00").do(crawler, 21)
schedule.every().day.at("22:00").do(crawler, 22)
schedule.every().day.at("23:00").do(crawler, 23)

while True:
    schedule.run_pending()
    x = random.randint(-3, 3)
    # y = random.randint(-3, 3)
    # 在设置范围内移动
    # pyautogui.moveTo(1300 + x, 100 + y)
    time.sleep(2)  # 别设置太小
    print(x)
