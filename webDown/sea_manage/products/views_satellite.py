import json
import os
import uuid
from io import BytesIO

import requests
from PIL import Image

from sea_manage.products import rest_api as api
from flask import request, jsonify, current_app
from flask_restplus import Resource
from ..untils.response_code import RET

ns = api.namespace("satellite", description="风云卫星专题模块API")


'http://satellite.nsmc.org.cn/PortalSite/WebServ/SatellitesSearchService.asmx/GetSatelliteSeries' # 获取风云四号、碳卫星  卫星编号
'http://satellite.nsmc.org.cn/PortalSite/WebServ/SatellitesSearchService.asmx/GetSatellitesBySeries' # 获取卫星之后的 具体名称
# {satelliteSeriesCode:'FY4X'}

'http://satellite.nsmc.org.cn/PortalSite/WebServ/SatellitesSearchService.asmx/GetInstrumentsBySatellite' # 获取卫星的 传感器
'http://satellite.nsmc.org.cn/PortalSite/WebServ/SatellitesSearchService.asmx/GetDataTypeGroupByInstrument' # 获取 卫星的 产品分类
'http://satellite.nsmc.org.cn/PortalSite/WebServ/SatellitesSearchService.asmx/GetDataTypesByGroupCode' # 获取 产品分类的 具体分类
'http://satellite.nsmc.org.cn/PortalSite/WebServ/SatellitesSearchService.asmx/GetProductionsByDataType' # 获取表格

'http://satellite.nsmc.org.cn/PortalSite/WebServ/DataService.asmx/GetArcDatasByProduction'  # 最后显示文件的表格
# {productID:'FY4B-_AGRI--_N_DISK_1330E_L2-_STOM_MULT_NOM_YYYYMMDDhhmmss_YYYYMMDDhhmmss_4000M_Vnnnn.JPG',txtBeginDate:'2022-08-03',txtBeginTime:'00:00:00', txtEndDate:'2022-08-04',txtEndTime:'23:59:59',cbAllArea:'',converStatus:'Part',East_CoordValue:'135.05',West_CoordValue:'73.45', North_CoordValue:'53.517',South_CoordValue:'3.8', rdbIsEvery:'on',beginindex:31,endindex:60,sortName:'DATABEGINDATE',sortOrder:'desc',where:''}


# Cookie = ''
# @ns.route('login')
# class LoginInfo(Resource):
#     def get(self):
#         """登录"""
#         url = "http://satellite.nsmc.org.cn/PortalSite/WebServ/SatellitesSearchService.asmx/GetSatelliteSeries"
#         data = {
#
#         }
#         response = requests.post(url=url,data=data)
#         Cookie = response.cookies



