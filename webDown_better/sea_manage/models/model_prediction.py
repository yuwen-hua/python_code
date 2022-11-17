from sea_manage import db


class Meta(db.Document):  # 元数据集合模型
    _id = db.ObjectIdField(required=True, primary_key=True)
    dimension = db.StringField()  # 解析文件的维度
    sort = db.FloatField()
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

    meta = {'collection': 'meta_data', 'strict': False, 'db_alias': 'prediction', }


class GV2021(db.Document):  # 通过 meta_data 查询 Hydrology表
    _id = db.ObjectIdField(required=True, primary_key=True)
    dimensions = db.ListField()  # 尺寸
    parameters = db.ListField()  # 范围
    units = db.DictField()  # 单位
    depth = db.FloatField()  # 深度
    lat_start = db.FloatField()  # 纬度开始值
    lon_start = db.FloatField()  # 经度开始值
    lon_length = db.IntField()  # 经度长度
    lat_length = db.IntField()  # 纬度长度
    lon_size = db.FloatField()  # 经度跨度
    lat_size = db.FloatField()  # 纬度跨度
    speed = db.ListField()
    values_u = db.ListField()  # u分量
    values_v = db.ListField()  # v分量
    data_source = db.StringField()  # 数据来源
    meta_data = db.ReferenceField(
        Meta,  # 指向该数据所在数据集元数据
    )  # meta_data的标识
    img = db.StringField()
    img2 = db.StringField()
    date_time = db.DateTimeField()  # 数据日期时间
    data_type = db.StringField()  # 数据中包含的变量名
    meta = {'collection': 'GV_2021', 'strict': False, 'db_alias': 'prediction', }

    def to_dict(self):
        gv_dict = {
            "lat_start": self.lat_start,
            "lon_start": self.lon_start,
            "lon_length": self.lon_length,
            "lat_length": self.lat_length,
            "lon_size": self.lon_size,
            "lat_size": self.lat_size,
            "img": self.img,
            "img2": self.img2,
            "values_u": self.values_u,
            "values_v": self.values_v
        }
        return gv_dict


class Velocity2022(db.Document):  # 通过 meta_data 查询 Hydrology表
    _id = db.ObjectIdField(required=True, primary_key=True)
    dimensions = db.ListField()  # 尺寸
    parameters = db.ListField()  # 范围
    units = db.DictField()  # 单位
    depth = db.FloatField()  # 深度
    lat_start = db.FloatField()  # 纬度开始值
    lon_start = db.FloatField()  # 经度开始值
    lon_length = db.IntField()  # 经度长度
    lat_length = db.IntField()  # 纬度长度
    lon_size = db.FloatField()  # 经度跨度
    lat_size = db.FloatField()  # 纬度跨度
    speed = db.ListField()
    values_u = db.ListField()  # u分量
    values_v = db.ListField()  # v分量
    data_source = db.StringField()  # 数据来源
    meta_data = db.ReferenceField(
        Meta,  # 指向该数据所在数据集元数据
    )  # meta_data的标识
    img = db.StringField()
    img2 = db.StringField()
    date_time = db.DateTimeField()  # 数据日期时间
    meta = {'collection': 'Velocity_2022', 'strict': False, 'db_alias': 'prediction', }

    def to_dict(self):
        gv_dict = {
            "lat_start": self.lat_start,
            "lon_start": self.lon_start,
            "lon_length": self.lon_length,
            "lat_length": self.lat_length,
            "lon_size": self.lon_size,
            "lat_size": self.lat_size,
            "img": self.img,
            "img2": self.img2,
            "values_u": self.values_u,
            "values_v": self.values_v
        }
        return gv_dict


