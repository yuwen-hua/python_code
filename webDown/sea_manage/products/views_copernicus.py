# coding:utf-8
import json
import math
import os
import time
import datetime

import requests
from bson import ObjectId
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from sea_manage.products import rest_api as api
from flask import request, jsonify, current_app
from flask_restplus import Resource
from ..models.model_measured import ArgoMetaData
from ..models.model_dict import Dict
from ..models.model_dataset import Dataset
from ..models.model_multibean import Multibean2019
from ..untils.response_code import RET
from sea_manage.models.model_measured import Profile

from selenium import webdriver
# chromedriver = "F:/chromedriver_win32/chromedriver"  # 驱动程序所在的位置
grib2 = "F:/grib2"
# file = "D:\\Downloads\\gfs"
#



ns = api.namespace('copernicus', description='哨兵2专题模块API')

cookie = ''

@ns.route('/login')
class LoginInfo(Resource):
    @api.doc('登录哨兵2')
    @ns.param('username','用户名')
    @ns.param('password','密码')
    def get(self):
        """登录哨兵2网站"""
        username = request.values.get("username")
        password = request.values.get("password")
        url = 'https://scihub.copernicus.eu/dhus//login'
        data = {
            "login_username": username,
            "login_password": password
        }
        response = requests.post(url,data)
        if response.status_code == 401:
            return jsonify(errno=RET.DBERR, data=data, errmsg="登录失败，请重新登录")
        global cookie
        cookie = requests.utils.dict_from_cookiejar(response.cookies),
        cookie = 'dhusAuth=' + cookie[0]['dhusAuth'] + '; ' + 'dhusIntegrity=' + cookie[0]['dhusIntegrity']
        data = {
            "headers": dict(response.headers),
            "cookies": requests.utils.dict_from_cookiejar(response.cookies),
            'fun': cookie
            # "res": response
        }
        return jsonify(errno=RET.OK, data=data, errmsg="登录成功")

# cookie = 'dhusAuth=9fcad148dfe18f785e5ee951774c1f5f; dhusIntegrity=751b0da3f8f0321ac26a2d94192c61f957c6198a'
# cookie =
sortedby = ['beginposition', 'ingestiondate','datatakesensingstart,hv_order_tileid']
order = ['desc', 'asc']
platform = ['S2A_*','S2B_*']
producttype:'S2MSI1C'
limit = ['25','50','75','100','125','150']

@ns.route('/search')
class SearchInfo(Resource):
    @api.doc('查询条件获取')
    def get(self):
        """获取查询条件"""
        data = {
            "sortedby": ['beginposition', 'ingestiondate','datatakesensingstart,hv_order_tileid'],
            "order": ['desc', 'asc'],
            "platform": ['S2A_*','S2B_*'],
            "limit": ['25','50','75','100','125','150']
        }
        return jsonify(errno=RET.OK, data=data, errmsg="查询成功")


@ns.route('/metas')
class MetaInfo(Resource):
    @api.doc('获取列表')
    @ns.param('limit','限制返回个数，可以随意填')
    @ns.param('sortedby','返回顺序')
    @ns.param('platform','哨兵平台')
    @ns.param('order','上升、下降')
    @ns.param('pageNum','页数')
    def get(self):
        """获取列表"""
        limit = request.values.get("limit")
        sortedby = request.values.get("sortedby")
        platform = request.values.get("platform")
        order = request.values.get("order")
        pageNum = request.values.get("pageNum")
        sum = (int(pageNum) -1) * limit
        url = 'https://scihub.copernicus.eu/dhus/api/stub/products?filter=(%20%20(platformname:Sentinel-2%20AND%20filename:{platform}%20AND%20producttype:S2MSI1C))&offset={sum}&limit={limit}&sortedby={sortedby}&order={order}'.format(platform=platform,sum=sum,limit=limit,sortedby=sortedby,order=order)
        global cookie
        print(cookie)
        headers = {
            "Cookie": cookie,
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br"
        }
        response = requests.get(url=url,headers=headers)
        if response.status_code == 401:
            return jsonify(errno=RET.DBERR, errmsg="查询失败，请重新登录")
        response = response.json()
        list = []
        for i in response['products']:
            obj = {
                # "content": response.content,
                # "text": response.text,
                "date": i['summary'][0].split(':')[1][1:],
                "name": i['summary'][2].split(':')[1][1:] + '.zip',
                "size": i['summary'][5].split(':')[1][1:],
                "instrument": i['summary'][3].split(':')[1][1:],
                "satellite": i['summary'][4].split(':')[1][1:],
                "path": 'https://scihub.copernicus.eu/dhus/odata/v1/Products('+ "'"  + i['uuid'] + "'"  + ')/$value'
            }
            list.append(obj)
        data = {
            "data": list,
            "total": response['totalresults']
        }
        return jsonify(errno=RET.OK, data=data, errmsg="查询成功")
        # downUrl = 'https://scihub.copernicus.eu/dhus/odata/v1/Products('fdc4c14e-201b-4c0c-b8f1-185a4fa49c19')/$value'

