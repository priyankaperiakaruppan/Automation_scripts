import datetime
import csv
import time
import json
import requests
from bs4 import BeautifulSoup
x = datetime.datetime.now()
header = ['name']
x=x.strftime("%d%B%H")
header = ['name']
name="/mnt/sda1/daily/V_NEW_RESULT20k_23k"+x
#name = "/home/t2sadmin/daily/Mod_ORDER_MS_EXECUTED24k_28k_changed"+x
#name = "/home/t2sadmin/Googlesearch/check_order"+x
#name = "/home/t2sadmin/testtttt"
filename = "%s.csv" % name
count=0
data=["STOREID","NAME\tPOSTCODE","FETCHEDURL","STATUS","FOODHUBWEBSITE","GPIN_DBSTATUS","SECURE","BEFORE GPIN STATUS","AFTER GPIN STATUS"]
with open(filename, 'a') as f1:
    writer = csv.writer(f1)
    writer.writerow(data)

###############################Iupdate in csv#############################################################################################################################################################
#                                                                                                                                                                                                         #     
#                                                                                                                                                                                                         # 
def update_record(data1):
    with open("MSfile", 'a') as f1:
        writer = csv.writer(f1)
        writer.writerow(data1)

auth_token="1f958fdb1b8dc29fbb8cdc0a42b9fdb2"
#auth_token="11f958fdb1b8dc29fbb8cdc0a42b9fdb2"
def update_config(host,data):
    print("HOST",host)
    headers1 = {
        'authority': 'ms.touch2success.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'dnt': '1',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-platform': '"macOS"',
        'origin': 'https://ms.touch2success.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://ms.touch2success.com/manage/manageSystemHardwareSettings.php?host='+str(host)+'&do=1&authtoken='+str(auth_token),
        'accept-language': 'en-US,en;q=0.9',
    }

    data1 = {
    'fieldname': 'google_pin',
    'val': data,
    'host': host,
    }

    response = requests.post('https://ms.touch2success.com/manage/update_cfg.php', headers=headers1, data=data1)
    print(response.json()["status"])
    print(response.text)
    if response.status_code == '200':
        val = "Success"
        return val
    else: 
        val = "NOT UPDATED"
        return val

def get_stat(storeID,secret,var,foodhub_web):
#    data1 = data
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,de;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://ms.foodhub.com',
        'Pragma': 'no-cache',
        'Referer': 'https://ms.foodhub.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        'api-version': 'v2021_02_25',
        'language': 'en',
    #    'locale': 'united kingdom',
       # 'region': '5',
        #'requested-by': 'Pavithra-g',
        'requested-by': 'Priyanka-A',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }
#   data=[]
    if var:
#        count=count+1
        time.sleep(2)
#        line = f.readline().strip()
 #       print(line)
#        print(line.split(",")[0])
 #       storeid=line.split(",")[0]
 #       print(line.split(",")[6])
#        web = str(line.split(",")[3].strip())
 #       api_key = str(line.split(",")[6].strip())
        web = var
        print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",web)
        storeid=storeID
        api_key = secret

        params = {
    'api_token': api_key,
}
        json_data = {
        'ID': storeid,
        'google_pin': 'completed'
}
        json_data1 = {
        'ID': storeid,
        'google_pin': 'pending'
}
        json_data2 = {
        'ID': storeid,
}
        ################get##############
        url = 'https://api.touch2success.com/settings/'+storeid
        response = requests.get(url, params=params, headers=headers, json=json_data2)
#        RESPONSE=response
        print(response.status_code)
        if response.status_code == 200:
            try:
                g_stat=response.json()['data'][0]['google_pin']
                print("GEEEEEEEEEEEET")
                print("G_stat",g_stat)  
                if g_stat is None:
                   g_stat = "empty"
            except(IndexError):
                print("GOOGLEPIN FIELD")
                g_stat = "ERROR"

        else:
            g_stat = "ERROR"
            print("error")
        return g_stat,response
        ################
#        url = 'https://api.touch2success.com/settings/'+storeid
        print(url)
#        print(json_data)
#        data=[]

def  update_gpin_MS(storeID,secret,var,foodhub_web):
        web = var
        g_stat,response=get_stat(storeID,secret,var,foodhub_web)
        if web == "FOODHUB WEBSITE":
            if g_stat == "completed":
                value1=g_stat+"\talready marked as completed"
            else:
                data="completed"
