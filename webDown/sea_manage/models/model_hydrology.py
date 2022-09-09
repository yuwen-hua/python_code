from sea_manage import db


class Meta(db.Document):  # 元数据集合模型
    _id = db.ObjectIdField(required=True, primary_key=True)

    dimension = db.StringField()  # 解析文件的维度
    # 通用参数部分
    dataset_id = db.StringField()
    dataset_name = db.StringField()  # 数据集名称
    ocean_area = db.ListField()  # 观测、观测海域
    project_info = db.StringField()  # 项目相关信息
    keywords = db.ListField()  # 数据集关键词
    subjects = db.ListField()  # 数据集所属科目类别
    platform = db.ListField()  # 观测、调查搭载平台
    instrument = db.ListField()  # 观测、调查设备名称
    parameters = db.ListField()  # 数据集中包含的观测、调查参数
    start_date = db.DateTimeField()  # 数据集起始日期时间
    end_date = db.DateTimeField()  # 数据集结束日期时间
    raw_data_url = db.StringField()  # 原始数据集下载地址
    data_volume = db.StringField()  # 原始数据集体积
    data_format = db.StringField()  # 原始数据集格式
    data_verification = db.ListField()  # 数据集校验人员姓名
    contact_name = db.StringField()  # 数据集联系人
    contact_number = db.StringField()  # 数据集联系人电话
    contact_email = db.EmailField()  # 数据集联系人邮箱
    institution = db.StringField()  # 数据集发布机构
    description = db.StringField()  # 数据集描述
    # 观测站数据部分
    station_name = db.StringField()  # 观测站点名称
    station_description = db.StringField()  # 观测站点的描述#模型数据部分
    model_dimensions = db.ListField()  # 模型数据维度
    model_variables = db.ListField()  # 模型数据变量
    model_dt = db.ListField()  # 模型数据时间
    model_depth = db.ListField()  # 模型水深数据
    # nc元特有数据信息
    e_name = db.StringField()  # 英文名
    subject = db.StringField()  # 学科分类
    # theme =  db.StringField()  # 主题分类
    shared = db.StringField()  # 共享方式
    update_frequency = db.StringField()  # 更新频率
    timeliness = db.StringField()  # 时效性
    sharing_level = db.StringField()  # 共享级别
    data_type = db.StringField()  # 数据要素类型
    data_file_path = db.StringField()  # 数据物理文件夹地址
    database_year = db.StringField()  # 数据所属年份

    meta = {'collection': 'meta_data', 'strict': False, 'db_alias': 'background', }


class Hydrology2022(db.Document):  # 通过 meta_data 查询 Hydrology表
    _id = db.ObjectIdField(required=True, primary_key=True)
    dimensions = db.ListField()  # 尺寸
    parameters = db.ListField()  # 范围
    units = db.DictField()  # 单位
    unit = db.StringField()
    depth = db.FloatField()  # 深度
    lat_start = db.FloatField()  # 纬度开始值
    lon_start = db.FloatField()  # 经度开始值
    lon_length = db.IntField()  # 经度长度
    lat_length = db.IntField()  # 纬度长度
    lon_size = db.FloatField()  # 经度跨度
    lat_size = db.FloatField()  # 纬度跨度
    values = db.ListField()  # 观测、调查设备名称
    data_source = db.StringField()  # 数据来源
    meta_data = db.ReferenceField(
        Meta,  # 指向该数据所在数据集元数据
    )  # meta_data的标识
    img = db.StringField()
    img2 = db.StringField()
    date_time = db.DateTimeField()  # 数据日期时间
    meta = {'collection': 'Density_2022', 'strict': False, 'db_alias': 'background', }

    def to_dict(self):
        hy_dict = {
            "lat_start": self.lat_start,
            "lon_start": self.lon_start,
            "lon_length": self.lon_length,
            "lat_length": self.lat_length,
            "lon_size": self.lon_size,
            "lat_size": self.lat_size,
            "img": self.img,
            "img2": self.img2,
            "values": self.values
        }
        return hy_dict


class Hydrology2021(db.Document):  # 通过 meta_data 查询 Hydrology表
    _id = db.ObjectIdField(required=True, primary_key=True)
    dimensions = db.ListField()  # 尺寸
    parameters = db.ListField()  # 范围
    units = db.DictField()  # 单位
    unit = db.StringField()
    depth = db.FloatField()  # 深度
    lat = db.ListField()  # 纬度
    lon = db.ListField()  # 经度
    values = db.ListField()  # 观测、调查设备名称
    data_source = db.StringField()  # 数据来源
    meta_data = db.ObjectIdField()  # meta_data的标识
    date_time = db.DateTimeField()  # 数据日期时间
    img = db.StringField()
    img2 = db.StringField()
    date_time = db.DateTimeField()  # 数据日期时间
    meta = {'collection': 'Density_2021', 'strict': False, 'db_alias': 'background', }

    def to_dict(self):
        hy_dict = {
            "lat_start": self.lat_start,
            "lon_start": self.lon_start,
            "lon_length": self.lon_length,
            "lat_length": self.lat_length,
            "lon_size": self.lon_size,
            "lat_size": self.lat_size,
            "img": self.img,
            "img2": self.img2,
            "values": self.values
        }
        return hy_dict


