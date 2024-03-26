from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR

from Models import Base


class _AttributeBase(Base):
    __abstract__ = True
    __tablename__ = 'attribute'


class Attribute(_AttributeBase):
    __tablename__ = _AttributeBase.__tablename__

    attribute_id = Column(INTEGER(11), primary_key=True)
    attribute_group_id = Column(INTEGER(11), nullable=False)
    sort_order = Column(INTEGER(3), nullable=False)


class AttributeDescription(_AttributeBase):
    __tablename__ = _AttributeBase.__tablename__ + '_description'

    attribute_id = Column(INTEGER(11), primary_key=True, autoincrement=False)
    language_id = Column(INTEGER(11), primary_key=True, autoincrement=False)
    name = Column(VARCHAR(64), nullable=False)


class AttributeGroup(_AttributeBase):
    __tablename__ = _AttributeBase.__tablename__ + '_group'

    attribute_group_id = Column(INTEGER(11), primary_key=True)
    sort_order = Column(INTEGER(3), nullable=False)


class AttributeGroupDescription(_AttributeBase):
    __tablename__ = AttributeGroup.__tablename__ + '_description'

    attribute_group_id = Column(INTEGER(11), primary_key=True, autoincrement=False)
    language_id = Column(INTEGER(11), primary_key=True, autoincrement=False)
    name = Column(VARCHAR(64), nullable=False)
