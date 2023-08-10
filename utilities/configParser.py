import configparser

def getconfig():

    config = configparser.ConfigParser()
    config.read('resources/properties.ini')

    return config