class CPOFP_surface2022(db.Document):  # 通过 meta_data 查询 Hydrology表
    _id = db.ObjectIdField(required=True, primary_key=True)
    dimensions = db.ListField()  # 尺寸
    parameters = db.ListField()  # 范围
    units = db.DictField()  # 单位
    depth = db.FloatField()  # 深度
    lat_start = db.FloatField()  # 纬度开始值
    lon_start = db.FloatField()  # 经度开始值
    lon_length = db.IntField()  # 经度长度
    lat_length = db.IntField()  # 纬度长度
    lon_size = db.FloatField()  # 经度跨度
    lat_size = db.FloatField()  # 纬度跨度
    speed = db.ListField()
    sort = db.FloatField()
    values = db.ImageField()
    values_u = db.ListField()  # u分量
    values_v = db.ListField()  # v分量
    data_source = db.StringField()  # 数据来源
    meta_data = db.ReferenceField(
        Meta,  # 指向该数据所在数据集元数据
    )  # meta_data的标识
    img = db.StringField()
    img2 = db.StringField()
    date_time = db.DateTimeField()  # 数据日期时间
    meta = {'collection': 'CPOFP_surface_2022', 'strict': False, 'db_alias': 'prediction', }

    def to_dict(self):
        gv_dict = {
            "lat_start": self.lat_start,
            "lon_start": self.lon_start,
            "lon_length": self.lon_length,
            "lat_length": self.lat_length,
            "lon_size": self.lon_size,
            "lat_size": self.lat_size,
            "img": self.img,
            "img2": self.img2,
            "values_u": self.values_u,
            "values_v": self.values_v
        }
        return gv_dict


class ICEC_surface2022(db.Document):  # 通过 meta_data 查询 Hydrology表
    _id = db.ObjectIdField(required=True, primary_key=True)
    dimensions = db.ListField()  # 尺寸
    parameters = db.ListField()  # 范围
    units = db.DictField()  # 单位
    depth = db.FloatField()  # 深度
    lat_start = db.FloatField()  # 纬度开始值
    lon_start = db.FloatField()  # 经度开始值
    lon_length = db.IntField()  # 经度长度
    lat_length = db.IntField()  # 纬度长度
    lon_size = db.FloatField()  # 经度跨度
    lat_size = db.FloatField()  # 纬度跨度
    speed = db.ListField()
    sort = db.FloatField()
    values = db.ImageField()
    values_u = db.ListField()  # u分量
    values_v = db.ListField()  # v分量
    data_source = db.StringField()  # 数据来源
    meta_data = db.ReferenceField(
        Meta,  # 指向该数据所在数据集元数据
    )  # meta_data的标识
    img = db.StringField()
    img2 = db.StringField()
    date_time = db.DateTimeField()  # 数据日期时间
    meta = {'collection': 'ICEC_surface_2022', 'strict': False, 'db_alias': 'prediction', }

    def to_dict(self):
        gv_dict = {
            "lat_start": self.lat_start,
            "lon_start": self.lon_start,
            "lon_length": self.lon_length,
            "lat_length": self.lat_length,
            "lon_size": self.lon_size,
            "lat_size": self.lat_size,
            "img": self.img,
            "img2": self.img2,
            "values_u": self.values_u,
            "values_v": self.values_v
        }
        return gv_dict


class ICETK_surface2022(db.Document):  # 通过 meta_data 查询 Hydrology表
    _id = db.ObjectIdField(required=True, primary_key=True)
    dimensions = db.ListField()  # 尺寸
    parameters = db.ListField()  # 范围
    units = db.DictField()  # 单位
    depth = db.FloatField()  # 深度
    lat_start = db.FloatField()  # 纬度开始值
    lon_start = db.FloatField()  # 经度开始值
    lon_length = db.IntField()  # 经度长度
    lat_length = db.IntField()  # 纬度长度
    lon_size = db.FloatField()  # 经度跨度
    lat_size = db.FloatField()  # 纬度跨度
    speed = db.ListField()
    sort = db.FloatField()
    values = db.ImageField()
    values_u = db.ListField()  # u分量
    values_v = db.ListField()  # v分量
    data_source = db.StringField()  # 数据来源
    meta_data = db.ReferenceField(
        Meta,  # 指向该数据所在数据集元数据
    )  # meta_data的标识
    img = db.StringField()
    img2 = db.StringField()
    date_time = db.DateTimeField()  # 数据日期时间
    meta = {'collection': 'ICETK_surface_2022', 'strict': False, 'db_alias': 'prediction', }

    def to_dict(self):
        gv_dict = {
            "lat_start": self.lat_start,
            "lon_start": self.lon_start,
            "lon_length": self.lon_length,
            "lat_length": self.lat_length,
            "lon_size": self.lon_size,
            "lat_size": self.lat_size,
            "img": self.img,
            "img2": self.img2,
            "values_u": self.values_u,
            "values_v": self.values_v
        }
        return gv_dict


