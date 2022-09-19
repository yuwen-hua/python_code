# config:utf-8

import redis


class Config(object):
    """配置信息"""
    SECRET_KEY = "********"
    JSON_AS_ASCII = False
    # DOWNLOADS = "http://192.168.199.207:4000/download/nc/Density/2022/01/Density_20220101.nc"

    # SQLALCHEMY_DATABASE_URL = "mysql://root:admin@192.168.199.5:3306/test"
    # SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis
    # REDIS_HOST = "127.0.0.1"
    # REDIS_PORT = 6379

    # flask-session配置
    # SESSION_TYPE = "redis"
    # SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # SESSION_USE_SIGNER = True  # 对cookie中的session_id进行隐藏
    # PERMANENT_SESSION_LIFETIME = 86400  # session数据有效期单位秒（1天的）

    # cache_default_timeout = 50  # 默认删除缓存时间为50s




class ProductConfig(Config):
    """生产模式配置信息"""
    DEBUG = False
    CHROMEDRIVER = "F:/chromedriver_win32/chromedriver"
    # CACHE_TYPE = 'redis'  # 缓存到redis数据库
    # # CACHE_TYPE = 'simple'  #缓存到内存
    # CACHE_KEY_PREFIX = 'blog/'
    # CACHE_REDIS_HOST = '114.242.60.27'
    # CACHE_REDIS_PORT = '6704'
    # CACHE_REDIS_DB = '0'
    # CACHE_DEFAULT_TIMEOUT = 60 * 60 * 24  # 有效时间
    # DATASETADDRESS = "114.242.60.27:8900"
    DOWNLOADS = "http://114.242.60.27:8890/download/"
    # TERRAINFILEPATH = "D:\\dataSource\\tif\\geotiff.tif"
    # 数据库
    MONGODB_SETTINGS = [

    ]


config_map = {
    "product": ProductConfig
}
