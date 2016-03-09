SECRET_KEY = 'qaz123'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = [
    'evostream',
    'testapp',
]

ROOT_URLCONF = 'testapp.urls'
