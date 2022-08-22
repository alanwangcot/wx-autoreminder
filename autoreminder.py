import requests
import json
from datetime import date

appID = "" #从https://mp.weixin.qq.com/debug/cgi-bin/sandboxinfo?action=showinfo&t=sandbox/index登录获取
appsecret = "" #同上
tokenurl = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=" + appID + "&secret=" + appsecret
token = requests.get(tokenurl).json()["access_token"]

wxuser = "" #想要发给谁，让ta关注后从上面链接获取openID
template_id = "" #从公众号平台创建模板获取

#在http://www.tianqiapi.com/获取以下appID和appsecret和城市id，记得删掉{{}}
weather_url = "https://v0.yiketianqi.com/api?unescape=1&version=v61&appid={{自己输入}}&appsecret={{自己输入}}&cityid={{自己查找城市id}}"
weather_response = requests.get(weather_url)
weather_data = weather_response.json()

#日期自行填写，比如发给ta就用ta的生日
enddate = date(2022,9,5)
startdate = date.today()
days = (enddate - startdate).days

data = { #在微信公众号接口平台使用{{keyword.DATA}}接收'value'的字符串。微信接口模板中还可以添加其它固定的字符串。
    "touser": wxuser,
    "template_id": template_id,
    "url": "", #发到公众号的提醒点击就会跳转到这个url，可以留空
    "data": {
        "dateMsg": {
            "value": str(weather_data["date"]),
            "color": "#173177"
        },
        "weatherMsg": {
            "value":  weather_data["wea"] + ",温度" + weather_data["tem"] + "度, 空气湿度" + weather_data["humidity"],
            "color": "#000"
        },
        "daysleftMsg": {
            "value": str(days),
            "color": "#173177"
        } #可以增加更多的keyword和信息
    }
}
url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=" + token
response = requests.post(url, data=json.dumps(data))
print(response.json())