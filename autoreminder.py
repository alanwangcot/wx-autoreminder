import requests
import json
from datetime import date

appID = "wxe1136b8c2bf1ef82"
appsecret = "eede467c87e2fbf70a9b45bb335e91ba"
tokenurl = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=" + appID + "&secret=" + appsecret
token = requests.get(tokenurl).json()["access_token"]

wxuserdebug = "oHWB75go3M5mAOuQ6ShTOjOyDCNg"
wxuser = "oHWB75vv2Qr73u48SDQcLaAGPPUo"
template_id = "3zp6LEP1az7HvhLw_ykP0cyNwYz-gkgfeSDAaGozMFo"


warn_url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=warnsum&lang=tc"
response = requests.get(warn_url)
response.encoding = 'utf-8'
json_data = response.json()
warning = "没有警告哦"

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

temp_url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=tc"
temp_response = requests.get(temp_url)
temp_response.encoding = 'utf-8'
temp_json_data = temp_response.json()
max = temp_json_data['weatherForecast'][0]['forecastMaxtemp']['value']
min = temp_json_data['weatherForecast'][0]['forecastMintemp']['value']
temp_str = "今日溫度" + str(min) + "度和" + str(max) + "度之間。"

startdate = date(2022,9,5)
enddate = date.today()
days = (enddate - startdate).days

# joke_url = "https://v2.alapi.cn/api/joke/random"
# headers = {'Content-Type': "application/x-www-form-urlencoded"}
# joke_response = requests.request("POST", joke_url, data="token=0e4TW86CjLPwmkSy", headers = headers)
# joke_data = joke_response.json()

# peom_token = "1PtlywpoukHYcEODbBbnyFLuEdFW3JOG"
# poem_headers = {'X-User-Token': peom_token}
poem_url = "https://v1.jinrishici.com/shuqing/sinian"
poem_response = requests.get(poem_url)
poem_data = poem_response.json()



jokes = [
    "我说：“你是猪。”你说：“我是猪才怪!”从此我就叫你猪才怪。终于有一天，你忍不住当着众人的面对我吼道：“我不是猪才怪!",
    "都说海底捞服务好，不是没道理，我上次吃了霸王餐，服务员亲自报警。警察来了还给警察递热毛巾，走的时候还给手铐上挂一袋妙脆角。",
    "有个少年立志要当上海贼王，于是上海人民纷纷锁紧了房门。",
    "从前有一只大鱼和一只小鱼。有一天，小鱼问大鱼：大～鱼～大～鱼～你～平～常～喜～欢～吃～什～么～丫。大鱼说：我～喜～欢～吃～说～话～慢～的～小～鱼。然后小鱼说：喔，酱紫，造了！",

    "冬天，农夫在路上捡到一条冬眠的蛇，就把它放在怀里带回了家。到家了蛇还没醒，！农夫就把它放到了酒罐子里准备泡酒喝。第二年春天，蛇从冬眠里醒来，从酒罐子里爬出来说的第一句话就是：“我他妈也是醉了。",
    '看到没，那棵树快要枯了\n那我过去抱抱它',
    "她生气了，夺门而出，他冲到楼下拦住她，把门夺了回来",
    "前几天去医院体检了，好开心，仅仅只花了200块钱就检查出六个病来。",
    "诸葛亮:“风啊，你向西刮”风:“你才像西瓜”！！！",
    "开车路过一个小泥潭，小泥潭溅的水好响，原来是好响泥。",
    
    "那天家里卧室隔壁的灯一闪一闪的，叫来维修师傅，师傅问什么问题？我说：“卧室隔壁灯太闪”他：“抓住爱情的藤蔓？",
    "甲:你有《时间简史》吗?乙:神经病，我有时间捡那玩意儿干啥?",
    "从前有只麋鹿，它在森林里玩儿，不小心走丢了。于是它给它的好朋友长颈鹿打电话：“喂…我迷路啦。”长颈鹿听见了回答说：“喂，我长颈鹿啦~ ",
    "在商场一个婴儿一直在哭搞得我很烦，朋友劝我要换位思考。现在我坐在婴儿车里，还是很烦。",
        "这是拿什么肉煲的汤？母鸡啦",

]
# weather_msg = weather_data["wea"] + "，温度" + weather_data["tem2"] + "~" + weather_data["tem1"] + "度，空气湿度" + weather_data["humidity"] + "，还有" + weather_data["win_speed"] + "风。"
# if weather_data["wea_img"] == "qing" or weather_data["wea_img"] == "yun":
#     weather_msg += "天气不错，要有好心情哦！"

# if weather_data["wea_img"] == "xue" or weather_data["wea_img"] == "yu" or weather_data["wea_img"] == "lei":
#     weather_msg += "下雨天，要记得带伞呀！"
# if weather_data["wea_img"] == "shachen" or weather_data["wea_img"] == "wu" or weather_data["wea_img"] == "yin":
#     weather_msg += "没有太阳，适合宅家！"
# if weather_data["wea_img"] == "bingbao":
#     weather_data += "什么鬼天气，竟然有冰雹，快在家里躲着吧！"

if days >= 0:
    joke_msg = jokes[days]
else:
    joke_msg = "冇更多笑话啦！不如同我倾计呀，我来撩你笑:)"

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

def send_msg(send_data):
    url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=" + token
    response = requests.post(url, data=json.dumps(send_data))
    with open("log.json", 'a') as f:
        f.write(enddate.strftime("%Y年%m月%d日"))
        f.write(response.text)

    return response.json



if __name__ == '__main__':
    send_msg(data_debug)