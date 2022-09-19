# coding:utf-8
import logging

from flask import Flask
from flask_cache import Cache
from flask_cors import CORS
from config import config_map
from flask_mongoengine import MongoEngine
from flask_session import Session
from flask_wtf import CSRFProtect
# from osgeo import gdal
import flask.scaffold
from flask_compress import Compress

from sea_manage.untils.response_code import RET

flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restplus import Api

# gdal = gdal
rest_api = Api()
db = MongoEngine()
compress = Compress()
# 创建redis连接对象
redis_store = None
SECRET_KEY = None
# 缓存
cache = Cache()



# 工厂模式
def create_app(config_name, physics=None):
    """
    创建flask的应用对象
    :param config_name: str 配置模式名称 ("develop","product")
    :return:
    """

    app = Flask(__name__)

    config_class = config_map[config_name]
    compress.init_app(app)
    app.config.from_object(config_class)
    global SECRET_KEY
    SECRET_KEY = config_class.SECRET_KEY
    db.init_app(app)
    cache.init_app(app)
    # 装载配置
    app.debug = config_class.DEBUG

    CORS(app, supports_credentials=True)  # 设置跨域

    rest_api.init_app(app, version='1.0', title='Python API',
                      description='星天海洋数据下载服务平台')

    # global redis_store
    # redis_store = redis.StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)

    # 利用falsk-session,将session 数据保存到redis中
    Session(app)
    # 为flask补充csrt防护
    # CSRFProtect(app)

    # 注册蓝图
    from . import  passport, products
    logging.debug('测试debugger日志')
    # app.register_blueprint(passport.api_passport, url_prefix="/api/v1.0")
    app.register_blueprint(products.api_sentinel, url_prefix="/api/v1.0")
    app.register_blueprint(products.api_satellite, url_prefix="/api/v1.0")
    app.register_blueprint(products.api_copernicus, url_prefix="/api/v1.0")
    app.register_blueprint(products.api_modis, url_prefix="/api/v1.0")
    app.register_blueprint(products.api_remote, url_prefix="/api/v1.0")
    app.register_blueprint(products.api_hydrology, url_prefix="/api/v1.0")
    app.register_blueprint(products.api_weather, url_prefix="/api/v1.0")
    app.register_blueprint(products.api_tide, url_prefix="/api/v1.0")
    app.register_blueprint(products.api_trend, url_prefix="/api/v1.0")
    return app
