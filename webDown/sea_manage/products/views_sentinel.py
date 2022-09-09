# coding:utf-8
import datetime
import math
import random
import time
from functools import partial
import json
import os

import requests
from bson import ObjectId

from sea_manage.products import rest_api as api
from flask import request, jsonify, current_app, send_file
from flask_restplus import Resource
from ..untils.response_code import RET

from selenium import webdriver

chromedriver = "F:/chromedriver_win32/chromedriver"  # 驱动程序所在的位置
grib2 = "F:/grib2"
# file = "D:\\Downloads\\gfs"
#
os.environ["webdriver.chrome.driver"] = chromedriver

ns = api.namespace('sentinel', description='哨兵1专题模块API')


# @ns.route('/login')
# class LoginInfo(Resource):
#     @api.doc('登录哨兵1')
#     @ns.param('username','用户名')
#     @ns.param('password','密码')
#     def get(self):
#         """登录哨兵1网站"""
#         username = request.values.get("username")
#         password = request.values.get("password")
#         url = ''


@ns.route('/search')
class SearchInfo(Resource):
    @api.doc('获取哨兵1的条件')
    def get(self):
        """获取哨兵1的条件"""
        data = {
            "processinglevel": ['GRD_HD','GRD_MD','GRD_MS','GRD_HS','SLC']
        }
        return jsonify(errno=RET.OK, data=data, errmsg="获取数据成功")

@ns.route('/metas')
class MetaInfo(Resource):
    @api.doc('获取哨兵1下载地址')
    # @ns.param('platform', '哨兵1')
    # @ns.param('instrument', 'C-SAR')
    @ns.param('maxResults', '最大结果250')
    # @ns.param('output', '数据范围')
    @ns.param('processinglevel', '要下载的类型')
    @ns.param('start','2022-02-01T16:00:00Z')
    @ns.param('end','2022-02-09T15:59:59Z')
    def get(self):
        """获取哨兵1下载地址"""
        maxResults = request.values.get("maxResults")
        output = request.values.get("output")
        processinglevel = request.values.get("processinglevel")
        start = request.values.get("start")
        end = request.values.get("end")
        list = []
        if start and end:
            print('start and end')
            url = 'https://api-prod-private.asf.alaska.edu/services/search/param?platform=SENTINEL-1&instrument=C-SAR&processinglevel={processinglevel}&maxResults={maxResults}&output=jsonlite2&start={start}&end={end}'.format(
                processinglevel=processinglevel, maxResults=maxResults, start=start, end=end)
        elif end:
            print('end')
            url = 'https://api-prod-private.asf.alaska.edu/services/search/param?platform=SENTINEL-1&instrument=C-SAR&processinglevel={processinglevel}&maxResults={maxResults}&output=jsonlite2&end={end}'.format(
                processinglevel=processinglevel, maxResults=maxResults, end=end)
        elif start:
            print('start')
            url = 'https://api-prod-private.asf.alaska.edu/services/search/param?platform=SENTINEL-1&instrument=C-SAR&processinglevel={processinglevel}&maxResults={maxResults}&output=jsonlite2&start={start}'.format(
                processinglevel=processinglevel, maxResults=maxResults, start=start)
        else:
            url = 'https://api-prod-private.asf.alaska.edu/services/search/param?platform=SENTINEL-1&instrument=C-SAR&processinglevel={processinglevel}&maxResults={maxResults}&output=jsonlite2'.format(
                processinglevel=processinglevel, maxResults=maxResults)
        # s = requests.session()
        # s.keep_alive = False
        res = requests.get(url)
        if res.status_code == 401:
            return jsonify(errno=RET.DBERR, errmsg="查询失败")
        res = res.json()
        for i in res['results']:
            # if i['f'] == 635:
            http = i['du'].split('{')[0]
            path = http + i['gn'] + '.zip'
            obj = {
                "path": path,
                "name": i['gn'] + '.zip',
                "size": str(round(i['s'],2)) + 'MB',
                "date": i['st'],
                "type": i['pt']
            }
            list.append(obj)
        return jsonify(errno=RET.OK, data=list, errmsg="获取数据成功")


