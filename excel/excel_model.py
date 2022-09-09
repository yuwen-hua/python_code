from mongoengine import *

class Tree(Document):
    label = StringField()
    children = ListField()
    meta = {  # 按所列属性建立索引
        'collection': 'enctree'
    }