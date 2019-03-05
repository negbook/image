import os
import sys

import pymysql
pymysql.install_as_MySQLdb()

sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = "main.settings"

### new django versions
from django.core.wsgi import get_wsgi_application
wsgi_application = get_wsgi_application()
 
def application(environ, start_response):
     
    if environ['wsgi.url_scheme'] == 'https':
        url = 'http://' + environ['HTTP_HOST'] + environ['REQUEST_URI']
        start_response('301 Moved Permanently', [('Location', url)])
        return []
         
    return wsgi_application(environ, start_response)


