""" 
74.208.107.6
root
Z0zpivUn
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
from django.conf import settings
from datetime import timedelta
import datetime


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i_pdk2m00ulx4*0&v)fz0m22u)e_nz(sy#zj$&h(!h(aey$&)&'

# SECURITY WARNING: don't run with debug turned on in production!
"""774.208.107.6  root Z0zpivUn"""
DEBUG = True

BASE_URL  = "http://localhost:8000/" 

ALLOWED_HOSTS = ["52.23.184.163",'*']
# hosting username pwd  70.35.201.35  root  H#9wA0NE5M   

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin', 
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'corsheaders',
     'rest_framework',
     'django_filters',
    'drf_yasg',
    "menumanager",
    'usermanager',
    'companymanager',
    'employeemanager',
    'attendencemanager',
    'salarymanager',
    'frontend',
    'rest_framework_simplejwt.token_blacklist',
   

]

MIDDLEWARE = [ 
    
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',   
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',    
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sd.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['tempaltes'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'sd.wsgi.application'
ORS_ORIGIN_ALLOW_ALL=True  
CORS_ORIGIN_WHITELIST =["http://localhost:5000"]
CORS_ALLOW_HEADERS = "*"

AUTH_TOKEN_VALIDITY = getattr(settings, 'AUTH_TOKEN_VALIDITY', timedelta(days=1))
#CORS_ALLOW_CREDENTIALS = True
# CORS_ALLOW_HEADERS = ['*']
# CORS_ORIGIN_WHITELIST = ('http://localhost:8000',)
# # Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'sdservice',
#         'USER': 'root',
#         'PASSWORD': 'pq5O8MGV',
#         'HOST': 'localhost',  # Or the hostname of your MySQL server
#         'PORT': '3306',       # MySQL default port
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static',]


# MEDIA_DIR = BASE_DIR / 'media'
# MEDIA_ROOT = MEDIA_DIR
# MEDIA_URL = '/media/'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'usermanager.User'


# SITE_ID = 1


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.TokenAuthentication',
        
         'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',
    # ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': ('rest_framework.parsers.JSONParser',),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 10,
    'NON_FIELD_ERRORS_KEY': 'nonfield',
}

 
 

 
SWAGGER_SETTINGS = {
    'DEFAULT_INFO': 'SD SRVICE',
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    'USE_SESSION_AUTH': False,
}

 