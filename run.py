import requests
import json
import logging
from handle import Handel

gaode_api = 'https://restapi.amap.com/v3/weather/weatherInfo'
city_key ={
    'city':350206, #城市code xiamen
    'key':'528b0342db8adb2889544b8962b2b34f'#高德天气api的apikey
}

if __name__ =='__main__':
    weather = Handel(gaode_api,city_key)
    weathers_data = weather.getWeather()
    users = weather.get_user()
    for openid in users:
        while True:
            ret = weather.send(openid,weathers_data)
            if ret:
                break
        print('发送完成{}'.format(openid))
    print('全部发送完成')
