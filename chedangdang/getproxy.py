import requests
import json
import os
req=requests.Session()
def getProxy():
    p=req.get(url="http://dev.kuaidaili.com/api/getproxy/?orderid=921729317830154&num=100&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=1&method=2&an_an=1&an_ha=1&sp1=1&format=json&sep=1")
    print(p.text)
def getlines():
    k=0
    for i in os.listdir("./data/"):
        w=open("./data/"+i,'r')
        for ii in w:
            k+=1
    print(k)
if __name__=='__main__':
    getlines()