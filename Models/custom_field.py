from sqlalchemy import Column
from sqlalchemy.dialects.mysql import TINYINT, TEXT, INTEGER, VARCHAR

from Models import Base


class _CustomFieldBase(Base):
    __abstract__ = True
    __tablename__ = 'custom_field'


class CustomField(_CustomFieldBase):
    __tablename__ = _CustomFieldBase.__tablename__

    custom_field_id = Column(INTEGER(11), primary_key=True)
    type = Column(VARCHAR(32), nullable=False)
    value = Column(TEXT, nullable=False)
    validation = Column(VARCHAR(255), nullable=False)
    location = Column(VARCHAR(10), nullable=False)
    status = Column(TINYINT(1), nullable=False)
    sort_order = Column(INTEGER(3), nullable=False)


class CustomFieldCustomerGroup(_CustomFieldBase):
    __tablename__ = _CustomFieldBase.__tablename__ + '_customer_group'

    custom_field_id = Column(INTEGER(11), primary_key=True, autoincrement=False)
    customer_group_id = Column(INTEGER(11), primary_key=True, autoincrement=False)
    required = Column(TINYINT(1), nullable=False)


class CustomFieldDescription(_CustomFieldBase):
    __tablename__ = _CustomFieldBase.__tablename__ + '_description'

    custom_field_id = Column(INTEGER(11), primary_key=True)
    language_id = Column(INTEGER(11), primary_key=True)
    name = Column(VARCHAR(128), nullable=False)


class CustomFieldValue(_CustomFieldBase):
    __tablename__ = _CustomFieldBase.__tablename__ + '_value'

    custom_field_value_id = Column(INTEGER(11), primary_key=True)
    custom_field_id = Column(INTEGER(11), nullable=False)
    sort_order = Column(INTEGER(3), nullable=False)


class CustomFieldValueDescription(_CustomFieldBase):
    __tablename__ = _CustomFieldBase.__tablename__ + '_value_description'

    custom_field_value_id = Column(INTEGER(11), primary_key=True)
    language_id = Column(INTEGER(11), primary_key=True)
    custom_field_id = Column(INTEGER(11), nullable=False)
    name = Column(VARCHAR(128), nullable=False)
