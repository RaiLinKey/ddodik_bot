import configparser
from os import environ

configfile = './config/config.ini'

config = configparser.ConfigParser()
config.read(configfile)

API_KEY = environ.get('API_KEY') if environ.get('API_KEY') else config.get('SETTINGS', 'API_KEY')

__users_tmp = environ.get('USERS') if environ.get('USERS') else config.get('SETTINGS', 'USERS')

USERS = [int(user_id) for user_id in __users_tmp.split(',')]
