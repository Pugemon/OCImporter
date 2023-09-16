from tortoise import fields
from tortoise.models import Model
from config import settings

database_prefix = settings.get("oc.database_prefix")


class OC_AttributeBaseModel(Model):
    attribute_id = fields.IntField(null=False, unique=True)


class OC_Atribute(OC_AttributeBaseModel):
    attribute_group_id = fields.IntField(null=False, unique=True)
    sort_order = fields.IntField(null=False)

    class Meta:
        table = f"{database_prefix}attribute"
        ordering = ["attribute_id"]


class OC_Attribute_Description(OC_AttributeBaseModel):
    language_id = fields.IntField(null=False, default=1)
    name = fields.CharField(null=False, max_length=64)

    class Meta:
        table = f"{database_prefix}attribute_description"
        ordering = ["attribute_id"]


class OC_Attribute_Group(OC_AttributeBaseModel):
    attribute_group_id = fields.IntField(pk=True, null=False, unique=True)
    sort_order = fields.IntField(null=False)

    class Meta:
        table = f"{database_prefix}attribute_group"
        ordering = ["attribute_group_id"]


class OC_Attribute_Group_Description(OC_AttributeBaseModel):
    attribute_group_id = fields.IntField(pk=True, null=False, unique=True)
    language_id = fields.IntField(null=False)
    name = fields.CharField(null=False, max_length=64)

    class Meta:
        table = f"{database_prefix}attribute_group_description"
        ordering = ["attribute_group_id"]
