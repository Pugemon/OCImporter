import Exceptions
from main import logger
from dynaconf import Dynaconf
from tortoise.exceptions import ConfigurationError

settings = Dynaconf(
    enviroments=True,
    envvar_prefix="DYNACONF",
    default_env="global",
    env="development",
    settings_files=['settings.toml', '.secrets.toml'],
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.

engine = settings.get("db.engine")
timezone = settings.get("db.timezone")
host = settings.get("db.host")
port = settings.get("db.port")
user = settings.get("db.user")
password = settings.get("db.password")
database = settings.get("db.database")

try:
    Exceptions.check_config_for_null(engine, timezone, host, port, user, password, database)
    Exceptions.check_config_database_engine(engine)
except ValueError as e:
    logger.error(f"Database configuration error: {e}")
except ConfigurationError as e:
    logger.error(f"Database configuration error: {e}")

if Exceptions.check_config_database_engine(engine):
    engine = "asyncmy"

tortoise_db_config = {
    'connections': {
        'default': {
            'engine': f'tortoise.backends.{engine}',
            'credentials': {
                'database': f'{database}',
                'host': f'{host}',
                'password': f'{password}',
                'port': f'{port}',
                'user': f'{user}',
            }
        }
    },
    'apps': {
        'oc_importer': {
            'models': {
                'models': ['Models.product', 'Models.manufacturer', 'Models.category', 'Models.attributes'],
                'default_connection': "default",
            },
        },
        'use_tz': False,
        'timezone': f'{timezone}',
    },
}
