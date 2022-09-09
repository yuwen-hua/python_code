from sea_manage import db


class LoginLog(db.Document):
    _id = db.ObjectIdField(required=True, primary_key=True)
    user_name = db.StringField()
    status = db.StringField()
    ip_addr = db.StringField()
    login_location = db.StringField()
    browser = db.StringField()
    os = db.StringField()
    msg = db.StringField()
    login_time = db.DateTimeField()

    meta = {'collection': 'sys_login_log', 'strict': False, 'strict': False , 'db_alias': 'seamanage'}

    def to_dict(self):
        role_dict = {
            "userName": self.user_name,
            "status": self.status,
            "ipAddr": self.ip_addr,
            "loginLocation": self.login_location,
            "browser": self.browser,
            "os": self.os,
            "msg": self.msg,
            "loginTime": self.login_time
        }
        return role_dict