class TMP_surface2022(db.Document):  # 通过 meta_data 查询 Hydrology表
    _id = db.ObjectIdField(required=True, primary_key=True)
    dimensions = db.ListField()  # 尺寸
    parameters = db.ListField()  # 范围
    units = db.DictField()  # 单位
    depth = db.FloatField()  # 深度
    lat_start = db.FloatField()  # 纬度开始值
    lon_start = db.FloatField()  # 经度开始值
    lon_length = db.IntField()  # 经度长度
    lat_length = db.IntField()  # 纬度长度
    lon_size = db.FloatField()  # 经度跨度
    lat_size = db.FloatField()  # 纬度跨度
    speed = db.ListField()
    sort = db.FloatField()
    values = db.ImageField()
    values_u = db.ListField()  # u分量
    values_v = db.ListField()  # v分量
    data_source = db.StringField()  # 数据来源
    meta_data = db.ReferenceField(
        Meta,  # 指向该数据所在数据集元数据
    )  # meta_data的标识
    img = db.StringField()
    img2 = db.StringField()
    date_time = db.DateTimeField()  # 数据日期时间
    meta = {'collection': 'TMP_surface_2022', 'strict': False, 'db_alias': 'prediction', }

    def to_dict(self):
        gv_dict = {
            "lat_start": self.lat_start,
            "lon_start": self.lon_start,
            "lon_length": self.lon_length,
            "lat_length": self.lat_length,
            "lon_size": self.lon_size,
            "lat_size": self.lat_size,
            "img": self.img,
            "img2": self.img2,
            "values_u": self.values_u,
            "values_v": self.values_v
        }
        return gv_dict



class GUST_surface2022(db.Document):  # 通过 meta_data 查询 Hydrology表
    _id = db.ObjectIdField(required=True, primary_key=True)
    dimensions = db.ListField()  # 尺寸
    parameters = db.ListField()  # 范围
    units = db.DictField()  # 单位
    depth = db.FloatField()  # 深度
    lat_start = db.FloatField()  # 纬度开始值
    lon_start = db.FloatField()  # 经度开始值
    lon_length = db.IntField()  # 经度长度
    lat_length = db.IntField()  # 纬度长度
    lon_size = db.FloatField()  # 经度跨度
    lat_size = db.FloatField()  # 纬度跨度
    speed = db.ListField()
    sort = db.FloatField()
    values = db.ImageField()
    values_u = db.ListField()  # u分量
    values_v = db.ListField()  # v分量
    data_source = db.StringField()  # 数据来源
    meta_data = db.ReferenceField(
        Meta,  # 指向该数据所在数据集元数据
    )  # meta_data的标识
    img = db.StringField()
    img2 = db.StringField()
    date_time = db.DateTimeField()  # 数据日期时间
    meta = {'collection': 'GUST_surface_2022', 'strict': False, 'db_alias': 'prediction', }

    def to_dict(self):
        gv_dict = {
            "lat_start": self.lat_start,
            "lon_start": self.lon_start,
            "lon_length": self.lon_length,
            "lat_length": self.lat_length,
            "lon_size": self.lon_size,
            "lat_size": self.lat_size,
            "img": self.img,
            "img2": self.img2,
            "values_u": self.values_u,
            "values_v": self.values_v
        }
        return gv_dict



class SNOD_surface2022(db.Document):  # 通过 meta_data 查询 Hydrology表
    _id = db.ObjectIdField(required=True, primary_key=True)
    dimensions = db.ListField()  # 尺寸
    parameters = db.ListField()  # 范围
    units = db.DictField()  # 单位
    depth = db.FloatField()  # 深度
    lat_start = db.FloatField()  # 纬度开始值
    lon_start = db.FloatField()  # 经度开始值
    lon_length = db.IntField()  # 经度长度
    lat_length = db.IntField()  # 纬度长度
    lon_size = db.FloatField()  # 经度跨度
    lat_size = db.FloatField()  # 纬度跨度
    speed = db.ListField()
    sort = db.FloatField()
    values = db.ImageField()
    values_u = db.ListField()  # u分量
    values_v = db.ListField()  # v分量
    data_source = db.StringField()  # 数据来源
    meta_data = db.ReferenceField(
        Meta,  # 指向该数据所在数据集元数据
    )  # meta_data的标识
    img = db.StringField()
    img2 = db.StringField()
    date_time = db.DateTimeField()  # 数据日期时间
    meta = {'collection': 'SNOD_surface_2022', 'strict': False, 'db_alias': 'prediction', }

    def to_dict(self):
        gv_dict = {
            "lat_start": self.lat_start,
            "lon_start": self.lon_start,
            "lon_length": self.lon_length,
            "lat_length": self.lat_length,
            "lon_size": self.lon_size,
            "lat_size": self.lat_size,
            "img": self.img,
            "img2": self.img2,
            "values_u": self.values_u,
            "values_v": self.values_v
        }
        return gv_dict


