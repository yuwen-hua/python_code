import json
from io import StringIO, BytesIO

import bson
import pymongo
from pymongo import MongoClient
from gridfs import *
import os



# 地形数据入库（.terrain）
def getFlist(file_dir, dbname):
    try:
        username = config['USAERNAME']
        client = MongoClient(config['MOGOHOST'], config['MOGOPORT'],username=config['USAERNAME'],password=config['PASSWORD'])
    except Exception as e:
        client = MongoClient(config['MOGOHOST'], config['MOGOPORT'])
    # dbname = file_dir.split('xyz\\')[1]
    for root, dirs, files in os.walk(file_dir):
        if len(files) > 0:
            f = root.split(file_dir)[1].split('\\')
            z = f[1]
            # z = 10
            # if int(z) > 6:
            # continue
            x = f[2]
            # x = f[1]
            dbn = dbname
            # dbn = dbname + z
            db = client[dbn]
            col = db['L' + str(z)]
            col.create_index([("TILEKEY", pymongo.HASHED)])
            docs = []
            for fileName in files:
                imgdir = root + '\\' + fileName
                y = fileName.split('.')[0]
                fileName = str(z) + '_' + y + '_' + x + ".terrain"
                print(imgdir)
                # print(fileName)
                datatmp = open(imgdir, 'rb')
                imgput = datatmp.read()
                # content = BytesIO(imgput)
                # content = bson.binary.Binary(content.getvalue())
                # print(content)
                datatmp.closed
                doc = {'TILEKEY': fileName, 'IMAGE': imgput}
                # col.save(dict(
                #     TILEKEY=fileName,
                #     IMAGE=content
                # ))
                docs.append(doc)
            col.insert_many(docs)
            print(col)


# png瓦片入库
def png2mongodb(file_dir, dbname):
    client = MongoClient(config['MOGOHOST'], config['MOGOPORT'])
    for root, dirs, files in os.walk(file_dir):
        if len(files) > 0:
            f = root.split(file_dir)[1].split('\\')
            z = f[1]
            x = f[2]
            # z='10'
            # if int(z) > 6:
            # continue
            x = f[2]
            # x=f[1]
            dbn = dbname  # + "_" + z
            db = client[dbn]
            # col = db['file0_0']
            col = db['L' + z]
            col.create_index([("TILEKEY", pymongo.HASHED)])
            docs = []
            for fileName in files:
                imgdir = root + '\\' + fileName
                y = fileName.split('.')[0]
                y = str((1 << int(z)) - int(y) - 1)
                fileName = 'EPSG_3857_' + z + '_' + x + '_' + y
                print(imgdir)
                # print(fileName)
                datatmp = open(imgdir, 'rb')
                imgput = datatmp.read()
                # content = BytesIO(imgput)
                # content = bson.binary.Binary(content.getvalue())
                # print(content)
                datatmp.closed
                doc = {'TILEKEY': fileName, 'GDALFORMAT': 'PNG', 'IMAGE': imgput}
                # col.save(dict(
                #     TILEKEY=fileName,
                #     IMAGE=content
                # ))
                docs.append(doc)
            col.insert_many(docs)


if __name__ == '__main__':
    config = open('../config.json','r')
    config = config.read()
    config = json.loads(config)
    print(config)
    # 链接mongodb
    # 本地硬盘上的图片目录
    # dirs = r'E:\dem\GEOCO2021\icesurface\426'
    # dbname = "SEA_Dom"
    dbname = "water_test"
    # dirs = r'D:\dataSource\测试\瓦片_TMS'
    # dirs = r'D:\dataSource\海图瓦片\15'
    dirs = r'D:\dataSource\电子海图\tiles3'
    # 列出目录下的所有图片
    getFlist(config['dirs'], config['dbname'])
    # getFlist(dirs, dbname)
    # png2mongodb(dirs, dbname)

# # 取得对应的collection
# db = client.image
# # 本地硬盘上的图片目录
# dirs = r'e:\TEST'
# # 列出目录下的所有图片
# files = os.listdir(dirs)
# # 遍历图片目录集合
# for file in files:
#     # 图片的全路径
#     filesname = dirs + '\\' + file
#     # 分割，为了存储图片文件的格式和名称
#     f = file.split('.')
#     # 类似于创建文件
#     datatmp = open(filesname, 'rb')
#     # 创建写入流
#     imgput = GridFS(db)
#     # 将数据写入，文件类型和名称通过前面的分割得到
#     insertimg = imgput.put(datatmp, content_type=f[1], filename=f[0])
# datatmp.close()
# print("js")
