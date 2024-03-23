from typing import Any

from config import settings

from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta

oc_database_prefix = settings.get("oc.database_prefix")


class PrefixerMeta(DeclarativeMeta):

    def __init__(cls, name, bases, dict_, classname: Any, **kw: Any):
        super().__init__(classname, bases, dict_, **kw)
        if '__tablename__' in dict_:
            cls.__tablename__ = dict_['__tablename__'] = \
                f'{oc_database_prefix}_' + dict_['__tablename__']


class Base(declarative_base(metaclass=PrefixerMeta)):
    __abstract__ = True
    __table_args__ = {
        'mysql_engine': 'MyISAM',
        'mysql_default_charset': 'utf8mb4',
        'mysql_collate': 'utf8mb4_general_ci'
    }
