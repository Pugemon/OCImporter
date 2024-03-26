from sqlalchemy import Column
from sqlalchemy.dialects.mysql import DATETIME, TINYINT, INTEGER, VARCHAR

from Models import Base


class _GdprBase(Base):
    __abstract__ = True
    __tablename__ = 'gdpr'


class Gdpr(_GdprBase):
    __tablename__ = _GdprBase.__tablename__

    gdpr_id = Column(INTEGER(11), primary_key=True)
    store_id = Column(INTEGER(11), nullable=False)
    language_id = Column(INTEGER(11), nullable=False)
    code = Column(VARCHAR(40), nullable=False)
    email = Column(VARCHAR(96), nullable=False)
    action = Column(VARCHAR(6), nullable=False)
    status = Column(TINYINT(1), nullable=False)
    date_added = Column(DATETIME, nullable=False)
