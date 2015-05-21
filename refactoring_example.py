# Bad Case-----------------------------------------------
class MyView(object):
    def __init__(self, request):
        self.request = request


    def index(self):
        s = SomeService()
        result = s.some_method(**self.request.params)
        return render('index.html', dict(result=result))


# Good Case----------------------------------------------
class MyView(object):
    someservice_cls = SomeService
    def __init__(self, request):
        self.request = request


    def index(self):
        s = self.someservice_cls()
        result = s.some_method(**self.request.params)
        self.render_context = dict(result=result)
        return render('index.html', self.render_context)


# Test with Good Case
class DummyRequest(object):
    def __init__(self, params):
        self.params = params


class DummySomeService(object):
    def somemethod(self, **kwargs):
        return kwargs


import unittest

class TestIt(unittest.TestCase):
    def test_it(self):
        request = DummyRequest(params={'a':1})
        target = MyView(request)
        target.someserivce_cls = DummySomeService
        result = target.index()
        self.assertEqual(target.render_context['result'], {'a':1})
