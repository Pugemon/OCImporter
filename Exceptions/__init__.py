from tortoise.exceptions import ConfigurationError


def check_config_for_null(**kwargs):
    for var_name, var_value in kwargs.items():
        if var_value is None:
            raise ValueError(f"You did not specify db.{var_name} in the configuration file.")


def check_config_database_engine(**kwargs):
    supported_engines = {"mysql", "mariadb"}
    for var_name, var_value in kwargs.items():
        if var_value not in supported_engines:
            raise ConfigurationError(f"OpenCart does not support {var_value}. Use MySQL or MariaDB.")
        else:
            return True
