"""
Django settings for eurofundusze project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!hm&cm_8yq(&qq5g9flp4*rkgc3&auq2ma_jq!aftri6i(yur$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

ZINNIA_PAGINATION=3

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django_comments',
    'mptt',
    'tagging',
    'zinnia',

    # Custom apps
    'widget_exchange_rates',
    'utils',
    'ef_multimedia',
    # Zinnia blog
    # 'django_comments',
    # 'mptt',
    # 'tagging',
    # 'zinnia',
)

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
    },
}

SITE_ID = 1
# THUMBNAIL_HIGH_RESOLUTION = True

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'cms.middleware.multilingual.MultilingualURLMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'django.middleware.locale.LocaleMiddleware',
    # 'django.middleware.doc.XViewMiddleware',
    # 'cms.middleware.user.CurrentUserMiddleware',
    # 'cms.middleware.page.CurrentPageMiddleware',
    # 'cms.middleware.toolbar.ToolbarMiddleware',
    # 'cms.middleware.language.LanguageCookieMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    # 'sekizai.context_processors.sekizai',
    # 'zinnia.context_processors.version',  # Optional
    # 'cms.context_processors.cms_settings',
    # 'cms.context_processors.media',
)

# TEMPLATE_LOADERS = (
# 'django.templates.loaders.app_directories.load_template_source',
# )

# THUMBNAIL_PROCESSORS = (
#     'easy_thumbnails.processors.colorspace',
#     'easy_thumbnails.processors.autocrop',
#     'easy_thumbnails.processors.scale_and_crop',
# 'filer.thumbnail_processors.scale_and_crop_with_subject_location',
# 'easy_thumbnails.processors.filters',
# )

# SOUTH_MIGRATION_MODULES = {
#         'easy_thumbnails': 'easy_thumbnails.south_migrations',
# }

ROOT_URLCONF = 'eurofundusze.urls'

WSGI_APPLICATION = 'eurofundusze.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'euro83_fundusze',
         'USER': 'fundusze',
         'PASSWORD': 'd140559e987cdca',
         'HOST': 'localhost',
         'PORT': '5432',
     },
    'deploment': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'eurofundusze.db',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'pl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
# STATIC_ROOT = '/home/gauee/DjangoProjects/LukaszPastuszynskiEuroDof/eurofundusze/eurofundusze/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "eurofundusze/static")

STATIC_URL = '/static/'
# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# )
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_ROOT = os.path.join(PROJECT_PATH, "../../media")
MEDIA_URL = "/media/"


#Templates
TEMPLATE_DIRS = (
    # The docs say it should be absolute path: PROJECT_PATH is precisely one.
    # Life is wonderful!
    os.path.join(PROJECT_PATH, "templates"),
)

# CMS_TEMPLATES = (
#     ('template_1.html', 'Template One'),
#     ('template_2.html', 'Template Two'),
# )

LANGUAGES = [
    #('en', 'English'),
    ('pl', 'Poland'),
]

# Logger
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
     'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': './logs/debug.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
