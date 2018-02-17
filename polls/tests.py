#from django.test import TestCase

# Create your tests here.
# Test uwsgi server
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]
