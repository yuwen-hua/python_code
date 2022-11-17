import json
import os
import time

from sea_manage.products import rest_api as api
from sea_manage.untils.response_code import RET
from flask_restplus import Resource
from flask import request, jsonify, current_app, send_file
import requests

ns = api.namespace('tide', description='潮汐专题模块API')


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


# province = ['丹东', '丹东新港', '石山子', '大鹿岛', '小长山岛', '大窑湾', '大连', '旅顺新港', '金县', '葫芦套', '长兴岛', '鱿鱼圈', '营口', '老北河口', '锦州港',
#             '菊花岛', '团山角', '芷锚湾', '山海关', '秦皇岛', '七里海', '京唐港', '曹妃甸', '崎口', '埕口外海', '黄骅港', '塘沽', '东风港', '湾湾沟口', '东营港',
#             '潍坊港', '莱州港', '龙口', '蓬莱', '南长山岛', '砣矶岛', '北隍城岛', '烟口', '威海', '成山角', '石岛', '张家埠', '乳山口', '千里岩', '女岛港', '青岛',
#             '黄岛', '董家口', '日照港', '岚山港', '连云港', '燕尾', '滨海港', '射阳河口', '新洋港', '大丰港', '弶港', '洋口港', '吕四', '天生港', '佘山', '崇明',
#             '中浚', '高桥', '吴淞', '黄浦公园', '芦潮港', '金山嘴', '绿华山', '大戢山', '嵊山', '乍浦', '澉浦', '滩浒', '海黄山', '长涂', '岱山', '西码头',
#             '沈家门', '定海', '沥港', '宁波', '镇海', '北仑港', '崎头角', '梅山', '西泽', '石浦', '旗门港', '健跳', '鱼山', '下大陈', '海门', '海门港', '东门村',
#             '坎门', '大门岛', '温州', '瑞安', '南麂山', '三沙', '赛岐', '帮门', '罗源迹头', '黄岐', '马尾', '福清湾', '竹屿', '郎官', '闽江口-川石', '闽江口-琯头',
#             '平潭', '三江口', '秀屿', '梯吴', '崇武', '后渚', '泉州', '深沪港', '围头', '石井', '厦门', '将军澳', '石码', '东山', '马公', '基隆', '高雄',
#             '南澳岛', '潮州港', '汕头', '海门-广东', '甲子', '汕尾', '马鞭洲', '惠州港', '大亚湾', '大鹏湾', '香港', '蛇口', '桂山岛', '内伶仃岛', '舢舨洲',
#             '深圳机场', '南沙', '海沁', '黄埔', '广州', '北街', '横门', '珠海-香洲', '珠海-九洲港', '澳门', '东澳岛', '大万山', '灯笼山', '三灶岛', '珠海港',
#             '横山', '井岸', '上川岛', '北津', '海陵山岛', '电白', '博贺', '西葛', '茂石化', '硇洲岛', '湛江', '下港', '海安', '流沙', '乌石', '下泊', '东沙岛',
#             '海口', '铺前', '清澜', '博鳌', '新村', '牙笼港', '三亚', '莺歌海', '东方', '洋浦', '新盈', '马村港', '永兴岛', '双子礁', '永暑礁', '中沙群岛－黄岩岛',
#             '铁山港', '涠洲岛', '北海', '龙门', '企沙', '炮台角', '防城港', '珍珠港', '白龙尾']


