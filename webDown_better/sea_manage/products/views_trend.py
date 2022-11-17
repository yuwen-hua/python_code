import json
import os
from sea_manage.products import rest_api as api
from sea_manage.untils.response_code import RET
from flask_restplus import Resource
from flask import request, jsonify, send_file
import requests

ns = api.namespace('trend', description='潮流专题模块API')


# def size_format(size):
#     if size < 1000:
#         return '%i' % size + 'size'
#     elif 1000 <= size < 1000000:
#         return '%.1f' % float(size / 1000) + 'KB'
#     elif 1000000 <= size < 1000000000:
#         return '%.1f' % float(size / 1000000) + 'MB'
#     elif 1000000000 <= size < 1000000000000:
#         return '%.1f' % float(size / 1000000000) + 'GB'
#     elif 1000000000000 <= size:
#         return '%.1f' % float(size / 1000000000000) + 'TB'
#
#
# province = ['大三山水道', '老铁山水道', '成山角', '连云港航线', '舟山渔场1号站', '黄浦', '长江口航线', '长江口附近', '长江口渔场', '杭州湾口', '北仑附近', '舟山航道-沈家门',
#             '温州至上海航线', '舟山航道-册子山附近', '浙江至上海航线', '鱼山渔场', '台湾海峡北口1号站', '台湾海峡北口2号站', '台湾海峡南口1号站', '台湾海峡南口2号站', '七洲岛北',
#             '琼州海峡西口2号站', '琼州海峡中部', '琼州海峡东口1号站', '涠洲岛附近']


@ns.route('/get_trend_station')
class TrendStation(Resource):
    @api.doc('获取国内潮位站信息')
    def get(self):
        """获取国内潮流站信息"""
        province = [{'code': 'GNWF001', 'name': '大三山水道'}, {'code': 'GNWF004', 'name': '老铁山水道'},
                    {'code': 'GNWF005', 'name': '成山角'}, {'code': 'GNWF012', 'name': '黄浦'},
                    {'code': 'GNWF014', 'name': '长江口航线'}, {'code': 'GNWF015', 'name': '杭州湾口'},
                    {'code': 'GNWF016', 'name': '北仑附近'}, {'code': 'GNWF018', 'name': '舟山航道-沈家门'},
                    {'code': 'GNWF019', 'name': '温州至上海航线'}, {'code': 'GNWF025', 'name': '台湾海峡北口1号站'},
                    {'code': 'GNWF026', 'name': '台湾海峡北口2号站'}, {'code': 'GNWF028', 'name': '台湾海峡南口1号站'},
                    {'code': 'GNWF029', 'name': '台湾海峡南口2号站'}, {'code': 'GNWF033', 'name': '涠洲岛附近'},
                    {'code': 'GNWF035', 'name': '七洲岛北'}, {'code': 'GNWF037', 'name': '琼州海峡西口2号站'},
                    {'code': 'GNWF039', 'name': '琼州海峡中部'}, {'code': 'GNWF040', 'name': '琼州海峡东口1号站'},
                    {'code': 'GNXZ009', 'name': '连云港航线'}, {'code': 'GNXZ013', 'name': '长江口附近'},
                    {'code': 'GNXZ017', 'name': '舟山航道-册子山附近'}, {'code': 'GNXZ020', 'name': '浙江至上海航线'},
                    {'code': 'GNXZ021', 'name': '长江口渔场'}, {'code': 'GNXZ022', 'name': '舟山渔场1号站'},
                    {'code': 'GNXZ024', 'name': '鱼山渔场'}]
        return jsonify(errno=RET.OK, data=province, errmsg="查询成功")


