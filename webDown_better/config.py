# config:utf-8

class Config(object):
    """配置信息"""
    SECRET_KEY = "********"
    JSON_AS_ASCII = False
    JOBS = [
        {
            'id': 'job1',
            'func': 'scheduler:task',
            'args': (1, 2),
            'trigger': 'cron',
            'day': '*',
            'hour': '13',
            'minute': '16',
            'second': '20'
        }
    ]
    SCHEDULER_API_ENABLED = True

class ProductConfig(Config):
    """生产模式配置信息"""
    DEBUG = False
    CHROMEDRIVER = "D:/chromedriver_win32/chromedriver"



config_map = {
    "product": ProductConfig
}
