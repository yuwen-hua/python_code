from werkzeug.security import check_password_hash

from sea_manage import db


class BaseModel(db.Document):
    create_time = db.DateTimeField()
    update_time = db.DateTimeField()

    meta = {'allow_inheritance': True, 'collection': 'sys_user', 'abstract': True, 'strict': False, 'db_alias': 'seamanage'}


class User(BaseModel):
    _id = db.ObjectIdField(required=True, primary_key=True)
    user_name = db.StringField(required=True, max_length=32, unique=True)
    password = db.StringField(required=True, max_length=150)
    real_name = db.StringField(max_length=150)
    avatar = db.BinaryField()
    sex = db.IntField()
    status = db.IntField()
    roleids = db.ListField()
    remark = db.StringField(max_length=500)

    meta = {'allow_inheritance': False}

    # meta = {'collection': 'User'}

    def __repr__(self):
        return 'User(user_name="{}")'.format(self.username, self.userid)

    def to_dict(self):
        """将对象转换为字典数据"""
        # sex = '男'
        # if self.sex == 1:
        #     sex = '女'
        # status = '正常'
        # if status == 0:
        #     status = '暂停'
        user_dict = {
            "id": str(self._id),
            "userName": self.user_name,
            "trueName": self.real_name,
            "avatar": self.avatar,
            "sex": str(self.sex),
            "status": str(self.status),
            "createTime": self.create_time,
            "roleIds": self.roleids,
            "updateTime": self.update_time,
            "remark": self.remark,
        }
        return user_dict

    def check_password(self, password):
        """
        检验密码正确性
        """

        return check_password_hash(self.password, password)
