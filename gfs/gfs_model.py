from mongoengine import *

class GFS(Document):
    # 通用参数部分
    sort = FloatField()
    dataset_id = StringField()
    dataset_name = StringField()  # 数据集名称
    ocean_area = ListField()  # 观测、观测海域
    project_info = StringField()  # 项目相关信息
    keywords = ListField()  # 数据集关键词
    subjects = ListField()  # 数据集所属科目类别
    platform = ListField()  # 观测、调查搭载平台
    instrument = ListField()  # 观测、调查设备名称
    parameters = ListField()  # 数据集中包含的观测、调查参数
    start_date = DateTimeField()  # 数据集起始日期时间
    end_date = DateTimeField()  # 数据集结束日期时间
    raw_data_url = StringField()  # 原始数据集下载地址
    data_volume = StringField()  # 原始数据集体积
    data_format = StringField()  # 原始数据集格式
    data_verification = ListField()  # 数据集校验人员姓名
    contact_name = StringField()  # 数据集联系人
    contact_number = StringField()  # 数据集联系人电话
    contact_email = EmailField()  # 数据集联系人邮箱
    institution = StringField()  # 数据集发布机构
    description = StringField()  # 数据集描述
    # 观测站数据部分
    station_name = StringField()  # 观测站点名称
    station_description = StringField()  # 观测站点的描述#模型数据部分
    model_dimensions = ListField()  # 模型数据维度
    model_variables = ListField()  # 模型数据变量
    model_dt = ListField()  # 模型数据时间
    model_depth = ListField()  # 模型水深数据
    # nc元特有数据信息
    e_name = StringField()  # 英文名
    # theme = StringField()  # 主题分类
    shared = StringField()  # 共享方式
    update_frequency = StringField()  # 更新频率
    timeliness = StringField()  # 时效性
    sharing_level = StringField()  # 共享级别
    data_type = StringField()  # 数据要素类型
    data_file_path = StringField()  # 数据物理文件夹地址
    database_year = StringField()  # 剖面存储年限
    meta = {  # 按所列属性建立索引
        'indexes': ['dataset_name', 'keywords', 'start_date', 'end_date', 'data_type', 'shared'],
        'collection': 'meta_data'
    }


class CPOFP_surface(Document):  # 水文 数据集合模型
    dimensions = ListField()  # NetCDF 数据集的维度信息
    parameters = ListField()  # 数据集中所包含的参数信息
    units = DictField()  # 不同参数的物理单位
    date_time = DateTimeField()  # 数据的时间维度
    depth = FloatField()  # 数据的水深维度
    # lat = ListField()  # 数据的纬度维度
    # lon = ListField()  # 数据的经度维度
    lat_start = FloatField()
    lon_start = FloatField()
    lat_length = IntField()
    lon_length = IntField()
    lat_size = FloatField()
    lon_size = FloatField()
    sort = FloatField()
    values = ImageField()  # 数据表述的具体参数值
    data_type = StringField()  # 数据中包含的变量名
    data_source = StringField()  # 数据来源
    img = StringField()
    img2 = StringField()
    meta_data = ReferenceField(
        GFS,  # 指向该数据所在数据集元数据
        reverse_delete_rule=DENY
    )  # 删除时防止删除指向的元数据
    meta = {  # 按所列属性建立索引
        'indexes': ['date_time', 'depth', 'parameters', 'data_type', 'meta_data'],
        'collection': 'CPOFP_surface_2022'
    }


class GUST_surface(Document):  # 水文 数据集合模型
    dimensions = ListField()  # NetCDF 数据集的维度信息
    parameters = ListField()  # 数据集中所包含的参数信息
    units = DictField()  # 不同参数的物理单位
    date_time = DateTimeField()  # 数据的时间维度
    depth = FloatField()  # 数据的水深维度
    # lat = ListField()  # 数据的纬度维度
    # lon = ListField()  # 数据的经度维度
    lat_start = FloatField()
    lon_start = FloatField()
    lat_length = IntField()
    lon_length = IntField()
    lat_size = FloatField()
    lon_size = FloatField()
    sort = FloatField()
    values = ImageField()  # 数据表述的具体参数值
    data_type = StringField()  # 数据中包含的变量名
    data_source = StringField()  # 数据来源
    img = StringField()
    img2 = StringField()
    meta_data = ReferenceField(
        GFS,  # 指向该数据所在数据集元数据
        reverse_delete_rule=DENY
    )  # 删除时防止删除指向的元数据
    meta = {  # 按所列属性建立索引
        'indexes': ['date_time', 'depth', 'parameters', 'data_type', 'meta_data'],
        'collection': 'GUST_surface_2022'
    }