class Sound2022(db.Document):  # 通过 meta_data 查询 Sound表
    _id = db.ObjectIdField(required=True, primary_key=True)
    dimensions = db.ListField()  # 尺寸
    parameters = db.ListField()  # 范围
    units = db.DictField()  # 单位
    unit = db.StringField()
    depth = db.FloatField()  # 深度
    lat_start = db.FloatField()  # 纬度开始值
    lon_start = db.FloatField()  # 经度开始值
    lon_length = db.IntField()  # 经度长度
    lat_length = db.IntField()  # 纬度长度
    lon_size = db.FloatField()  # 经度跨度
    lat_size = db.FloatField()  # 纬度跨度
    values = db.ListField()  # 观测、调查设备名称
    data_source = db.StringField()  # 数据来源
    meta_data = db.ReferenceField(
        Meta,  # 指向该数据所在数据集元数据
    )  # meta_data的标识
    img = db.StringField()
    img2 = db.StringField()
    date_time = db.DateTimeField()  # 数据日期时间
    meta = {'collection': 'Sound_2022', 'strict': False, 'db_alias': 'background', }

    def to_dict(self):
        hy_dict = {
            "lat_start": self.lat_start,
            "lon_start": self.lon_start,
            "lon_length": self.lon_length,
            "lat_length": self.lat_length,
            "lon_size": self.lon_size,
            "lat_size": self.lat_size,
            "img": self.img,
            "img2": self.img2,
            "values": self.values
        }
        return hy_dict


class Sound2021(db.Document):  # 通过 meta_data 查询 Sound表
    _id = db.ObjectIdField(required=True, primary_key=True)
    dimensions = db.ListField()  # 尺寸
    parameters = db.ListField()  # 范围
    units = db.DictField()  # 单位
    unit = db.StringField()
    depth = db.FloatField()  # 深度
    lat_start = db.FloatField()  # 纬度开始值
    lon_start = db.FloatField()  # 经度开始值
    lon_length = db.IntField()  # 经度长度
    lat_length = db.IntField()  # 纬度长度
    lon_size = db.FloatField()  # 经度跨度
    lat_size = db.FloatField()  # 纬度跨度
    values = db.ListField()  # 观测、调查设备名称
    data_source = db.StringField()  # 数据来源
    meta_data = db.ReferenceField(
        Meta,  # 指向该数据所在数据集元数据
    )  # meta_data的标识
    img = db.StringField()
    img2 = db.StringField()
    date_time = db.DateTimeField()  # 数据日期时间
    meta = {'collection': 'Sound_2021', 'strict': False, 'db_alias': 'background', }

    def to_dict(self):
        hy_dict = {
            "lat_start": self.lat_start,
            "lon_start": self.lon_start,
            "lon_length": self.lon_length,
            "lat_length": self.lat_length,
            "lon_size": self.lon_size,
            "lat_size": self.lat_size,
            "img": self.img,
            "img2": self.img2,
            "values": self.values
        }
        return hy_dict


class Temp2021(db.Document):  # 通过 meta_data 查询 Sound表
    _id = db.ObjectIdField(required=True, primary_key=True)
    dimensions = db.ListField()  # 尺寸
    parameters = db.ListField()  # 范围
    units = db.DictField()  # 单位
    unit = db.StringField()
    depth = db.FloatField()  # 深度
    lat_start = db.FloatField()  # 纬度开始值
    lon_start = db.FloatField()  # 经度开始值
    lon_length = db.IntField()  # 经度长度
    lat_length = db.IntField()  # 纬度长度
    lon_size = db.FloatField()  # 经度跨度
    lat_size = db.FloatField()  # 纬度跨度
    values = db.ListField()  # 观测、调查设备名称
    data_source = db.StringField()  # 数据来源
    meta_data = db.ReferenceField(
        Meta,  # 指向该数据所在数据集元数据
    )  # meta_data的标识
    img = db.StringField()
    img2 = db.StringField()
    date_time = db.DateTimeField()  # 数据日期时间
    meta = {'collection': 'Temp_2021', 'strict': False, 'db_alias': 'background', }

    def to_dict(self):
        hy_dict = {
            "lat_start": self.lat_start,
            "lon_start": self.lon_start,
            "lon_length": self.lon_length,
            "lat_length": self.lat_length,
            "lon_size": self.lon_size,
            "lat_size": self.lat_size,
            "img": self.img,
            "img2": self.img2,
            "values": self.values
        }
        return hy_dict


