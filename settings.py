from efforia.settings import *
import os

ADMINS = (('William Oliveira de Lagos', 'william@efforia.com.br'),)
MANAGERS = ADMINS
SECRET_KEY = 'x5dvfbk$u-(07^f1229p*_%rcuc+nka45j6awo==*jkyjiucql'

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'd6i6a0klirtqjd',
    'HOST': 'ec2-54-243-243-176.compute-1.amazonaws.com',
    'PORT': 5432,
    'USER': 'kkoaphemdgvutt',
    'PASSWORD': 'ztTIw8EcIYX2UlNolrVmTb8yZQ'
  }
}

PAYPAL_RECEIVER_EMAIL = 'efforiaca@gmail.com'
PAYPAL_NOTIFY_URL = '/paypal'
PAYPAL_RETURN_URL = '/'
PAYPAL_CANCEL_RETURN = '/cancel'

PAGSEGURO_EMAIL_COBRANCA = 'contato@efforia.com.br' 
PAGSEGURO_TOKEN = '1a3ea7wq2e7eq8e1e223add23ad23'
PAGSEGURO_URL_RETORNO = '/pagseguro/retorno/'
PAGSEGURO_URL_FINAL = '/obrigado/' 
PAGSEGURO_ERRO_LOG  = '/tmp/pagseguro_erro.log'

EFFORIA_APPS = ['promote']
EFFORIA_OBJS = { 'promote': ['Project','Event'] }
EFFORIA_NAMES = { 'promote': ('Promova','promote') }
EFFORIA_TOKENS = {
    "@": "efforia.Profile", 
    "!#":"efforia.Page",
    "#": "promote.Project", 
    "@#":"promote.Project", 
    "##":"promote.Movement",
    "@!":"promote.Event",
    "@": "promote.Event",
    "@@":"promote.Event"
}
EFFORIA_URL = 'promova.co'

STATICFILES_DIRS.extend([ os.path.abspath('promote/public') ])
TEMPLATE_DIRS.extend([
    os.path.abspath('promote/templates/jade'),
    os.path.abspath('promote/templates')
])

INSTALLED_APPS.extend(EFFORIA_APPS)
