import json
import os
import re
import time
import base64
from PIL import Image
from gfs_model import GFS, profile
import cv2
import xarray as xr
import numpy as np
from selenium import webdriver
from mongoengine import connect
import datetime
import netCDF4 as nc
from osgeo import gdal, osr, ogr

from flask import Flask
import datetime
from flask_apscheduler import APScheduler
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

connect('prediction', host='114.242.60.27', port=8900)

chromedriver = "F:/chromedriver_win32/chromedriver"  # 驱动程序所在的位置
grib2 = "F:/grib2"
# file = "D:\\Downloads\\gfs"
#
os.environ["webdriver.chrome.driver"] = chromedriver  # 将驱动程序三位路径计入到系统路径中
# # 创建Chrome浏览器配置对象实例
# chromeOptions = webdriver.ChromeOptions()
# # 设定下载文件的保存目录
# # 如果该目录不存在，将会自动创建
# prefs = {"download.default_directory": file}
# # 将自定义设置添加到Chrome配置对象实例中
# chromeOptions.add_experimental_option("prefs", prefs)

# gfs.t00z.pgrb2full.0p25.f000，“t00”大概表示格林威治时刻0时发布的文件。0p25指的是精度，每0.25度（经纬度）一个点

app = Flask(__name__)


def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday


class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': 'app:task',
            'args': (1, 2),
            'trigger': 'cron',
            'day': '*',
            'hour': '10',
            'minute': '28'
        }
    ]
    SCHEDULER_API_ENABLED = True


def task(a, b):
    print(33)
    chromeOptions = webdriver.ChromeOptions()
    # file_date = datetime.datetime.now().strftime('%Y\\%m\\%d')
    down_path = 'D:\\dataSource\\nc\\Temperature'
    prefs = {"download.default_directory": down_path}
    chromeOptions.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chromedriver, \
                              chrome_options=chromeOptions)
    driver.get('http://mds.nmdis.org.cn/pages/dataView.html?type=2&id=a5da2a0528904471b3a326c3cc85997d')
    time.sleep(5)
    driver.maximize_window()

    # 跳转到登录页面
    a = driver.find_element_by_xpath("/html/body/div[@class='out']/div[@class='dataView']/div[@id='app']/div[@class='container clearb']/div[@class='datasetContent clearf']/div[@class='datasetList'][1]/div[@class='rightMsg']/h1/a")
    a.click()
    time.sleep(5)
    total = driver.find_element_by_xpath("//div[@class='page']//ul[@class='el-pager']/li[8]")
    total = int(total.text)
    checkbox = driver.find_element_by_xpath("//div[@class='el-table__header-wrapper']/table[@class='el-table__header']/thead[@class='has-gutter']/tr/th[@class='el-table_1_column_1  is-center el-table-column--selection  is-leaf']/div[@class='cell']/label[@class='el-checkbox']/span[@class='el-checkbox__input']/span[@class='el-checkbox__inner']")
    checkbox.click()
    time.sleep(5)

    element = WebDriverWait(driver, 5, 0.5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'ob-download')),
        message='超时啦!')
    if element:
        download = driver.find_element_by_xpath("//div[@class='dataViewDetail']/div[@id='app']/div[@class='container']/div[@class='dataMsgBox clearf']/div[@class='dataList']/div[@class='dataTable']/div[@class='page']/a/i[@class='iconfont ob-download']")
        download.click()
        time.sleep(5)

        logins(driver)
        login = WebDriverWait(driver, 5, 0.5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'el-pagination')),
            message='超时啦!')
        if login:
            # index 为想要下载的起始页
            index = 12
            if index < 7:
                getInitial(driver, index)
            else:
                getMore(driver, index)



def getInitial(driver, index):
    for i in range(index, 7):
        try:
            driver.find_element_by_xpath("//div[@class='page']//ul[@class='el-pager']")
        except Exception as e:
            logins(driver)
            time.sleep(10)
            getInitial(driver, i)

        li = "//div[@class='page']//ul[@class='el-pager']/li[" +  str(i) + "]"
        page = driver.find_element_by_xpath(li)
        page.click()
        time.sleep(5)
        checkDown(driver, i)
        if i == index:
            x = driver.find_element_by_xpath("/html/body[@class='el-popup-parent--hidden']/div[@class='out']/div[@class='dataViewDetail']/div[@id='app']/div[@class='container']/div[@id='downloadInfo']/div[@id='dragger']/div[@class='box']/div[@class='el-dialog__wrapper']/div[@class='el-dialog']/div[@class='el-dialog__header']/button[@class='el-dialog__headerbtn']/i[@class='el-dialog__close el-icon el-icon-close']")
            x.click()
        time.sleep(5)
    getMore(driver,7)


