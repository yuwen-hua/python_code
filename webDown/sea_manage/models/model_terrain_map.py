from sea_manage import db


class TerrainMap(db.Document):
    _id = db.ObjectIdField(required=True, primary_key=True)
    label = db.StringField()
    children = db.ListField()
    remark = db.StringField(max_length=500)

    meta = {'collection': 'terrainmap', 'strict': False, 'db_alias': 'tree', }
