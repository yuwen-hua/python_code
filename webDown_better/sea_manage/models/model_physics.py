from sea_manage import db


class SeabedChina(db.Document):  # 元数据集合模型
    _id = db.ObjectIdField(required=True, primary_key=True)
    dataset_id = db.StringField()  # 数据集名称
    ocean_area = db.StringField()  # 所属海域
    lat = db.FloatField()  # 纬度
    lon = db.FloatField()  # 经度
    name = db.StringField()  # 名称
    en_name = db.StringField()  # 英文名称
    meta = {  # 按所列属性建立索引
        'indexes': ['dataset_id', 'name'],
        'collection': 'seabed_china',
        'strict': False,
        'db_alias': 'physics'
    }


class SeabedJapan(db.Document):  # 元数据集合模型
    _id = db.ObjectIdField(required=True, primary_key=True)
    dataset_id = db.StringField()  # 数据集id
    lat = db.FloatField()  # 纬度
    lon = db.FloatField()  # 经度
    name = db.StringField()  # 名称
    gn_name = db.StringField()  # 纬度
    meta = {  # 按所列属性建立索引
        'indexes': ['dataset_id', 'name'],
        'collection': 'seabed_japan',
        'strict': False,
        'db_alias': 'physics'
    }


class SeabedUSA(db.Document):  # 元数据集合模型
    _id = db.ObjectIdField(required=True, primary_key=True)
    dataset_id = db.StringField()
    RC = db.StringField()
    UFI = db.StringField()
    UNI = db.StringField()
    DDLAT = db.FloatField()
    DDLONG = db.FloatField()
    DMSLAT = db.StringField()
    DMSLONG = db.StringField()
    MGRS = db.StringField()
    JOG = db.StringField()
    FC = db.StringField()
    DSG = db.StringField()
    PC = db.StringField()
    CC1 = db.StringField()
    ADM1 = db.StringField()
    CC2 = db.StringField()
    LC = db.StringField()
    TC = db.StringField()
    FULL_NAME = db.StringField()
    FULLNAMEND = db.StringField()
    NT = db.StringField()
    SHORT_FORM = db.StringField()
    GENERIC = db.StringField()
    SORT_NAME = db.StringField()
    MOD_DATE = db.StringField()
    N_MOD_DATE = db.StringField()
    NAME_LINK = db.StringField()
    NAME_RANK = db.StringField()
    DISPLAY = db.StringField()
    NOTE = db.StringField()
    RNUM = db.StringField()
    meta = {  # 按所列属性建立索引
        'indexes': ['dataset_id', 'FULL_NAME'],
        'collection': 'seabed_usa',
        'strict': False,
        'db_alias': 'physics'
    }


class SeabedWorld(db.Document):  # 元数据集合模型
    _id = db.ObjectIdField(required=True, primary_key=True)
    dataset_id = db.StringField()
    name = db.StringField()
    type = db.StringField()
    meeting = db.StringField()
    proposer = db.StringField()
    proposal_y = db.StringField()
    discoverer = db.StringField()
    discovery_ = db.StringField()
    history = db.StringField()
    comments = db.StringField()
    lat = db.FloatField()
    lon = db.FloatField()
    meta = {  # 按所列属性建立索引
        'indexes': ['dataset_id', 'name'],
        'collection': 'seabed_world',
        'strict': False,
        'db_alias': 'physics'
    }


class SilkRoad(db.Document):  # 元数据集合模型
    dataset_id = db.StringField()
    china_invest = db.StringField()
    port_name = db.StringField()
    area = db.StringField()
    country = db.StringField()
    position = db.StringField
    lat = db.FloatField()
    lon = db.FloatField()
    meta = {  # 按所列属性建立索引
        'indexes': ['dataset_id', 'port_name'],
        'collection': 'silk_soad',
        'strict': False,
        'db_alias': 'physics'
    }


class MetaData(db.Document):  # 元数据集合模型
    _id = db.ObjectIdField(required=True, primary_key=True)
    # 通用参数部分
    dataset_id = db.StringField()  # 数据集id
    file_name = db.StringField()  # 文件名称
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
    # 重磁元特有数据信息
    survey_block = db.StringField()  # 调查区块
    dataset_create_time = db.StringField()  # 数据集创建时间
    survey_country = db.StringField()  # 调查国家
    investigation_organization = db.StringField()  # 调查机构
    survey_ship = db.StringField()  # 调查船
    investigation_type = db.StringField()  # 调查平台类型
    chief_scientist = db.StringField()  # 首席科学家
    port_origin = db.StringField()  # 起始港
    port_termination = db.StringField()  # 结束港
    navigator = db.StringField()  # 导航仪
    magnetometer = db.StringField()  # 磁力仪
    gravimeter = db.StringField()  # 重力仪
    lat_start = db.FloatField()  # 北边纬度
    lat_end = db.FloatField()  # 南边纬度
    lon_start = db.FloatField()  # 西边经度
    lon_end = db.FloatField()  # 东边经度

    meta = {  # 按所列属性建立索引
        'indexes': ['dataset_id', 'keywords', 'file_name', 'survey_block', 'dataset_create_time', 'survey_ship'],
        'collection': 'meta_data',
        'db_alias': 'physics',
    }


class MagnetismProfile(db.Document):
    file_name = db.StringField()  # 文件名
    survey_code = db.StringField()  # 测区号
    data_time = db.StringField()  # 日期
    quality_compliance = db.IntField()  # 质量符
    location = db.LineStringField()  # geo地理信息
    values = db.ListField()

    meta = {  # 按所列属性建立索引
        'indexes': ['file_name'],
        'collection': 'magnetism_profile',
        'db_alias': 'physics',
    }


class GravityProfile(db.Document):
    file_name = db.StringField()  # 文件名
    survey_code = db.StringField()  # 测区号
    data_time = db.StringField()  # 日期
    quality_compliance = db.IntField()  # 质量符
    location = db.LineStringField()  # geo地理信息
    values = db.ListField()

    meta = {  # 按所列属性建立索引
        'indexes': ['file_name'],
        'collection': 'gravity_profile',
        'db_alias': 'physics',
    }


Physics = {
    "cn": SeabedChina,
    "usa": SeabedUSA,
    "jp": SeabedJapan,
    "word": SeabedWorld,
    "port": SilkRoad
}
