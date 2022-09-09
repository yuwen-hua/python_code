# # coding:utf-8
#
# from flask import Blueprint, session, jsonify, request
# from sea_manage import rest_api
#
# # 创建蓝图对象
#
# api_passport = Blueprint("passport", __name__)
#
# rest_api.init_app(api_passport, version='v1.0', title='Python API',
#                   description='星天海洋环境数据服务平台')  # 添加restplus
#
#
# @api_passport.before_request
# def before():
#     if 'swagger' in request.path or request.path == '/' or '/login' in request.path:
#         pass
#     # else:
#     #     if session.get('name') is None:
#     #         return '需要登陆'
#     #     else:
#     #         pass
#
#
# # 导入蓝图视图
# from . import views_gfs
