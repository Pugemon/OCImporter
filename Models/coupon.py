from sqlalchemy import Column
from sqlalchemy.dialects.mysql import DATE, CHAR, DATETIME, DECIMAL, TINYINT, INTEGER, VARCHAR

from Models import Base


class _CouponBase(Base):
    __abstract__ = True
    __tablename__ = 'coupon'


class Coupon(_CouponBase):
    __tablename__ = _CouponBase.__tablename__

    coupon_id = Column(INTEGER(11), primary_key=True)
    name = Column(VARCHAR(128), nullable=False)
    code = Column(VARCHAR(20), nullable=False)
    type = Column(CHAR(1), nullable=False)
    discount = Column(DECIMAL(15, 4), nullable=False)
    logged = Column(TINYINT(1), nullable=False)
    shipping = Column(TINYINT(1), nullable=False)
    total = Column(DECIMAL(15, 4), nullable=False)
    date_start = Column(DATE, nullable=False, default='0000-00-00')
    date_end = Column(DATE, nullable=False, default='0000-00-00')
    uses_total = Column(INTEGER(11), nullable=False)
    uses_customer = Column(INTEGER(11), nullable=False)
    status = Column(TINYINT(1), nullable=False)
    date_added = Column(DATETIME, nullable=False)


class CouponCategory(_CouponBase):
    __tablename__ = _CouponBase.__tablename__ + '_category'

    coupon_id = Column(INTEGER(11), primary_key=True, autoincrement=False)
    category_id = Column(INTEGER(11), primary_key=True, autoincrement=False)


class CouponHistory(_CouponBase):
    __tablename__ = _CouponBase.__tablename__ + '_history'

    coupon_history_id = Column(INTEGER(11), primary_key=True)
    coupon_id = Column(INTEGER(11), nullable=False)
    product_id = Column(INTEGER(11), nullable=False)
