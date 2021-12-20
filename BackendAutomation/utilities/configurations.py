import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config

def getPassword():
    return "4171cb8e5d55465e9fc2a2e62b77c3fd0fe27d25"