# 下载第七页及以后
def getMore(driver,index, totalPage):
    total = driver.find_element_by_xpath("//div[@class='page']//ul[@class='el-pager']/li[9]")
    total = int(total.text)

    # while index < total + 1:
    for i in range(index, total + 1):
            try:
                driver.find_element_by_xpath("//div[@class='page']//ul[@class='el-pager']")
            except Exception as e:
                logins(driver)
                time.sleep(10)
                page = driver.find_element_by_xpath("//div[@class='page']//ul[@class='el-pager']/li[6]")
                page.click()
                time.sleep(5)
                value = i - 6
                changePage(driver, i)
                checkDown(driver, i)
                x = driver.find_element_by_xpath(
                    "/html/body[@class='el-popup-parent--hidden']/div[@class='out']/div[@class='dataViewDetail']/div[@id='app']/div[@class='container']/div[@id='downloadInfo']/div[@id='dragger']/div[@class='box']/div[@class='el-dialog__wrapper']/div[@class='el-dialog']/div[@class='el-dialog__header']/button[@class='el-dialog__headerbtn']/i[@class='el-dialog__close el-icon el-icon-close']")
                x.click()
                time.sleep(5)
                getMore(driver, i)
            changePage(driver, i)
            checkDown(driver, i)
            if i == index:
                x = driver.find_element_by_xpath(
                    "/html/body[@class='el-popup-parent--hidden']/div[@class='out']/div[@class='dataViewDetail']/div[@id='app']/div[@class='container']/div[@id='downloadInfo']/div[@id='dragger']/div[@class='box']/div[@class='el-dialog__wrapper']/div[@class='el-dialog']/div[@class='el-dialog__header']/button[@class='el-dialog__headerbtn']/i[@class='el-dialog__close el-icon el-icon-close']")
                x.click()
            time.sleep(5)
            # index += 1

# 第一次点击 第六页 之后依次点击
def changePage(driver, index):
    for j in range(1, index - 4):
        li = "//div[@class='page']//ul[@class='el-pager']/li[6]"
        page = driver.find_element_by_xpath(li)
        page.click()
        time.sleep(5)

# 点击多选按钮 点击下载
def checkDown(driver, index):
    try:
        checkbox = driver.find_element_by_xpath(
            "//div[@class='el-table__header-wrapper']/table[@class='el-table__header']/thead[@class='has-gutter']/tr/th[@class='el-table_1_column_1  is-center el-table-column--selection  is-leaf']/div[@class='cell']/label[@class='el-checkbox']/span[@class='el-checkbox__input']/span[@class='el-checkbox__inner']")
    except Exception as e:
        driver.refresh()
        if index < 7:
            getInitial(driver, index)
        else:
            getMore(driver, index)
    checkbox = driver.find_element_by_xpath(
        "//div[@class='el-table__header-wrapper']/table[@class='el-table__header']/thead[@class='has-gutter']/tr/th[@class='el-table_1_column_1  is-center el-table-column--selection  is-leaf']/div[@class='cell']/label[@class='el-checkbox']/span[@class='el-checkbox__input']/span[@class='el-checkbox__inner']")

    checkbox.click()
    time.sleep(5)
    download = driver.find_element_by_xpath(
        "//div[@class='dataViewDetail']/div[@id='app']/div[@class='container']/div[@class='dataMsgBox clearf']/div[@class='dataList']/div[@class='dataTable']/div[@class='page']/a/i[@class='iconfont ob-download']")
    download.click()
    time.sleep(5)

# 登录
def logins(driver):
    user = driver.find_element_by_xpath(
        "/html/body/div[@id='root']/div[@class='base']/div[@class='Cont']/form[@class='el-form el-form--label-right']/div[@class='el-form-item other is-required'][1]/div[@class='el-form-item__content']/div[@class='el-input']/input[@class='el-input__inner']")
    password = driver.find_element_by_xpath(
        "/html/body/div[@id='root']/div[@class='base']/div[@class='Cont']/form[@class='el-form el-form--label-right']/div[@class='el-form-item other is-required'][2]/div[@class='el-form-item__content']/div[@class='el-input']/input[@class='el-input__inner']")
    submit = driver.find_element_by_xpath(
        "/html/body/div[@id='root']/div[@class='base']/div[@class='Cont']/form[@class='el-form el-form--label-right']/div[@class='el-form-item deng-lu']/div[@class='el-form-item__content']/button[@class='el-button save el-button--default']")
    user.send_keys('13148286156')
    time.sleep(5)
    password.send_keys('huang2580')
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



if __name__ == '__main__':
    # app = Flask(__name__)
    # def scheduler_init(app):
    #     scheduler = APScheduler()
    #     scheduler.init_app(app)
    #     scheduler.start()
    #
    # app.config.from_object(Config)
    # scheduler_init(app)
    task(1, 2)
    # print(222222222222)
    app.run(port=8000, debug=False)
