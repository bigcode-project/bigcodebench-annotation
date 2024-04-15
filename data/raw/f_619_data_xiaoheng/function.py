import sys
from configparser import ConfigParser

# Constants
PATH_TO_APPEND = '/path/to/whatever'
CONFIG_FILE = '/path/to/config.ini'

def f_103(path_to_append=PATH_TO_APPEND, config_file=CONFIG_FILE):
    """
    Add a specific path to sys.path and update a configuration file with this path.

    Parameters:
    path_to_append (str): The path to append to sys.path. Default is '/path/to/whatever'.
    config_file (str): The path to the config file to update. Default is '/path/to/config.ini'.

    Returns:
    ConfigParser: The updated ConfigParser object.

    Requirements:
    - os
    - sys
    - configparser.ConfigParser

    Example:
    Example:
    >>> config = f_103('/path/to/new_directory', '/path/to/new_config.ini')
    >>> 'path_to_append' in config['DEFAULT']
    True
    """
    sys.path.append(path_to_append)

    config = ConfigParser()
    config.read(config_file)
    config.set('DEFAULT', 'path_to_append', path_to_append)
    with open(config_file, 'w') as file:
        config.write(file)

    return config, config_file
