from sqlalchemy import Column
from sqlalchemy.dialects.mysql import DATETIME, INTEGER, VARCHAR

from Models import Base


class _ExtensionBase(Base):
    __abstract__ = True
    __tablename__ = 'extension'


class Extension(_ExtensionBase):
    __tablename__ = _ExtensionBase.__tablename__

    extension_id = Column(INTEGER(11), primary_key=True)
    type = Column(VARCHAR(32), nullable=False)
    code = Column(VARCHAR(32), nullable=False)


class ExtensionInstall(_ExtensionBase):
    __tablename__ = _ExtensionBase.__tablename__ + '_install'

    extension_install_id = Column(INTEGER(11), primary_key=True)
    extension_download_id = Column(INTEGER(11), nullable=False)
    filename = Column(VARCHAR(255), nullable=False)
    date_added = Column(DATETIME, nullable=False)


class ExtensionPath(_ExtensionBase):
    __tablename__ = _ExtensionBase.__tablename__ + '_path'

    extension_path_id = Column(INTEGER(11), primary_key=True)
    extension_install_id = Column(INTEGER(11), nullable=False)
    path = Column(VARCHAR(255), nullable=False)
    date_added = Column(DATETIME, nullable=False)
