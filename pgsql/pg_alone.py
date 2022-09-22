import psycopg2.extras
import xlwt
import openpyxl
from model import Ships, ShipInfo

conn = psycopg2.connect(database='hys0915ulog',user='postgres',password='123456',host='192.168.199.139', port=5432)
with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
        sql_command1 = "select * from " + result[i][1] + " order by receivedtime desc"
        cursor.execute(sql_command1)
        data = cursor.fetchone()
        # for o in data.keys():
        if data['length'] is not None and not data['length']:
            data['length'] = "0"
        if data['width'] is not None and not data['width']:
            data['width'] = "0"
        if data['draught'] is not None and not data['draught']:
            data['draught'] = "0"
        if data['mmsi'] is not None and not data['mmsi']:
            data['mmsi'] = "0"
        if data['imo'] is not None and not data['imo']:
            data['imo'] = "0"
        if data['rot'] is not None and not data['rot']:
            data['rot'] = "0"
        print('第{n}个'.format(n=i+1),result[i][1])
        shio = Ships(
            ShipName=data['shipname'],
            CallSign=data['callsign'],
            ShipTypeCN=data['shiptypecn'],
            ShipTypeEN=data['shiptypeen'],
            MMSI=int(float(data['mmsi'])),
            IMO=int(float(data['imo'])),
            NavStatusCN=data['navstatuscn'],
            NavStatusEN=data['navstatusen'],
            Length=float(data['length']),
            Width=float(data['width']),
            Draught=float(data['draught']),
            Heading=float(data['heading']),
            Course=float(data['course']),
            Speed=float(data['speed']),
            Lon=data['lon'],
            Lat=data['lat'],
            Rot=float(data['rot']),
            Dest=data['dest'],
            ETA=data['eta'],
            Receivedtime=data['receivedtime'],
            UnixTime=int(float(data['unixtime'])),
            Lon_d=float(data['lon_d']),
            Lat_d=float(data['lat_d']),
            AisType=data['aistype'],
        )
        shio.save()