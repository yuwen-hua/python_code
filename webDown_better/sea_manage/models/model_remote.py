from sea_manage import db


class MetaData(db.Document):
    _id = db.ObjectIdField(required=True, primary_key=True)
    dataset_id = db.StringField()   # 数据集id
    sheet_no = db.StringField() # 图幅号
    denominator = db.IntField() #
    pub_time = db.StringField() # 发布时间
    levels = db.IntField()      #数量等级
    lon_start = db.FloatField()
    lat_start = db.FloatField()
    lon_end = db.FloatField()
    lat_end = db.FloatField()
    img = db.StringField()  # base64图片
    waters = db.ListField() # 海域范围

    meta = {'collection': 'meta_data', 'strict': False, 'db_alias': 'remote', }
