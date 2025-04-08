import configparser
from os import environ

configfile = './config/config.ini'

config = configparser.ConfigParser()
config.read(configfile)

API_KEY = environ.get('API_KEY') if environ.get('API_KEY') else config.get('SETTINGS', 'API_KEY')

__tzar_tmp = environ.get('TZAR') if environ.get('TZAR') else config.get('SETTINGS', 'TZAR')
TZAR = [int(user_id) for user_id in __tzar_tmp.split(',')]

__kick_him_tmp = environ.get('KICK_HIM') if environ.get('KICK_HIM') else config.get('SETTINGS', 'KICK_HIM')
KICK_HIM = [int(user_id) for user_id in __kick_him_tmp.split(',')]

__yes_true_tmp = environ.get('YES_TRUE') if environ.get('YES_TRUE') else config.get('SETTINGS', 'YES_TRUE')
YES_TRUE = [int(user_id) for user_id in __yes_true_tmp.split(',')]

__full_yes_true_off_tmp = environ.get('FULL_YES_TRUE_OFF') if environ.get('FULL_YES_TRUE_OFF') else config.get('SETTINGS', 'FULL_YES_TRUE_OFF')
FULL_YES_TRUE_OFF = [int(user_id) for user_id in __full_yes_true_off_tmp.split(',')]
