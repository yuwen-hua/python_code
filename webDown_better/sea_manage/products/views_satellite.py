import datetime
import json
import os
import uuid
from io import BytesIO

import requests
from PIL import Image

from sea_manage.products import rest_api as api
from flask import request, jsonify, current_app, send_file
from flask_restplus import Resource
from ..untils.response_code import RET

ns = api.namespace("satellite", description="风云卫星专题模块API")

'http://satellite.nsmc.org.cn/PortalSite/WebServ/SatellitesSearchService.asmx/GetSatelliteSeries'  # 获取风云四号、碳卫星  卫星编号
'http://satellite.nsmc.org.cn/PortalSite/WebServ/SatellitesSearchService.asmx/GetSatellitesBySeries'  # 获取卫星之后的 具体名称
# {satelliteSeriesCode:'FY4X'}

'http://satellite.nsmc.org.cn/PortalSite/WebServ/SatellitesSearchService.asmx/GetInstrumentsBySatellite'  # 获取卫星的 传感器
'http://satellite.nsmc.org.cn/PortalSite/WebServ/SatellitesSearchService.asmx/GetDataTypeGroupByInstrument'  # 获取 卫星的 产品分类
'http://satellite.nsmc.org.cn/PortalSite/WebServ/SatellitesSearchService.asmx/GetDataTypesByGroupCode'  # 获取 产品分类的 具体分类
'http://satellite.nsmc.org.cn/PortalSite/WebServ/SatellitesSearchService.asmx/GetProductionsByDataType'  # 获取表格

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


@ns.route('/get_one_satellite')
class SateInfo(Resource):
    @api.doc('获取卫星云图')
    def get(self):
        """获取1级卫星云图图片"""
        arr = ["-180,-90,-90,0", "-90,-90,0,0", "0,-90,90,0", "90,-90,180,0", "-180,0,-90,90", "-90,0,0,90",
               "0,0,90,90", "90,0,180,90"]
        today = datetime.datetime.now().strftime('%Y/%m/%d')
        down_path = 'D:/dataSource/satellite/' + today + '/1/'
        if not os.path.exists(down_path):
            os.makedirs(down_path)
        if not os.path.exists(down_path + '90,0,180,90.jpeg'):
            target = Image.new('RGB', (UNIT_SIZE * 4, UNIT_SIZE * 2))
            index = 0
            leftone = 0
            rightone = UNIT_SIZE

            lefttwo = 0
            righttwo = UNIT_SIZE
            for index,value in enumerate(arr):
                index += 1
                # url = 'https://satellite.nsmc.org.cn/mongoTile_DSS/FY/getLatestTile.php?layer=PRODUCT&PRODUCT=FY3D_MERSI_L2_PAD_MLT_GLL_YYYYMMDD_POAD_0250M_MS.HDF&DATE=20220806&TIME=0000&service=WMS&version=1.1.1&request=GetMap&styles=&format=image%2Fjpeg&layers=FY3D_MERSI&bbox=-90%2C-90%2C0%2C0&width=256&height=256&srs=EPSG%3A4326'
                url = 'https://satellite.nsmc.org.cn/mongoTile_DSS/FY/getLatestTile.php?layer=PRODUCT&PRODUCT=FY3D_MERSI_L2_PAD_MLT_GLL_YYYYMMDD_POAD_0250M_MS.HDF&service=WMS&version=1.1.1&request=GetMap&styles=&format=image%2Fjpeg&layers=FY3D_MERSI&bbox=' + value + '&width=256&height=256&srs=EPSG%3A4326'
                req = requests.get(url)
                image = Image.open(BytesIO(req.content))
                # fileName = str(uuid.uuid4()) + '.' + image.format.lower()
                fileName = value + '.' + image.format.lower()
                with open(down_path + fileName, 'wb') as f:
                    f.write(req.content)
                images = Image.open(down_path + fileName)
                if index > 4:
                    target.paste(images, (leftone, 0, rightone, UNIT_SIZE))
                    leftone += UNIT_SIZE  # 第一行左上角右移
                    rightone += UNIT_SIZE  # 右下角右移
                else:
                    target.paste(images, (lefttwo, UNIT_SIZE, righttwo, UNIT_SIZE * 2))
                    lefttwo += UNIT_SIZE  # 第一行左上角右移
                    righttwo += UNIT_SIZE  # 右下角右移
        # images = []
        # for root, dirs, files in os.walk(down_path):
        #     for file in files:
        #         images.append(Image.open(root + '/' + file))
        # pinjie(images, down_path)
        return send_file(down_path + '/1' + '.jpg', as_attachment=True)


