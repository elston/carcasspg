import os

from .base import *

DEBUG = True

# 
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static/'),
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mediatry',
        'USER': 'kobe',  
        'PASSWORD': 'bryant',
        'HOST': 'storage',
        'PORT': '5432',
        # 'HOST': get_env_variable('PG_HOST'),
        # 'PORT': get_env_variable('PG_PORT'),        
    }
}

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG