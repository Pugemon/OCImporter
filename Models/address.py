from Models import Base
from sqlalchemy import Column, Index
from sqlalchemy.dialects.mysql import TINYINT, TEXT, INTEGER, VARCHAR


class AddressBase(Base):
    __abstract__ = True
    __tablename__ = 'address'


class Address(AddressBase):
    __tablename__ = AddressBase.__tablename__

    address_id = Column(INTEGER(11), primary_key=True)
    customer_id = Column(INTEGER(11), nullable=False)
    firstname = Column(VARCHAR(32), nullable=False)
    lastname = Column(VARCHAR(32), nullable=False)
    company = Column(VARCHAR(40), nullable=False)
    address_1 = Column(VARCHAR(128), nullable=False)
    address_2 = Column(VARCHAR(128), nullable=False)
    city = Column(VARCHAR(128), nullable=False)
    postcode = Column(VARCHAR(10), nullable=False)
    country_id = Column(INTEGER(11), nullable=False, default=0)
    zone_id = Column(INTEGER(11), nullable=False, default=0)
    custom_field = Column(TEXT, nullable=False)
    default = Column(TINYINT(1), nullable=False)

    __table_args__ = (
        Index('customer_id', 'customer_id'),
        {'mysql_engine': 'MyISAM', 'mysql_default_charset': 'utf8mb4', 'mysql_collate': 'utf8mb4_general_ci'}
    )


class AddressFormat(AddressBase):
    __tablename__ = AddressBase.__tablename__ + '_format'

    address_format_id = Column(INTEGER(11), primary_key=True)
    name = Column(VARCHAR(128), nullable=False)
    address_format = Column(TEXT, nullable=False)
