import json
import os
import re
import time
import ftplib
import base64
from datetime import timedelta, datetime
import xarray as xr
import numpy as np
from selenium import webdriver

# 此方案废弃 改为 chromedriver 自动操作chrome

chromedriver = "F:/chromedriver_win32/chromedriver"  # 驱动程序所在的位置
grib2 = "F:/grib2"
# file = "D:\\Downloads\\gfs"
#
os.environ["webdriver.chrome.driver"] = chromedriver  # 将驱动程序三位路径计入到系统路径中

buffer_size = 1024 * 1024


class Copernicus():
    def __init__(self, data):
        for i in data:
            for j in i['children']:
                self.start(i, j)

    def login(self):
        host = "nrt.cmems-du.eu"
        username = "xchen7"
        password = "Wdmm9916@"
        ftpServer = ftplib.FTP(host)
        ftpServer.encoding = "utf-8"
        ftpServer.login(username, password)
        print('开启连接')
        return ftpServer

    def start(self, i, j):
        ftpServer = self.login()
        # host = "nrt.cmems-du.eu"
        # username = "xchen7"
        # password = "Wdmm9916@"
        # ftpServer = ftplib.FTP(host)
        # ftpServer.encoding = "utf-8"
        # ftpServer.login(username, password)

        # ftpServer.cwd() 进入文件夹
        ftpServer.cwd('Core')
        ftpServer.cwd(i['label'])
        ftpServer.cwd(j['label'])
        year = datetime.now().strftime('%Y')
        month = datetime.now().strftime('%m')
        yesterday = (datetime.today() + timedelta(days=-1)).strftime("%Y%m%d")
        yesterday_path = (datetime.today() + timedelta(days=-1)).strftime("%Y/%m/%d")
        beforeyesterday = (datetime.today() + timedelta(days=-2)).strftime("%Y%m%d")
        beforeyesterday_path = (datetime.today() + timedelta(days=-2)).strftime("%Y/%m/%d")
        day = datetime.now().strftime('%Y%m%d')
        day_path = datetime.now().strftime('%Y/%m/%d')
        print(i['label'], j['label'])
        ftpServer.cwd(year)
        if i['label'] != 'MULTIOBS_GLO_PHY_S_SURFACE_MYNRT_015_013':
            ftpServer.cwd(month)
        for filename in ftpServer.nlst():
            if "WIND_GLO_WIND_L3_NRT_OBSERVATIONS_012_002" == i['label'] or "OCEANCOLOUR_GLO_BGC_L3_NRT_009_101" == i[
                'label'] or "MULTIOBS_GLO_PHY_S_SURFACE_MYNRT_015_013" == i['label']:
                # 判断是否有当天的数据
                if beforeyesterday in filename:
                    print(i['label'] + '/' + j['label'] + '/' + filename)
                    dst_file_path = "D:/dataSource/copernicus/" + i['label'] + '/' + j['label'] + '/' + yesterday_path
                    if not os.path.exists(dst_file_path):
                        os.makedirs(dst_file_path)
                    try:
                        self.download(ftpServer, filename, dst_file_path)
                    except Exception as e:
                        print(e)
                        ftpServer = self.login()
                        self.download(ftpServer, filename, dst_file_path)
            else:
                if yesterday in filename:
                    print(i['label'] + '/' + j['label'] + '/' + filename)
                    dst_file_path = "D:/dataSource/copernicus/" + i['label'] + '/' + j['label'] + '/' + yesterday_path
                    if not os.path.exists(dst_file_path):
                        os.makedirs(dst_file_path)
                    try:
                        self.download(ftpServer, filename, dst_file_path)
                    except Exception as e:
                        print(e)
                        ftpServer = self.login()
                        self.download(ftpServer, filename, dst_file_path)

    def download(self, ftp, filename, dst_file_path):
        down_path = dst_file_path + '/' + filename
        f = open(down_path, "wb").write
        # with open(down_path, 'wb') as f:
        try:
            ftp.retrbinary("RETR %s" % filename, f, buffer_size)
            print('成功下载文件： "%s"' % filename)
        except ftplib.error_perm:
            return False
        return True

        # host="nrt.cmems-du.eu"
        # username="xchen7"
        # password="Wdmm9916@"
        # buffer_size = 1024 * 1024
        # ftpServer=ftplib.FTP(host)
        # ftpServer.encoding = "utf-8"
        # ftpServer.login(username,password)
        # login = True
        # print('开启连接')
        # ftpServer.cwd('Core')
        # ftpServer.cwd(i['label'])
        # ftpServer.cwd(j['label'])
        # year = datetime.now().strftime('%Y')
        # month = datetime.now().strftime('%m')
        # yesterday = (datetime.today() + timedelta(days=-1)).strftime("%Y%m%d")
        # yesterday_path = (datetime.today() + timedelta(days=-1)).strftime("%Y/%m")
        # beforeyesterday = (datetime.today() + timedelta(days=-2)).strftime("%Y%m%d")
        # beforeyesterday_path = (datetime.today() + timedelta(days=-2)).strftime("%Y/%m/%d")
        # day = datetime.now().strftime('%Y%m%d')
        # day_path = datetime.now().strftime('%Y/%m/%d')
        # print(i['label'],j['label'])
        # ftpServer.cwd(year)
        # if i['label'] != 'MULTIOBS_GLO_PHY_S_SURFACE_MYNRT_015_013':
        #     ftpServer.cwd(month)
        # for filename in ftpServer.nlst():
        #     if "WIND_GLO_WIND_L3_NRT_OBSERVATIONS_012_002" == i['label'] or "OCEANCOLOUR_GLO_BGC_L3_NRT_009_101" == i['label'] or "MULTIOBS_GLO_PHY_S_SURFACE_MYNRT_015_013" == i['label']:
        #         if beforeyesterday in filename:
        #             print(i['label'] + '/' +  j['label'] +'/'+ filename)
        #             dst_file_path = "D:/dataSource/copernicus/" + i['label'] + '/' + j['label'] + '/' + yesterday_path
        #             if not os.path.exists(dst_file_path):
        #                 os.makedirs(dst_file_path)
        #             data = download(ftpServer, filename,dst_file_path)
        #             if data:
        #
        #                 login = False
        #     else:
        #         if yesterday in filename:
        #             print(i['label'] + '/' +  j['label'] +'/'+ filename)
        #             dst_file_path = "D:/dataSource/copernicus/" + i['label'] + '/' + j['label'] + '/' + yesterday_path
        #             if not os.path.exists(dst_file_path):
        #                 os.makedirs(dst_file_path)
        #             try:
        #                 download(ftpServer, filename, dst_file_path)
        #             except Exception as e:
        # ftpServer.close()
        # ftpServer.quit()
        # year = datetime.datetime.now().strftime('%Y')
        # month = datetime.datetime.now().strftime('%m')
        # day = datetime.datetime.now().strftime('%d')
        # ftpServer.cwd(year)
        # ftpServer.cwd(month)
        # print(ftpServer.pwd())
        # for filename in ftpServer.nlst():
        #     date = filename.split('.nc')[0][-2:]
        #     if day == date:
        #         weather = download(ftpServer, filename)


