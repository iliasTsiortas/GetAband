DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'getaband',
        'USER': 'gab_user',
        'PASSWORD': 'iliasmortontoukosta',
        'HOST': '127.0.0.1',
        'OPTIONS': {
            'isolation_level': 'read committed'
        }
    }
}

SECRET_KEY = 'vivm3las@op1^0zf@lb+lj%*%*t7g4$v0r_)#h^ikzm@ea6ojp'