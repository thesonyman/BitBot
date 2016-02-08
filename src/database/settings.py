import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 't6h*ntyt1%qu75%#-&--p!ezu75i1vu*#!-z^+4hw&=6=!%pyy'

INSTALLED_APPS = ('db_core',)

MIDDLEWARE_CLASSES = ()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'database', 'db_core', 'db.sqlite3'),
    }
}
