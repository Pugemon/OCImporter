from tortoise import fields
from tortoise.models import Model

from config import settings

database_prefix = settings.get("oc.database_prefix")

class OC_ManufacturerBaseModel(Model):
    manufacturer_id = fields.IntField(pk=True)

class OC_Manufacturer(OC_ManufacturerBaseModel):
    image = fields.CharField(max_length=255)
    sort_order = fields.IntField(default=0)

    class Meta:
        table = f"{database_prefix}manufacturer"
        ordering = ["manufacturer_id"]

class OC_Manufacturer_to_store(OC_ManufacturerBaseModel):
    store_id = fields.IntField(default=0)

    class Meta:
        table = f"{database_prefix}manufacturer_to_store"
        ordering = ["manufacturer_id"]