UNIT_SIZE = 256
TARGET_WIDTH = 4 * UNIT_SIZE


@ns.route('/get_two_satellite')
class SateInfo(Resource):
    @api.doc('获取2级卫星云图图片')
    def get(self):
        """获取2级卫星云图图片"""
        lon = ["-180", "-135", "-90", "-45", "0", "45", "90", "135"]
        lat = ["-90", "-45", "0", "45"]
        today = datetime.datetime.now().strftime('%Y/%m/%d')
        down_path = 'D:/dataSource/satellite/' + today + '/2/'
        if not os.path.exists(down_path):
            os.makedirs(down_path)
        if not os.path.exists(down_path + '0,-45,45,0.jpeg'):

            target = Image.new('RGB', (UNIT_SIZE * 8, UNIT_SIZE * 4))
            index = 0
            # if not os.path.exists(down_path):
            #     os.makedirs(down_path)
            leftone = 0
            rightone = UNIT_SIZE

            lefttwo = 0
            righttwo = UNIT_SIZE

            leftthree = 0
            rightthree = UNIT_SIZE

            leftfour = 0
            rightfour = UNIT_SIZE
            for j in lat:
                for i in lon:
                    index = index +1
                    print(i, j, int(i) + 45, int(j) + 45)
                    bbox = i + ',' + j + ',' + str(int(i) + 45) + ',' + str(int(j) + 45)
                    url = 'https://satellite.nsmc.org.cn/mongoTile_DSS/FY/getLatestTile.php?layer=PRODUCT&PRODUCT=FY3D_MERSI_L2_PAD_MLT_GLL_YYYYMMDD_POAD_0250M_MS.HDF&service=WMS&version=1.1.1&request=GetMap&styles=&format=image%2Fjpeg&layers=FY3D_MERSI&bbox=' + bbox + '&width=256&height=256&srs=EPSG%3A4326'
                    req = requests.get(url)
                    image = Image.open(BytesIO(req.content))
                    fileName = bbox + '.' + image.format.lower()
                    with open(down_path + fileName, 'wb') as f:
                        f.write(req.content)
                    images = Image.open(down_path + fileName)
                    if index < 9:
                        target.paste(images, (leftone, UNIT_SIZE *3, rightone,UNIT_SIZE *4))
                        leftone += UNIT_SIZE  # 第一行左上角右移
                        rightone += UNIT_SIZE  # 右下角右移
                    elif index >8 and index <17:
                        print(index)
                        target.paste(images, (lefttwo, UNIT_SIZE * 2, righttwo, UNIT_SIZE * 3))
                        lefttwo += UNIT_SIZE  # 第一行左上角右移
                        righttwo += UNIT_SIZE  # 右下角右移
                    elif index > 16 and index < 25:
                        target.paste(images, (leftthree, UNIT_SIZE, rightthree, UNIT_SIZE * 2))
                        leftthree += UNIT_SIZE  # 第一行左上角右移
                        rightthree += UNIT_SIZE  # 右下角右移
                    elif index >24 and index <33:
                        target.paste(images, (leftfour, 0, rightfour, UNIT_SIZE))
                        leftfour += UNIT_SIZE  # 第一行左上角右移
                        rightfour += UNIT_SIZE  # 右下角右移
            target.save(down_path + '2' + '.jpg', quality=100)
        return send_file(down_path + '2' + '.jpg', as_attachment=True)


