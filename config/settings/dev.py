import socket

from .base import *

DEBUG = True

PEARS_INSTANCE_SLUG = env("PEARS_INSTANCE_SLUG", default="dev")
X_FRAME_OPTIONS = "SAMEORIGIN"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "ERROR",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django.request": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": False,
        },
    },
}


DOMAIN = env("DOMAIN", default="127.0.0.1:8000")
