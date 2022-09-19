import datetime
import json
import os
import time
import requests
from sea_manage.products import rest_api as api
from flask import request, jsonify, current_app, send_file
from flask_restplus import Resource
from ..untils.response_code import RET
from selenium import webdriver


ns = api.namespace('hydrology', description='国家海洋科学数据中心专题模块API')


@ns.route('/search')
class SearchInfo(Resource):
    @api.doc('获取国家海洋科学数据中心的条件')
    def get(self):
        """获取国家海洋科学数据中心的条件"""
        data = {
            "温度": "48",
            "地转流": "49",
            "密度": "50",
            "声速": "51",
            "盐度": "52",
        }
        print()
        return jsonify(errno=RET.OK, data=data, errmsg="获取数据成功")

res_json = ''
@ns.route('/select')
class listInfo(Resource):
    @api.doc('获取各类型的请求')
    @ns.param('id', 'search请求的结果')
    def get(self):
        """search请求的结果"""
        id = request.values.get("id")
        Grid_url = 'http://mds.nmdis.org.cn/service/sdm/front/DataGridValue/getGridOneById?id={id}'.format(id=id)
        res = requests.get(Grid_url)
        global res_json
        res_json = res.json()
        return jsonify(errno=RET.OK, data=res_json, errmsg="获取数据成功")



@ns.route('/metas')
class MetasInfo(Resource):
    @api.doc('获取列表')
    @ns.param('pageNumber', '页数')
    def get(self):
        """获取列表"""
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/json;charset=UTF-8"
        }
        meta_url = 'http://mds.nmdis.org.cn/service/sdm/front/DataGridValue/getValue'
        pageNumber = int(request.values.get("pageNumber"))
        res_json['data']['pageNumber'] = pageNumber
        response = requests.post(url=meta_url,headers=headers,data=json.dumps(res_json['data']))
        response = response.json()
        return jsonify(errno=RET.OK, data=response, errmsg="获取数据成功")

@ns.route('/down')
class MetaInfo(Resource):
    @api.doc('下载')
    @ns.param('id', 'id')
    @ns.param('path', '下载地址')
    @ns.param('name', '下载名称')
    @ns.param('username', '用户名')
    @ns.param('password', '密码')
    def get(self):
        """下载"""
        name = request.values.get('name').split(',')
        path = request.values.get('path').split(',')
        id = request.values.get('id')
        username = request.values.get('username')
        password = request.values.get('password')
        print(username,password)
        today = datetime.datetime.now().strftime('%Y\\%m\\%d')
        t = round(time.time())
        t_10 = str(t)
        down_path = 'D:\\dataSource\\webDown\\' + today + '\\' + t_10
        list = []
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
        cookie = logins(driver,username,password)
        access_token = cookie[2]['value']
        if len(path) > 1:
            for i in path:
                time.sleep(5)
                path = 'http://mds.nmdis.org.cn/service/sdm/front/DataGridValue/downLoad?datasetId={id}&gridId={id}&id={symbod}&access_token={access_token}'.format(id=id,symbod=i,access_token=access_token)
                driver.get(path)
            exists(down_path, name)
            for q in name:
                load = down_path + '\\' + q + '.nc'
                list.append(load)
        else:
            path = 'http://mds.nmdis.org.cn/service/sdm/front/DataGridValue/downLoad?datasetId={id}&gridId={id}&id={symbod}&access_token={access_token}'.format(id=id, symbod=path[0], access_token=access_token)
            driver.get(path)
            load = down_path + '\\' + name[0] + '.nc'
            loneExists(load)
            list.append(load)
        driver.quit()
        return jsonify(errno=RET.OK, data=list, errmsg="获取数据成功")
url = 'http://mds.nmdis.org.cn/service/sdm/front/DataGridValue/downLoad?datasetltld=48&gridld=48&id=b3a3ac3a36ed734e4893b89fc176c429fa'

login = 'http://mds.nmdis.org.cn/service/uaa/oauth/token'
# username: P0113148286156
# password2: m+GAAAQpc4+zSwiDwXyEYQuGWcG01aXBSGqYSjWwYeeXzcmj8FFJ2IROOTR/SOsqr3ySji/dbIf15raLr/pauA==
# client_id: webapp
# client_secret: webapp
# grant_type: password

def logins(driver,username,passwords):
    print(driver,username,passwords)
    driver.get('http://mds.nmdis.org.cn/pages/signIn.html')
    user = driver.find_element_by_xpath(
        "/html/body/div[@id='root']/div[@class='base']/div[@class='Cont']/form[@class='el-form el-form--label-right']/div[@class='el-form-item other is-required'][1]/div[@class='el-form-item__content']/div[@class='el-input']/input[@class='el-input__inner']")
    password = driver.find_element_by_xpath(
        "/html/body/div[@id='root']/div[@class='base']/div[@class='Cont']/form[@class='el-form el-form--label-right']/div[@class='el-form-item other is-required'][2]/div[@class='el-form-item__content']/div[@class='el-input']/input[@class='el-input__inner']")
    submit = driver.find_element_by_xpath(
        "/html/body/div[@id='root']/div[@class='base']/div[@class='Cont']/form[@class='el-form el-form--label-right']/div[@class='el-form-item deng-lu']/div[@class='el-form-item__content']/button[@class='el-button save el-button--default']")
    user.send_keys(username)
    time.sleep(5)
    password.send_keys(passwords)
    time.sleep(5)
    submit.click()
    time.sleep(5)
    # 滑动验证
    swiper = driver.find_element_by_xpath("//div[@class='verify-move-block']")
    action = webdriver.ActionChains(driver)  # 创建动作
    action.click_and_hold(swiper).perform()
    action.move_by_offset(0, 0).perform()
    verify_style = driver.find_element_by_xpath("//div[@class='verify-move-block']/div")
    verified_style = driver.find_element_by_xpath("//div[@class='verify-gap']")
    verified_left = float(verified_style.value_of_css_property('left').split('px')[0])
    verify_left = float(verify_style.value_of_css_property('left').split('px')[0])
    action.move_by_offset(verified_left - verify_left, 0)
    action.release().perform()
    time.sleep(10)
    cookie = driver.get_cookies()
    return cookie

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
        print('判断文件是否存在：', down_path + '\\' + j + '.nc')
        load = down_path + '\\' + j + '.nc'
        if os.path.exists(load):
            continue
        else:
            time.sleep(15)
            exists(down_path,name)