
import json
import configparser
from pathlib import Path

cfgFileFlaskApp='qa.ini'
cfgFileDir='config'

'''Create a ConfigParser instance for FlaskApp'''
configFlaskApp=configparser.ConfigParser()

BASE_DIR=Path(__file__).resolve().parent.parent
CONFIG_FILE_FLASKAPP=BASE_DIR.joinpath(cfgFileDir).joinpath(cfgFileFlaskApp)
configFlaskApp.read(CONFIG_FILE_FLASKAPP)

def getFlaskAppBaseURL():
    baseURL='http://'+ configFlaskApp['flaskapp']['url']+":"+configFlaskApp['flaskapp']['port'] + '/api/'
    return baseURL

print(getFlaskAppBaseURL())


BASE_DIRR=Path(__file__).resolve().parent.parent
print(BASE_DIR)
TEST_DATA_DIRR=BASE_DIR.joinpath('TestData')

def getJsonFromFile(filename):
    filepath=TEST_DATA_DIRR.joinpath(filename)
    with open(filepath,'r') as file:
        return json.load(file)




'''
The configparser module is used to read values from the .ini file
and make them available in your test code.

An .ini file is a plain text file used for configuration. It typically includes:

Environment settings (e.g., dev, qa, prod)

Browser type (e.g., chrome, firefox)

URLs

Timeouts

Credentials (though storing sensitive data in plain text is discouraged)
'''