#
# ftpServer.cwd('Core/GLOBAL_ANALYSIS_FORECAST_PHY_001_024/global-analysis-forecast-phy-001-024-statics')
# for i in ftpServer.nlst():
#     print(i)
# for i in ftpServer.nlst():
#     print(i)
#     day = i.split('.nc')[0][-2:]
#     date = datetime.datetime.now().strftime('%d')
#     print(day,date,type(day),type(date))
#     if day == date:
#         ftpServer.set_pasv(False)
#         weather = download(ftpServer,i)
#         if weather:
#             ftpServer.quit()
# ftpServer.cwd('Core')

import requests
# from sea_manage.products import rest_api as api
# from flask import request, jsonify, current_app
# from flask_restplus import Resource
# from ..untils.response_code import RET
# ns = api.namespace('marine', description='哥白尼专题模块API')
#
# @ns.route('/search')
# class SearchInfo(Resource):
#     def get(self):
#         date = datetime.datetime.now()
#         print(date)
#         # url = 'https://nrt.cmems-du.eu/motu-web/Motu?action=getsize&service=GLOBAL_ANALYSIS_FORECAST_WAV_001_027-TDS&product=global-analysis-forecast-wav-001-027&x_lo=-180&x_hi=179.9166666666666287710540927946567535400390625&y_lo=-80&y_hi=90&t_lo=2022-08-18%2000:00:00&t_hi=2022-08-18%2000:00:00&variable=VHM0&variable=VHM0_SW1&variable=VHM0_SW2&variable=VHM0_WW&variable=VMDR&variable=VMDR_SW1&variable=VMDR_SW2&variable=VMDR_WW&variable=VPED&variable=VSDX&variable=VSDY&variable=VTM01_SW1&variable=VTM01_SW2&variable=VTM01_WW&variable=VTM02&variable=VTM10&variable=VTPK'


# class Copernicus():
#     def __init__(self):
#         login_url = 'https://cmems-cas.cls.fr/cas/login'
#         headers = {
#             "Accept": "application/json, text/plain, */*",
#             "Accept-Language": "zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",
#             "Host": "cmems-cas.cls.fr",
#             "Origin": "https://resources.marine.copernicus.eu",
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
#         }
#         sss = requests.Session()
#         res = sss.get(login_url,headers = headers)
#         reg = '<input type="hidden" name="lt" value="(.*)" />'
#         pattern = re.compile(reg)
#         login_id = pattern.findall(res.text)[0]
#         login_cookie = requests.utils.dict_from_cookiejar(res.cookies)['JSESSIONID']
#         login_cookie = 'JSESSIONID=' + login_cookie
#         headers = {
#             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#             "Accept-Language": "zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",
#             "Accept-Encoding": "gzip, deflate, br",
#             "Access-Control-Allow-Credentials": "true",
#             "Access-Control-Allow-Origin": "*",
#             "Host": "cmems-cas.cls.fr",
#             "Cookie": login_cookie,
#             "Origin": "https://resources.marine.copernicus.eu",
#             "Content-Type": "application/x-www-form-urlencoded",
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
#         }
#         data = {
#             "username": "xchen7",
#             "password": "Wdmm9916@",
#             "It": login_id,
#             "_eventId": "submit",
#             "submit": ""
#         }
#         response = sss.post(login_url,data=data,headers=headers)
#         cookie = requests.utils.dict_from_cookiejar(response.cookies)['CASTGC']
#         cookie = 'CASTGC=' + cookie
#
#         # 获取 具体页面的 cookie
#         search_url = 'https://cmems-cas.cls.fr/cas/login?service=https%3A%2F%2Fnrt.cmems-du.eu%2Fmotu-web%2FMotu%3Faction%3Ddescribeproduct%26service%3DSEALEVEL_GLO_PHY_L4_NRT_OBSERVATIONS_008_046-TDS%26product%3Ddataset-duacs-nrt-global-merged-allsat-phy-l4'
#         search_headers = {
#             "Cookie": login_cookie + '; ' + cookie,
#             "Accept": "*/*",
#             "Accept-Encoding": "gzip, deflate, br",
#             "Accept-Language": "zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6"
#         }
#         search_res = sss.get(url=search_url,headers=search_headers)
#         print(search_res)
