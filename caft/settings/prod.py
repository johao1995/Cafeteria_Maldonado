from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cafeteria',
        'USER':'curso',
        'PASSWORD':'Curso2021',
        'HOST':'localhost',
        'PORT':'5432'
    }
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'../static')
]

MEDIA_URL='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'../media')