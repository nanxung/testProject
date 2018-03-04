import requests
import json
import re
req=requests.Session()



url="http://sms.czfw.cn/tpdyh/Service/HandServer.ashx?Method=checkwfcx"
header = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.1; Mi Note 3 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043906 Mobile Safari/537.36 MicroMessenger/6.6.5.1260(0x26060531) NetType/WIFI Language/zh_CN"
}

data={
    "hphm":"鲁NAB780",
    "hpzl":"02",
    "fdjh":"5219",
    "openId":"opBWWtzbftRBcf7LW-v2W9rLITGM"
}

p=req.post(url=url,data=data)
print(p.text,p.headers)
d=json.loads(p.text)
data['ts']=d['ts']
data['sign']=d['sign']
print(data)
header['Cookie']="userId=openId=oBFR-wiVgN35PFuse_kAIDZ5DSlg&unionId=oZFU2xG98njQ6UNVwqX5Z4MzInOo; ASP.NET_SessionId=43tkq4ncil4ofs0c2dz1wfg0; tpfwhopenId=o6wm-jtsyz8BYBdUpByvyJW0Eqns; tpdyhopenId=opBWWtzbftRBcf7LW-v2W9rLITGM"
pp=req.post(url="http://sms.czfw.cn/tpdyh/wzz/wfxx.aspx",data=data,headers=header)
print(pp.text)