class ICEC_surface(Document):  # 水文 数据集合模型
    dimensions = ListField()  # NetCDF 数据集的维度信息
    parameters = ListField()  # 数据集中所包含的参数信息
    units = DictField()  # 不同参数的物理单位
    date_time = DateTimeField()  # 数据的时间维度
    depth = FloatField()  # 数据的水深维度
    # lat = ListField()  # 数据的纬度维度
    # lon = ListField()  # 数据的经度维度
    lat_start = FloatField()
    lon_start = FloatField()
    lat_length = IntField()
    lon_length = IntField()
    lat_size = FloatField()
    lon_size = FloatField()
    sort = FloatField()
    values = ImageField()  # 数据表述的具体参数值
    data_type = StringField()  # 数据中包含的变量名
    data_source = StringField()  # 数据来源
    img = StringField()
    img2 = StringField()
    meta_data = ReferenceField(
        GFS,  # 指向该数据所在数据集元数据
        reverse_delete_rule=DENY
    )  # 删除时防止删除指向的元数据
    meta = {  # 按所列属性建立索引
        'indexes': ['date_time', 'depth', 'parameters', 'data_type', 'meta_data'],
        'collection': 'ICEC_surface_2022'
    }


class ICETK_surface(Document):  # 水文 数据集合模型
    dimensions = ListField()  # NetCDF 数据集的维度信息
    parameters = ListField()  # 数据集中所包含的参数信息
    units = DictField()  # 不同参数的物理单位
    date_time = DateTimeField()  # 数据的时间维度
    depth = FloatField()  # 数据的水深维度
    # lat = ListField()  # 数据的纬度维度
    # lon = ListField()  # 数据的经度维度
    lat_start = FloatField()
    lon_start = FloatField()
    lat_length = IntField()
    lon_length = IntField()
    lat_size = FloatField()
    lon_size = FloatField()
    sort = FloatField()
    values = ImageField()  # 数据表述的具体参数值
    data_type = StringField()  # 数据中包含的变量名
    data_source = StringField()  # 数据来源
    img = StringField()
    img2 = StringField()
    meta_data = ReferenceField(
        GFS,  # 指向该数据所在数据集元数据
        reverse_delete_rule=DENY
    )  # 删除时防止删除指向的元数据
    meta = {  # 按所列属性建立索引
        'indexes': ['date_time', 'depth', 'parameters', 'data_type', 'meta_data'],
        'collection': 'ICETK_surface_2022'
    }

class SNOD_surface(Document):  # 水文 数据集合模型
    dimensions = ListField()  # NetCDF 数据集的维度信息
    parameters = ListField()  # 数据集中所包含的参数信息
    units = DictField()  # 不同参数的物理单位
    date_time = DateTimeField()  # 数据的时间维度
    depth = FloatField()  # 数据的水深维度
    # lat = ListField()  # 数据的纬度维度
    # lon = ListField()  # 数据的经度维度
    lat_start = FloatField()
    lon_start = FloatField()
    lat_length = IntField()
    lon_length = IntField()
    lat_size = FloatField()
    lon_size = FloatField()
    sort = FloatField()
    values = ImageField()  # 数据表述的具体参数值
    data_type = StringField()  # 数据中包含的变量名
    data_source = StringField()  # 数据来源
    img = StringField()
    img2 = StringField()
    meta_data = ReferenceField(
        GFS,  # 指向该数据所在数据集元数据
        reverse_delete_rule=DENY
    )  # 删除时防止删除指向的元数据
    meta = {  # 按所列属性建立索引
        'indexes': ['date_time', 'depth', 'parameters', 'data_type', 'meta_data'],
        'collection': 'SNOD_surface_2022'
    }

