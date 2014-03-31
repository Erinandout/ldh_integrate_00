"""
Django settings for laurendennishair project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bt_vex*-(1f=g&9^4t9me$l5tu-z(*2%y5(^9#^g-@w(gsgiv5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'inplaceeditform_bootstrap',  # it is very important that this app is before that inplaceeditform and inplaceeditform_extra_fields
    'inplaceeditform',
    'inplaceeditform_extra_fields',  # this is optional but recommended
    'bootstrap3_datetime',
    'ldh',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)


ROOT_URLCONF = 'laurendennishair.urls'

WSGI_APPLICATION = 'laurendennishair.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    '/home/bdx/PycharmProjects/laurendennishair/ldh/templates',
)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)


MEDIA_URL = '/my_media/'
# django-inplaceedit customization

#INPLACEEDIT_EDIT_EMPTY_VALUE = 'Double click to edit...'
INPLACEEDIT_AUTO_SAVE = True
INPLACEEDIT_EVENT = 'click'
#INPLACEEDIT_DISABLE_CLICK = False
#INPLACEEDIT_EDIT_MESSAGE_TRANSLATION = 'Write a translation...'
#INPLACEEDIT_SUCCESS_TEXT = 'Edits saved!'
#INPLACEEDIT_UNSAVED_TEXT = 'You have unsaved changes!!!!'
#INPLACE_ENABLE_CLASS = 'enable'
#DEFAULT_INPLACE_EDIT_OPTIONS = {}
#DEFAULT_INPLACE_EDIT_OPTIONS_ONE_BY_ONE = False
#ADAPTOR_INPLACEEDIT_EDIT = 'inplace_edit.perms.AdminDjangoPermEditInline'
#ADAPTOR_INPLACEEDIT = {}
#INPLACE_GET_FIELD_URL = None
#INPLACE_SAVE_URL = None
#INPLACE_FIELD_TYPES = 'input, select, textarea'
#INPLACE_FOCUS_WHEN_EDITING = True

# django-inplaceedit-bootstrap customization

INPLACEEDIT_EDIT_TOOLTIP_TEXT = 'Click to edit' # By default 'Double click to edit'

# If inplaceeditform_extra_fields is installed

try:
    import inplaceeditform_extra_fields
    INSTALLED_APPS += ('inplaceeditform_extra_fields',)
    ADAPTOR_INPLACEEDIT = {'auto_fk': 'inplaceeditform_extra_fields.fields.AdaptorAutoCompleteForeingKeyField',
                           'auto_m2m': 'inplaceeditform_extra_fields.fields.AdaptorAutoCompleteManyToManyField',
                           'image_thumb': 'inplaceeditform_extra_fields.fields.AdaptorImageThumbnailField',
                           'tiny': 'inplaceeditform_extra_fields.fields.AdaptorTinyMCEField',
                           'tiny_simple': 'inplaceeditform_extra_fields.fields.AdaptorSimpleTinyMCEField'}
    try:
        import ajax_select
        INSTALLED_APPS += ('ajax_select',)
        AJAX_LOOKUP_CHANNELS = {
            'typeresource': {'model': 'multimediaresources.typeresource',
                             'search_field': 'name'},
            'user': {'model': 'auth.user',
                     'search_field': 'username'},
        }
    except ImportError:
        pass
    try:
        import sorl
        INSTALLED_APPS += ('sorl.thumbnail',)
        THUMBNAIL_DEBUG = DEBUG
    except ImportError:
        pass
except ImportError:
    pass


# If bootstrap3_datetime is installed

try:
    import bootstrap3_datetime
    INSTALLED_APPS += ('bootstrap3_datetime',)
    ADAPTOR_INPLACEEDIT = ADAPTOR_INPLACEEDIT or {}
    ADAPTOR_INPLACEEDIT['date'] = 'inplaceeditform_bootstrap.fields.AdaptorDateBootStrapField'
    ADAPTOR_INPLACEEDIT['datetime'] = 'inplaceeditform_bootstrap.fields.AdaptorDateTimeBootStrapField'
except ImportError:
    pass

# Custom settings to the different django versions

import django

if django.VERSION[0] >= 1 and django.VERSION[1] >= 4:
    TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.tz',)

if django.VERSION[0] >= 1 and django.VERSION[1] >= 3:
    INSTALLED_APPS += ('django.contrib.staticfiles',)
    # Absolute path to the directory static files should be collected to.
    # Don't put anything in this directory yourself; store your static files
    # in apps' "static/" subdirectories and in STATICFILES_DIRS.
    # Example: "/home/media/media.lawrence.com/static/"
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    # URL prefix for static files.
    # Example: "http://media.lawrence.com/static/"
    STATIC_URL = '/static/'

    # URL prefix for admin static files -- CSS, JavaScript and images.
    # Make sure to use a trailing slash.
    # Examples: "http://foo.com/static/admin/", "/static/admin/".
    ADMIN_MEDIA_PREFIX = '/static/admin/'

    # Additional locations of static files
    STATICFILES_DIRS = (
        # Put strings here, like "/home/html/static" or "C:/www/django/static".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
    )

    # List of finder classes that know how to find static files in
    # various locations.
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )
    TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.static',)

if django.VERSION[0] >= 1 and django.VERSION[1] >= 2:
    INSTALLED_APPS += ('django.contrib.messages',)