from music.settings.common import *

DEBUG = True

ALLOWED_HOSTS = ['musicvoteproj.herokuapp.com']

# DATABASES = {}
DATABASES['default'] = dj_database_url.config(default='postgres://vbehgvyyejofnj:4c204a9cc68f9b49b2a84c6ff1c682020d8dc9233e62c13e5e4abcfe4c809441@ec2-50-17-178-87.compute-1.amazonaws.com:5432/d5lhsic8v4ne1o')
