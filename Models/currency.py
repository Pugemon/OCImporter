from sqlalchemy import Column
from sqlalchemy.dialects.mysql import DOUBLE, CHAR, DATETIME, TINYINT, INTEGER, VARCHAR

from Models import Base


class _CurrencyBase(Base):
    __abstract__ = True
    __tablename__ = 'currency'


class Currency(_CurrencyBase):
    __tablename__ = _CurrencyBase.__tablename__

    currency_id = Column(INTEGER(11), primary_key=True)
    title = Column(VARCHAR(32), nullable=False)
    code = Column(VARCHAR(3), nullable=False)
    symbol_left = Column(VARCHAR(12), nullable=False)
    symbol_right = Column(VARCHAR(12), nullable=False)
    decimal_place = Column(CHAR(1), nullable=False)
    value = Column(DOUBLE(15, 8), nullable=False)
    status = Column(TINYINT(1), nullable=False)
    date_modified = Column(DATETIME, nullable=False)
