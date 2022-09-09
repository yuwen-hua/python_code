
import json
import os
import time
import base64
import datetime
import xarray as xr
import numpy as np
from selenium import webdriver


# 自动下载 气象预报数据


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



class DownLoad():
    def __init__(self):
        level = ['lev_surface', 'lev_max_wind', 'lev_2_m_above_ground', 'lev_low_cloud_layer']
        level = ['lev_low_cloud_layer']
        date = getYesterday()
        down_date = date.strftime('%Y%m%d')
        file_date = datetime.datetime.now().strftime('%Y\\%m\\%d')
        print(type(date), date)
        for i in level:
            down_path = 'D:\\dataSource\\gfs' + '\\' + i + '\\' + file_date
            downFile(down_date, i, down_path)
            re(date, i, down_path)


def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday


def task(a, b):
    level = ['lev_surface', 'lev_max_wind', 'lev_2_m_above_ground', 'lev_low_cloud_layer']
    date = getYesterday()
    down_date = date.strftime('%Y%m%d')
    file_date = datetime.datetime.now().strftime('%Y\\%m\\%d')
    print(type(date), date)
    for i in level:
        down_path = 'D:\\dataSource\\gfs' + '\\' + i + '\\' + file_date
        downFile(down_date, i, down_path)
        re(date, i, down_path)


def downFile(date, level, down_path):
    print(2222, date, level, down_path)
    chromeOptions = webdriver.ChromeOptions()
    # 设定下载文件的保存目录
    # 如果该目录不存在，将会自动创建
    prefs = {"download.default_directory": down_path}
    # 将自定义设置添加到Chrome配置对象实例中
    chromeOptions.add_experimental_option("prefs", prefs)
    # 启动带有自定义设置的Chrome浏览器
    driver = webdriver.Chrome(chromedriver, \
                              chrome_options=chromeOptions)
    driver.maximize_window()  # 窗口最大化（无关紧要哈）
    # gfs.t00z.pgrb2full.0p25.f000，“t00”大概表示格林威治时刻0时发布的文件。0p25指的是精度，每0.25度（经纬度）一个点

    for i in range(32, 56):  # 取值从1~75，表示从1到75个小时的预测时长上的
        if i < 10:
            i = "00%d" % i
        elif i < 100:
            i = "0%d" % i
        else:
            i = str(i)
        for j in [0]:  # 表示数据发布的时间分别是00,06,12,18

            if j < 10:
                j = "0%d" % j
            elif j < 100:
                j = "%d" % j
            else:
                j = str(j)
            path = "https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?file=gfs.t" + j + "z.pgrb2.0p25.f" + i + "&" + level + "=on&var_PRES=on&var_CPOFP=on&var_TMP=on&var_LCDC=on&var_TCDC=on&var_PLPL=on&var_GUST=on&var_UGRD=on&var_VGRD=on&var_ICEC=on&var_RH=on&var_ICETK=on&var_SNOD=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs." + date + "%2F" + j + "%2Fatmos"
            print('path', path)
            driver.get(path)  # 打开网址
    print('开始休眠等待浏览器将数据下载完成')
    time.sleep(60)
    driver.quit()


def re(date, level, file):
    print(111)
    # 转到wgrib2工具目录
    os.chdir(grib2)

    for root, dirs, files in os.walk(file):
        for file in files:
            p = os.path.join(root, file)
            nc_path = "wgrib2" + " " + p + " " + "-netcdf" + " " + p + ".nc"
            os.system(nc_path)