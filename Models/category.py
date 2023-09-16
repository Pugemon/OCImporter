from tortoise import fields
from tortoise.models import Model
from config import settings

database_prefix = settings.get("oc.database_prefix")


class OC_CategoryBaseModel(Model):
    category_id = fields.IntField(unique=True, pk=True)


class OC_Category(OC_CategoryBaseModel):
    image = fields.CharField(max_length=255, null=True)
    parent_id = fields.IntField(default=0)
    top = fields.SmallIntField(default=0)
    column = fields.IntField(default=0)
    sort_order = fields.IntField(default=0)
    status = fields.SmallIntField(default=1)
    date_added = fields.DatetimeField(auto_now_add=True)
    date_modified = fields.DatetimeField(auto_now=True)

    class Meta:
        table = f"{database_prefix}category"
        ordering = ["category_id"]


class OC_Category_Description(OC_CategoryBaseModel):
    language_id = fields.IntField(default=1, pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()
    meta_title = fields.CharField(max_length=255)
    meta_description = fields.CharField(max_length=255)
    meta_keyword = fields.CharField(max_length=255)

    class Meta:
        table = f"{database_prefix}category_description"
        ordering = ["category_id"]


class OC_Category_Filter(OC_CategoryBaseModel):
    category_id = fields.IntField(pk=True)
    filter_id = fields.IntField()

    class Meta:
        table = f"{database_prefix}category_filter"
        ordering = ["category_id"]


class OC_Category_Path(OC_CategoryBaseModel):
    category_id = fields.IntField(unique=False, pk=True)
    path_id = fields.IntField(unique=False)
    level = fields.IntField(default=0)

    class Meta:
        table = f"{database_prefix}category_path"
        ordering = ["category_id"]


class OC_Category_To_Store(OC_CategoryBaseModel):
    store_id = fields.IntField(default=0, pk=True)

    class Meta:
        table = f"{database_prefix}category_to_store"
        ordering = ["category_id"]
