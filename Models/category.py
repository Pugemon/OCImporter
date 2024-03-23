from Models import Base
from sqlalchemy import Column, Index
from sqlalchemy.dialects.mysql import DATETIME, DECIMAL, TINYINT, TEXT, INTEGER, VARCHAR


class CategoryBase(Base):
    __abstract__ = True
    __tablename__ = 'category'


class Category(CategoryBase):
    __tablename__ = CategoryBase.__tablename__

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


class CategoryDescription(CategoryBase):
    __tablename__ = CategoryBase.__tablename__ + '_description'

    category_id = Column(INTEGER(11), primary_key=True, autoincrement=False)
    language_id = Column(INTEGER(11), primary_key=True, autoincrement=False)
    name = Column(VARCHAR(255), nullable=False)
    description = Column(TEXT, nullable=False)
    meta_title = Column(VARCHAR(255), nullable=False)
    meta_description = Column(VARCHAR(255), nullable=False)
    meta_keyword = Column(VARCHAR(255), nullable=False)

    __table_args__ = Index('name', 'name')