@ns.route('/get_three_satellite')
class SateInfo(Resource):
    @api.doc('获取3级卫星云图图片')
    def get(self):
        """获取3级卫星云图图片"""
        lon = [-180,-157.5, -135, -112.5, -90, -67.5, -45, -22.5, 0, 22.5, 45, 67.5, 90, 112.5, 135, 157.5]
        lat = [-90, -67.5, -45, -22.5, 0, 22.5, 45, 67.5]
        today = datetime.datetime.now().strftime('%Y/%m/%d')
        down_path = 'D:/dataSource/satellite/' + today + '/3/'
        if not os.path.exists(down_path):
            os.makedirs(down_path)
        if not os.path.exists(down_path + '-45,-22.5,-22.5,0.5.jpeg'):
            target = Image.new('RGB', (UNIT_SIZE * 16, UNIT_SIZE * 8))
            index = 0
            leftone = 0
            rightone = UNIT_SIZE

            lefttwo = 0
            righttwo = UNIT_SIZE

            leftthree = 0
            rightthree = UNIT_SIZE

            leftfour = 0
            rightfour = UNIT_SIZE

            leftfive = 0
            rightfive = UNIT_SIZE

            leftsix = 0
            rightsix = UNIT_SIZE

            leftseven = 0
            rightseven = UNIT_SIZE

            lefteight = 0
            righteight = UNIT_SIZE

            for j in lat:
                for i in lon:
                    index = index +1
                    bbox = str(i) + ',' + str(j) + ',' + str(int(i) + 22.5) + ',' + str(int(j) + 22.5)
                    url = 'https://satellite.nsmc.org.cn/mongoTile_DSS/FY/getLatestTile.php?layer=PRODUCT&PRODUCT=FY3D_MERSI_L2_PAD_MLT_GLL_YYYYMMDD_POAD_0250M_MS.HDF&service=WMS&version=1.1.1&request=GetMap&styles=&format=image%2Fjpeg&layers=FY3D_MERSI&bbox=' + bbox + '&width=256&height=256&srs=EPSG%3A4326'
                    req = requests.get(url)
                    image = Image.open(BytesIO(req.content))
                    # fileName = str(uuid.uuid4()) + '.' + image.format.lower()
                    fileName = bbox + '.' + image.format.lower()
                    # fileName = bbox + '.' + 'jpeg'
                    with open(down_path + fileName, 'wb') as f:
                        f.write(req.content)
                    images = Image.open(down_path + fileName)
                    if index < 17:
                        target.paste(images, (leftone, UNIT_SIZE *7, rightone,UNIT_SIZE *8))
                        leftone += UNIT_SIZE  # 第一行左上角右移
                        rightone += UNIT_SIZE  # 右下角右移
                    elif index >8 and index <33:
                        print(index)
                        target.paste(images, (lefttwo, UNIT_SIZE * 6, righttwo, UNIT_SIZE * 7))
                        lefttwo += UNIT_SIZE  # 第一行左上角右移
                        righttwo += UNIT_SIZE  # 右下角右移
                    elif index > 32 and index < 49:
                        target.paste(images, (leftthree, UNIT_SIZE * 5, rightthree, UNIT_SIZE * 6))
                        leftthree += UNIT_SIZE  # 第一行左上角右移
                        rightthree += UNIT_SIZE  # 右下角右移
                    elif index > 48 and index < 65:
                        target.paste(images, (leftfour, UNIT_SIZE * 4, rightfour, UNIT_SIZE * 5))
                        leftfour += UNIT_SIZE  # 第一行左上角右移
                        rightfour += UNIT_SIZE  # 右下角右移
                    elif index > 64 and index < 81:
                        target.paste(images, (leftfive, UNIT_SIZE * 3, rightfive, UNIT_SIZE * 4))
                        leftfive += UNIT_SIZE  # 第一行左上角右移
                        rightfive += UNIT_SIZE  # 右下角右移
                    elif index > 80 and index < 97:
                        target.paste(images, (leftsix, UNIT_SIZE * 2, rightsix, UNIT_SIZE * 3))
                        leftsix += UNIT_SIZE  # 第一行左上角右移
                        rightsix += UNIT_SIZE  # 右下角右移
                    elif index > 96 and index < 113:
                        target.paste(images, (leftseven, UNIT_SIZE, rightseven, UNIT_SIZE * 2))
                        leftseven += UNIT_SIZE  # 第一行左上角右移
                        rightseven += UNIT_SIZE  # 右下角右移
                    elif index > 112 and index < 129:
                        target.paste(images, (lefteight, 0, righteight, UNIT_SIZE))
                        lefteight += UNIT_SIZE  # 第一行左上角右移
                        righteight += UNIT_SIZE  # 右下角右移
            target.save(down_path + '3' + '.jpg', quality=100)
        return send_file(down_path + '3' + '.jpg', as_attachment=True)




UNIT_SIZE = 256
TARGET_WIDTH_TWO = 4 * UNIT_SIZE