@ns.route('/down')
class MetaInfo(Resource):
    @api.doc('获取哨兵1下载地址')
    @ns.param('path', '下载地址')
    @ns.param('name', '下载名称')
    @ns.param('username', '用户名')
    @ns.param('password', '密码')
    def get(self):
        """下载哨兵2"""
        name = request.values.get('name').split(',')
        path = request.values.get('path').split(',')
        username = request.values.get('username')
        password = request.values.get('password')
        arr = []
        list_name = []
        list_path = []
        today = datetime.datetime.now().strftime('%Y\\%m\\%d')
        t = round(time.time())
        t_10 = str(t)
        # down_path = 'D:\\dataSource\\webDown\\' + today + '\\' + t_10
        down_path = 'D:\\dataSource\\webDown'
        for root, dirs, files in os.walk(down_path):
            for file in files:
                for i in range(len(name)):
                    if file == name[i]:
                        # load = down_path + '\\' + name[i]
                        # obj = {
                        #     "name": name[i],
                        #     "path": load
                        # }
                        # list.append(obj)
                        list_name.append(name[i])
                        list_path.append(path[i])
                        # name.pop(i)
                        # path.pop(i)
        list_name = list(set(list_name))
        list_path = list(set(list_path))
        name = [x for x in name if x not in list_name]
        path = [x for x in path if x not in list_path]
        print((name))
        print((path))
        for i in range(len(list_name)):
            load = down_path + '\\' + list_name[i]
            obj = {
                "name": list_name[i],
                "path": load
            }
            arr.append(obj)
        if len(name) != 0:
            os.environ["webdriver.chrome.driver"] = current_app.config['CHROMEDRIVER']
            chromeOptions = webdriver.ChromeOptions()
            # 设定下载文件的保存目录
            # 如果该目录不存在，将会自动创建
            prefs = {"profile.default_content_settings.popups": 0, "download.default_directory": down_path}
            # 将自定义设置添加到Chrome配置对象实例中
            chromeOptions.add_experimental_option("prefs", prefs)
            # 启动带有自定义设置的Chrome浏览器
            driver = webdriver.Chrome(current_app.config['CHROMEDRIVER'], \
                                      chrome_options=chromeOptions)
            driver.maximize_window()  # 窗口最大化（无关紧要哈）
            # driver.get(path[0])
            # print('开始')
            # WebDriverWait(driver, 20).until(EC.alert_is_present())
            # prompt = driver.switch_to.alert
            # prompt.send_keys("大力水手吃菠菜")  # 这里输入框中看不到输入的文字
            # time.sleep(2)
            # prompt.accept()
            driver.get('https://scihub.copernicus.eu/dhus/#/home')
            time.sleep(5)
            login = driver.find_element_by_class_name("login-ico")
            login.click()
            time.sleep(2)
            user = driver.find_element_by_id("loginUsername")
            user.send_keys(username)
            time.sleep(5)
            word = driver.find_element_by_name("password")
            # submit = driver.find_element_by_css_selector(".btn .btn-default .login-btn")
            # user = driver.find_element_by_xpath("//form[@class='ng-valid ng-dirty ng-valid-parse']/div[@class='row'][1]/div[@class='group']/input[@id='loginUsername']")
            # word = driver.find_element_by_xpath("//form[@class='ng-valid ng-dirty ng-valid-parse']/div[@class='row'][2]/div[@class='group']/input[@class='form-control ng-valid ng-dirty ng-valid-parse ng-touched']")
            submit = driver.find_element_by_xpath("/html/body/div[@class='ng-scope']/div/div/div[@class='ng-isolate-scope'][7]/div/div[@id='userBadge']/div[2]/form[@class='ng-valid ng-dirty ng-valid-parse']/div[@class='row'][3]/button[@class='btn btn-default login-btn']")
            word.send_keys(password)
            time.sleep(5)
            submit.click()
            # if len(name) > 1:
            for i in path:
                time.sleep(5)
                driver.get(i)
            exists(down_path, name)
            for q in name:
                load = down_path + '\\' + q
                obj = {
                    "name": q,
                    "path": load
                }
                arr.append(obj)
            # else:
            #     load = down_path + '\\' + name[0]
            #     loneExists(load)
            #     list.append(load)
            driver.quit()
        return jsonify(errno=RET.OK, data=arr, errmsg="获取数据成功")



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