class LCDC_surface2022(db.Document):  # 通过 meta_data 查询 Hydrology表
    _id = db.ObjectIdField(required=True, primary_key=True)
    dimensions = db.ListField()  # 尺寸
    parameters = db.ListField()  # 范围
    units = db.DictField()  # 单位
    depth = db.FloatField()  # 深度
    lat_start = db.FloatField()  # 纬度开始值
    lon_start = db.FloatField()  # 经度开始值
    lon_length = db.IntField()  # 经度长度
    lat_length = db.IntField()  # 纬度长度
    lon_size = db.FloatField()  # 经度跨度
    lat_size = db.FloatField()  # 纬度跨度
    speed = db.ListField()
    sort = db.FloatField()
    values = db.ImageField()
    values_u = db.ListField()  # u分量
    values_v = db.ListField()  # v分量
    data_source = db.StringField()  # 数据来源
    meta_data = db.ReferenceField(
        Meta,  # 指向该数据所在数据集元数据
    )  # meta_data的标识
    img = db.StringField()
    img2 = db.StringField()
    date_time = db.DateTimeField()  # 数据日期时间
    meta = {'collection': 'LCDC_surface_2022', 'strict': False, 'db_alias': 'prediction', }

    def to_dict(self):
        gv_dict = {
            "lat_start": self.lat_start,
            "lon_start": self.lon_start,
            "lon_length": self.lon_length,
            "lat_length": self.lat_length,
            "lon_size": self.lon_size,
            "lat_size": self.lat_size,
            "img": self.img,
            "img2": self.img2,
            "values_u": self.values_u,
            "values_v": self.values_v
        }
        return gv_dict


class PRES_surface2022(db.Document):  # 通过 meta_data 查询 Hydrology表
    _id = db.ObjectIdField(required=True, primary_key=True)
    dimensions = db.ListField()  # 尺寸
    parameters = db.ListField()  # 范围
    units = db.DictField()  # 单位
    depth = db.FloatField()  # 深度
    lat_start = db.FloatField()  # 纬度开始值
    lon_start = db.FloatField()  # 经度开始值
    lon_length = db.IntField()  # 经度长度
    lat_length = db.IntField()  # 纬度长度
    lon_size = db.FloatField()  # 经度跨度
    lat_size = db.FloatField()  # 纬度跨度
    speed = db.ListField()
    sort = db.FloatField()
    values = db.ImageField()
    values_u = db.ListField()  # u分量
    values_v = db.ListField()  # v分量
    data_source = db.StringField()  # 数据来源
    meta_data = db.ReferenceField(
        Meta,  # 指向该数据所在数据集元数据
    )  # meta_data的标识
    img = db.StringField()
    img2 = db.StringField()
    date_time = db.DateTimeField()  # 数据日期时间
    meta = {'collection': 'PRES_surface_2022', 'strict': False, 'db_alias': 'prediction', }

    def to_dict(self):
        gv_dict = {
            "lat_start": self.lat_start,
            "lon_start": self.lon_start,
            "lon_length": self.lon_length,
            "lat_length": self.lat_length,
            "lon_size": self.lon_size,
            "lat_size": self.lat_size,
            "img": self.img,
            "img2": self.img2,
            "values_u": self.values_u,
            "values_v": self.values_v
        }
        return gv_dict


