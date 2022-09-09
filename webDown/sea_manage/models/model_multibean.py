from sea_manage import db


# from flask_mongoengine import MongoEngine
# db = MongoEngine()

class Multibean2019(db.Document):
    _id = db.ObjectIdField(required=True, primary_key=True)
    dataset_id = db.StringField()
    dataset_name = db.StringField()  # 数据集名称
    keywords = db.ListField()  # 数据集关键字
    subject = db.ListField()  # 数据所属学科
    database_year = db.StringField()  # 数据集年份
    data = db.ListField()  # 多波束点数据
    lat_start = db.FloatField()  # 纬度开始
    lon_start = db.FloatField()  # 经度开始
    lat_length = db.IntField()  # 纬度网格长度
    lon_length = db.IntField()  # 经度网格长度
    lat_size = db.FloatField()  # 纬度间隙
    lon_size = db.FloatField()  # 经度间隙
    img = db.StringField()  # 图片 base64位
    meta = {'collection': 'multibean2019', 'strict': False, 'strict': False}


Multibean = {
    "2019": Multibean2019
}


class MetaData(db.Document):  # 元数据集合模型
    # 通用参数部分
    _id = db.ObjectIdField()
    dataset_id = db.StringField()  # 数据集id
    name = db.StringField()
    ename = db.StringField()
    range = db.ListField()
    level = db.ListField()
    coor_system = db.StringField()
    format = db.StringField()
    location = db.MultiLineStringField()
    tiff_file = db.ImageField()
    meta = {  # 按所列属性建立索引
        'indexes': ['dataset_id'],
        'collection': 'meta_data',
        'db_alias': 'startest'
    }


class Trajectory(db.Document):  #
    _id = db.ObjectIdField(required=True, primary_key=True)
    meta_id = db.StringField()
    location = db.DictField()
    meta = {  # 按所列属性建立索引
        'collection': 'trajectory',
        'strict': False,
        'db_alias': 'startest'
    }

class Profile_0(db.Document):
    meta_id = db.StringField()
    level = db.StringField()
    name = db.StringField()
    file = db.ImageField()
    left = db.FloatField()
    top = db.FloatField()
    lon_size = db.FloatField()
    lat_size = db.FloatField()
    location = db.PolygonField()
    meta = {  # 按所列属性建立索引
        'indexes': ['meta_id'],
        'collection': 'Profile_0',
    }


class Profile_1(db.Document):
    meta_id = db.StringField()
    level = db.StringField()
    name = db.StringField()
    file = db.ImageField()
    left = db.FloatField()
    top = db.FloatField()
    lon_size = db.FloatField()
    lat_size = db.FloatField()
    meta = {  # 按所列属性建立索引
        'indexes': ['meta_id'],
        'collection': 'Profile_1',
    }


class Profile_2(db.Document):
    meta_id = db.StringField()
    level = db.StringField()
    name = db.StringField()
    file = db.ImageField()
    left = db.FloatField()
    top = db.FloatField()
    lon_size = db.FloatField()
    lat_size = db.FloatField()
    meta = {  # 按所列属性建立索引
        'indexes': ['meta_id'],
        'collection': 'Profile_2',
    }


class Profile_3(db.Document):
    meta_id = db.StringField()
    level = db.StringField()
    name = db.StringField()
    file = db.ImageField()
    left = db.FloatField()
    top = db.FloatField()
    lon_size = db.FloatField()
    lat_size = db.FloatField()
    meta = {  # 按所列属性建立索引
        'indexes': ['meta_id'],
        'collection': 'Profile_3',
    }


class Profile_4(db.Document):
    meta_id = db.StringField()
    level = db.StringField()
    name = db.StringField()
    file = db.ImageField()
    left = db.FloatField()
    top = db.FloatField()
    lon_size = db.FloatField()
    lat_size = db.FloatField()
    meta = {  # 按所列属性建立索引
        'indexes': ['meta_id'],
        'collection': 'Profile_4',
    }


profile = {
    "0": Profile_0,
    "1": Profile_1,
    "2": Profile_2,
    "3": Profile_3,
    "4": Profile_4,
}
