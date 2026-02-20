import os
import logging

from django.core.exceptions import DisallowedHost
from dotenv import load_dotenv
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

env_file_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=env_file_path)


# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

SECRET_KEY = os.getenv('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = os.getenv(
    'DJANGO_ALLOWED_HOSTS',
    'seamarinefuels.com,www.seamarinefuels.com,165.232.190.192,127.0.0.1,localhost,0.0.0.0'
).split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bunkering_frontend',
    'django.contrib.sitemaps',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


class EndpointLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger("endpoint")

    def __call__(self, request):
        method = request.method
        path = request.get_full_path()
        if path.startswith("/static/") or path.startswith("/media/") or path.startswith("/favicon") or path.startswith("/apple-touch-icon"):
            return self.get_response(request)
        response = self.get_response(request)
        status = getattr(response, "status_code", None)
        content_type = response.get("Content-Type", "")
        body_preview = ""
        content = getattr(response, "content", None)
        if isinstance(content, (bytes, bytearray)) and ("text" in content_type or "json" in content_type):
            try:
                body_preview = content.decode("utf-8", errors="ignore")[:500]
            except Exception:
                body_preview = ""
        self.logger.info(
            "endpoint %s %s status=%s response_preview=%s",
            method,
            path,
            status,
            body_preview,
        )
        return response

MIDDLEWARE.insert(0, 'dj_bunkering_app.settings.EndpointLoggerMiddleware')

ROOT_URLCONF = 'dj_bunkering_app.urls'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'bunkering_frontend.context_processor.footer_items_context'
            ],
        },
    },
]

WSGI_APPLICATION = 'dj_bunkering_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Add your custom static file directories here
]

STATIC_ROOT = BASE_DIR / "staticfiles"  # Directory where `collectstatic` will place files
STATIC_URL = "/static/"

# Media files settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REACT_APP_DIR = os.path.join(BASE_DIR, 'bunkering_frontend')

# Email backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.hostinger.com'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = os.getenv('TO_EMAIL')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_TIMEOUT = 30
DEFAULT_FROM_EMAIL = os.getenv('FROM_EMAIL') or EMAIL_HOST_USER

CSRF_TRUSTED_ORIGINS = [
    "https://seamarinefuels.com",
    "https://www.seamarinefuels.com",
]
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
