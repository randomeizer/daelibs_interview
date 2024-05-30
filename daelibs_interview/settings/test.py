"""Test environment settings."""

from .base import *

# Set the flag to indicate that tests are running
import os
os.environ['RUNNING_TESTS'] = 'True'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