#                response = requests.put(url, params=params, headers=headers, json=json_data)
                UP_RESULT=update_config(foodhub_web,data)
                time.sleep(2)
                AFTER,response=get_stat(storeID,secret,var,foodhub_web)
                value1=g_stat+"\t"+AFTER
          #  print("**")
          #  print(response)
           # data1=line+",completed"
           # print(type(data1))
           # data1 = list(data1.split(","))
            if response.status_code == 200:
#                update_record(data1)
                value=value1
                return value
            else:
                value="check api response"
                return value
#               data1=line+",check api response"+str(response.status_code)
 #               print(type(data1))
  #              data1 = list(data1.split(","))
   #             update_record(data1)

        elif web == "NOT FOODHUB WEBSITE":
            if g_stat == "pending":
                value1=g_stat+"\talready marked as pending"
            else:
                data="pending"
                UP_RESULT=update_config(foodhub_web,data)
                time.sleep(2)
                AFTER,response=get_stat(storeID,secret,var,foodhub_web)
                value1=g_stat+"\t"+AFTER
#                response = requests.put(url, params=params, headers=headers, json=json_data1)
 #               value1=g_stat+"\tpending"
            #print(response)
     #       data1=line+",Pending"
    #        data1 = list(data1.split(","))
            if response.status_code == 200:
                value=value1
                return value
      #          update_record(data1)
            else:
                value="check api response"
                return value
       #         data1=line+",check api response"+str(response.status_code)
        #        print(type(data1))
         #       data1 = list(data1.split(","))
          #      update_record(data1)

        else:
            value=g_stat+"\tNo update"
            return value
         #   response = requests.put(url, params=params, headers=headers, json=json_data1)
            print(storeid)
            print(web)
            print("NNNNNNNNNNNNNN")
           # data1=line+",no update"
            #data1 = list(data1.split(","))
           # update_record(data1)
#update_gpin_MS(storeID,secret,var)

###############################Order field links################################################################################################################################################################
def getorder_function(url_PresMadrid):
    cookies = {
        'OGPC': '19027681-1:',
        'AEC': 'AakniGOZrdYuIKAxwyCJ6mAz0903vnjEkmWNphuMyMWkFkvIQgpsWiQDHQ',
        '1P_JAR': '2022-07-21-12',
        'NID': '511=LVZbVS3SsOhCG5F4FeH9bifUr6P2sHR33JGXObsvYtm9WABH1Rvlazd2ymm55_gkDSBxttEsYo-tkHN5eSkA32SpcU_z4j4UlUxh9ZSLVQyUW-oES9KZkmQO2TJuEvIGl3bvYJp8nsadlkYoMUPjgBX1eUqqcM2OXmDEBZFfqv-R3qBlkhW-7Y3Q8qBYSPJz-7V3BwahHaI1KvXc',
        'DV': 'g8r42gLtmA0vgLgKlP942ct_zkYNIpgNZohKe81r5cjqAgA',
    }

    headers = {
        'authority': 'www.google.com',
        'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'OGPC=19027681-1:; AEC=AakniGOZrdYuIKAxwyCJ6mAz0903vnjEkmWNphuMyMWkFkvIQgpsWiQDHQ; 1P_JAR=2022-07-21-12; NID=511=LVZbVS3SsOhCG5F4FeH9bifUr6P2sHR33JGXObsvYtm9WABH1Rvlazd2ymm55_gkDSBxttEsYo-tkHN5eSkA32SpcU_z4j4UlUxh9ZSLVQyUW-oES9KZkmQO2TJuEvIGl3bvYJp8nsadlkYoMUPjgBX1eUqqcM2OXmDEBZFfqv-R3qBlkhW-7Y3Q8qBYSPJz-7V3BwahHaI1KvXc; DV=g8r42gLtmA0vgLgKlP942ct_zkYNIpgNZohKe81r5cjqAgA',
        'referer': 'https://www.google.com/',
        'sec-ch-dpr': '1',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"103.0.5060.114"',
        'sec-ch-ua-full-version-list': '".Not/A)Brand";v="99.0.0.0", "Google Chrome";v="103.0.5060.114", "Chromium";v="103.0.5060.114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-ch-ua-platform-version': '"5.4.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-ch-viewport-width': '1298',
        'sec-fetch-dest': 'image',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-client-data': 'CJG2yQEIo7bJAQipncoBCKD0ygEIk6HLAQjb78sBCL6ezAEI77nMAQiyuswBCIm7zAEI07vMARirqcoB',
    }

    params = {
        'atyp': 'i',
        'ct': 'backbutton',
        'cad': '',
        'tt': 'pageshow',
        'ei': '50zZYpfhNPT54-EP9vmz-AY',
        'trs': '172809',
        'bft': '29',
        'nt': 'navigate',
        'zx': '1658408302792',
    }
    url=url_PresMadrid
    response = requests.get(url, params=params, cookies=cookies, headers=headers)
    #print(response.content)
    soup_PresMadrid = BeautifulSoup(response.content, "html.parser")
    #print(len(soup_PresMadrid.findAll("a", {"class": "xFAlBc"})))
    #print(soup_PresMadrid.findAll("a", {"class": "xFAlBc"}))
    list1=[]
    table = soup_PresMadrid.findAll('div',attrs={"class":"JV5xkf"})
