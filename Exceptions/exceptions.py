class BaseOCImporterException(Exception):
    '''
    Base OCImporter Exception.
    '''

class ConfigurationError(BaseOCImporterException):
    """
    The ConfigurationError exception is raised when the configuration of the OCImporter is invalid.
    """