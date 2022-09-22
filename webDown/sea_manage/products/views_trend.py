import datetime
import json
import os
import time

from sea_manage.products import rest_api as api
from sea_manage.untils.response_code import RET
from flask_restplus import Resource
from flask import request, jsonify, current_app, send_file
import requests


from selenium import webdriver

ns = api.namespace('trend', description='潮流专题模块API')

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


province = ['大三山水道','老铁山水道','成山角','连云港航线','舟山渔场1号站','黄浦','长江口航线','长江口附近','长江口渔场','杭州湾口','北仑附近','舟山航道-沈家门','温州至上海航线','舟山航道-册子山附近','浙江至上海航线','鱼山渔场','台湾海峡北口1号站','台湾海峡北口2号站','台湾海峡南口1号站','台湾海峡南口2号站','七洲岛北','琼州海峡西口2号站','琼州海峡中部','琼州海峡东口1号站','涠洲岛附近']

@ns.route('/test')
class DatasetInfo(Resource):
    @api.doc('copernicus自动下载地址')
    def get(self):
        """测试添加数据"""
        url = 'http://global-tide.nmdis.org.cn/Api/Service.ashx'
        data = {
            "ApiRequest": {"Server": "User", "Command": "GetData", "Data": {"code": "T221", "date": "2022-09-16"}}
        }
        data = {
            'ApiRequest': (None, json.dumps({"Server": "User", "Command": "GetHotSite", "Data": {"id": 4}}))
        }
        data = 'ApiRequest={"Server":"User","Command":"GetSiteListByGroupID","Data":{"tid":4}}'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Content-Length": "111",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Accept-Language": "zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",
            "X-Requested-With": "XMLHttpRequest",
            "Host": "global-tide.nmdis.org.cn",
            "Origin": "http://global-tide.nmdis.org.cn",
            "Referer": "http://global-tide.nmdis.org.cn/Site/Site.html",
        }
        print(headers)
        # data = bytes(urllib.parse.urlencode(data), encoding="utf-8")
        res = requests.post(url=url, headers=headers, data=data)
        print(res)
        if res.status_code != 200:
            res = requests.post(url)
        res = res.json()
        data = {}
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        date_path = datetime.datetime.now().strftime('%Y/%m/%d')
        day = datetime.datetime.now().strftime('%d')
        for i in res['Data']:
            for j in province:
                if j == i['Name']:
                    code = i['Code']
                    requ_data = 'ApiRequest={"Server":"User","Command":"GetData","Data":{"code":"' + code + '","date":"' + date + '"}}'
                    print(requ_data)
                    response = requests.post(url=url, headers=headers, data=requ_data)
                    response = response.json()
                    data.update({'Data': response['Data']['Data']})
                    data.update({'SubData': response['Data']['SubData']})
        down_path = 'D:/dataSource/trend' + '/' + date_path
        if not os.path.exists(down_path):
            os.makedirs(down_path)
        with open(down_path + '/' + day + '.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(data))
        return jsonify(errno=RET.OK, errmsg="查询成功")


@ns.route('/metas')
class DatasetInfo(Resource):
    @api.doc('潮流下载地址')
    @ns.param('date','日期')
    def get(self):
        """潮流下载地址"""
        list = []
        date = request.values.get('date')
        date_path = date.replace('-', '\\')
        path = 'D:\\dataSource\\trend' + '\\' + date_path
        for root, dirs, files in os.walk(path):
            for file in files:
                down_path = current_app.config['DOWNLOADS'] + root.split('dataSource')[1]
                down_path = down_path.replace('\\', '/') + '/' + file

                obj =  {
                    "name": file,
                    "size": size_format(os.path.getsize(root + '\\' + file)),
                    "path": root + '\\' + file,
                    "type": "trend",
                    "date": time.strftime("%Y-%m-%d", time.localtime(os.stat(root + '\\' + file).st_mtime))
                }
                list.append(obj)
        data = {
            "data": list,
        }
        return jsonify(errno=RET.OK, data=data, errmsg="查询成功")

