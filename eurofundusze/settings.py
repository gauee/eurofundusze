import os

PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '!hm&cm_8yq(&qq5g9flp4*rkgc3&auq2ma_jq!aftri6i(yur$'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

TEMPLATE_DEBUG = True

ZINNIA_PAGINATION = 2

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django_comments',
    'mptt',
    'tagging',
    'zinnia',
    'ckeditor',
    'zinnia_ckeditor',
    'south',
    'captcha',
    'social.apps.django_app.default',
    'djangobower',

    # Custom apps
    'widget_exchange_rates',
    'utils',
    'ef_multimedia',
    'ef_ads',
)

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
    },
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'django.core.context_processors.request',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)
# END SOCIAL APP AUTH

LOGIN_REDIRECT_URL = '/'

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'eurofundusze.urls'

WSGI_APPLICATION = 'eurofundusze.wsgi.application'

LANGUAGE_CODE = 'pl'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# STATICFILES
# STATIC_ROOT = os.path.join(BASE_DIR, "/")
# STATIC_ROOT = os.path.join(BASE_DIR, "static/collected")

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATIcFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "djangobower.finders.BowerFinder",
)

# END STATICFILES

# BOWER
BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, "components")
BOWER_PATH = '/usr/bin/bower'
BOWER_INSTALLED_APPS = (
    'bootstrap-social',
)
# END BOWER

MEDIA_ROOT = os.path.join(PROJECT_PATH, "../media")
MEDIA_URL = "/media/"

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, "templates"),
)

LANGUAGES = [
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
