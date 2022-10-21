import json
import os
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
# import netCDF4 as nc
import ecmwflibs
# from osgeo import gdal
# import pygrib
# import gribapi
# import eccodes
# import cfgrib
# import ecmwflibs

from osgeo import gdal, osr, ogr

from flask import Flask
import datetime
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler

from apscheduler.triggers.cron import CronTrigger

connect('prediction', host='114.242.60.27', port=6700, username='admin', password='123456',authentication_source='admin')

# 不需要grib2

chromedriver = "/data/pythonworks/down_gfs/chromedriver"  # 驱动程序所在的位置
#grib2 = "F:/grib2"
# chromedriver = '/data/pythonworks/down_gfs/chromedriver'
# grib2 = '/data/pythonworks/down_gfs/grib2'
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
            'hour': '01',
            'minute': '21'
        }
    ]
    SCHEDULER_API_ENABLED = True


# 下载文件、解析文件、删除文件
def task(a, b):
    level = ['lev_surface', 'lev_max_wind', 'lev_2_m_above_ground', 'lev_low_cloud_layer']
    date = getYesterday()
    down_date = date.strftime('%Y%m%d')
    file_date = datetime.datetime.now().strftime('%Y/%m/%d')
    # file_date = '2022\\10\\19'
    for i in level:
        # down_path = 'D:\\dataSource\\gfs' + '\\' + i + '\\' + file_date
        down_path = '/data/dataSource/gfs' + '/' + i + '/' + file_date
        print('保存路径',down_path)
        # 下载文件
        downFile(down_date,i, down_path)
        # 解析文件
        transformation(date, i, down_path)
        # 删除除tif类型以外的文件
        for root, dirs, files in os.walk(down_path):
            index = 0
            for file in files:
                index += 1
                if not file.endswith('.tif'):
                    print('删除：', root + '/' + file, root)
                    os.remove(root + '/' + file)
                # time.sleep(120)
        # 保存风速到json文件中
        if i == 'lev_max_wind':
            for root, dirs, files in os.walk(down_path):
                index = 0
                for file in files:
                    index += 1
                    if (index % 2) == 0:
                        sort = int(file[22:24]) - 32
                        v = Image.open(root + '/' + file)
                        v_arr = np.asarray(v)
                        u_name = file[:25]
                        u_name = u_name + 'U' + file[26:]
                        u = Image.open(root + '/' + u_name)
                        u_arr = np.asarray(u)
                        result = create_wind(u_arr, v_arr)
                        result = json.dumps(result)
                        # path = 'D:\\dataSource\\gfs' + '\\' + 'json' + '\\' + file_date + '\\'
                        path = '/data/dataSource/gfs' + '/' + 'json' + '/' + file_date + '/'
                        if not os.path.exists(path):
                            os.makedirs(path)
                        with open(path + str(sort) + '.json', 'w', encoding='utf-8') as f:
                            f.write(result)
    print(down_date, file_date, date, down_path)
    print(str(datetime.datetime.now()) + ' execute task ' + '{}+{}={}'.format(a, b, a + b))


def create_wind(u, v):
    result = {}
    result['lat_size'] = -0.25
    result['lon_size'] = -0.25
    dx = result['lat_size'] * 3
    dy = result['lon_size'] * 3
    header_u = {
        "lo1": 0,
        "lo2": 359.75,
        "la1": 90,
        "la2": -90,
        "dx": -dx,
        "dy": -dy,
        "nx": 480,
        "ny": 241,
        "refTime": datetime.datetime.now().strftime("%Y-%m-%d"),
        # "refTime": '2022-07-15',
        "parameterUnit": "m.s-1",
        "parameterNumber": 2,
        "parameterCategory": 2,
        "scale": "1.0.0"
    }
    header_v = {
        "lo1": 0,
        "lo2": 359.75,
        "la1": 90,
        "la2": -90,
        "dx": dx,
        "dy": dy,
        "nx": 480,
        "ny": 241,
        "refTime": datetime.datetime.now().strftime("%Y-%m-%d"),
        # "refTime": '2022-07-15',
        "parameterUnit": "m.s-1",
        "parameterNumber": 3,
        "parameterCategory": 2,
        "scale": "1.0.0"
    }
    u = u[slice(None, None, 3), slice(None, None, 3)]
    v = v[slice(None, None, 3), slice(None, None, 3)]
    # arr_u = u
    # arr_v = v
    # np.place(arr_u, u == -9999, np.nan)
    # np.place(arr_v, v == -9999, np.nan)
    # u = u * 10000
    # v = v * 10000
    # result1 = json.dumps({
    #     'hearder': hearder,
    #     'data': u.flatten('F').tolist()
    # }),
    result1 = {
                  'header': header_u,
                  'data': u.reshape(-1, ).tolist()
              },
    result2 = {
                  'header': header_v,
                  'data': v.reshape(-1, ).tolist()
              },
    wfJSON = []
    wfJSON.append(result1[0])
    wfJSON.append(result2[0])
    result['json'] = wfJSON
    return result