#print(table)
    for x in table:
        if x.find('b').text == "Order":
            for soup in x.findAll("a", {"class": "xFAlBc"}):
                list1.append(str(soup.get_text()))
    value=list1
    #value=soup.get_text()
    return value

def myfunction():
    cookies = {
    'FHD': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImI1ZDQwMzRkMjY1MzkyMDNlMGRhMGY5NmY4ZWE0ZTMwM2EzMWYwN2E1YzgzY2NkMjY0MTZkYmE1ZWYyNTQ3NDY4MDg3NTk1ZTFhOTUyMzY4In0.eyJhdWQiOiIxNzEyMzI3MjAiLCJqdGkiOiJiNWQ0MDM0ZDI2NTM5MjAzZTBkYTBmOTZmOGVhNGUzMDNhMzFmMDdhNWM4M2NjZDI2NDE2ZGJhNWVmMjU0NzQ2ODA4NzU5NWUxYTk1MjM2OCIsImlhdCI6MTY2ODAwODc1NywibmJmIjoxNjY4MDA4NzU3LCJleHAiOjE2Njg0NDA3NTcsInN1YiI6IiIsInNjb3BlcyI6WyIqIl19.bk_hPUCO4f0am0VJFW7pAKE6ONWFeDFOslMbFYk1gVZafNEYco3GjU6ozMtigneGts-tcTCBoS13XO33ZFBrg-fVIoWp2kQvPwc_-SHGDUkkA5zeLmRkJhzWrezfjw7Ei2NuGTxPPDyyYf54qNCmfUakcmerP6dtsZ2ztFCXcnMVod2NTuxOuxW72qbSrE-wzUyAaUJQHueusgxztQN-0oiQlOmAqCz9t3oRvnddQv8dptSOad4Q85WVIgpYfSMM7VanQ1gwH_f4CkbcZb_47NYwv34og6D_OyIKeNck9bI3bD1k3Rz4Jbn9bEqvMF4enWst5-mnQon3RAFYoamIhgZDAEAYPSz_kVwdTmw-LGg1lo_QxGjJ0A-02T1x9nKFsKxv_PDqLNrlHNXFPZkz4sUw2QnXosMd76JdwxN1FZDuD_cKyCnx7XCm2wGYfk9KwrfPqTgWICuanIFShx6S7HBS4D2SwPKH7PyndPSPsEVaOn6GGU4Cr9lP7t95M0p2cSJ1vmYeNaLZVRdOGZp94zPkSQHoA6tMG31B3bKyHwQJoRcM0j7rNDS6KLmEgUSzeEA7r2uuu-kH29zjqqVhfEzfeUS0vwX-6s8kgvZEW_iksDGsD8qYf00_XQEJFQNtvNLRfziF1ASjopS__PuAdhDkfLWXqzq5J4N4k72QjWQ',
    'FHD_EXPIRES': '1668440758',
    'homePageUrl': '',
    'instruction': '',
    'cart_id': '733088193',
    'cart_host': '853192',
    'TAKE_AWAY_CITY': 'order-now',
    'TAKE_AWAY_TOWN_BASKET': 'order-now',
    'order_type': 'delivery',
    'GEOMETRY_LOCATION': '%7B%22lat%22%3A53.52703899999999%2C%22long%22%3A-2.28064%7D',
}

    headers = {
    'authority': '0161burger.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'FHD=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImI1ZDQwMzRkMjY1MzkyMDNlMGRhMGY5NmY4ZWE0ZTMwM2EzMWYwN2E1YzgzY2NkMjY0MTZkYmE1ZWYyNTQ3NDY4MDg3NTk1ZTFhOTUyMzY4In0.eyJhdWQiOiIxNzEyMzI3MjAiLCJqdGkiOiJiNWQ0MDM0ZDI2NTM5MjAzZTBkYTBmOTZmOGVhNGUzMDNhMzFmMDdhNWM4M2NjZDI2NDE2ZGJhNWVmMjU0NzQ2ODA4NzU5NWUxYTk1MjM2OCIsImlhdCI6MTY2ODAwODc1NywibmJmIjoxNjY4MDA4NzU3LCJleHAiOjE2Njg0NDA3NTcsInN1YiI6IiIsInNjb3BlcyI6WyIqIl19.bk_hPUCO4f0am0VJFW7pAKE6ONWFeDFOslMbFYk1gVZafNEYco3GjU6ozMtigneGts-tcTCBoS13XO33ZFBrg-fVIoWp2kQvPwc_-SHGDUkkA5zeLmRkJhzWrezfjw7Ei2NuGTxPPDyyYf54qNCmfUakcmerP6dtsZ2ztFCXcnMVod2NTuxOuxW72qbSrE-wzUyAaUJQHueusgxztQN-0oiQlOmAqCz9t3oRvnddQv8dptSOad4Q85WVIgpYfSMM7VanQ1gwH_f4CkbcZb_47NYwv34og6D_OyIKeNck9bI3bD1k3Rz4Jbn9bEqvMF4enWst5-mnQon3RAFYoamIhgZDAEAYPSz_kVwdTmw-LGg1lo_QxGjJ0A-02T1x9nKFsKxv_PDqLNrlHNXFPZkz4sUw2QnXosMd76JdwxN1FZDuD_cKyCnx7XCm2wGYfk9KwrfPqTgWICuanIFShx6S7HBS4D2SwPKH7PyndPSPsEVaOn6GGU4Cr9lP7t95M0p2cSJ1vmYeNaLZVRdOGZp94zPkSQHoA6tMG31B3bKyHwQJoRcM0j7rNDS6KLmEgUSzeEA7r2uuu-kH29zjqqVhfEzfeUS0vwX-6s8kgvZEW_iksDGsD8qYf00_XQEJFQNtvNLRfziF1ASjopS__PuAdhDkfLWXqzq5J4N4k72QjWQ; FHD_EXPIRES=1668440758; homePageUrl=; instruction=; cart_id=733088193; cart_host=853192; TAKE_AWAY_CITY=order-now; TAKE_AWAY_TOWN_BASKET=order-now; order_type=delivery; GEOMETRY_LOCATION=%7B%22lat%22%3A53.52703899999999%2C%22long%22%3A-2.28064%7D',
    'if-modified-since': 'Wed, 09 Nov 2022 08:43:04 GMT',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}
    print(url)
    response = requests.get(url)#, cookies=cookies, headers=headers)
    print("^^^^^^^^^")
