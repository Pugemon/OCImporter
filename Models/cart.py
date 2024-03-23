from Models import Base
from sqlalchemy import Column, Index
from sqlalchemy.dialects.mysql import DATETIME, DECIMAL, TINYINT, TEXT, INTEGER, VARCHAR


class Cart(Base):
    __tablename__ = 'cart'

    cart_id = Column(INTEGER(11, unsigned=True), primary_key=True)
    api_id = Column(INTEGER(11), nullable=False)
    customer_id = Column(INTEGER(11), nullable=False)
    session_id = Column(VARCHAR(32), nullable=False)
    product_id = Column(INTEGER(11), nullable=False)
    subscription_plan_id = Column(INTEGER(11), nullable=False)
    option = Column(TEXT, nullable=False)
    quantity = Column(INTEGER(5), nullable=False)
    override = Column(TINYINT(1), nullable=False)
    price = Column(DECIMAL(15, 4), nullable=False)
    date_added = Column(DATETIME, nullable=False)

    __table_args__ = (
        Index('cart_id', 'api_id', 'customer_id', 'session_id', 'product_id', 'subscription_plan_id'),
        {'mysql_engine': 'MyISAM', 'mysql_default_charset': 'utf8mb4', 'mysql_collate': 'utf8mb4_general_ci'}
    )
