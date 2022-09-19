import json
import os


from sea_manage.products import rest_api as api
from sea_manage.untils.response_code import RET
from flask_restplus import Resource
from flask import request, jsonify, current_app, send_file
import requests


from selenium import webdriver

ns = api.namespace('weather', description='预报专题模块API')

def size_format(size):
    if size < 1000:
        return '%i' % size + 'size'
    elif 1000 <= size < 1000000:
        return '%.1f' % float(size/1000) + 'KB'
    elif 1000000 <= size < 1000000000:
        return '%.1f' % float(size/1000000) + 'MB'
    elif 1000000000 <= size < 1000000000000:
        return '%.1f' % float(size/1000000000) + 'GB'
    elif 1000000000000 <= size:
        return '%.1f' % float(size/1000000000000) + 'TB'

province = ['乌鲁木齐','呼和浩特','银川','西宁','兰州','西安','郑州','太原','石家庄','北京','拉萨','天津','济南','合肥','武汉','杭州','沈阳','哈尔滨','长春','上海','成都','重庆','长沙','南昌','贵阳','海口','深圳','广州','澳门','香港','台湾','台北','昆明']

@ns.route('/test')
class DatasetInfo(Resource):
    @api.doc('copernicus自动下载地址')
    def get(self):
        """测试添加数据"""
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
        with open(down_path + '/weather.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(data))

@ns.route('/metas')
class DatasetInfo(Resource):
    @api.doc('weather自动下载地址')
    @ns.param('date','日期')
    def get(self):
        """weather自动下载地址"""
        list = []
        date = request.values.get('date')
        date_path = date.replace('-', '\\')
        path = 'D:\\dataSource\\weather' + '\\' + date_path
        for root, dirs, files in os.walk(path):
            for file in files:
                down_path = current_app.config['DOWNLOADS'] + root.split('dataSource')[1]
                down_path = down_path.replace('\\', '/') + '/' + file

                obj =  {
                    "name": file,
                    "size": size_format(os.path.getsize(root + '\\' + file)),
                    "path": root + '\\' + file,
                    "type": "weather",
                    "date": date
                }
                list.append(obj)
        data = {
            "data": list,
        }
        return jsonify(errno=RET.OK, data=data, errmsg="查询成功")
