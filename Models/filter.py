from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR

from Models import Base


class _FilterBase(Base):
    __abstract__ = True
    __tablename__ = 'filter'


class Filter(_FilterBase):
    __tablename__ = _FilterBase.__tablename__

    filter_id = Column(INTEGER(11), primary_key=True)
    filter_group_id = Column(INTEGER(11), nullable=False)
    sort_order = Column(INTEGER(3), nullable=False)


class FilterDescription(_FilterBase):
    __tablename__ = _FilterBase.__tablename__ + '_description'

    filter_id = Column(INTEGER(11), primary_key=True)
    language_id = Column(INTEGER(11), primary_key=True)
    filter_group_id = Column(INTEGER(11), nullable=False)
    name = Column(VARCHAR(64), nullable=False)


class FilterGroup(_FilterBase):
    __tablename__ = _FilterBase.__tablename__ + '_group'

    filter_group_id = Column(INTEGER(11), primary_key=True)
    sort_order = Column(INTEGER(3), nullable=False)


class FilterGroupDescription(_FilterBase):
    __tablename__ = _FilterBase.__tablename__ + '_group_description'

    filter_group_id = Column(INTEGER(11), primary_key=True)
    language_id = Column(INTEGER(11), primary_key=True)
    name = Column(VARCHAR(64), nullable=False)