class RH_2maboveground2022(db.Document):  # 通过 meta_data 查询 Hydrology表
    _id = db.ObjectIdField(required=True, primary_key=True)
    dimensions = db.ListField()  # 尺寸
    parameters = db.ListField()  # 范围
    units = db.DictField()  # 单位
    depth = db.FloatField()  # 深度
    lat_start = db.FloatField()  # 纬度开始值
    lon_start = db.FloatField()  # 经度开始值
    lon_length = db.IntField()  # 经度长度
    lat_length = db.IntField()  # 纬度长度
    lon_size = db.FloatField()  # 经度跨度
    lat_size = db.FloatField()  # 纬度跨度
    speed = db.ListField()
    sort = db.FloatField()
    values = db.ImageField()
    values_u = db.ListField()  # u分量
    values_v = db.ListField()  # v分量
    data_source = db.StringField()  # 数据来源
    meta_data = db.ReferenceField(
        Meta,  # 指向该数据所在数据集元数据
    )  # meta_data的标识
    img = db.StringField()
    img2 = db.StringField()
    date_time = db.DateTimeField()  # 数据日期时间
    meta = {'collection': 'RH_2maboveground_2022', 'strict': False, 'db_alias': 'prediction', }

    def to_dict(self):
        gv_dict = {
            "lat_start": self.lat_start,
            "lon_start": self.lon_start,
            "lon_length": self.lon_length,
            "lat_length": self.lat_length,
            "lon_size": self.lon_size,
            "lat_size": self.lat_size,
            "img": self.img,
            "img2": self.img2,
            "values_u": self.values_u,
            "values_v": self.values_v
        }
        return gv_dict
class LCDC_lowcloudlayer2022(db.Document):  # 通过 meta_data 查询 Hydrology表
    _id = db.ObjectIdField(required=True, primary_key=True)
    dimensions = db.ListField()  # 尺寸
    parameters = db.ListField()  # 范围
    units = db.DictField()  # 单位
    depth = db.FloatField()  # 深度
    lat_start = db.FloatField()  # 纬度开始值
    lon_start = db.FloatField()  # 经度开始值
    lon_length = db.IntField()  # 经度长度
    lat_length = db.IntField()  # 纬度长度
    lon_size = db.FloatField()  # 经度跨度
    lat_size = db.FloatField()  # 纬度跨度
    speed = db.ListField()
    sort = db.FloatField()
    values = db.ImageField()
    values_u = db.ListField()  # u分量
    values_v = db.ListField()  # v分量
    data_source = db.StringField()  # 数据来源
    meta_data = db.ReferenceField(
        Meta,  # 指向该数据所在数据集元数据
    )  # meta_data的标识
    img = db.StringField()
    img2 = db.StringField()
    date_time = db.DateTimeField()  # 数据日期时间
    meta = {'collection': 'LCDC_lowcloudlayer_2022', 'strict': False, 'db_alias': 'prediction', }

    def to_dict(self):
        gv_dict = {
            "lat_start": self.lat_start,
            "lon_start": self.lon_start,
            "lon_length": self.lon_length,
            "lat_length": self.lat_length,
            "lon_size": self.lon_size,
            "lat_size": self.lat_size,
            "img": self.img,
            "img2": self.img2,
            "values_u": self.values_u,
            "values_v": self.values_v
        }
        return gv_dict

class VGRD_maxwind2022(db.Document):  # 通过 meta_data 查询 Hydrology表
    _id = db.ObjectIdField(required=True, primary_key=True)
    dimensions = db.ListField()  # 尺寸
    parameters = db.ListField()  # 范围
    units = db.DictField()  # 单位
    depth = db.FloatField()  # 深度
    lat_start = db.FloatField()  # 纬度开始值
    lon_start = db.FloatField()  # 经度开始值
    lon_length = db.IntField()  # 经度长度
    lat_length = db.IntField()  # 纬度长度
    lon_size = db.FloatField()  # 经度跨度
    lat_size = db.FloatField()  # 纬度跨度
    speed = db.ListField()
    grand = db.ListField()
    sort = db.FloatField()
    values = db.ImageField()
    values_u = db.ListField()  # u分量
    values_v = db.ListField()  # v分量
    data_source = db.StringField()  # 数据来源
    meta_data = db.ReferenceField(
        Meta,  # 指向该数据所在数据集元数据
    )  # meta_data的标识
    img = db.StringField()
    img2 = db.StringField()
    date_time = db.DateTimeField()  # 数据日期时间
    meta = {'collection': 'VGRD_maxwind_2022', 'strict': False, 'db_alias': 'prediction', }

    def to_dict(self):
        gv_dict = {
            "lat_start": self.lat_start,
            "lon_start": self.lon_start,
            "lon_length": self.lon_length,
            "lat_length": self.lat_length,
            "lon_size": self.lon_size,
            "lat_size": self.lat_size,
            "img": self.img,
            "img2": self.img2,
            "values_u": self.values_u,
            "values_v": self.values_v
        }
        return gv_dict

