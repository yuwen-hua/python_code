import os

import geojson
import pandas as pd
from osgeo import ogr
from shapely import wkt

from model_enc import ENC
from mongoengine import connect
connect('measured', host='localhost', port=27017)

def shp_mongo(file):
    # types = read_excel(r'D:\s57.xlsx')
    for root, dirs, files in os.walk(file):
        for fileName in files:
            if fileName.endswith('.shp'):
                if fileName == 'DepthsA.shp':
                # print('"'+fileName.split('.')[0] + '" :' +  fileName.split('.')[0]+' ,')
                    read_shp(file + '\\' + fileName, fileName.split('.')[0], 0)
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

def read_shp(file, fileName, index):
    ds = ogr.Open(file, 0)
    layer0 = ds.GetLayerByIndex(0)
    num = layer0.GetFeatureCount(0)
    for l in range(index, num):
        f = ENC[fileName]()
        ofeature = layer0.GetFeature(l)
        geo = ofeature.GetGeometryRef()
        # name = ofeature.GetFieldAsString('indx')
        # print(fileName, ':',ofeature.keys())
        for key in ofeature.keys():
            if l == 0:
                f.__setitem__(key, ofeature.GetFieldAsString(key))
            else:
                f[key] = ofeature.GetFieldAsString(key)
            # f[key] = ofeature.GetFieldAsString(key)
        location = geojson.loads(geojson.dumps(wkt.loads(str(geo))))
        if l == 4015:
            print(location)
        if fileName == 'SoundingsP':
            f.location = {
                'type': 'Point',
                'coordinates': [location.coordinates[0], location.coordinates[1]]
            }
            # f.depth = location.coordinates[2]
        elif fileName[-1:] == 'A':
            # arr = []
            # for j in location.coordinates:
            #     arr.append(j)
            f.location = {
                'type': 'Polygon',
                'coordinates': location.coordinates
            }
        elif fileName[-1:] == 'L':
            # arr = []
            # for j in location.coordinates:
            #     arr.append(j)
            f.location = {
                'type': 'LineString',
                'coordinates': location.coordinates
            }
        # if types.__contains__(fileName):
        #     f.type = types[fileName][f['FCSubtype']]
        print(fileName,l,f.location['type'])
        try:
            f.save()
        except Exception as e:
            print('出错了')
            # read_shp(file, fileName, l+1)


if __name__ == '__main__':
    # path = r'D:\dataSource\电子海图\完整\s57'
    path = r'D:\shp'
    shp_mongo(path)