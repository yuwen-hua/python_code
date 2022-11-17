import json
import os

import requests

province = ['乌鲁木齐', '呼和浩特', '银川', '西宁', '兰州', '西安', '郑州', '太原', '石家庄', '北京', '拉萨', '天津', '济南', '合肥', '武汉', '杭州', '沈阳',
            '哈尔滨', '长春', '上海', '成都', '重庆', '长沙', '南昌', '贵阳', '海口', '深圳', '广州', '澳门', '香港', '台湾', '台北', '昆明']


class Weather():
    def __init__(self):
        url = 'https://weather.cma.cn/api/map/weather/1'
        res = requests.get(url)
        if res.status_code != 200:
            res = requests.get(url)
        res = res.json()
        data = {}
        for i in res['data']['city']:
            for j in province:
                if j == i[1]:
                    # data.i[1] = i
                    data.update({i[1]: i})
        down_path = 'D:/dataSource/weather' + '/' + res['data']['date']
        if not os.path.exists(down_path):
            os.makedirs(down_path)
        with open(down_path + '/' + res['data']['date'][8:] + '.txt', 'w', encoding='utf-8') as f:
            f.write(json.dumps(data))
