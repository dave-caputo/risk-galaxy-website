from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Postgres database configuration..
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rgsite',
        'USER': 'rgadmin',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h6(wigfx9ca@8_460(rr3hu^sk&%w)=3ut@e(e$2_(#)*o94)q'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
