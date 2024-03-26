import logging
import sys

from dynaconf import Dynaconf
from loguru import logger
from tortoise.exceptions import ConfigurationError

from Exceptions import exceptions, check_config_database_engine, check_config_for_null

settings = Dynaconf(
    environments=True,
    default_env="global",
    settings_files=['../settings.toml', '../.secrets.toml'],
    envvar_prefix="DYNACONF",
    env="development",
    merge_enabled=True,
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.


# Remove the existing logger
logger.remove()
# Add a new logger with the given settings
logger.add(
    sys.stdout,
    colorize=settings.get("logging.colorize"),
    level=settings.get("logging.level"),
    format=settings.get("logging.format"),
)
# Add logging to file
logger.add(
    settings.get("logging.file_path"),
    level=settings.get("logging.level"),
    format=settings.get("logging.format"),
    rotation=settings.get("logging.rotation"),
    enqueue=settings.get("logging.enqueue"),
)

logger.info("Starting...")
logger.info("Configuration Initialization...")


# Handler class to intercept logger messages and convert them to Loguru format
class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = sys._getframe(6), 6
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


# Create an interceptor for the loggers
logger_db_client = logging.getLogger("tortoise.db_client")
logger_db_client.setLevel(logging.DEBUG)
logger_db_client.addHandler(InterceptHandler)

logger_tortoise = logging.getLogger("tortoise")
logger_tortoise.setLevel(logging.DEBUG)
logger_tortoise.addHandler(InterceptHandler)


def configure_tortoise():
    engine = settings.get("db.engine")
    timezone = settings.get("db.timezone")
    host = settings.get("db.host")
    port = settings.get("db.port")
    user = settings.get("db.user")
    password = settings.get("db.password")
    # database = settings.get("db.database")
    database = "test_db_oc"

    try:
        check_config_for_null(engine=engine, timezone=timezone, host=host, port=port, user=user,
                              password=password, database=database)
        check_config_database_engine(engine=engine)
    except exceptions.ConfigurationError as e:
        logger.error(f"Database configuration error: {e}")
    except ConfigurationError as e:
        logger.error(f"Database configuration error: {e}")

    if check_config_database_engine(engine=engine):
        engine = "mysql"

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
                'models': ['Models.product', ],
                # TODO 'Models.manufacturer', 'Models.category', 'Models.attributes'
            },
        },
        'use_tz': False,
        'timezone': f'{timezone}',
    }
    logger.info("Database configuration: \n"
                f"Engine: {engine} \n"
                f"Database: {database} \n"
                f"Host: {host} \n"
                f"Port: {port} \n"
                f"User: {user} \n"
                f"Timezone: {timezone}")
    del engine, timezone, database, host, password, port, user

    return tortoise_db_config


logger.info("Configuration Initialized")
