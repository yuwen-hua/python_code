
import json
import os
import re
import time
import base64
import datetime
import xarray as xr
import numpy as np
from selenium import webdriver

# 此方案废弃 改为 chromedriver 自动操作chrome

chromedriver = "F:/chromedriver_win32/chromedriver"  # 驱动程序所在的位置
grib2 = "F:/grib2"
# file = "D:\\Downloads\\gfs"
#
os.environ["webdriver.chrome.driver"] = chromedriver  # 将驱动程序三位路径计入到系统路径中



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





