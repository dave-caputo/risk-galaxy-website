import os

from config.settings.base import *


INSTALLED_APPS += [
    'storages'
]

DEBUG = False

# Allowed host settings
# NOTE! emails will be sent in production to last host in the list.
ALLOWED_HOSTS = [
    '127.0.0.1',
    'https://8zjzbkbkxk.execute-api.eu-west-2.amazonaws.com',
    'www.riskgalaxy.com'
]

# Postgres database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rgsite',
        'USER': 'davecaputo',
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': 'riskgalaxydb.cmdawdidbkjb.eu-west-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}

AWS_STORAGE_BUCKET_NAME = 'zappa-static-rgsite'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_OBJECT_PARAMETERS = {
    # 'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    # 'CacheControl': 'max-age=94608000',

    # Show correctly Wagtail static items...
    # 'Access-Control-Allow-Origin': '*'
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

SECURE_SSL_REDIRECT = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.office365.com'
EMAIL_HOST_USER = 'admin@riskgalaxy.com'
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'admin@riskgalaxy.com'
SERVER_EMAIL = 'admin@riskgalaxy.com'

USE_X_FORWARDED_HOST = True
FORCE_SCRIPT_NAME = "/"
