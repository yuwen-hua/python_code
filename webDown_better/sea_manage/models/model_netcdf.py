# _&_ coding: utf-8 _*_
# @Time : 2022/5/6 15:57
# @File: model.netcdf
# @Project : startest_sea_python



from sea_manage import db


class Netcdf(db.Document):
    _id = db.ObjectIdField(required=True, primary_key=True)
    name = db.StringField() # 保存文件名字
    size = db.IntField()    # 保存文件大小
    path = db.StringField() # 保存文件路径
    create_time = db.DateTimeField()# 文件上传时间
    ip = db.StringField()   # 文件上传时的ip
    user_name = db.StringField()    # 上传文件账号
    data_type = db.StringField()

    meta = {'collection': 'temp', 'strict': False, 'db_alias': 'Netcdf'}





class MetaData(db.Document):
    _id = db.ObjectIdField(required=True, primary_key=True)
    file_id = db.ListField()    # 上传文件的id
    dimension = db.StringField()    # 解析文件的维度
    collection_type = db.StringField()  # 采集数据所属类型
    thematic = db.StringField()
    dataset = db.StringField()
    json  = db.StringField()    #模板采集所用的json模板
    # type_id = db.ObjectIdField()    # 上传的类型
    # 通用参数部分
    dataset_name = db.StringField()  # 数据集名称
    ocean_area = db.ListField()  # 观测、观测海域
    project_info = db.StringField()  # 项目相关信息
    keywords = db.ListField()  # 数据集关键词
    subject = db.ListField()  # 数据集所属科目类别
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
    # subject = db.StringField()  # 学科分类
    # theme =  db.StringField()  # 主题分类
    shared = db.StringField()  # 共享方式
    update_frequency = db.StringField()  # 更新频率
    timeliness = db.StringField()  # 时效性
    sharing_level = db.StringField()  # 共享级别
    data_type = db.StringField()  # 数据要素类型
    data_file_path = db.StringField()  # 数据物理文件夹地址
    database_year = db.StringField()  # 数据物理文件夹地址

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

    status = db.IntField()  # 数据状态
    user_name = db.StringField()    # 录入人
    user_date = db.DateTimeField()  # 录入时间
    user_up_date = db.DateTimeField()  # 提审时间
    auditMind = db.StringField()    # 审核意见

    meta = {'collection': 'meta_data', 'strict': False, 'db_alias': 'Netcdf', }


class Check(db.Document):
    _id = db.ObjectIdField(required=True, primary_key=True)
    meta_id = db.ObjectIdField()
    status = db.IntField()  # 数据状态
    auditMind = db.StringField()
    ip = db.StringField()
    username = db.StringField()
    update_time = db.DateTimeField()

    meta = {'collection': 'user', 'strict': False, 'db_alias': 'Netcdf', }



