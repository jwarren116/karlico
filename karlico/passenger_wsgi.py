import sys, os
cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/karlico')  #You must add your project here

#Switch to new python
#if sys.version < "2.7.7": os.execl(cwd+"/env/bin/python", "python2.7", *sys.argv)

sys.path.insert(0,cwd+'/env/bin')
sys.path.insert(0,cwd+'/env/lib/python2.7/site-packages/django')
sys.path.insert(0,cwd+'/env/lib/python2.7/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = "karlico.settings"
os.environ.setdefault("DJANGO_CONFIGURATION", "Prod")

from configurations.wsgi import get_wsgi_application
application = get_wsgi_application()
