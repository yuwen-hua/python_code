from sea_manage import db


class Dict(db.Document):
    _id = db.ObjectIdField(required=True, primary_key=True)
    type = db.StringField(required=True, max_length=32, unique=True)
    update_time = db.DateTimeField()
    create_time = db.DateTimeField()
    remarks = db.StringField()
    dict = db.ListField()
    dict_name = db.StringField()
    meta = {'collection': 'sys_dict', 'strict': False, 'db_alias': 'seamanage'}
