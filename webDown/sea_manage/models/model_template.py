from sea_manage import db

class Json(db.Document):
    _id = db.ObjectIdField(required=True, primary_key=True)
    json = db.StringField()
    name = db.StringField()
    remark = db.StringField()

    meta = {'collection': 'template', 'strict': False, 'db_alias': 'Netcdf'}