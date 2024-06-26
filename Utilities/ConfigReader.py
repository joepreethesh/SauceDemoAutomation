import os
from configparser import ConfigParser

def readConfig(section, key):
    current_directory = os.getcwd()
    config_path = os.path.join(current_directory, 'Locators', 'locators.ini')
    config = ConfigParser()
    config.read(config_path)
    return config.get(section, key)