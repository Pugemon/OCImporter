from sqlalchemy import Column, Index, UniqueConstraint
from sqlalchemy.dialects.mysql import ENUM, DATE, DECIMAL, TINYINT, TEXT, INTEGER, VARCHAR

from Models import Base


class _GoogleShoppingBase(Base):
    __abstract__ = True
    __tablename__ = 'googleshopping'
    __table_args__ = {
        'mysql_default_charset': 'utf8',
    }


class GoogleShoppingCategory(_GoogleShoppingBase):
    __tablename__ = _GoogleShoppingBase.__tablename__ + '_category'

    google_product_category = Column(VARCHAR(10), primary_key=True)
    store_id = Column(INTEGER(11), primary_key=True, default=0)
    category_id = Column(INTEGER(11), nullable=False)

    __table_args__ = Index('category_id_store_id', 'category_id', 'store_id')


class GoogleShoppingProduct(_GoogleShoppingBase):
    __tablename__ = _GoogleShoppingBase.__tablename__ + '_product'

    product_advertise_google_id = Column(INTEGER(11, unsigned=True), primary_key=True)
    product_id = Column(INTEGER(11), nullable=True, default=None)
    store_id = Column(INTEGER(11), nullable=False, default=0)
    has_issues = Column(TINYINT(1), nullable=True, default=None)
    destination_status = Column(ENUM('pending', 'approved', 'disapproved'), nullable=False, default='pending')
    impressions = Column(INTEGER(11), nullable=False, default=0)
    clicks = Column(INTEGER(11), nullable=False, default=0)
    conversions = Column(INTEGER(11), nullable=False, default=0)
    cost = Column(DECIMAL(15, 4), nullable=False, default=0.0000)
    conversion_value = Column(DECIMAL(15, 4), nullable=False, default=0.0000)
    google_product_category = Column(VARCHAR(10), nullable=True, default=None)
    condition = Column(ENUM('new', 'refurbished', 'used'), nullable=True)
    adult = Column(TINYINT(1), nullable=True, default=None)
    multipack = Column(INTEGER(11), nullable=True, default=None)
    is_bundle = Column(TINYINT(1), nullable=True, default=None)
    age_group = Column(ENUM('newborn', 'infant', 'toddler', 'kids', 'adult'), nullable=True)
    color = Column(INTEGER(11), nullable=True, default=None)
    gender = Column(ENUM('male', 'female', 'unisex'), nullable=True, default=None)
    size_type = Column(ENUM('regular', 'petite', 'plus', 'big and tall', 'maternity'), nullable=True, default=None)
    size_system = Column(ENUM('AU', 'BR', 'CN', 'DE', 'EU', 'FR', 'IT', 'JP', 'MEX', 'UK', 'US'), nullable=True,
                         default=None)
    size = Column(INTEGER(11), nullable=True, default=None)
    is_modified = Column(TINYINT(1), nullable=False, default=0)

    __table_args__ = UniqueConstraint('product_id', 'store_id', name='product_id_store_id')


class GoogleShoppingProductStatus(_GoogleShoppingBase):
    __tablename__ = _GoogleShoppingBase.__tablename__ + '_product_status'

    product_id = Column(INTEGER(11), primary_key=True, default=0)
    store_id = Column(INTEGER(11), primary_key=True, default=0)
    product_variation_id = Column(VARCHAR(64), primary_key=True, default='')
    destination_statuses = Column(TEXT, nullable=False)
    data_quality_issues = Column(TEXT, nullable=False)
    item_level_issues = Column(TEXT, nullable=False)
    google_expiration_date = Column(INTEGER(11), nullable=False, default=0)


class GoogleShoppingProductTarget(_GoogleShoppingBase):
    __tablename__ = _GoogleShoppingBase + '_product_target'

    product_id = Column(INTEGER(11), primary_key=True)
    store_id = Column(INTEGER(11), default=0)
    advertise_google_target_id = Column(INTEGER(11, unsigned=True), primary_key=True, autoincrement=False)


class GoogleShoppingTarget(_GoogleShoppingBase):
    __tablename__ = _GoogleShoppingBase + '_target'

    advertise_google_target_id = Column(INTEGER(11, unsigned=True), primary_key=True, autoincrement=True)
    store_id = Column(INTEGER(11), nullable=False, default=0)
    campaign_name = Column(VARCHAR(255), nullable=False, default='')
    country = Column(VARCHAR(2), nullable=False, default='')
    budget = Column(DECIMAL(15, 4), nullable=False, default=0.0000)
    feeds = Column(TEXT, nullable=False)
    status = Column(ENUM('paused', 'active'), nullable=False, default='paused')
    date_added = Column(DATE)
    roas = Column(INTEGER(11), nullable=False, default=0)