# @ns.route("/GetSatelliteSeries")
# class MetaInfo(Resource):
#     @api.doc("获取卫星编号")
#     # @ns.param("satelliteCode")
#     # @ns.param("instrumentCode")
#     def get(self):
#         """获取卫星编号"""
#         list = []
#         cookie = requests.utils.dict_from_cookiejar(Cookie)
#         print(cookie)
#         url = "http://satellite.nsmc.org.cn/PortalSite/WebServ/SatellitesSearchService.asmx/GetSatelliteSeries"
#         par = {}
#         header = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
#             # "Cookie": cookie,
#             "Cookie": ".ASPXANONYMOUS=vqtK7jze2AEkAAAANTIxYzcwNDktMjc2ZS00YmZkLWFhNWQtOTc4M2Q5YWU3N2Uwdib_Y89R7egmYShGfi1HkaMBinY1; UserLanguage=zh-CN; ASP.NET_SessionId=1bjtyu4j5p3bjallgvctcfju; ViewHistory=FY3D_MWHSX_GBAL_L1_YYYYMMDD_HHmm_015KM_MS.HDF%2CFY3E_MWHS-_ORBD_L1_YYYYMMDD_HHmm_015KM_Vn.HDF%2CFY3E_MWHS-_ORBA_L1_YYYYMMDD_HHmm_015KM_Vn.HDF%2C",
#             "Host": "satellite.nsmc.org.cn",
#             "Origin": "http://satellite.nsmc.org.cn",
#             "Referer": "http://satellite.nsmc.org.cn/PortalSite/Data/Satellite.aspx",
#             "Content-Type": "application / json;charset = UTF - 8",
#             "Accept-Encoding": "gzip, deflate",
#             "Accept": "application/json, text/javascript, */*; q=0.01",
#             "Accept-Language": "zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",
#             "X-Requested-With": "XMLHttpRequest"
#         }
#         response = requests.post(url=url,headers=header)
#         data = response.content
#         # sss = response.json()
#         # obj = {
#         #     "GetSatelliteSeries": response,
#         #     # "json_GetSatelliteSeries": sss
#         # }
#         print(data)
#         print(response.cookies)
#
#         obj = {
#             "code": response.status_code,
#             "is_redirect": response.is_redirect,
#             # "cookies": response.cookies,
#             "is_permanent_redirect": response.is_permanent_redirect
#         }
#         return jsonify(errno=RET.OK, data=obj, errmsg="获取数据成功")
#
#
#
# @ns.route("/GetSatellitesBySeries")
# class MetaInfo(Resource):
#     @api.doc("获取具体名称")
#     # @ns.param("satelliteCode")
#     # @ns.param("instrumentCode")
#     def get(self):
#         """获取具体名称"""
#         list = []
#         cookie = requests.utils.dict_from_cookiejar(Cookie)
#         print(cookie)
#         url = "http://satellite.nsmc.org.cn/PortalSite/WebServ/SatellitesSearchService.asmx/GetSatellitesBySeries"
#
#
# @ns.route("/GetInstrumentsBySatellite")
# class MetaInfo(Resource):
#     @api.doc("获取传感器")
#     # @ns.param("satelliteCode")
#     # @ns.param("instrumentCode")
#     def get(self):
#         """获取传感器"""
#         list = []
#         cookie = requests.utils.dict_from_cookiejar(Cookie)
#         print(cookie)
#         url = "http://satellite.nsmc.org.cn/PortalSite/WebServ/SatellitesSearchService.asmx/GetInstrumentsBySatellite"
#
# @ns.route("/GetDataTypeGroupByInstrument")
# class MetaInfo(Resource):
#     @api.doc("获取产品分类")
#     # @ns.param("satelliteCode")
#     # @ns.param("instrumentCode")
#     def get(self):
#         """获取产品分类"""
#         list = []
#         cookie = requests.utils.dict_from_cookiejar(Cookie)
#         print(cookie)
#         url = "http://satellite.nsmc.org.cn/PortalSite/WebServ/SatellitesSearchService.asmx/GetDataTypeGroupByInstrument"
#
#
# @ns.route("/GetDataTypesByGroupCode")
# class MetaInfo(Resource):
#     @api.doc("获取具体分类")
#     # @ns.param("satelliteCode")
#     # @ns.param("instrumentCode")
#     def get(self):
#         """获取具体分类"""
#         list = []
#         cookie = requests.utils.dict_from_cookiejar(Cookie)
#         print(cookie)
#         url = "http://satellite.nsmc.org.cn/PortalSite/WebServ/SatellitesSearchService.asmx/GetDataTypesByGroupCode"



@ns.route('/satellite')
class SateInfo(Resource):
    @api.doc('获取卫星云图')
    def get(self):
        """获取卫星云图图片"""
        obj = {
        "bbox": "0, 0, 90, 90",
        "bbox1": "0, -90, 180, 90",
        "bbox2": "0, -90, 90, 0",
        "bbox3": "90, 0, 180, 90",
        "bbox4": "90, -90, 180, 0",
        "bbox5": "-90, 0, 0, 90",
        "bbox6": "-90, -90, 0, 0",
        "bbox7": "-180, -90, 0, 90",
        "bbox8": "-180, 0, -90, 90",
        "bbox9": "-180, -90, -90, 0"
        }
        # arr = ["-180,-90,-90,0","-90,-90,0,0","0,-90,90,0","90,-90,180,0"]
        arr = ["-180,-90,-90,0","-90,-90,0,0","0,-90,90,0","90,-90,180,0","-180,0,-90,90","-90,0,0,90","0,0,90,90","90,0,180,90"]
        for i in arr:

        # url = 'https://satellite.nsmc.org.cn/mongoTile_DSS/FY/getLatestTile.php?layer=PRODUCT&PRODUCT=FY3D_MERSI_L2_PAD_MLT_GLL_YYYYMMDD_POAD_0250M_MS.HDF&DATE=20220806&TIME=0000&service=WMS&version=1.1.1&request=GetMap&styles=&format=image%2Fjpeg&layers=FY3D_MERSI&bbox=-90%2C-90%2C0%2C0&width=256&height=256&srs=EPSG%3A4326'
            url = 'https://satellite.nsmc.org.cn/mongoTile_DSS/FY/getLatestTile.php?layer=PRODUCT&PRODUCT=FY3D_MERSI_L2_PAD_MLT_GLL_YYYYMMDD_POAD_0250M_MS.HDF&service=WMS&version=1.1.1&request=GetMap&styles=&format=image%2Fjpeg&layers=FY3D_MERSI&bbox=' + i +  '&width=256&height=256&srs=EPSG%3A4326'
            req = requests.get(url)
            image = Image.open(BytesIO(req.content))
            # fileName = str(uuid.uuid4()) + '.' + image.format.lower()
            fileName = i + '.' + image.format.lower()
            with open('D:/dataSource/satellite/' + fileName, 'wb') as f:
                f.write(req.content)
        return jsonify(errno=RET.OK, data=111, errmsg="获取数据成功")

