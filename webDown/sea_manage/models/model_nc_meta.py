from sea_manage import db


class NcMeta(db.Document):  # 元数据集合模型
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
    # e_name = StringField()  # 英文名
    # subject = StringField()  # 学科分类
    # theme = StringField()  # 主题分类
    # shared = StringField()  # 共享方式
    # update_frequency = StringField()  # 更新频率
    # timeliness = StringField()  # 时效性
    # sharing_level = StringField()  # 共享级别
    # e_name = StringField()  # 英文名
    meta = {'collection': 'meta_data', 'strict': False, 'db_alias': 'netcdf', }


