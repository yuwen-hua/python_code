from sea_manage import db
from sea_manage.models.model_nc_meta import NcMeta


class NcSource(db.Document):  # NetCDF 数据集合模型
    dimensions = db.ListField()  # NetCDF 数据集的维度信息
    parameters = db.ListField()  # 数据集中所包含的参数信息
    units = db.DictField()  # 不同参数的物理单位
    date_time = db.DateTimeField()  # 数据的时间维度
    depth = db.FloatField()  # 数据的水深维度
    lat = db.ListField()  # 数据的纬度维度
    lon = db.ListField()  # 数据的经度维度
    values = db.ListField()  # 数据表述的具体参数值
    data_type = db.StringField()  # 数据中包含的变量名
    data_source = db.StringField()  # 数据来源
    # meta_data = db.ReferenceField(
    #     NcMeta,  # 指向该数据所在数据集元数据
    #     reverse_delete_rule='DENY'
    # )  # 删除时防止删除指向的元数据
    meta = {  # 按所列属性建立索引
        'db_alias': 'netcdf',
        'collection': 'nc_source',
        'indexes': ['date_time', 'depth', 'parameters', 'lat', 'lon', 'data_type']
    }