class UGRD_maxwind2022(db.Document):  # 通过 meta_data 查询 Hydrology表
    _id = db.ObjectIdField(required=True, primary_key=True)
    dimensions = db.ListField()  # 尺寸
    parameters = db.ListField()  # 范围
    units = db.DictField()  # 单位
    depth = db.FloatField()  # 深度
    lat_start = db.FloatField()  # 纬度开始值
    lon_start = db.FloatField()  # 经度开始值
    lon_length = db.IntField()  # 经度长度
    lat_length = db.IntField()  # 纬度长度
    lon_size = db.FloatField()  # 经度跨度
    lat_size = db.FloatField()  # 纬度跨度
    speed = db.ListField()
    grand = db.ListField()
    sort = db.FloatField()
    values = db.ImageField()
    values_u = db.ListField()  # u分量
    values_v = db.ListField()  # v分量
    data_source = db.StringField()  # 数据来源
    meta_data = db.ReferenceField(
        Meta,  # 指向该数据所在数据集元数据
    )  # meta_data的标识
    img = db.StringField()
    img2 = db.StringField()
    date_time = db.DateTimeField()  # 数据日期时间
    meta = { 'collection': 'UGRD_maxwind_2022', 'strict': False, 'db_alias': 'prediction', }

    def to_dict(self):
        gv_dict = {
            "lat_start": self.lat_start,
            "lon_start": self.lon_start,
            "lon_length": self.lon_length,
            "lat_length": self.lat_length,
            "lon_size": self.lon_size,
            "lat_size": self.lat_size,
            "img": self.img,
            "img2": self.img2,
            "values_u": self.values_u,
            "values_v": self.values_v
        }
        return gv_dict


class TrendData(db.Document):  # 元数据集合模型
    # 通用参数部分
    _id = db.ObjectIdField(required=True, primary_key=True)

    dataset_id = db.StringField()  # 数据集id
    station_code = db.StringField()
    name = db.StringField()
    en_name = db.StringField()
    py_name = db.StringField()
    lon = db.FloatField()
    lat = db.FloatField()

    meta = {  # 按所列属性建立索引
        'indexes': ['dataset_id'],
        'collection': 'meta_data',
        'strict': False,
        'db_alias': 'prediction',
    }


class TideData(db.Document):
    _id = db.ObjectIdField(required=True, primary_key=True)

    dataset_id = db.StringField()  # 数据集id
    area_name = db.StringField()
    station_code = db.StringField()
    name = db.StringField()
    en_name = db.StringField()
    py_name = db.StringField()
    lon = db.FloatField()
    lat = db.FloatField()
    meta = {  # 按所列属性建立索引
        'indexes': ['dataset_id'],
        'collection': 'meta_data',
        'strict': False,
        'db_alias': 'prediction',
    }


class GlossData(db.Document):  # 元数据集合模型
    _id = db.ObjectIdField(required=True, primary_key=True)

    # 通用参数部分
    dataset_id = db.StringField()  # 数据集id
    station_name = db.StringField()
    lat = db.FloatField()
    lon = db.FloatField()

    meta = {  # 按所列属性建立索引
        'indexes': ['dataset_id', 'station_name'],
        'collection': 'meta_data',
        'strict': False,
        'db_alias': 'prediction',
    }


Prediction = {
    "GV": {
        "2021": GV2021,
    },
    "Velocity": {
        "2022": Velocity2022,
    },
    "CPOFP_surface": {
        "2022": CPOFP_surface2022
    },
    "ICEC_surface": {
        "2022": ICEC_surface2022
    },
    "ICETK_surface": {
        "2022": ICETK_surface2022
    },
    "TMP_surface": {
        "2022": TMP_surface2022
    },
    "GUST_surface": {
        "2022": GUST_surface2022
    },
    "SNOD_surface": {
        "2022": SNOD_surface2022
    },
    "LCDC_surface": {
        "2022": LCDC_surface2022
    },
    "PRES_surface": {
        "2022": PRES_surface2022
    },
    "RH_2maboveground": {
        "2022": RH_2maboveground2022
    },
    "LCDC_lowcloudlayer": {
        "2022": LCDC_lowcloudlayer2022
    },
    "VGRD_maxwind": {
        "2022": VGRD_maxwind2022
    },
    "UGRD_maxwind": {
        "2022": UGRD_maxwind2022
    },
    "Trend": TrendData,
    "Tide": TideData,
    "Gloss": GlossData
}
