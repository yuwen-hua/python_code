# _&_ coding: utf-8 _*_
# @Time : 2022/5/11 09:24
# @File: model_platform
# @Project : startest_sea_python


from sea_manage import db


class Threedata(db.Document):
    _id = db.ObjectIdField(required=True, primary_key=True)
    amount = db.ListField() # 数据总量
    source = db.ListField() #数据来源
    category = db.ListField() #数据类别
    project_name = db.StringField() # 项目名称
    latitude = db.FloatField()  # 纬度
    longitude = db.FloatField()  # 经度
    date = db.DateTimeField()

    meta = {'collection': '3d_data', 'strict': False, 'db_alias': 'Netcdf', }

class Monographic(db.Document):
    _id = db.ObjectIdField(required=True, primary_key=True)
    project_name = db.StringField()  # 项目名称
    latitude = db.FloatField()  # 纬度
    longitude = db.FloatField()  # 经度
    flow = db.ListField()   # 专题流量
    topic = db.ListField()   # 专题

    meta = {'collection': 'monographic', 'strict': False, 'db_alias': 'Netcdf', }
