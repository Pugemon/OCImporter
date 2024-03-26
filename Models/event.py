from sqlalchemy import Column
from sqlalchemy.dialects.mysql import TINYINT, TEXT, INTEGER, VARCHAR

from Models import Base


class _EventBase(Base):
    __abstract__ = True
    __tablename__ = 'event'


class Event(_EventBase):
    __tablename__ = _EventBase.__tablename__

    event_id = Column(INTEGER(11), primary_key=True)
    code = Column(VARCHAR(64), nullable=False)
    trigger = Column(TEXT, nullable=False)
    action = Column(TEXT, nullable=False)
    status = Column(TINYINT(1), nullable=False)
    sort_order = Column(INTEGER(3), nullable=False)
