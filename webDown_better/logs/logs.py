import os
import logging
from logging.handlers import RotatingFileHandler


"""
日志使用方式
logging.debug("测试debug日志")
logging.info("测试info日志")
logging.warning("测试warning日志")
logging.error("测试error日志")
"""

# 获取当前绝对路径
def get_cwd():
    return os.path.dirname(os.path.abspath(__file__))


def log_config():
    # 设置日志的的登记
    logging.basicConfig(level=logging.DEBUG)

    # 日志输出目录
    log_path = os.path.join(get_cwd(), 'flask.log')
    # 创建日志记录器，设置日志的保存路径和每个日志的大小和日志的总大小
    file_log_handler = RotatingFileHandler(log_path, encoding='UTF-8', maxBytes=1024 * 1024 * 100, backupCount=100)
    # 创建日志记录格式，日志等级，输出日志的文件名 行数 日志信息
    # formatter = logging.Formatter("%(levelname)s %(asctime)s [%(filename)s]: %(lineno)s - %(funcName)s - %(message)s")
    formatter = logging.Formatter("%(levelname)s %(asctime)s [%(filename)s]: %(lineno)s - %(funcName)s - %(message)s")
    # 为日志记录器设置记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flaks app使用的）加载日志记录器
    logging.getLogger().addHandler(file_log_handler)
