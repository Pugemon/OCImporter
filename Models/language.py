from sqlalchemy import Column, Index
from sqlalchemy.dialects.mysql import TINYINT, INTEGER, VARCHAR

from Models import Base


class _LanguageBase(Base):
    __abstract__ = True
    __tablename__ = 'language'


class Language(_LanguageBase):
    __tablename__ = _LanguageBase.__tablename__

    language_id = Column(INTEGER(11), primary_key=True)
    name = Column(VARCHAR(32), nullable=False)
    code = Column(VARCHAR(5), nullable=False)
    locale = Column(VARCHAR(255), nullable=False)
    image = Column(VARCHAR(64), nullable=False)
    directory = Column(VARCHAR(32), nullable=False)
    sort_order = Column(INTEGER(3), nullable=False, default=0)
    status = Column(TINYINT(1), nullable=False)

    __table_args__ = (
        Index('name', 'name'),
    )