@ns.route('/get_tide_station')
class TideAndTrendStation(Resource):
    @api.doc('获取国内潮位站信息')
    def get(self):
        """获取国内潮汐站信息"""
        province = [{'code': 'T001', 'name': '丹东'}, {'code': 'T002', 'name': '丹东新港'}, {'code': 'T003', 'name': '石山子'},
                    {'code': 'T004', 'name': '大鹿岛'}, {'code': 'T005', 'name': '小长山岛'}, {'code': 'T006', 'name': '大窑湾'},
                    {'code': 'T007', 'name': '大连'}, {'code': 'T008', 'name': '旅顺新港'}, {'code': 'T009', 'name': '金县'},
                    {'code': 'T010', 'name': '葫芦套'}, {'code': 'T011', 'name': '长兴岛'}, {'code': 'T013', 'name': '营口'},
                    {'code': 'T014', 'name': '老北河口'}, {'code': 'T015', 'name': '锦州港'}, {'code': 'T016', 'name': '菊花岛'},
                    {'code': 'T017', 'name': '团山角'}, {'code': 'T018', 'name': '芷锚湾'}, {'code': 'T019', 'name': '山海关'},
                    {'code': 'T020', 'name': '秦皇岛'}, {'code': 'T021', 'name': '七里海'}, {'code': 'T022', 'name': '京唐港'},
                    {'code': 'T023', 'name': '曹妃甸'}, {'code': 'T024', 'name': '塘沽'}, {'code': 'T026', 'name': '埕口外海'},
                    {'code': 'T027', 'name': '黄骅港'}, {'code': 'T028', 'name': '东风港'}, {'code': 'T029', 'name': '湾湾沟口'},
                    {'code': 'T030', 'name': '东营港'}, {'code': 'T031', 'name': '潍坊港'}, {'code': 'T032', 'name': '莱州港'},
                    {'code': 'T033', 'name': '龙口'}, {'code': 'T034', 'name': '蓬莱'}, {'code': 'T035', 'name': '南长山岛'},
                    {'code': 'T036', 'name': '砣矶岛'}, {'code': 'T037', 'name': '北隍城岛'}, {'code': 'T039', 'name': '威海'},
                    {'code': 'T040', 'name': '成山角'}, {'code': 'T041', 'name': '石岛'}, {'code': 'T042', 'name': '张家埠'},
                    {'code': 'T043', 'name': '乳山口'}, {'code': 'T044', 'name': '千里岩'}, {'code': 'T045', 'name': '女岛港'},
                    {'code': 'T046', 'name': '青岛'}, {'code': 'T047', 'name': '黄岛'}, {'code': 'T048', 'name': '董家口'},
                    {'code': 'T049', 'name': '日照港'}, {'code': 'T050', 'name': '岚山港'}, {'code': 'T051', 'name': '连云港'},
                    {'code': 'T052', 'name': '燕尾'}, {'code': 'T053', 'name': '滨海港'}, {'code': 'T054', 'name': '射阳河口'},
                    {'code': 'T055', 'name': '新洋港'}, {'code': 'T056', 'name': '大丰港'}, {'code': 'T057', 'name': '弶港'},
                    {'code': 'T058', 'name': '洋口港'}, {'code': 'T059', 'name': '吕四'}, {'code': 'T060', 'name': '天生港'},
                    {'code': 'T061', 'name': '佘山'}, {'code': 'T062', 'name': '崇明'}, {'code': 'T063', 'name': '中浚'},
                    {'code': 'T064', 'name': '高桥'}, {'code': 'T065', 'name': '吴淞'}, {'code': 'T066', 'name': '黄浦公园'},
                    {'code': 'T067', 'name': '芦潮港'}, {'code': 'T068', 'name': '金山嘴'}, {'code': 'T069', 'name': '绿华山'},
                    {'code': 'T070', 'name': '大戢山'}, {'code': 'T071', 'name': '嵊山'}, {'code': 'T072', 'name': '乍浦'},
                    {'code': 'T073', 'name': '澉浦'}, {'code': 'T074', 'name': '滩浒'}, {'code': 'T075', 'name': '海黄山'},
                    {'code': 'T076', 'name': '长涂'}, {'code': 'T077', 'name': '岱山'}, {'code': 'T078', 'name': '西码头'},
                    {'code': 'T079', 'name': '沈家门'}, {'code': 'T080', 'name': '定海'}, {'code': 'T081', 'name': '沥港'},
                    {'code': 'T082', 'name': '宁波'}, {'code': 'T083', 'name': '镇海'}, {'code': 'T084', 'name': '北仑港'},
                    {'code': 'T085', 'name': '崎头角'}, {'code': 'T086', 'name': '梅山'}, {'code': 'T087', 'name': '西泽'},
                    {'code': 'T088', 'name': '石浦'}, {'code': 'T089', 'name': '旗门港'}, {'code': 'T090', 'name': '健跳'},
                    {'code': 'T091', 'name': '鱼山'}, {'code': 'T092', 'name': '下大陈'}, {'code': 'T093', 'name': '海门'},
                    {'code': 'T094', 'name': '海门港'}, {'code': 'T095', 'name': '东门村'}, {'code': 'T096', 'name': '坎门'},
                    {'code': 'T097', 'name': '大门岛'}, {'code': 'T098', 'name': '温州'}, {'code': 'T099', 'name': '瑞安'},
                    {'code': 'T100', 'name': '南麂山'}, {'code': 'T101', 'name': '三沙'}, {'code': 'T102', 'name': '赛岐'},
                    {'code': 'T103', 'name': '帮门'}, {'code': 'T104', 'name': '罗源迹头'}, {'code': 'T105', 'name': '黄岐'},
                    {'code': 'T106', 'name': '马尾'}, {'code': 'T107', 'name': '福清湾'}, {'code': 'T108', 'name': '竹屿'},
                    {'code': 'T109', 'name': '郎官'}, {'code': 'T110', 'name': '闽江口-川石'},
                    {'code': 'T111', 'name': '闽江口-琯头'}, {'code': 'T112', 'name': '平潭'}, {'code': 'T113', 'name': '三江口'},
                    {'code': 'T114', 'name': '秀屿'}, {'code': 'T115', 'name': '梯吴'}, {'code': 'T116', 'name': '崇武'},
                    {'code': 'T117', 'name': '后渚'}, {'code': 'T118', 'name': '泉州'}, {'code': 'T119', 'name': '深沪港'},
                    {'code': 'T120', 'name': '围头'}, {'code': 'T121', 'name': '石井'}, {'code': 'T122', 'name': '厦门'},
                    {'code': 'T123', 'name': '将军澳'}, {'code': 'T124', 'name': '石码'}, {'code': 'T125', 'name': '东山'},
                    {'code': 'T126', 'name': '马公'}, {'code': 'T127', 'name': '基隆'}, {'code': 'T128', 'name': '高雄'},
                    {'code': 'T129', 'name': '南澳岛'}, {'code': 'T130', 'name': '潮州港'}, {'code': 'T131', 'name': '汕头'},
                    {'code': 'T132', 'name': '海门-广东'}, {'code': 'T133', 'name': '甲子'}, {'code': 'T134', 'name': '汕尾'},
                    {'code': 'T135', 'name': '马鞭洲'}, {'code': 'T136', 'name': '惠州港'}, {'code': 'T137', 'name': '大亚湾'},
                    {'code': 'T138', 'name': '大鹏湾'}, {'code': 'T139', 'name': '香港'}, {'code': 'T140', 'name': '蛇口'},
                    {'code': 'T141', 'name': '桂山岛'}, {'code': 'T142', 'name': '内伶仃岛'}, {'code': 'T143', 'name': '舢舨洲'},
                    {'code': 'T144', 'name': '深圳机场'}, {'code': 'T145', 'name': '南沙'}, {'code': 'T146', 'name': '海沁'},
                    {'code': 'T147', 'name': '黄埔'}, {'code': 'T148', 'name': '广州'}, {'code': 'T149', 'name': '北街'},
                    {'code': 'T150', 'name': '横门'}, {'code': 'T151', 'name': '珠海-香洲'},
                    {'code': 'T152', 'name': '珠海-九洲港'}, {'code': 'T153', 'name': '澳门'}, {'code': 'T154', 'name': '东澳岛'},
                    {'code': 'T155', 'name': '大万山'}, {'code': 'T156', 'name': '灯笼山'}, {'code': 'T157', 'name': '三灶岛'},
                    {'code': 'T158', 'name': '珠海港'}, {'code': 'T159', 'name': '横山'}, {'code': 'T160', 'name': '井岸'},
                    {'code': 'T161', 'name': '上川岛'}, {'code': 'T162', 'name': '北津'}, {'code': 'T163', 'name': '海陵山岛'},
                    {'code': 'T164', 'name': '电白'}, {'code': 'T165', 'name': '博贺'}, {'code': 'T166', 'name': '西葛'},
                    {'code': 'T167', 'name': '茂石化'}, {'code': 'T168', 'name': '硇洲岛'}, {'code': 'T169', 'name': '湛江'},
                    {'code': 'T170', 'name': '下港'}, {'code': 'T171', 'name': '海安'}, {'code': 'T172', 'name': '流沙'},
                    {'code': 'T173', 'name': '乌石'}, {'code': 'T174', 'name': '下泊'}, {'code': 'T175', 'name': '东沙岛'},
                    {'code': 'T176', 'name': '海口'}, {'code': 'T177', 'name': '铺前'}, {'code': 'T178', 'name': '清澜'},
                    {'code': 'T179', 'name': '博鳌'}, {'code': 'T180', 'name': '新村'}, {'code': 'T181', 'name': '牙笼港'},
                    {'code': 'T182', 'name': '三亚'}, {'code': 'T183', 'name': '莺歌海'}, {'code': 'T184', 'name': '东方'},
                    {'code': 'T185', 'name': '洋浦'}, {'code': 'T186', 'name': '新盈'}, {'code': 'T187', 'name': '马村港'},
                    {'code': 'T188', 'name': '永兴岛'}, {'code': 'T189', 'name': '双子礁'}, {'code': 'T190', 'name': '永暑礁'},
                    {'code': 'T191', 'name': '铁山港'}, {'code': 'T192', 'name': '涠洲岛'}, {'code': 'T193', 'name': '北海'},
                    {'code': 'T194', 'name': '龙门'}, {'code': 'T195', 'name': '企沙'}, {'code': 'T196', 'name': '炮台角'},
                    {'code': 'T197', 'name': '防城港'}, {'code': 'T198', 'name': '珍珠港'}, {'code': 'T199', 'name': '白龙尾'},
                    {'code': 'T485', 'name': '中沙群岛－黄岩岛'}]
        return jsonify(errno=RET.OK, data=province, errmsg="查询成功")


