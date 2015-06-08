import os
from configurations import Settings


class Base(Settings):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'blog',
        'sorl.thumbnail',
    )

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = 'karlico.urls'

    WSGI_APPLICATION = 'karlico.wsgi.application'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'America/Los_Angeles'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    STATIC_ROOT = BASE_DIR + '/public/static/'
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'karlico/static/'),
    )

    MEDIA_URL = '/img/'
    MEDIA_ROOT = BASE_DIR + '/public/media/'

    TEMPLATE_DIRS = (
        os.path.join(BASE_DIR, 'blog/templates/blog/'),
        os.path.join(BASE_DIR, 'karlico/templates/'),
    )


class Dev(Base):
    ALLOWED_HOSTS = ['*']
    SECRET_KEY = '7j!g$yf)qfz6he-(^w0w94uxs4p=99@+sk$b66zyvifuw8aavz'
    DEBUG = True
    THUMBNAIL_DEBUG = DEBUG
    TEMPLATE_DEBUG = DEBUG


class Prod(Base):
    ALLOWED_HOSTS = ['.karli.co']
    SECRET_KEY = os.environ.get('SECRET_KEY', 's3cr!th4$]-[')
    DEBUG = False
    THUMBNAIL_DEBUG = DEBUG
    TEMPLATE_DEBUG = DEBUG