class TMP_surface(Document):  # 水文 数据集合模型
    dimensions = ListField()  # NetCDF 数据集的维度信息
    parameters = ListField()  # 数据集中所包含的参数信息
    units = DictField()  # 不同参数的物理单位
    date_time = DateTimeField()  # 数据的时间维度
    depth = FloatField()  # 数据的水深维度
    # lat = ListField()  # 数据的纬度维度
    # lon = ListField()  # 数据的经度维度
    lat_start = FloatField()
    lon_start = FloatField()
    lat_length = IntField()
    lon_length = IntField()
    lat_size = FloatField()
    lon_size = FloatField()
    sort = FloatField()
    values = ImageField()  # 数据表述的具体参数值
    data_type = StringField()  # 数据中包含的变量名
    data_source = StringField()  # 数据来源
    img = StringField()
    img2 = StringField()
    meta_data = ReferenceField(
        GFS,  # 指向该数据所在数据集元数据
        reverse_delete_rule=DENY
    )  # 删除时防止删除指向的元数据
    meta = {  # 按所列属性建立索引
        'indexes': ['date_time', 'depth', 'parameters', 'data_type', 'meta_data'],
        'collection': 'TMP_surface_2022'
    }


class PRES_surface(Document):  # 水文 数据集合模型
    dimensions = ListField()  # NetCDF 数据集的维度信息
    parameters = ListField()  # 数据集中所包含的参数信息
    units = DictField()  # 不同参数的物理单位
    date_time = DateTimeField()  # 数据的时间维度
    depth = FloatField()  # 数据的水深维度
    # lat = ListField()  # 数据的纬度维度
    # lon = ListField()  # 数据的经度维度
    lat_start = FloatField()
    lon_start = FloatField()
    lat_length = IntField()
    lon_length = IntField()
    lat_size = FloatField()
    lon_size = FloatField()
    sort = FloatField()
    values = ImageField()  # 数据表述的具体参数值
    data_type = StringField()  # 数据中包含的变量名
    data_source = StringField()  # 数据来源
    img = StringField()
    img2 = StringField()
    meta_data = ReferenceField(
        GFS,  # 指向该数据所在数据集元数据
        reverse_delete_rule=DENY
    )  # 删除时防止删除指向的元数据
    meta = {  # 按所列属性建立索引
        'indexes': ['date_time', 'depth', 'parameters', 'data_type', 'meta_data'],
        'collection': 'PRES_surface_2022'
    }


class RH_2maboveground(Document):  # 水文 数据集合模型
    dimensions = ListField()  # NetCDF 数据集的维度信息
    parameters = ListField()  # 数据集中所包含的参数信息
    units = DictField()  # 不同参数的物理单位
    date_time = DateTimeField()  # 数据的时间维度
    depth = FloatField()  # 数据的水深维度
    # lat = ListField()  # 数据的纬度维度
    # lon = ListField()  # 数据的经度维度
    lat_start = FloatField()
    lon_start = FloatField()
    lat_length = IntField()
    lon_length = IntField()
    lat_size = FloatField()
    lon_size = FloatField()
    sort = FloatField()
    values = ImageField()  # 数据表述的具体参数值
    data_type = StringField()  # 数据中包含的变量名
    data_source = StringField()  # 数据来源
    img = StringField()
    img2 = StringField()
    meta_data = ReferenceField(
        GFS,  # 指向该数据所在数据集元数据
        reverse_delete_rule=DENY
    )  # 删除时防止删除指向的元数据
    meta = {  # 按所列属性建立索引
        'indexes': ['date_time', 'depth', 'parameters', 'data_type', 'meta_data'],
        'collection': 'RH_2maboveground_2022'
    }


