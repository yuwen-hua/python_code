import datetime
import json
import os
import time
import urllib

from sea_manage.products import rest_api as api
from sea_manage.untils.response_code import RET
from flask_restplus import Resource
from flask import request, jsonify, current_app, send_file
import requests


from selenium import webdriver

ns = api.namespace('tide', description='潮汐专题模块API')


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


province = ['丹东','丹东新港','石山子','大鹿岛','小长山岛','大窑湾','大连','旅顺新港','金县','葫芦套','长兴岛','鱿鱼圈','营口','老北河口','锦州港','菊花岛','团山角','芷锚湾','山海关','秦皇岛','七里海','京唐港','曹妃甸','崎口','埕口外海','黄骅港','塘沽','东风港','湾湾沟口','东营港','潍坊港','莱州港','龙口','蓬莱','南长山岛','砣矶岛','北隍城岛','烟口','威海','成山角','石岛','张家埠','乳山口','千里岩','女岛港','青岛','黄岛','董家口','日照港','岚山港','连云港','燕尾','滨海港','射阳河口','新洋港','大丰港','弶港','洋口港','吕四','天生港','佘山','崇明','中浚','高桥','吴淞','黄浦公园','芦潮港','金山嘴','绿华山','大戢山','嵊山','乍浦','澉浦','滩浒','海黄山','长涂','岱山','西码头','沈家门','定海','沥港','宁波','镇海','北仑港','崎头角','梅山','西泽','石浦','旗门港','健跳','鱼山','下大陈','海门','海门港','东门村','坎门','大门岛','温州','瑞安','南麂山','三沙','赛岐','帮门','罗源迹头','黄岐','马尾','福清湾','竹屿','郎官','闽江口-川石','闽江口-琯头','平潭','三江口','秀屿','梯吴','崇武','后渚','泉州','深沪港','围头','石井','厦门','将军澳','石码','东山','马公','基隆','高雄','南澳岛','潮州港','汕头','海门-广东','甲子','汕尾','马鞭洲','惠州港','大亚湾','大鹏湾','香港','蛇口','桂山岛','内伶仃岛','舢舨洲','深圳机场','南沙','海沁','黄埔','广州','北街','横门','珠海-香洲','珠海-九洲港','澳门','东澳岛','大万山','灯笼山','三灶岛','珠海港','横山','井岸','上川岛','北津','海陵山岛','电白','博贺','西葛','茂石化','硇洲岛','湛江','下港','海安','流沙','乌石','下泊','东沙岛','海口','铺前','清澜','博鳌','新村','牙笼港','三亚','莺歌海','东方','洋浦','新盈','马村港','永兴岛','双子礁','永暑礁','中沙群岛－黄岩岛','铁山港','涠洲岛','北海','龙门','企沙','炮台角','防城港','珍珠港','白龙尾']


@ns.route('/test')
class DatasetInfo(Resource):
    @api.doc('copernicus自动下载地址')
    def get(self):
        url = 'http://global-tide.nmdis.org.cn/Api/Service.ashx'
        data = {
            "ApiRequest": {"Server":"User","Command":"GetData","Data":{"code":"T221","date":"2022-09-16"}}
        }
        data = {
            'ApiRequest': (None, json.dumps({"Server":"User","Command":"GetHotSite","Data":{"id":3}}))
        }
        data = 'ApiRequest={"Server":"User","Command":"GetSiteListByGroupID","Data":{"tid":3}}'
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
        res = requests.post(url=url,headers=headers,data=data)
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
        down_path = 'D:/dataSource/tide' + '/' + date_path
        if not os.path.exists(down_path):
            os.makedirs(down_path)
        with open(down_path + '/' + day + '.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(data))
        return jsonify(errno=RET.OK, errmsg="查询成功")

@ns.route('/metas')
class DatasetInfo(Resource):
    @api.doc('潮汐自动下载地址')
    @ns.param('date','日期')
    def get(self):
        """weather自动下载地址"""
        list = []
        date = request.values.get('date')
        date_path = date.replace('-', '\\')
        path = 'D:\\dataSource\\tide' + '\\' + date_path
        for root, dirs, files in os.walk(path):
            for file in files:
                down_path = current_app.config['DOWNLOADS'] + root.split('dataSource')[1]
                down_path = down_path.replace('\\', '/') + '/' + file

                obj =  {
                    "name": file,
                    "size": size_format(os.path.getsize(root + '\\' + file)),
                    "path": root + '\\' + file,
                    "type": "tide",
                    "date": time.strftime("%Y-%m-%d", time.localtime(os.stat(root + '\\' + file).st_mtime))
                }
                list.append(obj)
        data = {
            "data": list,
        }
        return jsonify(errno=RET.OK, data=data, errmsg="查询成功")