@ns.route('/get_trend')
class Tidal(Resource):
    @api.doc('获取潮流列表')
    @ns.param('tide_time', '时间')
    @ns.param('code', '潮位站代码')
    def get(self):
        """获取潮流列表"""
        tide_time = request.values.get('tide_time')
        code = request.values.get('code')
        url = 'http://global-tide.nmdis.org.cn/Api/Service.ashx'
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
        if not all([tide_time, code]):
            return jsonify(errno=RET.PARAMERR, errmsg="参数不完整")
        json = []
        for c in code.split(','):
            requ_data = 'ApiRequest={"Server":"User","Command":"GetData","Data":{"code":"' + c + '","date":"' + tide_time + '"}}'
            response = requests.post(url=url, headers=headers, data=requ_data)
            if response.status_code != 200:
                return jsonify(errno=RET.OK, data="网络地址无法访问,请联系管理员")
            res = response.json()['Data']
            json.append(res)
        # requ_data = 'ApiRequest={"Server":"User","Command":"GetData","Data":{"code":"' + code + '","date":"' + tide_time + '"}}'
        # response = requests.post(url=url, headers=headers, data=requ_data)
        # if response.status_code != 200:
        #     return jsonify(errno=RET.OK, data="网络地址无法访问,请联系管理员")
        # res = response.json()['Data']
        # date_path = tide_time.replace('-', '//')
        # down_path = 'D:/dataSource/trend' + '/' + date_path
        # if not os.path.exists(down_path):
        #     os.makedirs(down_path)
        # with open(down_path + '/' + code + '.json', 'w', encoding='utf-8') as f:
        #     f.write(json.dumps(res))
        return jsonify(errno=RET.OK, data=json, errmsg="查询成功")


@ns.route('/down_trend')
class Tidal(Resource):
    @api.doc('下载潮流水位')
    @ns.param('tide_time', '时间')
    @ns.param('code', '潮位站代码')
    def get(self):
        """下载潮流水位"""
        tide_time = request.values.get('tide_time')
        code = request.values.get('code')
        url = 'http://global-tide.nmdis.org.cn/Api/Service.ashx'
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
        if not all([tide_time, code]):
            return jsonify(errno=RET.PARAMERR, errmsg="参数不完整")
        json = []
        for c in code.split(','):
            requ_data = 'ApiRequest={"Server":"User","Command":"GetData","Data":{"code":"' + c + '","date":"' + tide_time + '"}}'
            response = requests.post(url=url, headers=headers, data=requ_data)
            if response.status_code != 200:
                return jsonify(errno=RET.OK, data="网络地址无法访问,请联系管理员")
            res = response.json()['Data']
            json.append(res)
        date_path = tide_time.replace('-', '//')
        down_path = 'D:/dataSource/trend' + '/' + date_path
        if not os.path.exists(down_path):
            os.makedirs(down_path)
        with open(down_path + '/' + code + '.json', 'w', encoding='utf-8') as f:
            f.write(str(json))
        return send_file(down_path + '/' + code + '.json', as_attachment=True)
        # return jsonify(errno=RET.OK, data=res, errmsg="查询成功")

# [{'code': 'GNWF001', 'name': '大三山水道'}, {'code': 'GNWF004', 'name': '老铁山水道'}, {'code': 'GNWF005', 'name': '成山角'}, {'code': 'GNWF012', 'name': '黄浦'}, {'code': 'GNWF014', 'name': '长江口航线'}, {'code': 'GNWF015', 'name': '杭州湾口'}, {'code': 'GNWF016', 'name': '北仑附近'}, {'code': 'GNWF018', 'name': '舟山航道-沈家门'}, {'code': 'GNWF019', 'name': '温州至上海航线'}, {'code': 'GNWF025', 'name': '台湾海峡北口1号站'}, {'code': 'GNWF026', 'name': '台湾海峡北口2号站'}, {'code': 'GNWF028', 'name': '台湾海峡南口1号站'}, {'code': 'GNWF029', 'name': '台湾海峡南口2号站'}, {'code': 'GNWF033', 'name': '涠洲岛附近'}, {'code': 'GNWF035', 'name': '七洲岛北'}, {'code': 'GNWF037', 'name': '琼州海峡西口2号站'}, {'code': 'GNWF039', 'name': '琼州海峡中部'}, {'code': 'GNWF040', 'name': '琼州海峡东口1号站'}, {'code': 'GNXZ009', 'name': '连云港航线'}, {'code': 'GNXZ013', 'name': '长江口附近'}, {'code': 'GNXZ017', 'name': '舟山航道-册子山附近'}, {'code': 'GNXZ020', 'name': '浙江至上海航线'}, {'code': 'GNXZ021', 'name': '长江口渔场'}, {'code': 'GNXZ022', 'name': '舟山渔场1号站'}, {'code': 'GNXZ024', 'name': '鱼山渔场'}]

