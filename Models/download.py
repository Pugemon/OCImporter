from sqlalchemy import Column
from sqlalchemy.dialects.mysql import DATETIME, INTEGER, VARCHAR

from Models import Base


class _DownloadBase(Base):
    __abstract__ = True
    __tablename__ = 'download'


class Download(_DownloadBase):
    __tablename__ = _DownloadBase.__tablename__

    download_id = Column(INTEGER(11), primary_key=True)
    filename = Column(VARCHAR(160), nullable=False)
    mask = Column(VARCHAR(128), nullable=False)
    date_added = Column(DATETIME, nullable=False)


class DownloadDescription(_DownloadBase):
    __tablename__ = _DownloadBase.__tablename__ + '_description'

    download_id = Column(INTEGER(11), primary_key=True)
    language_id = Column(INTEGER(11), primary_key=True)
    name = Column(VARCHAR(64), nullable=False)
