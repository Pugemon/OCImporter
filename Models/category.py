from sqlalchemy import Column, Index
from sqlalchemy.dialects.mysql import DATETIME, TINYINT, TEXT, INTEGER, VARCHAR

from Models import Base


class _CategoryBase(Base):
    __abstract__ = True
    __tablename__ = 'category'


class Category(_CategoryBase):
    __tablename__ = _CategoryBase.__tablename__

    category_id = Column(INTEGER(11), primary_key=True)
    image = Column(VARCHAR(255), default=None)
    parent_id = Column(INTEGER(11), nullable=False, default=0)
    top = Column(TINYINT(1), nullable=False)
    column = Column(INTEGER(3), nullable=False)
    sort_order = Column(INTEGER(3), nullable=False, default=0)
    status = Column(TINYINT(1), nullable=False, default=0)
    date_added = Column(DATETIME, nullable=False)
    date_modified = Column(DATETIME, nullable=False)

    __table_args__ = Index('parent_id', 'parent_id')


class CategoryDescription(_CategoryBase):
    __tablename__ = _CategoryBase.__tablename__ + '_description'

    category_id = Column(INTEGER(11), primary_key=True, autoincrement=False)
    language_id = Column(INTEGER(11), primary_key=True, autoincrement=False)
    name = Column(VARCHAR(255), nullable=False)
    description = Column(TEXT, nullable=False)
    meta_title = Column(VARCHAR(255), nullable=False)
    meta_description = Column(VARCHAR(255), nullable=False)
    meta_keyword = Column(VARCHAR(255), nullable=False)

    __table_args__ = Index('name', 'name')


class CategoryFilter(_CategoryBase):
    __tablename__ = _CategoryBase.__tablename__ + '_filter'

    category_id = Column(INTEGER(11), primary_key=True, autoincrement=False)
    filter_id = Column(INTEGER(11), primary_key=True, autoincrement=False)


class CategoryPath(_CategoryBase):
    __tablename__ = _CategoryBase.__tablename__ + '_path'

    category_id = Column(INTEGER(11), primary_key=True, autoincrement=False)
    path_id = Column(INTEGER(11), primary_key=True, autoincrement=False)
    level = Column(INTEGER(11), nullable=False)


class CategoryToLayout(_CategoryBase):
    __tablename__ = _CategoryBase.__tablename__ + '_to_layout'

    category_id = Column(INTEGER(11), primary_key=True, autoincrement=False)
    store_id = Column(INTEGER(11), primary_key=True, autoincrement=False)
    layout_id = Column(INTEGER(11), nullable=False)


class CategoryToStore(_CategoryBase):
    __tablename__ = _CategoryBase.__tablename__ + '_to_store'

    category_id = Column(INTEGER(11), primary_key=True, autoincrement=False)
    store_id = Column(INTEGER(11), primary_key=True, autoincrement=False)