# @app.route('/download')
# def download():
#     chromeOptions = webdriver.ChromeOptions()
#     date = datetime.datetime.now().strftime('%Y%m%d')
#     hour = int(datetime.datetime.now().strftime('%H')) - 8
#     # 将要获取的格林威治时刻应该 减去8
#     driver = webdriver.Chrome(chromedriver, \
#                               chrome_options=chromeOptions)
#     if hour < 10:
#         hour = "00%d" % hour
#     elif hour < 100:
#         hour = "0%d" % hour
#     else:
#         hour = str(hour)
#     for j in [0]:  # 表示数据发布的时间分别是00,06,12,18
#
#         if j < 10:
#             j = "0%d" % j
#         elif j < 100:
#             j = "%d" % j
#         else:
#             j = str(j)
#         path = "https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?file=gfs.t" + j + "z.pgrb2.0p25.f" + hour + "&var_PRES=on&var_CPOFP=on&var_TMP=on&var_LCDC=on&var_TCDC=on&var_PLPL=on&var_GUST=on&var_VGRD=on&var_UGRD=on&var_ICEC=on&var_RH=on&var_ICETK=on&var_SNOD=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs." + date + "%2F" + j + "%2Fatmos"
#         print('path', path)
#         driver.get(path)  # 打开网址
#     print('开始休眠等待浏览器将数据下载完成')
#     time.sleep(60)
#     driver.quit()
#     return 'Hello World!'


