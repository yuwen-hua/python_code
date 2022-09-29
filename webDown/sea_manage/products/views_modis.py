import os
import re
import json
import time
import datetime

import requests
from sea_manage.products import rest_api as api
from flask import request, jsonify, current_app
from flask_restplus import Resource
from ..untils.response_code import RET


from selenium import webdriver
# chromedriver = "F:/chromedriver_win32/chromedriver"  # 驱动程序所在的位置
grib2 = "F:/grib2"
# file = "D:\\Downloads\\gfs"
#


ns = api.namespace('modis', description='modis专题模块API')


# def token():
#     url = 'https://urs.earthdata.nasa.gov/home'
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept-Language': 'zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6'
#     }
#     sss = requests.Session()
#     res = sss.get(url, headers = headers)
#     reg = '<input type="hidden" name="authenticity_token" value="(.*)" autocomplete="off" />'
#     pattern = re.compile(reg)
#     result = pattern.findall(res.text)[0]
#     return result

# @ns.route('/login')
# class LoginInfo(Resource):
#     @api.doc('登录modis网站')
#     @ns.param('username','用户名')
#     @ns.param('password','密码')
#     def get(self):
#         """登录modis网站"""
#         username = request.values.get("username")
#         password = request.values.get("password")
#         url = 'https://urs.earthdata.nasa.gov/login'
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
#             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#             'Accept-Encoding': 'gzip, deflate, br',
#             'Accept-Language': 'zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
#             'Content-Type': 'application/x-www-form-urlencoded',
#             # 'Cookie': '_gid=GA1.2.945304860.1660099013; _ga=GA1.4.507718093.1660023289; _gid=GA1.4.945304860.1660099013; urs_guid_ops=e4f4e771-6894-48ee-9681-f66a8f24e2ba; _ga_XXXXXXXXXX=GS1.1.1660099215179.boqrjt6l.1.0.1660099215.0; _urs-gui_session=c82e4c86ec371553541057b56af4a52c; _ga=GA1.1.507718093.1660023289'
#         }
#         sss = requests.Session()
#         res = sss.get(url, headers=headers)
#         reg = '<input type="hidden" name="authenticity_token" value="(.*)" autocomplete="off" />'
#         pattern = re.compile(reg)
#         authenticity_token = pattern.findall(res.text)[0]
#         urs_session = requests.utils.dict_from_cookiejar(res.cookies)['_urs-gui_session']
#         headers['Cookie'] = '_gid=GA1.2.945304860.1660099013; _ga=GA1.4.507718093.1660023289; _gid=GA1.4.945304860.1660099013; urs_guid_ops=e4f4e771-6894-48ee-9681-f66a8f24e2ba; _ga_XXXXXXXXXX=GS1.1.1660099215179.boqrjt6l.1.0.1660099215.0; _urs-gui_session=' + urs_session + '; _ga=GA1.1.507718093.1660023289'
#         data = {
#             "authenticity_token": authenticity_token,
#             "username": username,
#             "password": password,
#             "commit": "Log in",
#             # "client_id": "",
#             # "redirect_uri": ""
#         }
#         response = sss.post(url=url,headers=headers,data=data)
#         if response.status_code == 401:
#             return jsonify(errno=RET.DBERR, data=data, errmsg="登录失败，请重新登录")
#         global cookie
#         cookie = requests.utils.dict_from_cookiejar(response.cookies),
#         cookie = 'dhusAuth=' + cookie[0]['dhusAuth'] + '; ' + 'dhusIntegrity=' + cookie[0]['dhusIntegrity']
#         data = {
#             "headers": dict(response.headers),
#             "cookies": requests.utils.dict_from_cookiejar(response.cookies),
#             'fun': cookie
#             # "res": response
#         }
#         return jsonify(errno=RET.OK, data=data, errmsg="登录成功")