@ns.route('/down')
class MetaInfo(Resource):
    @api.doc('获取哨兵1下载地址')
    @ns.param('path', '下载地址')
    @ns.param('name', '下载名称')
    @ns.param('username', '用户名')
    @ns.param('password', '密码')
    def get(self):
        """下载哨兵1"""
        name =  request.values.get('name').split(',')
        path = request.values.get('path').split(',')
        username = request.values.get('username')
        password = request.values.get('password')
        today = datetime.datetime.now().strftime('%Y\\%m\\%d')
        t = round(time.time())
        t_10 = str(t)
        down_path = 'D:\\dataSource\\webDown\\' + today + '\\' + t_10
        list = []
        # for q in name:
        #     load = down_path + '\\' + q
        #
        #     print(load)
        # return
        chromeOptions = webdriver.ChromeOptions()
        # 设定下载文件的保存目录
        # 如果该目录不存在，将会自动创建
        prefs = {"profile.default_content_settings.popups": 0,"download.default_directory": down_path}
        # 将自定义设置添加到Chrome配置对象实例中
        chromeOptions.add_experimental_option("prefs", prefs)
        # 启动带有自定义设置的Chrome浏览器
        driver = webdriver.Chrome(chromedriver, \
                                  chrome_options=chromeOptions)
        driver.maximize_window()  # 窗口最大化（无关紧要哈）
        driver.get(path[0])
        user = driver.find_element_by_xpath("//form[@id='login']/p[1]/input[@id='username']")
        user.send_keys(username)
        time.sleep(5)
        word = driver.find_element_by_xpath("//form[@id='login']/p[2]/input[@id='password']")
        time.sleep(5)
        word.send_keys(password)
        submit = driver.find_element_by_xpath("//form[@id='login']/p[8]/input[@class='eui-btn--round eui-btn--green']")
        submit.click()
        detail_url = driver.find_element_by_xpath("//section[@class='page-block']/p[3]/a").get_attribute("href")
        time.sleep(5)
        # cookies = driver.get_cookies()
        # for cookie in cookies:
        #     if 'expiry' in cookie:  # 有的cookie里面有这个参数，有的没有。有的话，需要做处理。
        #         del cookie['expiry']
        #     driver.add_cookie(cookie)  # 传入cookie
        # driver.refresh()  # 刷新页面
        # js = "window.open({detail_url})".format(detail_url=detail_url)
        # driver.execute_script(js)
        # driver.close()
        print(detail_url)
        if len(name) > 1:
            for i in path[1:]:
                time.sleep(5)
                driver.get(i)
            exists(down_path,name)
            for q in name:
                load = down_path + '\\' + q
                list.append(load)
        else:
            load = down_path + '\\' + name[0]
            loneExists(load)
            list.append(load)
        driver.quit()
            # down_url = down_path + name
            # list.append(down_url)
        # driver.get(detail_url)
        # js = "window.open({path})".format(path)
        # driver.execute_script(js)
        # time.sleep(60)
        # driver.close()
        return jsonify(errno=RET.OK, data=list, errmsg="获取数据成功")

'https://datapool.asf.alaska.edu/GRD_MS/SA/S1A_EW_GRDM_1SSH_20220209T080909_20220209T081009_041833_04FADD_817C.zip'
'S1A_EW_GRDM_1SSH_20220209T080909_20220209T081009_041833_04FADD_817C'

logout = 'https://auth.asf.alaska.edu/loginservice/logout'


def loneExists(load):
    print('判断文件是否存在：', load)
    whether = os.path.exists(load)
    if whether:
        return True
    else:
        time.sleep(10)
        loneExists(load)

# 过个文件
def exists(down_path,name):
    for j in name:
        print('判断文件是否存在：', down_path + '\\' + j)
        load = down_path + '\\' + j
        if os.path.exists(load):
            continue
        else:
            time.sleep(15)
            exists(down_path,name)
# @ns.route('/down')
# class MetaInfo(Resource):
#     @api.doc('下载')
#     @ns.param('{list}', '数据要素类型')
#     def post(self):
#         """下载SLC"""
#         req_dict = request.get_json()
#         list = req_dict.get('list')

# authenticity_token: 7OYzqmmu4PpAWz7C466b7JsXJBty5ZmWRoAeqFIeRBm20/MQpy7O9ty/lzKXlICjoGZ1AOb0C1hQFDXEUVpteQ==
# username: ChrisOsta
# password: Huang2580.
# client_id: BO_n7nTIlMljdvU6kRRB3g
# redirect_uri: https://auth.asf.alaska.edu/login
# response_type: code
# state: https://search.asf.alaska.edu
# stay_in: 1
# commit: Log in
#
#
#
# https://urs.earthdata.nasa.gov/login