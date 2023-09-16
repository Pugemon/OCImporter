from tortoise import fields
from tortoise.models import Model
from config import settings

database_prefix = settings.get("oc.database_prefix")

class OC_Product(Model):
    product_id = fields.IntField(pk=True, unique=True)
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