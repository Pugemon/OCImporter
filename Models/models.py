from tortoise import fields
from tortoise.models import Model
from config import settings



class OC_Atribute(Model):
    attribute_id = fields.IntField(null=False, unique=True)
    attribute_group_id = fields.IntField(null=False, unique=True)
    sort_order = fields.IntField(null=False)

class OC_Attribute_Description(Model):
    attribute_id = fields.IntField(null=False, unique=True)
    language_id = fields.IntField(null=False)
    name = fields.CharField(null=False, max_length=64)

class OC_Attribute_Group(Model):
    attribute_group_id = fields.IntField(null=False, unique=True)
    sort_order = fields.IntField(null=False)

class OC_Attribute_Group_Description(Model):
    attribute_group_id = fields.IntField(null=False, unique=True)
    language_id = fields.IntField(null=False)
    name = fields.CharField(null=False, max_length=64)
