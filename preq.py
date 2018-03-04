import requests
import json
import re
req=requests.Session()


header={
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    # "Host":"sd.122.gov.cn",
    # "Origin":"http://sd.122.gov.cn",
    "Referer":"http://sd.122.gov.cn/views/inquiry.html?q=j",
    # "X-Requested-With":"XMLHttpRequest"
}


imgurl="http://sd.122.gov.cn/captcha?nocache=1519907612436"
def saveImg(url):
    c=req.get(url=url,headers=header).content
    with open("./img.jpg","wb") as w:
        w.write(c)
    print(req.cookies)

saveImg(imgurl)

code=input("输入验证码:")

data={
    "hpzl":"02",
    "hphm1b":"AQV901",
    "hphm":"鲁AQV901",
    "fdjh":"220548",
    "captcha":code,
    "qm":"wf",
    "page":"1"
}
req.headers['Date']=""
p=req.post(url="http://sd.122.gov.cn/m/publicquery/vio",headers=header,data=data)

print(p.text)
print(req.cookies.items())