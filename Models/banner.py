from sqlalchemy import Column
from sqlalchemy.dialects.mysql import TINYINT, INTEGER, VARCHAR

from Models import Base


class _BannerBase(Base):
    __abstract__ = True
    __tablename__ = 'banner'


class Banner(_BannerBase):
    __tablename__ = _BannerBase.__tablename__

    banner_id = Column(INTEGER(11), primary_key=True)
    name = Column(VARCHAR(64), nullable=False)
    status = Column(TINYINT(1), nullable=False)


class BannerImage(_BannerBase):
    __tablename__ = _BannerBase.__tablename__ + '_image'

    banner_image_id = Column(INTEGER(11), primary_key=True)
    banner_id = Column(INTEGER(11), nullable=False)
    language_id = Column(INTEGER(11), nullable=False)
    title = Column(VARCHAR(64), nullable=False)
    link = Column(VARCHAR(255), nullable=False)
    image = Column(VARCHAR(255), nullable=False)
    sort_order = Column(INTEGER(3), nullable=False, default=0)
