from sea_manage import db

class Temp(db.Document):
    _id = db.ObjectIdField(required=True, primary_key=True)
    name = db.StringField() # 保存文件名字
    size = db.IntField()    # 保存文件大小
    path = db.StringField() # 保存文件路径
    create_time = db.DateTimeField()# 文件上传时间
    ip = db.StringField()   # 文件上传时的ip
    user_name = db.StringField()    # 上传文件账号

    meta = {'collection': 'temp', 'strict': False, 'db_alias': 'Netcdf'}



class Check(db.Document):
    _id = db.ObjectIdField(required=True, primary_key=True)
    meta_id = db.ObjectIdField()
    status = db.IntField()  # 数据状态
    auditMind = db.StringField()
    ip = db.StringField()
    username = db.StringField()
    update_time = db.DateTimeField()

    meta = {'collection': 'user', 'strict': False, 'db_alias': 'Netcdf', }

class MetaData(db.Document):
    _id = db.ObjectIdField(required=True, primary_key=True)
    file_id = db.ListField()  # 上传argo文件的id
    profile_id = db.ListField()  # 上传profile文件的id
    file_type = db.StringField()    # 元数据的类型
    collection_type = db.StringField() # 采集数据所属类型
    thematic = db.StringField()
    dataset = db.StringField()

    dataset_name = db.StringField()  # 数据集名称
    ocean_area = db.ListField()  # 观测海域
    project_info = db.StringField()  # 项目相关信息
    keywords = db.ListField()  # 数据集关键字
    subject = db.ListField()  # 数据集所属科目类别
    platform = db.ListField()  # 观测、调查搭载平台
    instrument = db.ListField()  # 观测、调查设备名称
    parameters = db.ListField()  # 数据集包含的观测、调查参数
    start_date = db.DateTimeField()  # 数据集起始日期时间
    end_date = db.DateTimeField()  # 数据集结束日期时间
    raw_data_url = db.StringField()  # 原始数据集下载地址
    data_volume = db.StringField()  # 原始数据集体积
    data_format = db.StringField()  # 原始数据集格式
    data_verification = db.ListField()  # 数据集校验人员性命
    contact_name = db.StringField()  # 数据集联系人
    contact_number = db.StringField()  # 数据集联系人电话
    contact_email = db.EmailField()  # 数据集联系人邮箱
    institution = db.StringField()  # 数据集发布机构
    description = db.StringField()  # 数据集描述
    # 观测站数据部分
    station_name = db.StringField()  # 观测站点名称
    station_description = db.StringField()  # 观测站点的描述
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
    location = db.PointField()  # geo地理信息
    data_file_path = db.StringField()  # 数据物理文件夹地址
    database_year = db.StringField()  # 数据物理文件夹地址

    status = db.IntField()  # 数据状态
    user_name = db.StringField()  # 录入人
    user_date = db.DateTimeField()  # 录入时间
    user_up_date = db.DateTimeField()  # 提审时间
    auditMind = db.StringField()  # 审核意见
    meta = {  # 按所列属性建立索引
        'indexes': ['dataset_name', 'keywords', 'station_name', 'launch_latitude', 'launch_latitude', 'data_centre'],
        'collection': 'meta_data', 'strict': False, 'db_alias': 'Netcdf'
    }