# @ns.route('/test')
# class DatasetInfo(Resource):
#     @api.doc('copernicus自动下载地址')
#     def get(self):
#         """测试添加数据"""
#         url = 'http://global-tide.nmdis.org.cn/Api/Service.ashx'
#         data = {
#             "ApiRequest": {"Server": "User", "Command": "GetData", "Data": {"code": "T221", "date": "2022-09-16"}}
#         }
#         data = {
#             'ApiRequest': (None, json.dumps({"Server": "User", "Command": "GetHotSite", "Data": {"id": 4}}))
#         }
#         data = 'ApiRequest={"Server":"User","Command":"GetSiteListByGroupID","Data":{"tid":4}}'
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
#             "Accept": "application/json, text/javascript, */*; q=0.01",
#             "Accept-Encoding": "gzip, deflate",
#             "Content-Length": "111",
#             "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#             "Accept-Language": "zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",
#             "X-Requested-With": "XMLHttpRequest",
#             "Host": "global-tide.nmdis.org.cn",
#             "Origin": "http://global-tide.nmdis.org.cn",
#             "Referer": "http://global-tide.nmdis.org.cn/Site/Site.html",
#         }
#         # data = bytes(urllib.parse.urlencode(data), encoding="utf-8")
#         res = requests.post(url=url, headers=headers, data=data)
#         if res.status_code != 200:
#             res = requests.post(url)
#         res = res.json()
#         data = {}
#         date = datetime.datetime.now().strftime('%Y-%m-%d')
#         date_path = datetime.datetime.now().strftime('%Y/%m/%d')
#         day = datetime.datetime.now().strftime('%d')
#         provices = []
#         for i in res['Data']:
#             for j in province:
#                 if j == i['Name']:
#                     code = i['Code']
#                     p = {}
#                     p['code'] = code
#                     p['name'] = i['Name']
#                     provices.append(p)
#         #             requ_data = 'ApiRequest={"Server":"User","Command":"GetData","Data":{"code":"' + code + '","date":"' + date + '"}}'
#         #             response = requests.post(url=url, headers=headers, data=requ_data)
#         #             response = response.json()
#         #             data.update({'Data': response['Data']['Data']})
#         #             data.update({'SubData': response['Data']['SubData']})
#         # down_path = 'D:/dataSource/trend' + '/' + date_path
#         print(provices)
#         # if not os.path.exists(down_path):
#         #     os.makedirs(down_path)
#         # with open(down_path + '/' + day + '.json', 'w', encoding='utf-8') as f:
#         #     f.write(json.dumps(data))
#         # return jsonify(errno=RET.OK, errmsg="查询成功")
#
#
# @ns.route('/metas')
# class DatasetInfo(Resource):
#     @api.doc('潮流下载地址')
#     @ns.param('date', '日期')
#     def get(self):
#         """潮流下载地址"""
#         list = []
#         date = request.values.get('date')
#         date_path = date.replace('-', '\\')
#         path = 'D:\\dataSource\\trend' + '\\' + date_path
#         for root, dirs, files in os.walk(path):
#             for file in files:
#                 down_path = current_app.config['DOWNLOADS'] + root.split('dataSource')[1]
#                 down_path = down_path.replace('\\', '/') + '/' + file
#
#                 obj = {
#                     "name": file,
#                     "size": size_format(os.path.getsize(root + '\\' + file)),
#                     "path": root + '\\' + file,
#                     "type": "trend",
#                     "date": time.strftime("%Y-%m-%d", time.localtime(os.stat(root + '\\' + file).st_mtime))
#                 }
#                 list.append(obj)
#         data = {
#             "data": list,
#         }
#         return jsonify(errno=RET.OK, data=data, errmsg="查询成功")