# 下载文件
def downFile(date, level, down_path):
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("no-sandbox")
    chromeOptions.add_argument('--headless')
    chromeOptions.add_argument('--disable-gpu')
    # 设定下载文件的保存目录
    # 如果该目录不存在，将会自动创建
    prefs = {"download.default_directory": down_path}
    # 将自定义设置添加到Chrome配置对象实例中
    chromeOptions.add_experimental_option("prefs", prefs)
    # 启动带有自定义设置的Chrome浏览器
    driver = webdriver.Chrome(executable_path=chromedriver, \
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


def transformation(date, level, file):
    print(file)
    # 转到wgrib2工具目录
    # os.chdir(grib2)

    for root, dirs, files in os.walk(file):
        for file in files:
            path = root + '/' +file
            # p = os.path.join(root, file)
            # nc_path ="wgrib2"+ " " + p + " " + "-netcdf" + " " + p + ".nc"
            print(root + '/' + file)
            if level == 'lev_surface':
                keyList = ['t', 'sde', 'cpofp', 'unknown', 'sp','siconc','gust']
            elif level == 'lev_2_m_above_ground':
                keyList = ['r2']
            elif level == 'lev_low_cloud_layer':
                keyList = ['lcc']
            elif level == 'lev_max_wind':
                keyList = ['u', 'v']
            get_nc(keyList, path, file)
            # # nc_path = CMD ["wgrib2", p, "-netcdf", p, ".nc"]
            # # 转化为nc文件
            # os.system(nc_path)
            # p = p + '.nc'
            main(path,'互联网公开数据', 'gfs', date,level,file,keyList)

    #         read_path = "wgrib2" " " + p + " " + "-v"
    #         os.system(read_path)
    # #
    # # # 匹配SOIL_M
    #         down_path = "wgrib2" " " + p + " " + "-csv" + " " "D:/abc.csv"
    #         os.system(down_path)

    return None


# 解析nc文件并保存元数据
def nc2mg(path, var_key, data_source, file_name, data_time, p):
    print('元数据解析')
    if var_key == 'lcc':
        ds = xr.open_dataset(path, engine='cfgrib', filter_by_keys={'stepType': 'instant'})
    else:
        ds = xr.open_dataset(path, engine='cfgrib')
    if var_key == 'VMGWD_surface' or var_key == 'UMGWD_surface':
        print('这是')
    else:
        lon_name = 'longitude'  # 你的nc文件中经度的命名
        ds['longitude_adjusted'] = xr.where(
            ds[lon_name] > 180,
            ds[lon_name] - 360,
            ds[lon_name])
        ds = (
            ds
                .swap_dims({lon_name: 'longitude_adjusted'})
                .sel(**{'longitude_adjusted': sorted(ds.longitude_adjusted)})
                .drop(lon_name))
        ds = ds.rename({'longitude_adjusted': lon_name})
        ds[lon_name].attrs['units'] = 'degree_east'

    var = ds[var_key]
    varlist = ds.variables.mapping.keys()
    dimensions = ds.dims.mapping.keys()
    for d in dimensions:
        if 'lat' in d:
            lat_key = d
        if 'lon' in d:
            lon_key = d
        if 'dep' in d:
            dep_key = d
    unitsDic = {}
    for dm in varlist:
        if dm == 'time' or dm == 'step' or dm == 'latitude' or dm == 'valid_time' or dm == 'longitude' or dm == 'surface' or dm == 'maxWind' or dm == 'pres' or dm == 'heightAboveGround' or dm == 't2m' or dm == 'lowCloudLayer':
            continue
        print(dm)
        tif_name,dataset_id = toSurface(dm)
        unitsDic[tif_name] = ds[dm].GRIB_units
    lat = ds[lat_key][:]
    lon = ds[lon_key][:]
    # depths = ds[dep_key][:]
    # depths1 = np.array(ds[dep_key][:]).tolist()
    # c= []
    # for i in depths1:
    #     i = i * -1
    #     c.append(i)
    # print(c)
    # print(depths1)

    data_time = (data_time + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    sort = int(file_name[-2:]) - 32
    var_key,dataset_id = toSurface(var_key)
    ncmeta = GFS(
        dataset_id=dataset_id,
        dataset_name=file_name,
        data_format='GFS',
        contact_name='yyp',
        institution='xintian',
        model_variables=varlist,
        model_dimensions=dimensions,
        keywords=['天气预报', file_name],
        ocean_area=[0],
        subjects=[1],
        # model_depth=depths1,
        model_dt=[data_time],
        sort=sort,
        database_year=data_time[0:4],
        shared='625d05ad44fb0bfb1b12f3a4',
        timeliness='实时',
        data_type=var_key,
        data_file_path=p
    )
    tif_path = path.split('.nc')[0] + '_' + var_key + '.tif'
    print(tif_path)
    ncmeta.save()
    print('元数据保存')
    saveData(var, tif_path, dimensions, data_source, unitsDic, data_time, lat, lon, ncmeta, var_key, sort)


# 保存数据
def saveData(var, tif_path, dimensions, data_source, unitsDic, data_time, lat, lon, ncmeta, var_key, sort):
    # for depth in depths:
    # temp = var.sel()
    grand = np.array(var)
    [rows, cols] = np.array(var).shape
    print('开始生成色斑图')
    r, g, b, a = getRgbArrayList(grand, '0')
    data = np.zeros((rows, cols), dtype=np.uint8)
    img = cv2.cvtColor(data, cv2.COLOR_GRAY2BGRA)
    img[:, :, 0] = b
    img[:, :, 1] = g
    img[:, :, 2] = r
    img[:, :, 3] = a
    print('色斑图生成完毕')
    img_str = 'data:image/png;base64,' + base64.b64encode(cv2.imencode('.png', img)[1]).decode()
    elevation = open(tif_path, 'rb')
    if var_key == 'VGRD_maxwind' or var_key == 'UGRD_maxwind':
        nc = profile[var_key](
            dimensions=dimensions,
            data_source=data_source,
            units=unitsDic,
            date_time=datetime.datetime.now().strftime('%Y-%m-%d'),
            lat_start=lat.values[0],
            lon_start=lon.values[0],
            lat_length=len(lat.values),
            lon_length=len(lon.values),
            lat_size=lat.values[0] - lat.values[1],
            lon_size=lon.values[0] - lon.values[1],
            img=img_str,
            # img2=img_str2,
            # grand=grand.tolist(),
            values=elevation,
            meta_data=ncmeta,
            sort=sort
            # unit=
        )
    else:
        nc = profile[var_key](
            dimensions=dimensions,
            data_source=data_source,
            units=unitsDic,
            date_time=datetime.datetime.now().strftime('%Y-%m-%d'),
            lat_start=lat.values[0],
            lon_start=lon.values[0],
            lat_length=len(lat.values),
            lon_length=len(lon.values),
            lat_size=lat.values[0] - lat.values[1],
            lon_size=lon.values[0] - lon.values[1],
            img=img_str,
            # img2=img_str2,
            values=elevation,
            meta_data=ncmeta,
            sort=sort
            # unit=
        )

    nc.save()
    print('nc数据保存', nc)


# 将nc文件转化为tif文件并保存元数据
def main(path, data_source, key, date, level, filename, keyList):
    # var_keyh = path.split("\\nc\\")[1].split("\\")[0]
    # 每一个类型有固定的数据
    # if level == 'lev_surface':
    #     keyList = ['CPOFP_surface', 'PRES_surface', 'GUST_surface', 'ICEC_surface', 'ICETK_surface', 'SNOD_surface',
    #                'TMP_surface']
    # elif level == 'lev_2_m_above_ground':
    #     keyList = ['RH_2maboveground']
    # elif level == 'lev_low_cloud_layer':
    #     keyList = ['LCDC_lowcloudlayer']
    # elif level == 'lev_max_wind':
    #     keyList = ['UGRD_maxwind', 'VGRD_maxwind']
    # 转为tif
    # get_nc(keyList, path, filename)
    for i in keyList:
        var_keyh = i
        file_name = filename
        data_time = date
        nc2mg(path, var_keyh, data_source, file_name, data_time, path.split(key)[1])


def linearInterpolation(x, x1, x2, x1value, x2value):
    a = ((x2 - x) / (x2 - x1) * x1value) + ((x - x1) / (x2 - x1) * x2value)
    return int(a)


# 获取每个值的颜色rgb数组
def get_l_co(value, colorArr, breakArray, type):
    breakArrLenth = len(breakArray)
    colLenth = len(colorArr)
    for i in range(breakArrLenth):
        breakValue = breakArray[i]
        rgba = colorArr[i]
        if np.isnan(value):
            if type == '0':
                return 255, 255, 255, 255
            else:
                return 0, 0, 0, 0
        if value > breakArray[breakArrLenth - 1]:
            return colorArr[breakArrLenth - 1][0], colorArr[breakArrLenth - 1][1], colorArr[breakArrLenth - 1][2], 255
        if (value <= breakValue):
            if i == 0:
                return rgba[0], rgba[1], rgba[2], 255
            else:
                lastBreak = breakArray[i - 1]
                lastrgba = colorArr[i - 1]
                r = linearInterpolation(value, lastBreak, breakValue, lastrgba[0], rgba[0])
                g = linearInterpolation(value, lastBreak, breakValue, lastrgba[1], rgba[1])
                b = linearInterpolation(value, lastBreak, breakValue, lastrgba[2], rgba[2])
                a = linearInterpolation(value, lastBreak, breakValue, lastrgba[3], rgba[3])
                return r, g, b, 255


# 生成rgb线性数组
def getRgbArrayList(array, type):
    [rows, cols] = array.shape
    d = np.nan_to_num(array, True, 99999)
    m = np.nan_to_num(array, True, -10000)
    max = np.max(m)
    min = np.min(d)
    jg = (max - min) / 6
    breaks = []
    for i in range(6):
        breaks.append(min + i * jg)
    r = np.zeros([rows, cols])
    g = np.zeros([rows, cols])
    b = np.zeros([rows, cols])
    a = np.zeros([rows, cols])
    # breakArray = [0, 5, 10, 15, 20, 30]
    colorArr = [[0, 0, 204, 1], [94, 179, 255, 1], [168, 243, 255, 1], [255, 232, 0, 1], [255, 53, 0, 1],
                [128, 0, 0, 1]]
    for i in range(cols):
        for j in range(rows):
            # if not getlinearColor(array[i, j], colorArr, breakArray):
            r[j][i], g[j][i], b[j][i], a[j][i] = get_l_co(array[j, i], colorArr, breaks, type)
    return r, g, b, a


# 获取nc文件数据
def get_nc(key_list, path, filename):
    # for root, dirs, files in os.walk(path):
    #     for file_name in files:
    # if path.endswith('.nc'):
    if key_list[0] == 'lcc':
        ds = xr.open_dataset(path, engine='cfgrib', filter_by_keys={'stepType': 'instant'})
    else:
        ds = xr.open_dataset(path, engine='cfgrib')
    lon_name = 'longitude'  # 你的nc文件中经度的命名
    ds['longitude_adjusted'] = xr.where(
        ds[lon_name] > 180,
        ds[lon_name] - 360,
        ds[lon_name])
    ds = (
        ds
            .swap_dims({lon_name: 'longitude_adjusted'})
            .sel(**{'longitude_adjusted': sorted(ds.longitude_adjusted)})
            .drop(lon_name))
    ds = ds.rename({'longitude_adjusted': lon_name})
    ds[lon_name].attrs['units'] = 'degree_east'
    for key in key_list:
        nc_tif(ds, path, key, filename.split('.nc')[0])


# nc数据集转tif
def nc_tif(ds, path, key, file_name):
    Lat = np.array(ds['latitude'])
    Lon = np.array(ds['longitude'])
    value = np.array(ds[key])
    [rows, cols] = value.shape
    dara = np.insert(value, cols - 1, value[:, cols - 1], axis=1)
    [rows, cols] = dara.shape
    value = np.insert(dara, cols - 1, dara[:, cols - 1], axis=1)

    LonMin, LatMax, LonMax, LatMin = [Lon.min(), Lat.max(), Lon.max(), Lat.min()]
    LonMin = -180
    N_Lat = len(Lat)
    N_Lon = len(Lon) + 2
    Lon_Res = (LonMax - LonMin) / (float(N_Lon) - 1)
    Lat_Res = (LatMax - LatMin) / (float(N_Lat) - 1)
    driver = gdal.GetDriverByName('GTiff')
    tif_name,dataset_id = toSurface(key)

    out_tif_name = path.split('.nc')[0] + '_' + tif_name + '.tif'
    out_tif = driver.Create(out_tif_name, N_Lon, N_Lat, 1, gdal.GDT_Float32)
    geotransform = (LonMin, Lon_Res, 0, LatMax, 0, -Lat_Res)
    out_tif.SetGeoTransform(geotransform)
    srs = osr.SpatialReference()
    srs.ImportFromEPSG(4326)  # 定义输出的坐标系为"WGS 84"，AUTHORITY["EPSG","4326"]
    out_tif.SetProjection(srs.ExportToWkt())  # 给新建图层赋予投影信息
    out_tif.GetRasterBand(1).WriteArray(value[::-1])  # 将数据写入内存，此时没有写入硬盘
    out_tif.FlushCache()  # 将数据写入硬盘
    out_tif = None  # 注意必须关闭tif文件

def toSurface(key):
    if key == 't':
        tif_name = 'TMP_surface'
        dataset_id = '62b2c4b76c0200005c001c43'
    elif key == 'sp':
        tif_name = 'PRES_surface'
        dataset_id = '62b2c5486c0200005c001c48'
    elif key == 'sde':
        tif_name = 'SNOD_surface'
        dataset_id = '62b2c53f6c0200005c001c47'
    elif key == 'cpofp':
        tif_name = 'CPOFP_surface'
        dataset_id = '62b2c5276c0200005c001c45'
    elif key == 'unknown':
        tif_name = 'ICETK_surface'
        dataset_id = '62b2c5196c0200005c001c44'
    elif key == 'siconc':
        tif_name = 'ICEC_surface'
        dataset_id = '62b1551fc926000078007e22'
    elif key == 'gust':
        tif_name = 'GUST_surface'
        dataset_id = '62b2c5556c0200005c001c49'
    elif key == 'v':
        tif_name = 'VGRD_maxwind'
        dataset_id = '62ce61b5c22a00003e002584'
    elif key == 'u':
        tif_name = 'UGRD_maxwind'
        dataset_id = '62ce61a8c22a00003e002583'
    elif key == 'lcc':
        tif_name = 'LCDC_lowcloudlayer'
        dataset_id = '62b2c5366c0200005c001c46'
    elif key == 'r2':
        tif_name = 'RH_2maboveground'
        dataset_id = '62b2c58c6c0200005c001c4a'
    return tif_name,dataset_id


def toKey(key):
    if key == 'TMP_surface':
        tif_name = 't'
    elif key == 'PRES_surface':
        tif_name = 'sp'
    elif key == 'SNOD_surface':
        tif_name = 'sde'
    elif key == 'CPOFP_surface':
        tif_name = 'cpofp'
    elif key == 'ICETK_surface':
        tif_name = 'unknown'
    elif key == 'ICEC_surface':
        tif_name = 'siconc'
    elif key == 'GUST_surface':
        tif_name = 'gust'
    elif key == 'VGRD_maxwind':
        tif_name = 'v'
    elif key == 'UGRD_maxwind':
        tif_name = 'u'
    elif key == 'RH_2maboveground':
        tif_name = 'r2'
    elif key == 'LCDC_lowcloudlayer':
        tif_name = 'lcc'
    return tif_name


if __name__ == '__main__':

    def scheduler_init(app):
        scheduler = APScheduler()
        scheduler.init_app(app)
        scheduler.start()

    app.config.from_object(Config)
    scheduler_init(app)
    # task(1, 2)
    print(datetime.datetime.now())
    # sched = BackgroundScheduler()
    # trggier1 = CronTrigger(day_of_week='*', hour=1, minute=55)
    # sched.add_job(task(1, 2), id='label1', trigger=trggier1, misfire_grace_time=500)
    # sched.start()
    app.run(port=8200, debug=False)