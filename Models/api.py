from sqlalchemy import Column
from sqlalchemy.dialects.mysql import DATETIME, TINYINT, TEXT, INTEGER, VARCHAR

from Models import Base


class _ApiBase(Base):
    __abstract__ = True
    __tablename__ = 'api'


class Api(_ApiBase):
    __tablename__ = _ApiBase.__tablename__

    api_id = Column(INTEGER(11), primary_key=True)
    username = Column(VARCHAR(64), nullable=False)
    key = Column(TEXT, nullable=False)
    status = Column(TINYINT(1), nullable=False)
    date_added = Column(DATETIME, nullable=False)
    date_modified = Column(DATETIME, nullable=False)


class ApiIp(_ApiBase):
    __tablename__ = _ApiBase.__tablename__ + '_ip'

    api_ip_id = Column(INTEGER(11), primary_key=True)
    api_id = Column(INTEGER(11), nullable=False)
    ip = Column(VARCHAR(40), nullable=False)


class ApiSession(_ApiBase):
    __tablename__ = _ApiBase.__tablename__ + '_session'

    api_session_id = Column(INTEGER(11), primary_key=True)
    api_id = Column(INTEGER(11), nullable=False)
    session_id = Column(VARCHAR(32), nullable=False)
    ip = Column(VARCHAR(40), nullable=False)
    date_added = Column(DATETIME, nullable=False)
    date_modified = Column(DATETIME, nullable=False)
