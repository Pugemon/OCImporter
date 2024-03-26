from sqlalchemy import Column
from sqlalchemy.dialects.mysql import TINYINT, INTEGER, VARCHAR

from Models import Base


class _CountryBase(Base):
    __abstract__ = True
    __tablename__ = 'country'


class Country(_CountryBase):
    __tablename__ = _CountryBase.__tablename__

    country_id = Column(INTEGER(11), primary_key=True)
    name = Column(VARCHAR(128), nullable=False)
    iso_code_2 = Column(VARCHAR(2), nullable=False)
    iso_code_3 = Column(VARCHAR(3), nullable=False)
    address_format_id = Column(INTEGER(11), nullable=False)
    postcode_required = Column(TINYINT(1), nullable=False)
    status = Column(TINYINT(1), nullable=False, default=1)
