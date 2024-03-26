from sqlalchemy import Column, Index
from sqlalchemy.dialects.mysql import DATETIME, DECIMAL, TINYINT, TEXT, INTEGER, VARCHAR

from Models import Base


class _CustomerBase(Base):
    __abstract__ = True
    __tablename__ = 'customer'


class Customer(_CustomerBase):
    __tablename__ = _CustomerBase.__tablename__

    customer_id = Column(INTEGER(11), primary_key=True)
    customer_group_id = Column(INTEGER(11), nullable=False)
    store_id = Column(INTEGER(11), nullable=False, default=0)
    language_id = Column(INTEGER(11), nullable=False)
    firstname = Column(VARCHAR(32), nullable=False)
    lastname = Column(VARCHAR(32), nullable=False)
    email = Column(VARCHAR(96), nullable=False)
    telephone = Column(VARCHAR(32), nullable=False)
    fax = Column(VARCHAR(32), nullable=False)
    password = Column(VARCHAR(255), nullable=False)
    cart = Column(TEXT)
    wishlist = Column(TEXT)
    newsletter = Column(TINYINT(1), nullable=False, default=0)
    address_id = Column(INTEGER(11), nullable=False, default=0)
    custom_field = Column(TEXT, nullable=False)
    ip = Column(VARCHAR(40), nullable=False)
    status = Column(TINYINT(1), nullable=False)
    safe = Column(TINYINT(1), nullable=False)
    token = Column(TEXT, nullable=False)
    code = Column(VARCHAR(40), nullable=False)
    date_added = Column(DATETIME, nullable=False)


class CustomerActivity(_CustomerBase):
    __tablename__ = _CustomerBase.__tablename__ + '_activity'

    customer_activity_id = Column(INTEGER(11), primary_key=True)
    customer_id = Column(INTEGER(11), nullable=False)
    key = Column(VARCHAR(64), nullable=False)
    data = Column(TEXT, nullable=False)
    ip = Column(VARCHAR(40), nullable=False)
    date_added = Column(DATETIME, nullable=False)


class CustomerAffiliate(_CustomerBase):
    __tablename__ = _CustomerBase.__tablename__ + '_affiliate'

    customer_id = Column(INTEGER(11), primary_key=True, autoincrement=False)
    company = Column(VARCHAR(60), nullable=False)
    website = Column(VARCHAR(255), nullable=False)
    tracking = Column(VARCHAR(64), nullable=False)
    commission = Column(DECIMAL(4, 2), nullable=False, default=0.00)
    tax = Column(VARCHAR(64), nullable=False)
    payment = Column(VARCHAR(6), nullable=False)
    cheque = Column(VARCHAR(100), nullable=False)
    paypal = Column(VARCHAR(64), nullable=False)
    bank_name = Column(VARCHAR(64), nullable=False)
    bank_branch_number = Column(VARCHAR(64), nullable=False)
    bank_swift_code = Column(VARCHAR(64), nullable=False)
    bank_account_name = Column(VARCHAR(64), nullable=False)
    bank_account_number = Column(VARCHAR(64), nullable=False)
    custom_field = Column(TEXT, nullable=False)
    status = Column(TINYINT(1), nullable=False)
    date_added = Column(DATETIME, nullable=False)


class CustomerAffiliateReport(_CustomerBase):
    __tablename__ = _CustomerBase.__tablename__ + '_affiliate_report'

    customer_affiliate_report_id = Column(INTEGER(11), primary_key=True, autoincrement=False)
    customer_id = Column(INTEGER(11), nullable=False)
    store_id = Column(INTEGER(11), nullable=False)
    ip = Column(VARCHAR(40), nullable=False)
    country = Column(VARCHAR(2), nullable=False)
    date_added = Column(DATETIME, nullable=False)


class CustomerApproval(_CustomerBase):
    __tablename__ = _CustomerBase.__tablename__ + '_approval'

    customer_approval_id = Column(INTEGER(11), primary_key=True)
    customer_id = Column(INTEGER(11), nullable=False)
    type = Column(VARCHAR(9), nullable=False)
    date_added = Column(DATETIME, nullable=False)


class CustomerGroup(_CustomerBase):
    __tablename__ = _CustomerBase.__tablename__ + '_group'

    customer_group_id = Column(INTEGER(11), primary_key=True)
    approval = Column(INTEGER(1), nullable=False)
    sort_order = Column(INTEGER(3), nullable=False)


