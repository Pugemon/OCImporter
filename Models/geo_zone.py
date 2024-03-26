from sqlalchemy import Column
from sqlalchemy.dialects.mysql import DATETIME, INTEGER, VARCHAR

from Models import Base


class _GeoZoneBase(Base):
    __abstract__ = True
    __tablename__ = 'geo_zone'


class GeoZone(_GeoZoneBase):
    __tablename__ = _GeoZoneBase.__tablename__

    geo_zone_id = Column(INTEGER(11), primary_key=True)
    name = Column(VARCHAR(32), nullable=False)
    description = Column(VARCHAR(255), nullable=False)
    date_added = Column(DATETIME, nullable=False)
    date_modified = Column(DATETIME, nullable=False)
