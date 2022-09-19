import math
import os
import xlrd
import pandas as pd
from excel_model import Tree
from mongoengine import connect
connect('tree', host='114.242.60.27', port=6700,username='admin',password='123456')

path = 'D:/s57.xlsx'
data = pd.read_excel(io=path)
children = []
index = 0
types = []
for i in data.values:
    types.append(i[0])
ids = list(set(types))
print(type(ids))
for i in ids:
    obj = {
        "id": index,
        "label": i,
        "children": [],
        "chinese_name": ""
    }
    index = index + 1
    children.append(obj)
for i in data.values:
    for j in children:
        if i[0] == j['label']:
            # print(i[4],type(i[4]))
            if type(i[4]) == float:
                i[4] = ''
            if type(i[1]) == float:
                i[1] = ''
            if type(i[3]) == float:
                i[3] = ''
            if math.isnan(i[2]):
                print((i[2]))
                i[2] = 0
            obj = {
                "id": len(j['children']),
                "label": i[1],
                "values": i[2],
                "type": i[3],
                "chinese_name": i[4]
            }
            j['children'].append(obj)
collection = Tree(
    label='s57',
    children=children
)
collection.save()
