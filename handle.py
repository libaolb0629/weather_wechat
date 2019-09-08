import requests
import json
import time
class Handel():
    def __init__(self,gaodeApi,city_key):
        self.access_token = self.get_access_token()
        self.url = gaodeApi
        self.cityKey = city_key

    def get_access_token(self):
        url = 'https://api.weixin.qq.com/cgi-bin/token'
        data = {
            'grant_type': 'client_credential',
            'appid': 'wx7541c0c21aa8be11',
            'secret': '75b65bcfbe9866703a326105e6c0bea0'
        }
        ret = requests.get(url, data)
        token_data = (json.loads(ret.text))
        self.access_token = token_data.get('access_token')
        print('获取token成功')


    def get_user(self):
        self.get_access_token()
        url = 'https://api.weixin.qq.com/cgi-bin/user/get'
        param = {
            'access_token':self.access_token,
            'next_openid':'' #	第一个拉取的OPENID，不填默认从头开始拉取
        }
        ret= requests.get(url, param)
        users = json.loads(ret.text)['data'].get('openid') ##list
        print('获取用户列表完成')
        return users
    def getWeather(self):
        ret = requests.get(self.url,self.cityKey)
        if ret.status_code ==200:
            weathers = json.loads(ret.text)
            print('获取天气成功')
        else:
            print('获取天气失败')

        return  weathers['lives'][0]
    def send(self,openid,weather):
        url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token='+self.access_token
        date = time.strftime("%Y-%m-%d", time.localtime())
        #天气模板
        data = {
            "touser": openid,
            "template_id": "u6j9_lD98uyjzbuWDQs1DHzWcrXaFGpHIHgNxhTKRDU",
            "url": "http://baogegh.top",
            "data": {
                "date": {
                    "value": date,
                    "color": "#173177"
                },

                "temperature": {
                    "value": weather['temperature'],
                    "color": "#173177"
                },
                "location": {
                    "value": weather['province']+' '+weather['city'],
                    "color": "#173177"
                },
                "weather": {
                    "value": weather['weather'],
                    "color": "#173177"
                },
                "reporttime": {
                    "value": weather['reporttime'],
                    "color": "#173177"
                },
                "windpower": {
                    "value": weather['windpower'],
                    "color": "#173177"
                },
            }
        }
        ret = requests.post(url,json=data)
        if ret.status_code==200:
            data = json.loads(ret.text)
            if data['errcode'] ==0:
                return True
            else:
                return False
        else:
            return False
