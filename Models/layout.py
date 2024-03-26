from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR

from Models import Base


class _LayoutBase(Base):
    __abstract__ = True
    __tablename__ = 'layout'


class Layout(_LayoutBase):
    __tablename__ = _LayoutBase.__tablename__

    layout_id = Column(INTEGER(11), primary_key=True)
    name = Column(VARCHAR(64), nullable=False)


class LayoutModule(_LayoutBase):
    __tablename__ = _LayoutBase.__tablename__ + '_module'

    layout_module_id = Column(INTEGER(11), primary_key=True)
    layout_id = Column(INTEGER(11), nullable=False)
    code = Column(VARCHAR(64), nullable=False)
    position = Column(VARCHAR(14), nullable=False)
    sort_order = Column(INTEGER(3), nullable=False)


class LayoutRoute(_LayoutBase):
    __tablename__ = _LayoutBase.__tablename__ + '_route'

    layout_route_id = Column(INTEGER(11), primary_key=True)
    layout_id = Column(INTEGER(11), nullable=False)
    store_id = Column(INTEGER(11), nullable=False)
    route = Column(VARCHAR(64), nullable=False)