class CustomerGroupDescription(_CustomerBase):
    __tablename__ = _CustomerBase.__tablename__ + '_group_description'

    customer_group_id = Column(INTEGER(11), primary_key=True)
    language_id = Column(INTEGER(11), primary_key=True)
    name = Column(VARCHAR(32), nullable=False)
    description = Column(TEXT, nullable=False)


class CustomerHistory(_CustomerBase):
    __tablename__ = _CustomerBase.__tablename__ + '_history'

    customer_history_id = Column(INTEGER(11), primary_key=True)
    customer_id = Column(INTEGER(11), nullable=False)
    comment = Column(TEXT, nullable=False)
    date_added = Column(DATETIME, nullable=False)


class CustomerIP(_CustomerBase):
    __tablename__ = _CustomerBase.__tablename__ + '_ip'

    customer_ip_id = Column(INTEGER(11), primary_key=True)
    customer_id = Column(INTEGER(11), nullable=False)
    store_id = Column(INTEGER(11), nullable=False)
    ip = Column(VARCHAR(40), nullable=False)
    country = Column(VARCHAR(2), nullable=False)
    date_added = Column(DATETIME, nullable=False)

    __table_args__ = (
        Index('ip', 'ip'),
    )


class CustomerLogin(_CustomerBase):
    __tablename__ = _CustomerBase.__tablename__ + '_login'

    customer_login_id = Column(INTEGER(11), primary_key=True)
    email = Column(VARCHAR(96), nullable=False)
    ip = Column(VARCHAR(40), nullable=False)
    total = Column(INTEGER(4), nullable=False)
    date_added = Column(DATETIME, nullable=False)
    date_modified = Column(DATETIME, nullable=False)

    __table_args__ = (
        Index('email', 'email'),
        Index('ip', 'ip'),
    )


class CustomerOnline(_CustomerBase):
    __tablename__ = _CustomerBase.__tablename__ + '_online'

    ip = Column(VARCHAR(40), primary_key=True)
    customer_id = Column(INTEGER(11), nullable=False)
    url = Column(TEXT, nullable=False)
    referer = Column(TEXT, nullable=False)
    date_added = Column(DATETIME, nullable=False)


class CustomerReward(_CustomerBase):
    __tablename__ = _CustomerBase.__tablename__ + '_reward'

    customer_reward_id = Column(INTEGER(11), primary_key=True)
    customer_id = Column(INTEGER(11), nullable=False, default=0)
    order_id = Column(INTEGER(11), nullable=False, default=0)
    description = Column(TEXT, nullable=False)
    points = Column(INTEGER(8), nullable=False, default=0)
    date_added = Column(DATETIME, nullable=False)


class CustomerSearch(_CustomerBase):
    __tablename__ = _CustomerBase.__tablename__ + '_search'

    customer_search_id = Column(INTEGER(11), primary_key=True)
    store_id = Column(INTEGER(11), nullable=False)
    language_id = Column(INTEGER(11), nullable=False)
    customer_id = Column(INTEGER(11), nullable=False)
    keyword = Column(VARCHAR(255), nullable=False)
    category_id = Column(INTEGER(11))
    sub_category = Column(TINYINT(1), nullable=False)
    description = Column(TINYINT(1), nullable=False)
    products = Column(INTEGER(11), nullable=False)
    ip = Column(VARCHAR(40), nullable=False)
    date_added = Column(DATETIME, nullable=False)


class CustomerTransaction(_CustomerBase):
    __tablename__ = _CustomerBase.__tablename__ + '_transaction'

    customer_transaction_id = Column(INTEGER(11), primary_key=True)
    customer_id = Column(INTEGER(11), nullable=False)
    order_id = Column(INTEGER(11), nullable=False)
    description = Column(TEXT, nullable=False)
    amount = Column(DECIMAL(15, 4), nullable=False)
    date_added = Column(DATETIME, nullable=False)


class CustomerWishlist(_CustomerBase):
    __tablename__ = _CustomerBase.__tablename__ + '_wishlist'

    customer_id = Column(INTEGER(11), primary_key=True, autoincrement=False)
    product_id = Column(INTEGER(11), primary_key=True, autoincrement=False)
    date_added = Column(DATETIME, nullable=False)
