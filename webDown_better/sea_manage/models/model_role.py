from sea_manage import db


class Role(db.Document):
    _id = db.ObjectIdField(required=True, primary_key=True)
    role_id = db.StringField()
    role_name = db.StringField(required=True, max_length=32, unique=True)
    role_key = db.StringField(required=True, max_length=150)
    menuids = db.ListField()
    remark = db.StringField()
    meta = {'collection': 'sys_role', 'strict': False, 'strict': False, 'db_alias': 'seamanage'}

    def to_dict(self):
        role_dict = {
            "id": self.role_id,
            "roleName": self.role_name,
            "roleKey": self.role_key,
            "remark": self.remark,
            "menuIds": get_list(self.menuids)
        }
        return role_dict


def get_list(datas):
    data = []
    for i in datas:
        data.append(str(i))
    return data