@ns.route('/get_tidal')
class Tidal(Resource):
    @api.doc('获取潮汐列表')
    @ns.param('tide_time', '时间')
    @ns.param('code', '潮位站代码')
    def get(self):
        '''获取潮汐列表'''
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
        return jsonify(errno=RET.OK, data=json, errmsg="查询成功")


@ns.route('/down_trend')
class Tidal(Resource):
    @api.doc('下载潮汐水位')
    @ns.param('tide_time', '时间')
    @ns.param('code', '潮位站代码')
    def get(self):
        """下载潮汐水位"""
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
# @ns.route('/metas')
# class DatasetInfo(Resource):
#     @api.doc('潮汐自动下载地址')
#     @ns.param('date', '日期')
#     def get(self):
#         """weather自动下载地址"""
#         list = []
#         date = request.values.get('date')
#         date_path = date.replace('-', '\\')
#         path = 'D:\\dataSource\\tide' + '\\' + date_path
#         for root, dirs, files in os.walk(path):
#             for file in files:
#                 down_path = current_app.config['DOWNLOADS'] + root.split('dataSource')[1]
#                 down_path = down_path.replace('\\', '/') + '/' + file
#
#                 obj = {
#                     "name": file,
#                     "size": size_format(os.path.getsize(root + '\\' + file)),
#                     "path": root + '\\' + file,
#                     "type": "tide",
#                     "date": time.strftime("%Y-%m-%d", time.localtime(os.stat(root + '\\' + file).st_mtime))
#                 }
#                 list.append(obj)
#         data = {
#             "data": list,
#         }
#         return jsonify(errno=RET.OK, data=data, errmsg="查询成功")
