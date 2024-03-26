from sqlalchemy import Column
from sqlalchemy.dialects.mysql import MEDIUMTEXT, TINYINT, INTEGER, VARCHAR

from Models import Base


class _InformationBase(Base):
    __abstract__ = True
    __tablename__ = 'information'


class Information(_InformationBase):
    __tablename__ = _InformationBase.__tablename__

    information_id = Column(INTEGER(11), primary_key=True)
    bottom = Column(INTEGER(1), nullable=False, default=0)
    sort_order = Column(INTEGER(3), nullable=False, default=0)
    status = Column(TINYINT(1), nullable=False, default=1)


class InformationDescription(_InformationBase):
    __tablename__ = _InformationBase.__tablename__ + '_description'

    information_id = Column(INTEGER(11), primary_key=True)
    language_id = Column(INTEGER(11), primary_key=True)
    title = Column(VARCHAR(64), nullable=False)
    description = Column(MEDIUMTEXT, nullable=False)
    meta_title = Column(VARCHAR(255), nullable=False)
    meta_description = Column(VARCHAR(255), nullable=False)
    meta_keyword = Column(VARCHAR(255), nullable=False)


class InformationToLayout(_InformationBase):
    __tablename__ = _InformationBase.__tablename__ + '_to_layout'

    information_id = Column(INTEGER(11), primary_key=True)
    store_id = Column(INTEGER(11), primary_key=True)
    layout_id = Column(INTEGER(11), nullable=False)


class InformationToStore(_InformationBase):
    __tablename__ = _InformationBase.__tablename__ + '_to_store'

    information_id = Column(INTEGER(11), primary_key=True)
    store_id = Column(INTEGER(11), primary_key=True)
