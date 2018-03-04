import requests
import time
req=requests.Session()

headers_input={
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
}


def getCurtTime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())



request_data={

    "msg":"车辆信息违章查询接口",
    "sendTime":getCurtTime(),
    "sign":"MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAK6tZLxKeyzTgzkJ+gRAZndXkc"
           "y/q++cgDdCeo+uk+qca/f3iZgOBQK48KqOzer5ipOigSaMZAnMt/YkiHukGw6G5Bl41J0NnTTk"
           "O0kqEXIBVGbwqKXhPojzkdh+unDCPmHccukA5zcdwypDJQp9kEvh8qLwYm/MOayvH27oFRd5Ag"
           "MBAAECgYBaMnzu4YLjLcD3xhgM8/g1LcnCsUKmMujeH/zLjrkgj28NFww8sRiTRE45tA3OhNay"
           "z1njPuE1Ujm35zt2pNG2/nvW1nK+1Ocj32I+kxz8sEQQZWoR/gx81Y2/7snL5qjDjQJnW/fl9y"
           "x0yjLJOZg2s9cz5+uFVsXDuS7bswFJJQJBAOWtktPR1mrJuMDn6U3qQbbHCAOOvAZ9gW0yONd/"
           "xLDy9slB7C+i9mLTk/sUEPMCPBgH37slSSWms+A3WmTuESsCQQDCsi10G45ZX0qda6SB+f+C9Q"
           "idqtv8wv1Txptj47Wt0AcEaPyl8O1dnvwH0G+1OX4e6myNaSskVoKneXf7lX/rAkB6udvqGYc0"
           "OqPhWEp/GryQeRucIwnvgeLFwX9ED36/eqRJ+FLHRZHYTuwUzq0b3MbVpGd1bb//QWt+VLWVlu"
           "xPAkEAn0+gtdMeha7dpTZBZEGmfAf4xtraK1d6ZqSq3e+j59fDBi7KHRapg+PlopdB8O5cbvuv"
           "W37k2FUZj+Rq8yf/hQJBALtbK+XpyRRk1YikZkQ+q6SvHnynIbUMzQSndx25HCmREKkHIClNgf"
           "l/hRcj4xsSpOuSicWTW4RQ5ZW9NFj2iWk=",

    "data":{
        'applicationID':"FG6YWn4O3u5cWFYZ",
        "licenseNo": "渝A759L3",
        "frameNo": "LS5A3ABRXEA112011",
        "engineNo": "E34B015901",
	    "mobile": "18610077627",
        # "verificationCode ": "186100"

    }
}

mobile_url="http://apiplus.ztwltech.com/v2.0/valueadd/peccancy"

p=req.post(url=mobile_url,data=request_data)
print(p.text)