"""
Django settings for DjangoFrame_demo project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

# 导入系统模块
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 项目根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 将来如果某个功能需要进行加密直接可以使用Django为我们提供好的秘钥,不用再手动去生成
SECRET_KEY = 'zy17a3n274^u169g@o+0)f!8(kp7rbb=hc@sg7de5vj8#_v43w'

# SECURITY WARNING: don't run with debug turned on in production!
# 默认Django就为我们开启调试模式,将来项目部署上线时需要把DEBUG改为False
# Django框架它能为我们提供静态文件访问的原因是DEBUG为True,如果DEBUG设置为False时,Django不再为我们提供静态文件访问的能力
# Django框架是一个动态业务逻辑框架,更倾向于动态业务处理,不擅长静态文件处理
DEBUG = True

# 允许哪个域名访问我们Django后端服务
ALLOWED_HOSTS = []


# Application definition

# 注册子应用(源生, 第三方, 自己的)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',  # DRF
    'django_filters',  # 需要注册应用

    # 如果子应用中需要用模型迁移建表,必修注册子应用
    # 如果子应用中也使用了'模板'也需要注册
    # 如果子应用中只和视图路由相关,那么子应用可以不注册
    'users.apps.UsersConfig',  # 注册子应用
    'request_response.apps.RequestResponseConfig',
    'booktest.apps.BooktestConfig',
]

# 中间件的配置项(类似于Flask中的请求勾子)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'middleware.my_middleware',  # 注册自定义中间件
    # 'middleware.my_middleware2',
]

# 工程路由入口
ROOT_URLCONF = 'DjangoFrame_demo.urls'

# 模板配置项
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# 生产环境工程启动入口
WSGI_APPLICATION = 'DjangoFrame_demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# 数据库的配置项
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_sz22',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'mysql'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

# 密码认证配置项
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
# https://docs.djangoproject.com/en/1.11/topics/i18n/
# 语言本地化 默认是英文  zh-hans --> 中文
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'
# 时区 默认世界时间  亚洲/上海
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
# 默认静态文件访问的路由前缀
STATIC_URL = '/static/'

# 配置静态访问的访问路径(存放路径)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'static/abc'),
]

# session存储位置配置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')

# REST_FRAMEWORK DRF配置项全部写在此变量
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (  # 全部认证类配置,必须要配置权限使用
        'rest_framework.authentication.BasicAuthentication',   # 基本认证
        'rest_framework.authentication.SessionAuthentication',  # session认证
    ),
    # 限流配置
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day'
    },
    # 指定过滤后端
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),

    'EXCEPTION_HANDLER': 'exception.exception_handler',  # 指定自定义捕获异常函数
}
