import requests
import json
import re
req=requests.Session()


header={
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
}

url="http://www.122.gov.cn/m/map/select"

page=req.get(url=url,headers=header)

print(page.text)


pattern=re.compile(r"<i sfdm=\"(\d+)\" sfmc=\"(.*?)\" ym=\"(.*?)\" fzjg=\"(.*?)\".*?sftjb=\"(.*?)\"></i>",re.S)
d=re.findall(pattern,page.text)
s={}
for i in d:
    s[i[0]]={"address":i[1],"url":i[2],"cp":i[3],"sftjb":i[4]}
print(s)

json.dump(s,open("./info.json","w"))