class Temp2022(db.Document):  # 通过 meta_data 查询 Sound表
    _id = db.ObjectIdField(required=True, primary_key=True)
    dimensions = db.ListField()  # 尺寸
    parameters = db.ListField()  # 范围
    units = db.DictField()  # 单位
    unit = db.StringField()
    depth = db.FloatField()  # 深度
    lat_start = db.FloatField()  # 纬度开始值
    lon_start = db.FloatField()  # 经度开始值
    lon_length = db.IntField()  # 经度长度
    lat_length = db.IntField()  # 纬度长度
    lon_size = db.FloatField()  # 经度跨度
    lat_size = db.FloatField()  # 纬度跨度
    values = db.ListField()  # 观测、调查设备名称
    data_source = db.StringField()  # 数据来源
    meta_data = db.ReferenceField(
        Meta,  # 指向该数据所在数据集元数据
    )  # meta_data的标识
    img = db.StringField()
    img2 = db.StringField()
    date_time = db.DateTimeField()  # 数据日期时间
    meta = {'collection': 'Temp_2022', 'strict': False, 'db_alias': 'background', }

    def to_dict(self):
        hy_dict = {
            "lat_start": self.lat_start,
            "lon_start": self.lon_start,
            "lon_length": self.lon_length,
            "lat_length": self.lat_length,
            "lon_size": self.lon_size,
            "lat_size": self.lat_size,
            "img": self.img,
            "img2": self.img2,
            "values": self.values
        }
        return hy_dict

class Salinity2021(db.Document):  # 通过 meta_data 查询 Sound表
    _id = db.ObjectIdField(required=True, primary_key=True)
    dimensions = db.ListField()  # 尺寸
    parameters = db.ListField()  # 范围
    units = db.DictField()  # 单位
    unit = db.StringField()
    depth = db.FloatField()  # 深度
    lat_start = db.FloatField()  # 纬度开始值
    lon_start = db.FloatField()  # 经度开始值
    lon_length = db.IntField()  # 经度长度
    lat_length = db.IntField()  # 纬度长度
    lon_size = db.FloatField()  # 经度跨度
    lat_size = db.FloatField()  # 纬度跨度
    values = db.ListField()  # 观测、调查设备名称
    data_source = db.StringField()  # 数据来源
    meta_data = db.ReferenceField(
        Meta,  # 指向该数据所在数据集元数据
    )  # meta_data的标识
    img = db.StringField()
    img2 = db.StringField()
    date_time = db.DateTimeField()  # 数据日期时间
    meta = {'collection': 'Salinity_2021', 'strict': False, 'db_alias': 'background', }

    def to_dict(self):
        hy_dict = {
            "lat_start": self.lat_start,
            "lon_start": self.lon_start,
            "lon_length": self.lon_length,
            "lat_length": self.lat_length,
            "lon_size": self.lon_size,
            "lat_size": self.lat_size,
            "img": self.img,
            "img2": self.img2,
            "values": self.values
        }
        return hy_dict


class Salinity2022(db.Document):  # 通过 meta_data 查询 Sound表
    _id = db.ObjectIdField(required=True, primary_key=True)
    dimensions = db.ListField()  # 尺寸
    parameters = db.ListField()  # 范围
    units = db.DictField()  # 单位
    depth = db.FloatField()  # 深度
    unit = db.StringField()
    lat_start = db.FloatField()  # 纬度开始值
    lon_start = db.FloatField()  # 经度开始值
    lon_length = db.IntField()  # 经度长度
    lat_length = db.IntField()  # 纬度长度
    lon_size = db.FloatField()  # 经度跨度
    lat_size = db.FloatField()  # 纬度跨度
    values = db.ListField()  # 观测、调查设备名称
    data_source = db.StringField()  # 数据来源
    meta_data = db.ReferenceField(
        Meta,  # 指向该数据所在数据集元数据
    )  # meta_data的标识
    img = db.StringField()
    img2 = db.StringField()
    date_time = db.DateTimeField()  # 数据日期时间
    meta = {'collection': 'Salinity_2022', 'strict': False, 'db_alias': 'background', }

    def to_dict(self):
        hy_dict = {
            "lat_start": self.lat_start,
            "lon_start": self.lon_start,
            "lon_length": self.lon_length,
            "lat_length": self.lat_length,
            "lon_size": self.lon_size,
            "lat_size": self.lat_size,
            "img": self.img,
            "img2": self.img2,
            "values": self.values
        }
        return hy_dict

Hydrology = {
    "T": {
        "2021": Temp2021,
        "2022": Temp2022,
    },
    "Density": {
        "2022": Hydrology2022,
        "2021": Hydrology2021,
    },
    "Sound": {
        "2022": Sound2022,
        "2021": Sound2021,
    },
    "temp": {
        "2021": Temp2021,
        "2022": Temp2022,
    },
    "salinity": {
        "2021": Salinity2021,
        "2022": Salinity2022,
    },
    "Salinity": {
        "2021": Salinity2021,
        "2022": Salinity2022,
    }
}
