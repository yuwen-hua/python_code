from mongoengine import *
from sea_manage import db


# connect('measured', host='localhost', port=27017)


class ArgoMetaData(Document):
    _id = db.ObjectIdField(required=True, primary_key=True)
    dataset_id = db.StringField()
    # dataset_name = db.StringField()  # 数据集名称
    ocean_area = db.ListField()  # 观测海域
    data_type = db.StringField()  # 数据要素类型
    # project_info = db.StringField()  # 项目相关信息
    keywords = db.ListField()  # 数据集关键字
    subject = db.ListField()  # 数据集所属科目类别
    platform = db.ListField()  # 观测、调查搭载平台
    instrument = db.ListField()  # 观测、调查设备名称
    parameters = db.ListField()  # 数据集包含的观测、调查参数
    # start_date = db.DateTimeField()  # 数据集起始日期时间
    # end_date = db.DateTimeField()  # 数据集结束日期时间
    # raw_data_url = db.StringField()  # 原始数据集下载地址
    # data_volume = db.StringField()  # 原始数据集体积
    # data_format = db.StringField()  # 原始数据集格式
    data_verification = db.ListField()  # 数据集校验人员姓名
    # contact_name = db.StringField()  # 数据集联系人
    # contact_number = db.StringField()  # 数据集联系人电话
    # contact_email = db.EmailField()  # 数据集联系人邮箱
    # institution = db.StringField()  # 数据集发布机构
    # description = db.StringField()  # 数据集描述
    # 观测站数据部分
    # station_name = db.StringField()  # 观测站点名称
    # station_description = db.StringField()  # 观测站点的描述
    # 模型数据部分  # 数据集名称
    model_dimensions = db.ListField()  # 模型数据纬度
    model_variables = db.ListField()  # 模型数据变量
    model_dt = db.ListField()  # 模型数据时间
    model_depth = db.ListField()  # 模型水深数据
    # argo浮标专用
    platform_number = db.IntField()  # argo浮标编号/站台号
    format_version = db.StringField()  # 格式版本
    transmission_id = db.StringField()  # 变速器识别码
    transmission_system = db.StringField()  # 传输系统
    transmission_frequency = db.StringField()  # 传输频率
    transmission_system_id = db.StringField()  # 传输系统ID
    positioning_system = db.StringField()  # 定位系统
    platform_model = db.StringField()  # 平台模型
    platform_maker = db.StringField()  # 平台制造商
    platform_firmware_version = db.StringField()  # 平台固件版本
    float_serial_number = db.StringField()  # 浮点数
    float_manual_version = db.StringField()  # 浮动手动版本
    standard_format_id = db.StringField()  # 标准格式ID
    dac_fromat_id = db.StringField()  # DAC FROMAT ID
    wmo_instrument_type = db.StringField()  # 世界气象组织仪器类型
    project_name = db.StringField()  # 项目名称
    data_centre = db.StringField()  # 数据中心
    pi_name = db.StringField()  # pi名称
    startup_date_of_the_float = db.DateTimeField()  # 浮动的启动日期
    launch_latitude = db.FloatField()  # 发射纬度
    launch_longitude = db.FloatField()  # 发射经度
    deployment_platform = db.StringField()  # 部署平台
    deployment_cruise_id = db.StringField()  # 部署导航ID
    sensors_on_the_float = db.StringField()  # 传感器
    sensor_maker = db.StringField()  # 传感器制造商
    sensor_model = db.StringField()  # 传感器型号
    sensor_serial_number = db.StringField()  # 传感器序列号
    sensor_units = db.StringField()  # 传感器单位
    sensor_accuracy = db.StringField()  # 传感器精度
    sensor_resolution = db.StringField()  # 传感器分辨率
    cycle_time = db.FloatField()  # 循环时间
    down_time = db.FloatField()  # 停机时间
    up_time = db.FloatField()  # 启动时间
    parking_time = db.FloatField()  # 停止时间
    descent_profiling_time = db.FloatField()  # 下降分析时间
    ascent_profiling_time = db.FloatField()  # 上升剖面时间
    park_pressure = db.FloatField()  # 驻车时间
    profile_pressure = db.FloatField()  # 刨面压力
    date_of_creation = db.DateTimeField()  # 创建时间
    date_of_update = db.DateTimeField()  # 更新时间
    launch_date = db.DateTimeField()  # 发布日期
    project_name = db.StringField()
    data_centre = db.StringField()
    sensors_on_the_float = db.StringField()
    location = db.PointField()

    meta = {  # 按所列属性建立索引
        'indexes': ['keywords', 'launch_latitude', 'launch_latitude', 'data_centre'],
        'collection': 'meta_data', 'strict': False, 'db_alias': 'measured',
    }


class Profile2021(Document):  # 查询profile列表
    _id = db.ObjectIdField(required=True, primary_key=True)
    platform_number = db.IntField()  # argo浮标编号/站台号
    cycle_number = db.StringField()  #
    date_creation = db.StringField()  #
    date_update = db.StringField()  #
    project_name = db.StringField()  #
    pi_name = db.StringField()  #
    instrument_type = db.StringField()  #
    float_serial_no = db.StringField()  #
    firmware_version = db.StringField()  #
    wmo_instrument_type = db.StringField()  #
    transmission_system = db.StringField()  #
    positioning_system = db.StringField()  #
    sample_direction = db.StringField()  #
    data_mode = db.StringField()  #
    julian_day = db.StringField()  #
    qc_flag_for_date = db.StringField()  #
    qc_flag_for_location = db.StringField()  #
    date = db.DateTimeField()  #
    latitude = db.FloatField()  # 发射纬度
    longitude = db.FloatField()  # 发射经度
    profile_data1 = db.DictField()  #
    profile_data2 = db.DictField()  #
    profile_data3 = db.DictField()  #
    profile_data4 = db.DictField()  #
    profile_data5 = db.DictField()  #

    meta = {  # 按所列属性建立索引
        # 'indexes': ['keywords', 'launch_latitude', 'launch_latitude', 'data_centre'],
        'collection': 'profile_2021', 'strict': False, 'db_alias': 'measured',
    }

class Profile2022(Document):  # 查询profile列表
    _id = db.ObjectIdField(required=True, primary_key=True)
    platform_number = db.IntField()  # argo浮标编号/站台号
    cycle_number = db.StringField()  #
    date_creation = db.StringField()  #
    date_update = db.StringField()  #
    project_name = db.StringField()  #
    pi_name = db.StringField()  #
    instrument_type = db.StringField()  #
    float_serial_no = db.StringField()  #
    firmware_version = db.StringField()  #
    wmo_instrument_type = db.StringField()  #
    transmission_system = db.StringField()  #
    positioning_system = db.StringField()  #
    sample_direction = db.StringField()  #
    data_mode = db.StringField()  #
    julian_day = db.StringField()  #
    qc_flag_for_date = db.StringField()  #
    qc_flag_for_location = db.StringField()  #
    date = db.DateTimeField()  #
    latitude = db.FloatField()  # 发射纬度
    longitude = db.FloatField()  # 发射经度
    profile_data1 = db.DictField()  #
    profile_data2 = db.DictField()  #
    profile_data3 = db.DictField()  #
    profile_data4 = db.DictField()  #
    profile_data5 = db.DictField()  #

    meta = {  # 按所列属性建立索引
        # 'indexes': ['keywords', 'launch_latitude', 'launch_latitude', 'data_centre'],
        'collection': 'profile_2022', 'strict': False, 'db_alias': 'measured',
    }


Profile = {
    "2021": Profile2021,
    "2022": Profile2022,
}
