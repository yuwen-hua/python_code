# -*- coding: utf-8 -*-
import os

import geojson
import pandas as pd
from osgeo import ogr
from shapely import wkt

from 电子海图.model_enc import ENC

os.environ[
    'PROJ_LIB'] = r'D:\software\Miniconda3\envs\py39\Lib\site-packages\pyproj\proj_dir\share\proj'


def shp_mongo(file):
    types = read_excel(r'D:\dataSource\电子海图\完整\s57.xlsx')
    for root, dirs, files in os.walk(file):
        for fileName in files:
            if fileName.endswith('.shp'):
                # print('"'+fileName.split('.')[0] + '" :' +  fileName.split('.')[0]+' ,')
                read_shp(file + '\\' + fileName, fileName.split('.')[0], types)
                print(fileName)


def read_excel(file):
    ex_data = pd.read_excel(file, index_col=None)
    types = {}
    head_list = list(ex_data.columns)  # 拿到表头: [A, B, C, D]
    for i in ex_data.values:
        if types.__contains__(i[0]):
            types[i[0]][str(int(i[2]))] = i[3]
        else:
            types[i[0]] = {}
            types[i[0]][str(int(i[2]))] = i[3]
    return types


def read_shp(file, fileName, types):
    ds = ogr.Open(file, 0)
    layer0 = ds.GetLayerByIndex(0)
    num = layer0.GetFeatureCount(0)
    for l in range(0, num):
        f = ENC[fileName]()
        ofeature = layer0.GetFeature(l)
        geo = ofeature.GetGeometryRef()
        # name = ofeature.GetFieldAsString('indx')
        for key in ofeature.keys():
            if l == 0:
                f.__setitem__(key, ofeature.GetFieldAsString(key))
            else:
                f[key] = ofeature.GetFieldAsString(key)
            # f[key] = ofeature.GetFieldAsString(key)
        location = geojson.loads(geojson.dumps(wkt.loads(str(geo))))
        if fileName == 'SoundingsP':
            f.location = {
                'type': 'Point',
                'coordinates': [location.coordinates[0], location.coordinates[1]]
            }
            f.depth = location.coordinates[2]
        else:
            f.location = location
        if types.__contains__(fileName):
            f.type = types[fileName][f['FCSubtype']]
        f.save()


if __name__ == '__main__':
    # path = r'D:\dataSource\电子海图\完整\s57'
    path = r'D:\dataSource\电子海图\大连\需要'
    shp_mongo(path)
