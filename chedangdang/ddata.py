import requests
import json
import time
from chedangdang import province
req=requests.Session()

header={
    "Cookie":"JSESSIONID=E74163334EBE58A90425682F195CC17B-n2;",
    "token":"18079954801:6f277a204a02dc534f544ce3860721b0:android:-1:e35d3630cfa94cec99950fdc63c8524c",
    "Content-Type":"application/x-www-form-urlencoded",
    "Host":"120.55.138.140",
    "User-Agent":"okhttp/3.8.1",

}

header0={
    "Cookie":"JSESSIONID=1447DB16B4275B2F7A7C510BAE4D39E2-n2;",
    "Cookie2":"$Version=1",
    "token":"18079954801:6f277a204a02dc534f544ce3860721b0:-1:e35d3630cfa94cec99950fdc63c8524c",
    "Content-Type":"application/x-www-form-urlencoded",
    "Host":"120.55.138.140",
    "User-Agent":"Mozilla/5.0 (Linux; Android 7.1.1; Mi Note 3 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36",
    "version":"4.1.7",
    "Accept-Encoding":"gzip",
}
def toFile(name,content):
    with open("./data1/{}.csv".format(name),"a+") as w:
        w.write(content)
t=False
tt=False
for i in province.province['data']['provinces']:
    id=i['id']

    if id==17:
        t=True
    if t:
        p0=req.post(url="http://120.55.138.140/mhwcw/api/address/getCityByProvince",headers=header0,data={"provinceId":id})
        print(p0.text)
        p0d=json.loads(p0.text)
        for ii in p0d["data"]["citys"]:
            if ii['cityName']=="铜川市":
                tt=True
            print(ii['cityName'])
            if tt:
                pageIndex=1
                while True:
                    cityId=ii['id']
                    data={
                        "accid":"129744",
                        "type":"2",
                        "pageIndex":pageIndex,
                        "pageSize":"10",
                        "serviceType":'1',
                        "provinceId":id,
                        "cityId":cityId
                    }
                    p=req.post(url="http://120.55.138.140/mhwcw/api/businesscenter/getJoinBusinessList",headers=header,data=data)
                    print(p.text)
                    dc=json.loads(p.text)
                    # print(dc)
                    if '该地区暂时没有服务商家' in p.text:
                        break
                    for s in dc['data']['businesses']:
                        toFile(i["provinceName"]+"-"+ii["cityName"],s['address']+","+s['location']+","+s["businessName"]+","+s["realName"]+","+s['star']+","+s['telephone']+"\n")
                        print(s['address']+","+s['location']+","+s["businessName"]+","+s["realName"]+","+s['star']+","+s['telephone']+"\n")
                    if pageIndex<int(dc['data']['totalPage']):
                        pageIndex+=1
                    else:
                        break
                    # time.sleep(2)
