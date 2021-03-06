import re


def camelcase(value):
    """
    Convert a module name or string with underscores and periods to camel case.
    :param value: the string to convert
    :type value: str
    :returns: the value converted to camel case.
    """
    return ''.join(x.capitalize() if x else '_' for x in
                   re.split("[._]+", value))
