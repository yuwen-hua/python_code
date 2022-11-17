from flask import jsonify, request, current_app
from flask_httpauth import HTTPBasicAuth
from authlib.jose import jwt, JoseError
from sea_manage.models.model_user import User

from bson import json_util
# 在上面的基础上导入
import functools

auth = HTTPBasicAuth()


# 生成token, 有效时间为60min
def generate_auth_token(user_id):
    """生成用于邮箱验证的JWT（json web token）"""
    # 签名算法
    header = {'alg': 'HS256'}
    # 用于签名的密钥
    key = current_app.config['SECRET_KEY']
    # 待签名的数据负载
    data = {'user_id': user_id}
    return jwt.encode(header=header, payload=data, key=key)


def verify_token(token):
    '''
    校验token
    :param token:
    :return: 用户信息 or None
    '''

    key = current_app.config['SECRET_KEY']

    try:
        data = jwt.decode(token, key)
    except JoseError:
        return jsonify(code=4101, msg="登录已过期")
    user = is_admin(data["user_id"])
    return json_util.dumps(user)


def is_admin(user_id):
    pipeline = [
        # {
        #     "$addFields":
        #         {
        #             "_id": {"$toString": "$_id"}
        #             # "roleids": {"$toObjectId": "$roleids"}
        #         }
        # },
        {
            "$lookup":
                {
                    "from": "sys_role",  # 要一起合并的数据库
                    "localField": "roleids",  # Customer中的字段
                    "foreignField": "_id",  # linkman中的字段
                    "as": "roles"  # 将查询到的表合并成一个list
                }
        },
        {
            "$lookup":
                {
                    "from": "sys_menu",  # 要一起合并的数据库
                    "localField": "roles.menuids",  # Customer中的字段
                    "foreignField": "_id",  # linkman中的字段
                    "as": "menus"  # 将查询到的表合并成一个list
                }
        },
        # ,{
        #     "$match": {
        #         "menus.parentid": "0"
        #     }
        # }
    ]
    user = User.objects(_id=user_id).aggregate(*pipeline)
    for i in user:
        user = i
    permissions = []
    roles = []
    if user_id == '91451e408ff8489c959e014a7a4bcf05':
        permissions.append("*:*:*")
        user["admin"] = True
    else:
        user["admin"] = False
        for p in user.get('menus'):
            permissions.append(p.get('perms'))
    for r in user.get('roles'):
        roles.append(r.get('role_key'))
    user["permissions"] = permissions
    user["roless"] = roles
    sys_roles = []
    menus = []
    for r in i.get('roles'):
        for r_id in r.get('menuids'):
            sys_roles.append(r_id)
    for m in i.get('menus'):
        if not m.get('_id') in sys_roles:
            i.get('menus').remove(m)
    return user


def login_required(view_func):
    @functools.wraps(view_func)
    def verify_token(*args, **kwargs):
        try:
            # 在请求头上拿到token
            token = request.headers["Authorization"]
        except Exception:
            # 没接收的到token,给前端抛出错误
            # 这里的code推荐写一个文件统一管理。这里为了看着直观就先写死了。
            return jsonify(code=4103, msg='缺少参数token')
        key = current_app.config['SECRET_KEY']

        try:
            s = jwt.decode(token, key)
            print(s)
        except JoseError:
            return jsonify(code=4101, msg="登录已过期")

        # s = Serializer(SECRET_KEY)
        # try:
        #     s.loads(token)
        # except Exception:
        #     return jsonify(code=4101, msg="登录已过期")

        return view_func(*args, **kwargs)

    return verify_token
