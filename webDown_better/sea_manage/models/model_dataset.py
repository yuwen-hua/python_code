from sea_manage import db

class Dataset(db.Document):
    _id = db.ObjectIdField(required=True, primary_key=True)
    dataset_name = db.StringField()
    data_type = db.StringField()
    english_name = db.StringField()
    data_time = db.StringField()
    dataset_own = db.StringField()
    thematic_class = db.StringField()
    reference = db.StringField()
    share_type = db.StringField()
    time_liness = db.StringField()
    share_level = db.StringField()
    ocean_area = db.ListField()
    subject_class = db.StringField()
    keywords = db.ListField()
    Dataset_summary = db.StringField()
    img = db.StringField()
    type = db.IntField()
    meta = {'collection': 'dataset', 'strict': False, 'db_alias': 'dataset_manage'}




class Thematic(db.Document):
    _id = db.ObjectIdField(required=True, primary_key=True)
    thematic_class = db.StringField()
    thematic_introduce = db.StringField()
    thematic_vistis = db.IntField()
    create_time = db.DateTimeField()
    describe = db.StringField()
    thematic_name = db.StringField()
    img = db.StringField()
    meta = {'collection': 'thematic', 'strict': False, 'db_alias': 'dataset_manage'}
