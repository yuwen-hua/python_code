from sea_manage import db


class Image(db.DynamicDocument):
    _id = db.ObjectIdField(required=True, primary_key=True)
    TILEKEY = db.StringField()
    GDALFORMAT = db.StringField()
    IMAGE = db.StringField()

    # meta = {'collection': 'L0', 'strict': False, 'db_alias': 'dem_gebco2021', }
    # meta = {'strict': False, 'db_alias': 'dem_gebco2021', }
