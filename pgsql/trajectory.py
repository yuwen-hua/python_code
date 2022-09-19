import psycopg2.extras
import xlwt
import openpyxl
from model import Ships, ShipInfo, ShipTrajectory

conn = psycopg2.connect(database='hys09141058',user='postgres',password='123456',host='192.168.199.139', port=5432)


try:
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
        sql = """select * from pg_tables where schemaname='public'"""
        cursor.execute(sql)
        # result = cursor.fetchall()
        result = cursor.fetchall()
        result = result[81871:]
        print('共{n}个'.format(n=len(result)))
        for i in range(len(result)):
            # obj = {
            #     "database": result[i][2],
            #     "tablename": result[i][1],
            #     "schemaname": result[i][0],
            # }
            # results.append(obj)
            sql_command1 = "select course,lon_d,lat_d from " + result[i][1] + " order by receivedtime desc"
            cursor.execute(sql_command1)
            data = cursor.fetchall()
            course = []
            location = []
            for j in data:
                course.append(float(j['course']))
                aaa = []
                aaa.append(float(j['lon_d']))
                aaa.append(float(j['lat_d']))
                location.append(aaa)
            print('第{n}个'.format(n=i + 1), result[i][1])
            shio = ShipTrajectory(
                mmsi = result[i][1][1:],
                course = course,
                location = location
            )
            shio.save()
            # for o in data.keys():
            # for j in range(len(data)):



finally:
    conn.close()