@ns.route('/search')
class SearchInfo(Resource):
    @api.doc('查询条件获取')
    def get(self):
        """获取查询条件"""
        data = {
            "product": ['MOD00F', 'MOD012KM','MOD02HKM,MOD02QKM','MOD02SSH','MOD03','MYD00F','MYD021KM','MYD02HKM','MYD02OBC','MYD02QKM','MYD02SSH','MYD03'],
        }
        return jsonify(errno=RET.OK, data=data, errmsg="查询成功")


@ns.route('/metas')
class MetaInfo(Resource):
    @api.doc('获取列表')
    @ns.param('product','类型')
    @ns.param('start','开始日期：2022-07-27')
    @ns.param('end','开始日期：2022-08-10')
    @ns.param('W','选择区域')
    @ns.param('N','选择区域')
    @ns.param('E','选择区域')
    @ns.param('S','选择区域')
    def get(self):
        """获取列表"""
        product = request.values.get("product")
        start = request.values.get("start")
        end = request.values.get("end")
        W = request.values.get("W")
        N = request.values.get("N")
        E = request.values.get("E")
        S = request.values.get("S")
        date = start + '..' + end
        areaOfInterest = 'x' + W + 'y' + N + ',x' + E + 'y' + S
        url = 'https://ladsweb.modaps.eosdis.nasa.gov/api/v1/files/product=' + product + '&collection=61&dateRanges=' + date +'&areaOfInterest=' + areaOfInterest + '&dayCoverage=true&dnboundCoverage=true'
        res = requests.get(url)
        res = res.json()
        list = []
        for i in res:
            fileURL = res[i]['fileURL'].replace('\/','/')
            path = 'https://ladsweb.modaps.eosdis.nasa.gov' + fileURL
            size = round(int(res[i]['size']) / 1000000)
            obj = {
                "name": res[i]['name'],
                "size": str(size) + 'MB',
                "path": path,
                "date": res[i]['end']
            }
            list.append(obj)
        return jsonify(errno=RET.OK, data=list, errmsg="查询成功")

@ns.route('/down')
class MetaInfo(Resource):
    @api.doc('获取modis下载地址')
    @ns.param('path', '下载地址')
    @ns.param('name', '下载名称')
    @ns.param('username', '用户名')
    @ns.param('password', '密码')
    def get(self):
        """下载modis L1B"""
        name =  request.values.get('name').split(',')
        path = request.values.get('path').split(',')
        username = request.values.get('username')
        password = request.values.get('password')
        list = []
        today = datetime.datetime.now().strftime('%Y\\%m\\%d')
        t = round(time.time())
        t_10 = str(t)
        # down_path = 'D:\\dataSource\\webDown\\' + today + '\\' + t_10
        down_path = 'D:\\dataSource\\webDown'
        for root, dirs, files in os.walk(down_path):
            for file in files:
                for i in range(len(name)):
                    if file == name[i]:
                        load = down_path + '\\' + name[i]
                        obj = {
                            "name": name[i],
                            "path": load
                        }
                        list.append(obj)
                        name.pop(i)
                        path.pop(i)
        # for q in name:
        #     load = down_path + '\\' + q
        #
        #     print(load)
        # return
        os.environ["webdriver.chrome.driver"] = current_app.config['CHROMEDRIVER']

        chromeOptions = webdriver.ChromeOptions()
        # 设定下载文件的保存目录
        # 如果该目录不存在，将会自动创建
        prefs = {"profile.default_content_settings.popups": 0,"download.default_directory": down_path}
        # 将自定义设置添加到Chrome配置对象实例中
        chromeOptions.add_experimental_option("prefs", prefs)
        # 启动带有自定义设置的Chrome浏览器
        driver = webdriver.Chrome(current_app.config['CHROMEDRIVER'], \
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
            list.append(obj)
        # if len(name) > 1:
        #     for i in path[1:]:
        #         time.sleep(5)
        #         driver.get(i)
        #     exists(down_path,name)
        #     for q in name:
        #         load = down_path + '\\' + q
        #         list.append(load)
        # else:
        #     driver.get(path[0])
        #     load = down_path + '\\' + name[0]
        #     loneExists(load)
        #     list.append(load)
        driver.quit()
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
            time.sleep(30)
            exists(down_path,name)