class LCDC_lowcloudlayer(Document):  # 水文 数据集合模型
    dimensions = ListField()  # NetCDF 数据集的维度信息
    parameters = ListField()  # 数据集中所包含的参数信息
    units = DictField()  # 不同参数的物理单位
    date_time = DateTimeField()  # 数据的时间维度
    depth = FloatField()  # 数据的水深维度
    # lat = ListField()  # 数据的纬度维度
    # lon = ListField()  # 数据的经度维度
    lat_start = FloatField()
    lon_start = FloatField()
    lat_length = IntField()
    lon_length = IntField()
    lat_size = FloatField()
    lon_size = FloatField()
    sort = FloatField()
    values = ImageField()  # 数据表述的具体参数值
    data_type = StringField()  # 数据中包含的变量名
    data_source = StringField()  # 数据来源
    img = StringField()
    img2 = StringField()
    meta_data = ReferenceField(
        GFS,  # 指向该数据所在数据集元数据
        reverse_delete_rule=DENY
    )  # 删除时防止删除指向的元数据
    meta = {  # 按所列属性建立索引
        'indexes': ['date_time', 'depth', 'parameters', 'data_type', 'meta_data'],
        'collection': 'LCDC_lowcloudlayer_2022'
    }


class UGRD_maxwind(Document):  # 水文 数据集合模型
    dimensions = ListField()  # NetCDF 数据集的维度信息
    parameters = ListField()  # 数据集中所包含的参数信息
    units = DictField()  # 不同参数的物理单位
    date_time = DateTimeField()  # 数据的时间维度
    depth = FloatField()  # 数据的水深维度
    # lat = ListField()  # 数据的纬度维度
    # lon = ListField()  # 数据的经度维度
    lat_start = FloatField()
    lon_start = FloatField()
    lat_length = IntField()
    lon_length = IntField()
    lat_size = FloatField()
    lon_size = FloatField()
    grand = ListField()
    sort = FloatField()
    values = ImageField()  # 数据表述的具体参数值
    data_type = StringField()  # 数据中包含的变量名
    data_source = StringField()  # 数据来源
    img = StringField()
    img2 = StringField()
    meta_data = ReferenceField(
        GFS,  # 指向该数据所在数据集元数据
        reverse_delete_rule=DENY
    )  # 删除时防止删除指向的元数据
    meta = {  # 按所列属性建立索引
        'indexes': ['date_time', 'depth', 'parameters', 'data_type', 'meta_data'],
        'collection': 'UGRD_maxwind_2022'
    }


class VGRD_maxwind(Document):  # 水文 数据集合模型
    dimensions = ListField()  # NetCDF 数据集的维度信息
    parameters = ListField()  # 数据集中所包含的参数信息
    units = DictField()  # 不同参数的物理单位
    date_time = DateTimeField()  # 数据的时间维度
    depth = FloatField()  # 数据的水深维度
    # lat = ListField()  # 数据的纬度维度
    # lon = ListField()  # 数据的经度维度
    lat_start = FloatField()
    lon_start = FloatField()
    lat_length = IntField()
    lon_length = IntField()
    lat_size = FloatField()
    lon_size = FloatField()
    grand = ListField()
    sort = FloatField()
    values = ImageField()  # 数据表述的具体参数值
    data_type = StringField()  # 数据中包含的变量名
    data_source = StringField()  # 数据来源
    img = StringField()
    img2 = StringField()
    meta_data = ReferenceField(
        GFS,  # 指向该数据所在数据集元数据
        reverse_delete_rule=DENY
    )  # 删除时防止删除指向的元数据
    meta = {  # 按所列属性建立索引
        'indexes': ['date_time', 'depth', 'parameters', 'data_type', 'meta_data'],
        'collection': 'VGRD_maxwind_2022'
    }


profile = {
    "TMP_surface": TMP_surface,
    "SNOD_surface": SNOD_surface,
    "ICETK_surface": ICETK_surface,
    "ICEC_surface": ICEC_surface,
    "GUST_surface": GUST_surface,
    "CPOFP_surface": CPOFP_surface,
    "PRES_surface": PRES_surface,
    'RH_2maboveground': RH_2maboveground,
    'LCDC_lowcloudlayer': LCDC_lowcloudlayer,
    'UGRD_maxwind': UGRD_maxwind,
    'VGRD_maxwind': VGRD_maxwind
}