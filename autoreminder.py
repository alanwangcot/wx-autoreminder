import requests
import json
from datetime import date

appID = "wxe1136b8c2bf1ef82"
appsecret = "eede467c87e2fbf70a9b45bb335e91ba"
tokenurl = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=" + appID + "&secret=" + appsecret
token = requests.get(tokenurl).json()["access_token"]

wxuserdebug = "oHWB75go3M5mAOuQ6ShTOjOyDCNg"
wxuser = "oHWB75vv2Qr73u48SDQcLaAGPPUo"
template_id = "EjK-oxpO8tnWEcZDc6bg-HJ-b684DQH3i2viwAzeFNk"


warn_url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=warnsum&lang=tc"
response = requests.get(warn_url)
response.encoding = 'utf-8'
json_data = response.json()
warning = "没有警告哦"
print("got warning")

if 'WTCSGNL' in json_data:
    warning = "有風球警告！" + json_data['WTCSGNL']['type']
# elif json_data['WFIRE'] or json_data['WFROST'] or json_data['WHOT'] or json_data['WCOLD'] or json_data['WMSGNL'] or json_data['WRAIN'] or json_data['WTMW'] or json_data['WL'] or json_data['WFNTSA'] or json_data['WTS']:
elif 'WFIRE' in json_data:
    warning = "有" + json_data['WFIRE']['name']
elif 'WFROST' in json_data:
    warning = "有" + json_data['WFROST']['name']
elif 'WHOT' in json_data:
    warning = "有" + json_data['WHOT']['name']
elif 'WCOLD' in json_data:
    warning = "有" + json_data['WCOLD']['name']
elif 'WMSGNL' in json_data:
    warning = "有" + json_data['WMSGNL']['name']
elif 'WRAIN' in json_data:
    warning = "有" + json_data['WRAIN']['name']
elif 'WTMW' in json_data:
    warning = "有" + json_data['WTMW']['name']
elif 'WL' in json_data:
    warning = "有" + json_data['WL']['name']
elif 'WFNTSA' in json_data:
    warning = "有" + json_data['WFNTSA']['name']
elif 'WTS' in json_data:
    warning = "有" + json_data['WTS']['name']
    
wea_url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=flw&lang=tc"
response = requests.get(wea_url)
response.encoding = 'utf-8'
json_data = response.json()
forecast = json_data['forecastDesc']
print("got forecast msg")

temp_url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=tc"
temp_response = requests.get(temp_url)
temp_response.encoding = 'utf-8'
temp_json_data = temp_response.json()
max = temp_json_data['weatherForecast'][0]['forecastMaxtemp']['value']
min = temp_json_data['weatherForecast'][0]['forecastMintemp']['value']
temp_str = "今日溫度" + str(min) + "度和" + str(max) + "度之間。"
print("got temp msg")

startdate = date(2022,8,22)
enddate = date.today()
days = (enddate - startdate).days

joke_url = "https://api.vvhan.com/api/joke?type=json"
# headers = {'Content-Type': "application/x-www-form-urlencoded"}
# joke_response = requests.request("POST", joke_url, data="token=0e4TW86CjLPwmkSy", headers = headers)
joke_response = requests.get(joke_url)
joke_data = joke_response.json()
print("got joke")
joke_msg = joke_data["joke"]

data_debug = {
    "touser": wxuserdebug,
    "template_id": template_id,
    "url": "https://hk.sz.gov.cn/userPage/login",
    "data": {
        "dateMsg": {
            "value": enddate.strftime("%Y年%m月%d日"),
            "color": "#173177"
        },
        "weatherMsg": {
            "value":  temp_str + "\n" + forecast,
            "color": "#545454"
        },
        "warningMsg": {
            "value": warning + "！",
            "color": "#520"
        },
        "daysAgoMsg": {
            "value": str(days + 1),
            "color": "#173177"
        },
        # "jokeTitle": {
        #     "value": joke_data['data']['title'],
        #     "color": "#6B238E"
        # },
        "jokeContent": {
            "value": joke_msg,
            "color": "#545454"
        }
    }
}
data = {
    "touser": wxuser,
    "template_id": template_id,
    "url": "https://hk.sz.gov.cn/userPage/login",
    "data": {
        "dateMsg": {
            "value": enddate.strftime("%Y年%m月%d日"),
            "color": "#173177"
        },
        "weatherMsg": {
            "value":  temp_str + "\n" + forecast,
            "color": "#545454"
        },
        "warningMsg": {
            "value": warning + "！",
            "color": "#520"
        },
        "daysleftMsg": {
            "value": str(days + 1),
            "color": "#173177"
        },
        # "jokeTitle": {
        #     "value": joke_data['data']['title'],
        #     "color": "#6B238E"
        # },
        "jokeContent": {
            "value": joke_msg,
            "color": "#545454"
        }
    }
}

# print(data)
url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=" + token
response1 = requests.post(url, data=json.dumps(data_debug))
print("message sent to API!")
# response2 = requests.post(url, data=json.dumps(data))
with open('log.json', 'w') as f:
    f.write(startdate.strftime("%Y年%m月%d日"))
    f.write(str(response1.json()))
    # f.write(str(response2.json()))
    # f.close()
