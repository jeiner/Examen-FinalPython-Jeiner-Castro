
from .base import *  # noqa: F403
from decouple import config
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1e&l(z7+49c&i_2b#c2)zvq1gfiqbbi)lih+ng88s8b6l+_qm7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
# Permite crear una lista para indicar que IP's se pueden conectar a nuestro aplicativo.
# * : Permite que cualquier IP se pueda conectar.

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config('ENGINE', cast=str),
        'NAME': config('NAME_DB', cast=str),
        'USER': config('USER_DB', cast=str),
        'PASSWORD': config('PASSWORD', cast=str),
        'HOST': config('HOST_DB', cast=str),
        'PORT': config('PORT_DB'),
    }
}


"""
-> Base de Datos relacionales:
 - mysql
 - postgresql
 - sqlserver
 - RDS (AWS)

-> Base de Datos no relaciones:
- firebase
- mongo DB
- Dynamo DB (AWS)
"""

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
