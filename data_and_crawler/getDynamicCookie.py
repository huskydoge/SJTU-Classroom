# 获取网站的动态cookie，使爬虫可以持续进行

from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('headless')


def getCookie():
    chr = webdriver.Chrome(r'/Users/husky/Downloads/chromedriver', options=option)
    dic = dict()

    while ("Hm_lvt_b5e89d165916dae4f0dca6193b9d4f4d" not in dic.keys()) or (
            "Hm_lpvt_b5e89d165916dae4f0dca6193b9d4f4d" not in dic.keys()) or ("JSESSIONID" not in dic.keys()) or (
            "SECKEY_ABVK" not in dic.keys()):
        chr.get('https://ids.sjtu.edu.cn/sysConfig/findSysConfigInfos')
        Cookie = chr.get_cookies()
        for c in Cookie:
            dic[c['name']] = c['value']

    res = "_ga=GA1.3.183396916.1643871094; " \
          "Qs_lvt_374225=1669017559,1669189787,1669364986,1669527441,1669777509; " \
          "Qs_pv_374225=4084250698850740000,289474851380865100,336714975456755460,1162725617322055200,1048580809875088000; " \
          "buildId=; " \
          "Hm_lvt_b5e89d165916dae4f0dca6193b9d4f4d=" + dic["Hm_lvt_b5e89d165916dae4f0dca6193b9d4f4d"] + ";" \
                                                                                                        "JSESSIONID=" + \
          dic["JSESSIONID"] + "; " \
                              "schoolArea=3; " \
                              "_gid=GA1.3.364948003.1671212658; " \
                              "Hm_lpvt_b5e89d165916dae4f0dca6193b9d4f4d=" + dic[
              "Hm_lpvt_b5e89d165916dae4f0dca6193b9d4f4d"] + "; " \
                                                            "SECKEY_ABVK=" + dic["SECKEY_ABVK"]
    return res
