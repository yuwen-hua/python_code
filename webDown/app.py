# coding:utf-8
import datetime

from flask import Flask
from sea_manage import create_app
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler

from sea_manage.passport.views_gfs import DownLoad
# from sea_manage.passport.views_copernicus import Copernicus
from sea_manage.passport.chromedriver import Chrome
# gunicorn 部署
app = create_app('product')  # 生产环境
# app = create_app('dev') # 开发环境

# app = Flask(__name__)
#
#
index = 0
def down(www):
    Chrome()
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == '__main__':

    sched = BackgroundScheduler()
    sched.add_job(down, 'cron',args=[index+1], id='3_second_job', day_of_week='*', hour=2,minute=22)
    # sched.add_job(down, 'interval',args=[index], id='3_second_job', seconds=5)
    sched.start()

    # app.run(host='0.0.0.0', debug=True, port=9000,use_reloader=True)
    # user_reloader 需要在服务器上运行时关闭， 否则会开启两个进程
    app.run(host='0.0.0.0', debug=False, port=9000,use_reloader=False)

