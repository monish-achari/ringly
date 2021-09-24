"""
Django settings for ringly project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#=@ky3t=a0-v94pz87c#wjqfm*3_52%95-wwqh+936j-t_8-$m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ringly.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': [str(BASE_DIR) + '/templates/',],
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

WSGI_APPLICATION = 'ringly.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
import os
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# config = {
#     "apiKey": "AIzaSyCvM_boGl1FEU_zkI6SDzJBbF9ZuuREtIg",
#     "authDomain": "ringlyringtone.firebaseapp.com",
#     "databaseURL": "https://ringlyringtone.firebaseio.com",
#     "projectId": "ringlyringtone",
#     "storageBucket": "ringlyringtone.appspot.com",
#     "messagingSenderId": "792746928664",
#     "appId": "1:792746928664:web:57596daf3f0799e87f716d",
#     "measurementId": "G-KSLEP6H6HL"
# }


config = {
    "apiKey": "AIzaSyB5A_FC5ev5qlEJEo6Pgkx1VOGnr28Q1pQ",
    "authDomain": "ringtoneapp-4fcae1.firebaseapp.com",
    "databaseURL": "https://ringtoneapp-4fcae1.firebaseio.com",
    "projectId": "ringtoneapp-4fcae1",
    "storageBucket": "ringtoneapp-4fcae1.appspot.com",
    "messagingSenderId": "312391400362",
    "appId": "1:312391400362:web:00796e00d4e3c8725249d3",
    "measurementId": "G-WRSYH1GBKR"
}


"""
<!-- The core Firebase JS SDK is always required and must be listed first -->
<script src="https://www.gstatic.com/firebasejs/7.24.0/firebase-app.js"></script>

<!-- TODO: Add SDKs for Firebase products that you want to use
     https://firebase.google.com/docs/web/setup#available-libraries -->
<script src="https://www.gstatic.com/firebasejs/7.24.0/firebase-analytics.js"></script>

<script>
  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  var firebaseConfig = {
    apiKey: "AIzaSyCvM_boGl1FEU_zkI6SDzJBbF9ZuuREtIg",
    authDomain: "ringlyringtone.firebaseapp.com",
    databaseURL: "https://ringlyringtone.firebaseio.com",
    projectId: "ringlyringtone",
    storageBucket: "ringlyringtone.appspot.com",
    messagingSenderId: "792746928664",
    appId: "1:792746928664:web:57596daf3f0799e87f716d",
    measurementId: "G-KSLEP6H6HL"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  firebase.analytics();
</script>
"""

# Activate Django-Heroku.
# import django_heroku
# django_heroku.settings(locals())



"""
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional

const firebaseConfig = {
  apiKey: "AIzaSyB5A_FC5ev5qlEJEo6Pgkx1VOGnr28Q1pQ",
  authDomain: "ringtoneapp-4fcae1.firebaseapp.com",
  databaseURL: "https://ringtoneapp-4fcae1.firebaseio.com",
  projectId: "ringtoneapp-4fcae1",
  storageBucket: "ringtoneapp-4fcae1.appspot.com",
  messagingSenderId: "312391400362",
  appId: "1:312391400362:web:00796e00d4e3c8725249d3",
  measurementId: "G-WRSYH1GBKR"
};


// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

"""