#    url="https://chaiimasterhayes.co.uk/"
 #   url="https://tammysthaikitchen.com.au/"
#    url="https://gpwittsfishchips.com/"
    print("U______________________________________________RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR__________________________________LLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
#    req_PresPadrid = requests.get(url)
    time.sleep(2)
    soup_PresMadrid = BeautifulSoup(response.content, "html.parser")
    print("CHECK")
#    print(soup_PresMadrid)

################################################################################
#check class id there
################################################################################
    print("****************************************************")
    class_check = []
    print("NEW")
    class_check=soup_PresMadrid.findAll("img", {"src": "https://nativesites.touch2success.com/compressed_images/Powered by-FH_white bg.png"})
    if class_check==[]:
        print("Not a foodhub website")
        value = "NOT FOODHUB WEBSITE"
        print(soup_PresMadrid.findAll("footer"))
        try:
       # if soup_PresMadrid.findAll("a"):
            for check_food in soup_PresMadrid.findAll("footer"):
                print("check",check_food.findAll("a"))
                for href in check_food.findAll("a"):
                #    print(href['href'])
                    if "foodhub" in href['href']:
                        dev_foodhub=href['href']
                        print("CONTAINS FOODHUB LINK",dev_foodhub)
                        value="FOODHUB WEBSITE"
                        return value
            print("CHECKING--------------------------------------------------------------ALL ORDER LINK")
            hrefs=soup_PresMadrid.findAll("a")
            print(len(hrefs))
            for data in hrefs:
#            if "order-now" in data or "order" in data['href']:
                print(data)
#                print(data['href'])
 #               if data['href']:
                if "order-now" in data or "order" in data['href']:

#                    print("DATE",data['href'])
                    orderlink=data['href'].encode('utf-8').strip()
                    print("*")
                    print("ORDERLINK",orderlink)
                    if orderlink!= []:
                        req_PresPadrid = requests.get(orderlink, cookies=cookies, headers=headers)
                        time.sleep(2)
                        orderlink_Check=[]
                        soup_PresMadrid = BeautifulSoup(req_PresPadrid.content, "html.parser")
                        orderlink_Check=soup_PresMadrid.findAll("img", {"src": "https://nativesites.touch2success.com/compressed_images/Powered by-FH_white bg.png"})
                        if len(orderlink_Check) != 0:
                             print("FOODHUB LOGO",soup_PresMadrid.findAll("img", {"src": "https://nativesites.touch2success.com/compressed_images/Powered by-FH_white bg.png"}))
                             value="FOODHUB WEBSITE"

        except(KeyError,requests.exceptions.InvalidSchema,requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError,requests.exceptions.TooManyRedirects,requests.exceptions.ContentDecodingError,requests.exceptions.MissingSchema,requests.exceptions.ReadTimeout):
            value="NOT FOODHUB WEBSITE"

    else:
        print("FOODHUB LOGO",soup_PresMadrid.findAll("img", {"src": "https://nativesites.touch2success.com/compressed_images/Powered by-FH_white bg.png"}))
        value="FOODHUB WEBSITE"

    return value


cookies = {
    'OTZ': '6820745_56_56_123900_52_436380',
    '1P_JAR': '2022-12-30-11',
    'AEC': 'AakniGN2qzAPyAd9jEXYPMWcB3X71DoPBjGXchKLv-lNANUKYdJC0WTYxQ',
    'NID': '511=jX11ZUyM5lJGpLbZ4jSRLPA-i-kJAFSCkgvYrXI_fnoCvwZ9OozePKV-OEigXCG-W9BKAxReFqpdbx9ICqSUTtCjhk-cywPEOlj-qKQYp3X1RR5KawmeyZiJgQv4l1HtIQPUaR4rd0Mdbhb2Bhwqdix6KPiHDtVwUJdGDdU8uzzmQ3VHBb6XTPQmEhQ',
}

headers = {
    'authority': 'www.google.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'OTZ=6820745_56_56_123900_52_436380; 1P_JAR=2022-12-30-11; AEC=AakniGN2qzAPyAd9jEXYPMWcB3X71DoPBjGXchKLv-lNANUKYdJC0WTYxQ; NID=511=jX11ZUyM5lJGpLbZ4jSRLPA-i-kJAFSCkgvYrXI_fnoCvwZ9OozePKV-OEigXCG-W9BKAxReFqpdbx9ICqSUTtCjhk-cywPEOlj-qKQYp3X1RR5KawmeyZiJgQv4l1HtIQPUaR4rd0Mdbhb2Bhwqdix6KPiHDtVwUJdGDdU8uzzmQ3VHBb6XTPQmEhQ',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'x-client-data': 'CJG2yQEIo7bJAQipncoBCKD0ygEIlKHLAQjr8swBCOH5zAEYwMvMAQ==',
}

#response = requests.get('https://www.google.com/search', params=params, cookies=cookies, headers=headers)
#with open('/home/t2sadmin/DATA1_5k_250.txt') as f:
#with open('/home/t2sadmin/Googlesearch/test.txt') as f:
#with open('/home/t2sadmin/DATA1_5k.txt') as f:
with open('/home/t2sadmin/Googlesearch/DATA_20k_23k.txt') as f:
#--tested --with open('/home/t2sadmin/test_251.txt') as f:
#with open('/home/t2sadmin/webpython/RES222.txt') as f:
#with open('/home/t2sadmin/Googlesearch/check_each.txt') as f:
#with open('/home/t2sadmin/Googlesearch/DATA_24k_28k_new_check.txt') as f:
#with open('/home/t2sadmin/Googlesearch/DATA_20k_24k_new2.txt') as f:
#with open('/home/t2sadmin/DATA_1_5k_new.txt') as f:
    line = f.readline()
    while line:
        line = f.readline()
        print("LINE",line)

        str1="https://www.google.com/search?q="
        str2="&oq="
        str3="&aqs="
        searchedname = line.rstrip("\n")
        s_no = line.split("\t")[0].rstrip("\n")
        line11 = line.split("\t")[1].rstrip("\n")
#    Res_name = line.split("\t")[2].rstrip("\n")
        line1 = line.split("\t")[2].rstrip("\n").replace("&","%26").replace("'","%27")
        line2 = line.split("\t")[3].rstrip("\n")
        line3 = line.split("\t")[4].rstrip("\n")
        status = line.split("\t")[5].rstrip("\n")
 #   customer_level = str(line.split("\t")[6].rstrip("\n"))
        secret = str(line.split("\t")[7].rstrip("\n"))
        line1_2 = line1+"\t"+line2
    #line.split("\t")
    #line=line.replace("\t","###",2).replace("###","\t",1)
        print(searchedname)
        line4 = line1_2
        print(line)
        line = line4.replace(","," ")
        searchedname = line.replace("%26","&").replace("%27","'").rstrip("\n")
        print(searchedname)
        line = line.replace("\t","+")
        line= line.replace(" ","+")
        line=line.rstrip("\n")
        url=str1+line+str2+line+str3
        print(url)
        text = line11+","+searchedname+","+url+","+line3+","+status+","+secret+","+s_no#,customer_level,secret
        line = text
        print("LINE",line)
    
#response = requests.get('https://www.google.com/search', params=params, cookies=cookies, headers=headers)

        count=count+1
        time.sleep(2)
#        line = f.readline()
        print(line)
        print(line.split(",")[1])
        storeID = line.split(",")[0].strip()
        foodhub_web = line.split(",")[3].strip()
        Gp = line.split(",")[4].strip()
        secret = line.split(",")[5].strip()
        SNO = line.split(",")[6].strip()
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("'''''''''''''''''''''''''''''''''''''''")
        print(foodhub_web)
        print("*")
        print("*")
        print("*")
       #url_PresMadrid="https://www.google.com/search?q=Bursley+Burslem+ST6+3EX&oq"
        url_PresMadrid=line.split(",")[2].strip()
        name=line.split(",")[1].strip()
        ORDER=getorder_function(url_PresMadrid)
        print("ORDERRRRRRRRRRRRRRRRRR",ORDER)
        if "\t" in name:
            name=name
        else:
            name=name+"\t"
        try:
            params = {
    'q': searchedname,
    'oq': searchedname,
    'aqs': '',
}

            req_PresPadrid = requests.get('https://www.google.com/search', params=params, cookies=cookies, headers=headers)

            #req_PresPadrid = requests.get(url_PresMadrid)
            print(url_PresMadrid)
            soup_PresMadrid = BeautifulSoup(req_PresPadrid.content, "html.parser")
    #        if(req_PresPadrid.status == 200 and len(soup_PresMadrid.findAll("div", {"class": "skVgpb"})) != 0):
            print("LENGTH")
            print(len(soup_PresMadrid.findAll("div", {"class": "skVgpb"})))
#            print(soup_PresMadrid.findAll("div", {"class": "kCrYT"}))
            if(req_PresPadrid.status_code == 429):
                with open("/home/t2sadmin/exception429.csv", 'a') as f2:
                    data1 = ["wait 10mins","and continue",count,"exception429",filename]
                    writer = csv.writer(f2)
                    writer.writerow(data1)
                    break
            if(req_PresPadrid.status_code == 200 and len(soup_PresMadrid.findAll("div", {"class": "skVgpb"}))==0):
                var="NO WEBSITE FIELDS FOUND"
                up=update_gpin_MS(storeID,secret,var,foodhub_web)
                data=[SNO,storeID,name,"NO WEBSITE FIELDS FOUND","-",foodhub_web,Gp,secret,ORDER,up]
         #       update_gpin_MS(data1)
                with open(filename, 'a') as f1:
                    writer = csv.writer(f1)
                    writer.writerow(data)

            print("LENNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")
            print(req_PresPadrid)
            print(len(soup_PresMadrid.findAll("div", {"class": "skVgpb"}))) 
            for data in soup_PresMadrid.findAll("div", {"class": "skVgpb"}):
                print("**********************************",data)
                elms = data.select("a")
#               elms = data.select("div.VGHMXd a")
                print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE",elms)
    #            data=[name,"NO WEBSITE FIELDS FOUND","-"]
                #print(elms)
    #            data=[name,"NO WEBSITE FIELDS FOUND","-"]
                for i in elms:
                    a=i["href"]
                    #print(a.replace('/url?q=', ''))
                    url=a.replace('/url?q=', '')
                    print("&&&&&&&&&&&&&&*****************************************************************",url)
                    if(url.startswith("https://maps.google.com/") and not(len(elms)) == 1):
                       # data=[name,"NO WEBSITE FIELDS FOUND","-"]
                        pass
                    elif(url.startswith("https://maps.google.com/") and len(elms) == 1):
                            print("TTTTTTTTTTTTTTTTTTTTTTTTTT")
                            print("RRRR")
                            print("UUUUU")
                         #   data=[storeID,name,"NO WEBSITE FIELDS FOUND","-",foodhub_web,Gp,secret,ORDER]
                            var="NO WEBSITE FIELDS FOUND"
                            up=update_gpin_MS(storeID,secret,var,foodhub_web)
                            data=[SNO,storeID,name,"NO WEBSITE FIELDS FOUND","-",foodhub_web,Gp,secret,ORDER,up]
                            with open(filename, 'a') as f1:
                                writer = csv.writer(f1)

        # write the data
                                writer.writerow(data)
                    else:
                        url=url.split("/&")[0].split("&")[0].split("%")[0]
                        print(url)
                        try:
                            response = requests.get(url, timeout=15)
                            res = "ok"
                            print(res)
                            response = requests.get(url)
                            if(response.status_code == 200 or response.status_code==404 or response.status_code == 403 or response.status_code == 406 or response.status_code == 510 or response.status_code == 463 or response.status_code == 503):
                                res == "ok"
#                                myfunction()
                                var = myfunction()
                                print(var)
                            else:
                                var = "website not reached"
                                print("***********************************",var)
          #                  update_gpin_Ms(storeID,secret,var)
#                            data=[storeID,name,url,var,foodhub_web,Gp,secret,ORDER,update_MS]
                            up=update_gpin_MS(storeID,secret,var,foodhub_web)
                           # update_MS="check"
                            data=[SNO,storeID,name,url,var,foodhub_web,Gp,secret,ORDER,up]#date_MS]
                            with open(filename, 'a') as f1:
                                writer = csv.writer(f1)

        # write the data
                                writer.writerow(data)
                           # continue
                       # except requests.ConnectionError:
    #                    except requests.ChunkedEncodingError:
                       # except (requests.ConnectionError, requests.ChunkedEncodingError) as err:
                        except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError,requests.exceptions.TooManyRedirects,requests.exceptions.ContentDecodingError,requests.exceptions.MissingSchema,requests.exceptions.ReadTimeout) as err:
                            print("EXEC")
                           # time.sleep(50)
                            print("Can't connect to the site, sorry")
                            res = "not ok"
                            print(res)
#                            data=[storeID,name,url,"SHOWN WEBSITE URL NOT REACHABLE or NOT ABLE TO CONNECT",foodhub_web,Gp,secret,ORDER]
                            var="SHOWN WEBSITE URL NOT REACHABLE or NOT ABLE TO CONNECT"
                            up=update_gpin_MS(storeID,secret,var,foodhub_web)
                            data=[SNO,storeID,name,url,"SHOWN WEBSITE URL NOT REACHABLE or NOT ABLE TO CONNECT",foodhub_web,Gp,secret,ORDER,up]
                            with open(filename, 'a') as f1:
                                writer = csv.writer(f1)
                                writer.writerow(data)
                            continue                            

        except (requests.exceptions.ConnectionError,requests.exceptions.MissingSchema) as error:
            print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
            print("*")
            print("MMMMMMMMMMMMMMMMMMMMMM")
            print("*")
            data1 = ["wait 10mins","and continue",count,filename]
            count=count+1
            with open("/home/t2sadmin/connectioncheck.csv", 'a') as f2:
#                data1 = ["wait 10mins","and continue",count]
                writer = csv.writer(f2)
                writer.writerow(data1)
            time.sleep(200)
            continue

            req_PresPadrid.close()

#myfile.close()
