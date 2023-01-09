# from pathlib import Path
import os
import dj_database_url

if not os.environ.get("PRODUCTION"):
    from dotenv import load_dotenv

    load_dotenv()


# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = str(os.getenv("SECRET_KEY"))

DEBUG = True

ALLOWED_HOSTS = [
    "http://localhost:3000",
    'https://motorcycle-app.vercel.app'
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "bikes.apps.BikesConfig",
    "rest_framework",
    "django_filters",
    "crispy_forms",
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "advrider_django.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "advrider_django.wsgi.application"


DATABASES = {    
    'default': {        
        'ENGINE': 'django.db.backends.sqlite3',        
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),    
    }
}

if os.environ.get("PRODUCTION"):

    DATABASES["default"] = dj_database_url.config(conn_max_age=600)


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATIC_URL = "/static/"

# STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


DATA_UPLOAD_MAX_NUMBER_FIELDS = 102400  # higher than the count of fields


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 30,
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}


# CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    'https://advriderfleamarketclassifiedinterface.vercel.app/',
]
# if os.getcwd() == "/app":
#     DEBUG = False

# Configure Django App for Heroku.
import django_heroku

django_heroku.settings(locals())
if not os.environ.get("PRODUCTION"):
    options = DATABASES["default"].get("OPTIONS", {})
    options.pop("sslmode", None)
