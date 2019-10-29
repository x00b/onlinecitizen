from configparser import ConfigParser
from onctz.api.app import run_api

config = ConfigParser()
config.read('conf.ini')
run_api()



