import sys
import urllib.request
import urllib.parse
import threading
import requests

url = "http://xk.csust.edu.cn:8080/wsxk/stu_xszx_rpt.aspx?func=1"
header = {
    "Accept": "text/html, application/xhtml+xml, image/jxr, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-Hans-CN,zh-Hans;q=0.8,en-US;q=0.5,en;q=0.3",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
    "Cookie": "ASP.NET_SessionId=no4jwa45nedynm551p5dmdzg",
    "Content-Length": "704",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "http://xk.csust.edu.cn:8080/wsxk/stu_xszx_rpt.aspx",
    "Connection": "Keep-Alive",
    "Host": "xk.csust.edu.cn:8080"
}

mydata = "chkKC7=140193%250001%7c01%7c03%7c02%7c2.0%7c0001%7c0%7c%5b0504330136%5d%c3%c0%ca%f5%bc%f8%c9%cd(%d2%d5%ca%f5%bc%b0%c6%e4%cb%fb)%7c%7cawbjahkayqbpadgadgbqagianabiagiaaaa5agkaygb1ahuaywbyahmadwavageacgaraheapqa%3d&chkSKBJ7=0%240000495%24140193-007%24%24eqbkadiadwbnag0adabmahaabwbhaggaegbsacsazabwahoacqbxadyacwbyaguazqa&sel_xnxq=20171&mcount=28&sel_lx=2&SelSpeciality=&id=TTT%2c0%240000495%24140193-007%24%24eqbkadiadwbnag0adabmahaabwbhaggaegbsacsazabwahoacqbxadyacwbyaguazqa%a1%e8140193%250001%7c01%7c03%7c02%7c2.0%7c0001%7c0%7c%5b0504330136%5d%c3%c0%ca%f5%bc%f8%c9%cd(%d2%d5%ca%f5%bc%b0%c6%e4%cb%fb)%7c%7cawbjahkayqbpadgadgbqagianabiagiaaaa5agkaygb1ahuaywbyahmadwavageacgaraheapqa%3d&yxsjct=&sel_xq=1&hid_ReturnStr=&hid_N"

for i in range(0, 100000000):
    req1 = requests.post(url, data=mydata, headers=header)
    print(str(i) + " :1")
    # req3 = requests.post(url, data=mydata3, headers=header)
    # print(str(i) + " :公关礼仪")
    # req3 = requests.post(url, data=mydata4, headers=header)
    # print(str(i) + " :管理学概论")
    # req3 = requests.post(url, data=mydata5, headers=header)
    # print(str(i) + " :管理学概论")
# req = urllib.request.Request(url, data=mydata, headers=header)
# urllib.request.urlopen(req)
#data = urllib.request.urlopen(req)


# class One(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#     def run(self):
#         for i in range(0, 10000):
#             req1 = requests.post(url, data=mydata1, headers=header)
#             print("线程1: " + str(i) + " :红楼梦1")
#             req2 = requests.post(url, data=mydata2, headers=header)
#             print("线程1: " + str(i) + " :红楼梦2")
#
# class Two(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#     def run(self):
#         for i in range(0, 10000):
#             req3 = requests.post(url, data=mydata3, headers=header)
#             print("线程2: " + str(i) + " :公关礼仪")
#
# one = One()
# two = Two()
# one.start()
# two.start()

