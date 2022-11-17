from sea_manage import db


class BaseMap(db.Document):
    _id = db.ObjectIdField(required=True, primary_key=True)
    label = db.StringField()
    children = db.ListField()
    remark = db.StringField(max_length=500)

    meta = {'collection': 'basemap', 'strict': False, 'db_alias': 'tree', }
