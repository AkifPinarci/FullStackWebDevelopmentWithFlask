import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "b'\x01\x9c\xa14/4\n\xa4\xe2\xabuk\xf7\xf7\x96\x90'"

    MONGODB_SETTINGS =  { 'db' : 'UTA_Enrollment' }