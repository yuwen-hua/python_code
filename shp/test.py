import time

import geojson
import base64
import json
import os
import ast
from datetime import datetime

from osgeo import gdal, osr, ogr
from shapely import wkt
from werkzeug.utils import secure_filename
from bson import ObjectId

from mongoengine.context_managers import switch_db, switch_collection

from model_enc import Enc_Vector_Data_Point, Enc_Vector_Data_LineString, Enc_Vector_Data_Polygon


filename = 'LIGHTS'
file = 'D:\\data\\dataSource\\test'
arr = []
for root, dirs, files in os.walk(file):
    for fileName in files:
        if fileName.endswith('.shp'):
            path = (file + '\\' + fileName)
# path = filepath + '.shp'
ds = ogr.Open(path, 0)
layer0 = ds.GetLayerByIndex(0)
num = layer0.GetFeatureCount(0)
print('此文件扫描出{}项'.format(num))
types = 'Point'
if types == 'Point':
            for l in range(0, num):
                ofeature = layer0.GetFeature(l)
                geo = ofeature.GetGeometryRef()
                location = geojson.loads(geojson.dumps(wkt.loads(str(geo))))
                c = {}
                try:
                    c['location'] = {
                        'type': 'Point',
                        'coordinates': [location.coordinates[0], location.coordinates[1]]
                    }
                except Exception as e:
                    c['location'] = {
                        'type': 'Point',
                        'coordinates': [location.coordinates[0][0], location.coordinates[0][1]]
                    }
                for key in ofeature.keys():
                    value = ofeature.GetFieldAsString(key)
                    c[key] = value
                # c._id = ObjectId()
                arr.append(c)
elif types == 'LineString':
    with switch_db(Enc_Vector_Data_LineString, 'Enc_Vector_Data') as t:
        with switch_collection(t, filename) as col:
            for l in range(0, num):
                ofeature = layer0.GetFeature(l)
                geo = ofeature.GetGeometryRef()
                location = geojson.loads(geojson.dumps(wkt.loads(str(geo))))
                c = col()
                c.location = {
                    'type': 'LineString',
                    'coordinates': location.coordinates
                }
                for key in ofeature.keys():
                    value = ofeature.GetFieldAsString(key)
                    c[key] = value
                c._id = ObjectId()
elif types == 'Polygon':
    with switch_db(Enc_Vector_Data_Polygon, 'Enc_Vector_Data') as t:
        with switch_collection(t, filename) as col:
            for l in range(0, num):
                ofeature = layer0.GetFeature(l)
                geo = ofeature.GetGeometryRef()
                location = geojson.loads(geojson.dumps(wkt.loads(str(geo))))
                c = col()
                c.location = {
                    'type': 'Polygon',
                    'coordinates': location.coordinates
                }
                for key in ofeature.keys():
                    value = ofeature.GetFieldAsString(key)
                    c[key] = value
                c._id = ObjectId()
print(arr)