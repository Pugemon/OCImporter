from tortoise import fields
from tortoise.models import Model
from config import settings

database_prefix = settings.get("oc.database_prefix")

class OC_ProductBaseModel(Model):
    product_id = fields.IntField(pk=True, unique=True)

class OC_Product(OC_ProductBaseModel):
    #TODO заполнить соответственно требованиям дб
    model = fields.CharField(max_length=64)
    sku = fields.CharField(max_length=64)
    location = fields.CharField(max_length=128)
    quantity = fields.IntField()
    stock_status_id = fields.IntField()
    image = fields.CharField(max_length=255)
    manufacturer_id = fields.IntField()
    shipping = fields.SmallIntField()
    price = fields.DecimalField(max_digits=15, decimal_places=4)
    points = fields.IntField()
    tax_class_id = fields.IntField()
    date_available = fields.DateField()
    weight = fields.DecimalField(max_digits=15, decimal_places=8)
    weight_class_id = fields.IntField()
    lenght = fields.DecimalField(max_digits=15, decimal_places=8)
    width = fields.DecimalField(max_digits=15, decimal_places=8)
    height = fields.DecimalField(max_digits=15, decimal_places=8)
    lenght_class_id = fields.IntField(default=1)
    substract = fields.SmallIntField(default=1)
    minimum = fields.IntField(default=1)
    sort_order = fields.IntField(default=0)
    status = fields.SmallIntField(default=1)
    viewed = fields.IntField()
    date_added = fields.DatetimeField(auto_now_add=True)
    date_modified = fields.DatetimeField(auto_now=True)

    class Meta:
        table = f"{database_prefix}product"
        ordering = ["manufacturer_id"]

class OC_Product_Attribute(OC_ProductBaseModel):
    #TODO указать pk
    product_attribute_id = fields.IntField()
    attribute_id = fields.IntField()
    language_id = fields.IntField()
    text = fields.TextField()

    class Meta:
        #TODO Заполнить мету, и указать ordering
        table = f"{database_prefix}product_attribute"
        ordering = [""]

class OC_Product_Description(OC_ProductBaseModel):
    #TODO заполнить соответственно требованиям дб
    language_id = fields.IntField()
    name = fields.CharField()
    description = fields.TextField()
    tag = fields.TextField()
    meta_title = fields.CharField()
    meta_description = fields.CharField()
    meta_keyword = fields.CharField()

    class Meta:
        #TODO указать ordering
        table = f"{database_prefix}product_description"
        ordering = [""]

class OC_Product_Filter(OC_ProductBaseModel):
    #TODO указать pk
    filter_id = fields.IntField()

    class Meta:
        #TODO указать ordering
        table = f"{database_prefix}product_filter"
        ordering = [""]
class OC_Product_Image(OC_ProductBaseModel):
    #TODO указать требования дб
    product_image_id = fields.IntField()
    image = fields.CharField()
    sort_order = fields.IntField()

    class Meta:
        #TODO указать ordering
        table = f"{database_prefix}product_image"
        ordering = [""]

class OC_Product_To_Category(OC_ProductBaseModel):
    #TODO указать pk
    category_id = fields.IntField()

    class Meta:
        #TODO указать ordering
        table = f"{database_prefix}product_to_category"
        ordering = [""]

class OC_Product_To_Download(OC_ProductBaseModel):
    download_id = fields.IntField()

    class Meta:
        #TODO указать ordering
        table = f"{database_prefix}product_to_download"
        ordering = [""]

class OC_Product_To_Store(OC_ProductBaseModel):
    store_id = fields.IntField(default=0)

    class Meta:
        table = f"{database_prefix}product_to_store"
        ordering = ["product_id"]