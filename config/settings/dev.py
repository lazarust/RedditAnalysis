import socket

from .base import *

DEBUG = True

PEARS_INSTANCE_SLUG = env('PEARS_INSTANCE_SLUG', default='dev')
EMAIL_HOST = env('EMAIL_HOST', default='smtp.mailtrap.io')
EMAIL_PORT = env.int('EMAIL_PORT', default=587)
X_FRAME_OPTIONS = 'SAMEORIGIN'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}


DOMAIN = env('DOMAIN', default='127.0.0.1:8000')