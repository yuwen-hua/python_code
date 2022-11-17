from sea_manage import db


class Menu(db.Document):
    _id = db.ObjectIdField(required=True, primary_key=True)
    menu_id = db.StringField()
    alwaysShow = db.BooleanField()
    name = db.StringField()
    component = db.StringField()
    path = db.StringField()
    order_num = db.FloatField()
    redirect = db.StringField()
    remark = db.StringField()
    metas = db.DictField()
    perms = db.StringField()
    icon = db.StringField()
    children = db.ListField()
    parentid = db.StringField()
    is_frame = db.BooleanField()
    is_cache = db.BooleanField()
    menu_type = db.StringField()
    meta = {'collection': 'sys_menu', 'strict': False, 'strict': False, 'db_alias': 'seamanage'}

    def to_dict(self):
        menu_dict = {
            "id": str(self._id),
            "component": self.component,
            "path": self.path,
            "perms": self.perms,
            "menuName": self.name,
            "orderNum": self.order_num,
            "metas": self.metas,
            "isFrame": self.is_frame,
            "parentId": self.parentid,
            "menuType": self.menu_type,
            "isCache": self.is_cache,
            "name": self.name
        }
        return menu_dict

    def to_dic(self):
        menu_dic = {
            "id": str(self._id),
            "label": self.name
        }
        return menu_dic


