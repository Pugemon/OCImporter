from tortoise import fields
from tortoise.contrib.mysql.indexes import Index
from tortoise.models import Model

from config import settings

database_prefix = settings.get("oc.database_prefix")


class OC_Product(Model):
    product_id = fields.IntField(pk=True, unique=True)
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
    date_available = fields.DateField(default='2020-01-01')
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
    date_added = fields.DatetimeField()
    date_modified = fields.DatetimeField()

    class Meta:
        table = f"{database_prefix}product"
        ordering = ["product_id"]


class OC_Product_Attribute(Model):
    product_id = fields.IntField(unique=False)
    attribute_id = fields.IntField()
    language_id = fields.IntField()
    text = fields.TextField()

    class Meta:
        table = f"{database_prefix}product_attribute"
        ordering = ["product_id"]
        unique_together = ("product_id", "attribute_id", "language_id")


class OC_Product_Description(Model):
    product_id = fields.IntField(pk=True, unique=True)
    language_id = fields.IntField(default=1, unique=True)
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
        unique_together = ("product_id", "language_id")


class OC_Product_Filter(Model):
    product_id = fields.IntField(pk=True, unique=True)
    filter_id = fields.IntField(unique=True)

    class Meta:
        table = f"{database_prefix}product_filter"
        ordering = ["product_id"]
        unique_together = ("product_id", "filter_id")


class OC_Product_Image(Model):
    product_image_id = fields.IntField(pk=True, unique=True)
    product_id = fields.IntField()
    image = fields.CharField(max_length=255, null=True)
    sort_order = fields.IntField()

    class Meta:
        table = f"{database_prefix}product_image"
        ordering = ["product_image_id"]
        indexes = [
            Index(fields={"product_id"}, name="product_id")
        ]
        unique_together = ("product_id", "product_image_id")


class OC_Product_To_Category(Model):
    product_id = fields.IntField(pk=True, unique=True)
    category_id = fields.IntField()

    class Meta:
        table = f"{database_prefix}product_to_category"
        ordering = ["product_id"]
        indexes = [
            Index(fields={"category_id"}, name="category_id")
        ]
        unique_together = ("product_id", "category_id")


class OC_Product_To_Download(Model):
    product_id = fields.IntField(pk=True, unique=True)
    download_id = fields.IntField(unique=True)

    class Meta:
        table = f"{database_prefix}product_to_download"
        ordering = ["product_id"]
        unique_together = ("product_id", "download_id")


class OC_Product_To_Store(Model):
    product_id = fields.IntField(pk=True, unique=True)
    store_id = fields.IntField(default=0, unique=True)

    class Meta:
        table = f"{database_prefix}product_to_store"
        ordering = ["product_id"]
        unique_together = ("product_id", "store_id")
