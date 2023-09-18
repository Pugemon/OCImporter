import tortoise.contrib.mysql.indexes
from tortoise import fields
from tortoise.models import Model
from config import settings
from tortoise.contrib.mysql.indexes import Index

database_prefix = settings.get("oc.database_prefix")

class OC_ProductBaseModel(Model):
    product_id = fields.IntField(pk=True, unique=True)

class OC_Product(OC_ProductBaseModel):
    model = fields.CharField(max_length=64)
    sku = fields.CharField(max_length=64)
    location = fields.CharField(max_length=128)
    quantity = fields.IntField(default=0)
    stock_status_id = fields.IntField()
    image = fields.CharField(max_length=255, null=True)
    manufacturer_id = fields.IntField()
    shipping = fields.SmallIntField(default=1)
    price = fields.DecimalField(max_digits=15, decimal_places=4, default=0.0000)
    points = fields.IntField(default=0)
    tax_class_id = fields.IntField()
    date_available = fields.DateField(default='0000-00-00')
    weight = fields.DecimalField(max_digits=15, decimal_places=8, default=0.00000000)
    weight_class_id = fields.IntField(default=0)
    lenght = fields.DecimalField(max_digits=15, decimal_places=8, default=0.00000000)
    width = fields.DecimalField(max_digits=15, decimal_places=8, default=0.00000000)
    height = fields.DecimalField(max_digits=15, decimal_places=8, default=0.00000000)
    lenght_class_id = fields.IntField(default=0)
    substract = fields.SmallIntField(default=1)
    minimum = fields.IntField(default=1)
    sort_order = fields.IntField(default=0)
    status = fields.SmallIntField(default=1)
    viewed = fields.IntField(default=0)
    date_added = fields.DatetimeField(auto_now_add=True)
    date_modified = fields.DatetimeField(auto_now=True)

    class Meta:
        table = f"{database_prefix}product"
        ordering = ["product_id"]

class OC_Product_Attribute(OC_ProductBaseModel):
    product_id = fields.IntField(pk=True, unique=False)
    attribute_id = fields.IntField(pk=True)
    language_id = fields.IntField(pk=True)
    text = fields.TextField()

    class Meta:
        table = f"{database_prefix}product_attribute"
        ordering = ["product_id"]

class OC_Product_Description(OC_ProductBaseModel):
    language_id = fields.IntField(pk=True, default=1)
    name = fields.CharField(max_length=255)
    description = fields.TextField()
    tag = fields.TextField()
    meta_title = fields.CharField(max_length=255)
    meta_description = fields.CharField(max_length=255)
    meta_keyword = fields.CharField(max_length=255)

    class Meta:
        table = f"{database_prefix}product_description"
        ordering = ["product_id"]
        indexes = [
            Index(fields={"name"}, name="name")
        ]


class OC_Product_Filter(OC_ProductBaseModel):
    filter_id = fields.IntField(pk=True)

    class Meta:
        table = f"{database_prefix}product_filter"
        ordering = ["product_id"]

class OC_Product_Image(OC_ProductBaseModel):
    product_image_id = fields.IntField(pk=True)
    image = fields.CharField(max_length=255, null=True)
    sort_order = fields.IntField()

    class Meta:
        table = f"{database_prefix}product_image"
        ordering = ["product_id"]
        indexes = [
            Index(fields={"product_id"}, name="product_id")
        ]

class OC_Product_To_Category(OC_ProductBaseModel):
    category_id = fields.IntField(pk=True)

    class Meta:
        table = f"{database_prefix}product_to_category"
        ordering = ["product_id"]
        indexes = [
            Index(fields={"category_id"}, name="category_id")
        ]

class OC_Product_To_Download(OC_ProductBaseModel):
    download_id = fields.IntField(pk=True)

    class Meta:
        table = f"{database_prefix}product_to_download"
        ordering = ["product_id"]

class OC_Product_To_Store(OC_ProductBaseModel):
    store_id = fields.IntField(default=0, pk=True)

    class Meta:
        table = f"{database_prefix}product_to_store"
        ordering = ["product_id"]