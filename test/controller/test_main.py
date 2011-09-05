from StringIO import StringIO
from main import MainHandler
import unittest
from google.appengine.ext import webapp

class MyTestCase(unittest.TestCase):
    def test_get(self):
        request = webapp.Request({
            "wsgi.input": StringIO(),
            "CONTENT_LENGTH": 0,
            "METHOD": "GET",
            "PATH_INFO": "/"
        })
        response = webapp.Response()
        handler = MainHandler()
        handler.initialize(request, response)
        handler.get()
        self.assertEqual(response.out.getvalue(), "Hello world!")