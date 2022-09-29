# coding:utf-8
import datetime
import os
import time

import requests
import re

from sea_manage.products import rest_api as api
from flask import request, jsonify, current_app, send_file
from flask_restplus import Resource

from sea_manage.untils.response_code import RET
from sea_manage.passport.views_copernicus import Copernicus


ns = api.namespace('marine', description='哥白尼模块API')


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

@ns.route('/test')
class TestInfo(Resource):
    def get(self):
        Copernicus()
        return jsonify(errno=RET.OK, errmsg="查询成功")


@ns.route('/metas')
class DatasetInfo(Resource):
    @api.doc('copernicus自动下载地址')
    @ns.param('label','父类型')
    @ns.param('chileLabel', '子类型')
    @ns.param('date','日期')
    def get(self):
        """copernicus自动下载地址"""
        list = []
        label = request.values.get('label')
        chileLabel = request.values.get('chileLabel')
        date = request.values.get('date')
        path = 'D:\\dataSource\\copernicus'
        if label:
            path = path + '\\' + label
        if chileLabel:
            path = path + '\\' + chileLabel
        if date:
            date_path = date.replace('-', '/')
            path = path + '\\' + date_path
        for root, dirs, files in os.walk(path):
            for file in files:
                down_path = current_app.config['DOWNLOADS'] + root.split('dataSource')[1]
                down_path = down_path.replace('\\', '/') + '/' + file

                obj =  {
                    "name": file,
                    "size": size_format(os.path.getsize(root + '\\' + file)),
                    "path": root + '\\' + file,
                    "type": "copernicus",
                    "date": time.strftime("%Y-%m-%d", time.localtime(os.stat(root + '\\' + file).st_mtime))
                }
                list.append(obj)
        data = {
            "data": list,
        }

        return jsonify(errno=RET.OK, data=data, errmsg="查询成功")

@ns.route('/down')
class DatasetInfo(Resource):
    @api.doc('copernicus自动下载地址')
    @ns.param('date', '日期')
    @ns.param('name','名称')
    def get(self):
        name = request.values.get('name')
        date = request.values.get('date')
        date = date.replace('-', '\\')
        down_path = 'D:\\dataSource\\copernicus' + '\\' + date + '\\' + name
        return send_file(down_path, as_attachment=True)


# @ns.route('/search')
# class SearchInfo(Resource):
#     def get(self):
#         date = datetime.datetime.now().strftime('%Y-%m-%d')
#         date = date + ' 00:00:00'
#         date = '2022-08-18 12:00:00'
#         print(date)
#         first_url = 'https://nrt.cmems-du.eu/motu-web/Motu?action=getsize&service=GLOBAL_ANALYSIS_FORECAST_PHY_001_024-TDS&product=global-analysis-forecast-phy-001-024&x_lo=-180&x_hi=179.9166717529296875&y_lo=-80&y_hi=90&t_lo=' + date + '&t_hi=' + date + '&z_lo=0.49402499198913574&z_hi=0.49402499198913574&variable=bottomT&variable=mlotst&variable=siconc&variable=sithick&variable=so&variable=thetao&variable=uo&variable=usi&variable=vo&variable=vsi&variable=zos'
#         first_url = 'https://nrt.cmems-du.eu/motu-web/Motu?action=getsize&service=GLOBAL_ANALYSIS_FORECAST_PHY_001_024-TDS&product=global-analysis-forecast-phy-001-024&x_lo=-180&x_hi=179.9166717529296875&y_lo=-80&y_hi=90&t_lo=' + date + '&t_hi=' + date + '&z_lo=0.49402499198913574&z_hi=0.49402499198913574&variable=bottomT&variable=mlotst&variable=usi&variable=vo&variable=vsi&variable=zos'
#         headers = {
#             "Cookie": "JSESSIONID=5CD7F6A0C7785D57B0607E5F81629F75",
#             "Accept": "*/*",
#             "Accept-Language": "zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",
#             "Host": "nrt.cmems-du.eu",
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
#         }
#
#         first_res = requests.get(url=first_url,headers=headers)
#         if first_res.status_code == 401:
#             return jsonify(errno=RET.DBERR, errmsg="查询失败")
#         # second_url = 'https://nrt.cmems-du.eu/motu-web/Motu?action=productdownload&service=GLOBAL_ANALYSIS_FORECAST_WAV_001_027-TDS&product=global-analysis-forecast-wav-001-027&x_lo=-180&x_hi=179.9166666666666287710540927946567535400390625&y_lo=-80&y_hi=90&t_lo=' + date + '&t_hi=' + date + '&variable=VHM0&variable=VHM0_SW1&variable=VHM0_SW2&variable=VHM0_WW&variable=VMDR&variable=VMDR_SW1&variable=VMDR_SW2&variable=VMDR_WW&variable=VPED&variable=VSDX&variable=VSDY&variable=VTM01_SW1&variable=VTM01_SW2&variable=VTM01_WW&variable=VTM02&variable=VTM10&variable=VTPK&output=netcdf&mode=status'
#         second_url = 'https://nrt.cmems-du.eu/motu-web/Motu?action=productdownload&service=GLOBAL_ANALYSIS_FORECAST_PHY_001_024-TDS&product=global-analysis-forecast-phy-001-024&x_lo=-180&x_hi=179.9166717529296875&y_lo=-80&y_hi=90&t_lo=' + date + '&t_hi=' + date + '&z_lo=0.49402499198913574&z_hi=0.49402499198913574&variable=bottomT&variable=mlotst&variable=siconc&variable=sithick&variable=so&variable=thetao&variable=uo&variable=usi&variable=vo&variable=vsi&variable=zos&output=netcdf&mode=status'
#         second_res = requests.get(url=second_url, headers=headers)
#         requestid = second_res.text[87:100]
#         # third_url = 'https://nrt.cmems-du.eu/motu-web/Motu?action=getreqstatus&service=GLOBAL_ANALYSIS_FORECAST_WAV_001_027-TDS&product=global-analysis-forecast-wav-001-027&requestid=' + requestid
#         third_url = 'https://nrt.cmems-du.eu/motu-web/Motu?action=getreqstatus&service=GLOBAL_ANALYSIS_FORECAST_PHY_001_024-TDS&product=global-analysis-forecast-phy-001-024&requestid=' + requestid
#         third_res = requests.get(url=third_url,headers=headers)
#         pattern = re.compile('"([^"]+)"')
#         # str_speaker_content_1 = third_res.replace(',', '')
#         str_speaker_content_2 = pattern.findall(third_res.text[56:])
#         data = {
#             "date": str_speaker_content_2[6],
#             "size": str_speaker_content_2[3] + "MB",
#             "path": str_speaker_content_2[4],
#         }
#         return jsonify(errno=RET.OK, data=data, errmsg="查询成功")
