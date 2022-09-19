# coding:utf-8

from flask import Blueprint
from sea_manage import rest_api

# 创建蓝图对象

api_sentinel = Blueprint("sentinel", __name__)
api_satellite = Blueprint("satellite", __name__)
api_copernicus = Blueprint("copernicus", __name__)
api_modis = Blueprint("modis", __name__)
api_hydrology = Blueprint("hydrology", __name__)
api_startest = Blueprint("startest", __name__)
api_remote = Blueprint("remote", __name__)
api_weather = Blueprint("weather", __name__)
api_tide = Blueprint("tide", __name__)
api_trend = Blueprint("trend", __name__)


rest_api.init_app(api_sentinel, version='v1.0', title='Python API',
                  description='星天海洋数据下载服务平台')  # 添加restplus

# # @api_passport.before_request
# # def before():
# #     if 'swagger' in request.path or request.path == '/' or '/login' in request.path:
# #         pass
# #     # else:
# #     #     if session.get('name') is None:
# #     #         return '需要登陆'
# #     #     else:
# #     #         pass
#
#
# # 导入蓝图视图
from . import views_sentinel
from . import views_copernicus
from . import views_modis
from . import views_satellite
from . import views_copernicus_down
from . import views_hydrology
from . import views_weather
from . import views_tide
from . import views_trend
