from mongoengine import *

class DepthsA(Document):
    # label = StringField()
    # children = ListField()
    DSNM = StringField()
    LNAM = StringField()
    NAME = StringField()
    NOID = StringField()
    INFORM = StringField()
    NINFOM = StringField()
    NTXTDS = StringField()
    PICREP = StringField()
    TXTDSC = StringField()
    RECDAT = StringField()
    RECIND = StringField()
    SORDAT = StringField()
    SORIND = StringField()
    OBJNAM = StringField()
    NOBJNM = StringField()
    EDITOR = StringField()
    LAST_MOD = StringField()
    EDITOR_COM = StringField()
    VERIFIED = StringField()
    VERIFIER = StringField()
    VERIFIED_D = StringField()
    IS_DELETE = StringField()
    DELETE_COM = StringField()
    PLTS_COMP_ = StringField()
    NIS_PRODUC = StringField()
    NIS_VERIFI = StringField()
    NIS_VERI_1 = StringField()
    NIS_VERIFY = StringField()
    NIS_EDITOR = StringField()
    NIS_LAST_M = StringField()
    NIS_EDIT_1 = StringField()
    IS_CONFLAT = StringField()
    QUASOU = StringField()
    SOUACC = StringField()
    VERDAT = StringField()
    DRVAL1 = StringField()
    DRVAL2 = StringField()
    FCSubtype = StringField()
    RESTRN = StringField()
    TECSOU = StringField()
    NIS_EDIT_D = StringField()
    EDIT_DATE = StringField()
    SCAMIN_STE = StringField()
    Shape_Leng = StringField()
    Shape_Area = StringField()
    location = PolygonField()
    meta = {  # 按所列属性建立索引
        'collection': 'DepthsA'
    }

class DepthsL(Document):
    # label = StringField()
    # children = ListField()
    DSNM = StringField()
    LNAM = StringField()
    NAME = StringField()
    NOID = StringField()
    INFORM = StringField()
    NINFOM = StringField()
    NTXTDS = StringField()
    PICREP = StringField()
    TXTDSC = StringField()
    RECDAT = StringField()
    RECIND = StringField()
    SORDAT = StringField()
    SORIND = StringField()
    OBJNAM = StringField()
    NOBJNM = StringField()
    EDITOR = StringField()
    LAST_MOD = StringField()
    EDITOR_COM = StringField()
    VERIFIED = StringField()
    VERIFIER = StringField()
    VERIFIED_D = StringField()
    IS_DELETE = StringField()
    DELETE_COM = StringField()
    PLTS_COMP_ = StringField()
    NIS_PRODUC = StringField()
    NIS_VERIFI = StringField()
    NIS_VERI_1 = StringField()
    NIS_VERIFY = StringField()
    NIS_EDITOR = StringField()
    NIS_LAST_M = StringField()
    NIS_EDIT_1 = StringField()
    IS_CONFLAT = StringField()
    QUASOU = StringField()
    SOUACC = StringField()
    VERDAT = StringField()
    DRVAL1 = StringField()
    DRVAL2 = StringField()
    FCSubtype = StringField()
    RESTRN = StringField()
    TECSOU = StringField()
    SCAMIN_STE = StringField()
    Shape_Leng = StringField()
    Shape_Area = StringField()
    P_QUAPOS = StringField()
    P_POSACC = StringField()
    P_HORDAT = StringField()
    VALDCO = StringField()
    NIS_EDIT_D = StringField()
    EDIT_DATE = StringField()
    location = LineStringField()
    meta = {  # 按所列属性建立索引
        'collection': 'DepthsL'
    }

ENC = {
    "DepthsA": DepthsA,
    "DepthsL": DepthsL
}