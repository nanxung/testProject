#coding:utf-8
import time
import requests
from selenium import webdriver

req=requests.Session()

headers_input={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
}

def search():
    url="http://www.qichacha.com/more_shixin?sstype=1&key=%E4%B9%90%E8%A7%86&index=&province=&startDateBegin=&startDateEnd=&ajaxflag=true&p=2"
    headers_input['Cookie']=getCookie()
    p=req.get(url=url,headers=headers_input)
    print(p.text)

def api0():
    urlClassfy=['more_brand','more_zhuanli','more_zzq','more_rjzzq','']
    data={
        'key': '陈波',
        'index':'',
        'status':'',
        'sortField':'',
        'isSortAsc':'',
        'ipc':'',
        'startDateBegin':'',
        'startDateEnd':'',
        'kind':'',
        'ajaxflag': 'true',
        'p': 2
    }
    url = "http://www.qichacha.com/more_zhuanli"
    headers_input['Cookie'] = getCookie()
    p = req.get(url=url, headers=headers_input,params=data)
    print(p.text)
def api1():
    urlClassfy=['more_shixin',]
    '''
    失信人 sstype 0
    被执行人 sstype 1
    裁判文书 2
    '''
    data={
        'key': '贾跃亭',
        'index':'',
        'province':'',
        'casetype':'',
        'sortField':'',
        'isSortAsc':'',
        'sstype':'2',
        'ajaxflag': 'true',
        'p': 2
    }
def getCookie():
    web=webdriver.Chrome()
    web.get("http://www.qichacha.com/user_login")
    qqbutton=web.find_element_by_xpath("//*[@id=\"normalLoginPanel\"]/div[2]/div/div/div[3]/a[2]")
    qqbutton.click()
    web.switch_to_frame("ptlogin_iframe")
    qqloginButton=web.find_element_by_xpath("//*[@id=\"switcher_plogin\"]")
    qqloginButton.click()
    # web.switch_to_frame("ptlogin_iframe")
    username=web.find_element_by_xpath("//*[@id=\"u\"]")
    username.send_keys("418732021")
    passwd=web.find_element_by_xpath("//*[@id=\"p\"]")
    passwd.send_keys("renshenghaichang")
    loginBtn=web.find_element_by_xpath("//*[@id=\"login_button\"]")
    loginBtn.click()
    time.sleep(10)
    web.get("http://www.qichacha.com/more_shixin?key=%E4%B9%90%E8%A7%86&sstype=1")
    time.sleep(10)
    b=web.get_cookies()
    print(b)
    cookie = ''
    for elem in web.get_cookies():
        cookie += elem["name"] + "=" + elem["value"] + ";"
    return cookie

if __name__=='__main__':
    api0()