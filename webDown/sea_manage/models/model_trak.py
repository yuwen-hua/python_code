from sea_manage import db


class TrakLineMetaData(db.Document):
    _id = db.ObjectIdField(required=True, primary_key=True)
    survey_id = db.StringField()
    platform = db.StringField()
    survey_year = db.IntField()
    source = db.StringField()
    ngdc_id = db.StringField()
    chief_scientist = db.StringField()
    instrument = db.StringField()
    file_count = db.IntField()
    track_length = db.IntField()
    total_time = db.IntField()
    bathy_beams = db.IntField()
    amp_beams = db.IntField()
    sidescans = db.IntField()
    entered_date = db.StringField()
    start_time = db.IntField()
    end_time = db.IntField()
    download_url = db.StringField()
    location = db.MultiLineStringField()  # geo地理信息
    meta = {  # 按所列属性建立索引
        'indexes': ['survey_id', 'location'],
        'collection': 'trak_meta_data', 'strict': False, 'db_alias': 'trak',
    }


class Trakfiles(db.Document):
    _id = db.ObjectIdField(required=True, primary_key=True)
    survey_id = db.StringField()
    file_name = db.StringField()
    data_type = db.StringField()
    meta = {  # 按所列属性建立索引
        'indexes': ['survey_id'],
        'collection': 'trak_files', 'strict': False, 'db_alias': 'trak',
    }
