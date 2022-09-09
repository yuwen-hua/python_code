import os
import requests
import time
path = 'D:/dataSource/gfs/json/2022/07/18'
# date =
# path = 'D:/dataSource/gfs/json/' + date
for root, dirs, files in os.walk(path):
    for file in files:
        print(root + '/' + file)
        url = 'http://114.242.60.27:6770/api/v1.0/collection_netcdf/json'
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
        # 文件注意换成自己的对应的文件
        filess = {'file': open(root + '/' + file, 'rb')}
        res = requests.post(url=url, headers=header, files=filess)
        print(res)
        time.sleep(3)