UNIT_SIZE = 256
TARGET_WIDTH = 4 * UNIT_SIZE
@ns.route('/img')
class SateInfo(Resource):
    @api.doc('拼接卫星云图')
    def get(self):
        path = 'D:/dataSource/satellite'

        num = 0
        images = []  # images in each folder
        for root, dirs, files in os.walk(path):  # traverse each folder
            for file in files:
                images.append(Image.open(path + '/' + file))
        pinjie(images,path)
        return jsonify(errno=RET.OK, data=11111, errmsg="获取数据成功")

def pinjie(images,path):
    target = Image.new('RGB', (UNIT_SIZE*4, UNIT_SIZE*2))   # result is 2*5
    leftone = 0
    lefttwo = 0
    rightone = UNIT_SIZE
    righttwo = UNIT_SIZE
    for i in range(len(images)):
        if(i%2!=0):
            target.paste(images[i], (leftone, 0, rightone, UNIT_SIZE))
            leftone += UNIT_SIZE #第一行左上角右移
            rightone += UNIT_SIZE #右下角右移
        else:
            target.paste(images[i], (lefttwo, UNIT_SIZE, righttwo, UNIT_SIZE*2))
            lefttwo += UNIT_SIZE #第二行左上角右移
            righttwo += UNIT_SIZE #右下角右移
    quality_value = 100
    target.save(path+'/result'+'.jpg', quality = quality_value)


@ns.route('/two')
class SateInfo(Resource):
    @api.doc('获取卫星云图')
    def get(self):
        lon = ["-180","-135", "-90","-45","0","45","90","135"]
        lat = ["-90","-45","0","45"]
        for i in lon:
            for j in lat:
                print(i,j, int(i) + 45, int(j) + 45)
                bbox = i + ',' + j + ',' + str(int(i) + 45) + ',' + str(int(j) + 45)
                url = 'https://satellite.nsmc.org.cn/mongoTile_DSS/FY/getLatestTile.php?layer=PRODUCT&PRODUCT=FY3D_MERSI_L2_PAD_MLT_GLL_YYYYMMDD_POAD_0250M_MS.HDF&service=WMS&version=1.1.1&request=GetMap&styles=&format=image%2Fjpeg&layers=FY3D_MERSI&bbox=' + bbox + '&width=256&height=256&srs=EPSG%3A4326'
                req = requests.get(url)
                image = Image.open(BytesIO(req.content))
                # fileName = str(uuid.uuid4()) + '.' + image.format.lower()
                fileName = bbox + '.' + image.format.lower()
                with open('D:/dataSource/satellite/2' + fileName, 'wb') as f:
                    f.write(req.content)
        return jsonify(errno=RET.OK, data=111, errmsg="获取数据成功")


UNIT_SIZE = 256
TARGET_WIDTH_TWO = 4 * UNIT_SIZE
@ns.route('/twoimg')
class SateInfo(Resource):
    @api.doc('拼接卫星云图')
    def get(self):
        path = 'D:/dataSource/satellite'

        num = 0
        images = []  # images in each folder
        for root, dirs, files in os.walk(path):  # traverse each folder
            for file in files:
                images.append(Image.open(path + '/' + file))
        pinjie_two(images,path)
        return jsonify(errno=RET.OK, data=11111, errmsg="获取数据成功")

def pinjie_two(images,path):
    target = Image.new('RGB', (UNIT_SIZE*8, UNIT_SIZE*4))
    leftone = 0
    lefttwo = 0
    rightone = UNIT_SIZE
    righttwo = UNIT_SIZE
    for i in range(len(images)):
        print(images)
        if(i%2!=0):
            target.paste(images[i], (leftone, 0, rightone, UNIT_SIZE))
            leftone += UNIT_SIZE #第一行左上角右移
            rightone += UNIT_SIZE #右下角右移
        else:
            target.paste(images[i], (lefttwo, UNIT_SIZE, righttwo, UNIT_SIZE*2))
            lefttwo += UNIT_SIZE #第二行左上角右移
            righttwo += UNIT_SIZE #右下角右移
    quality_value = 100
    target.save(path+'/result'+'.jpg', quality = quality_value)
