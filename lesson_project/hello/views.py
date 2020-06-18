from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, Djnago!!")


def hello_template(request):
    template_name = "hello.html"
    context = {}
    return render(request, template_name, context)


def hello_param(request):
    template_name = "hello.html"
    humans = [
        TestHuman('Mike', 20, 'us'),
        TestHuman('Emily', 22, 'us'),
        TestHuman('Andy', 17, 'us'),
        TestHuman('Taro', 20, 'jp'),
        TestHuman('Hanako', 21, 'jp'),
    ]
    context = {
        'test_param': 'これはテストです',
        'test_humans': humans
    }
    return render(request, template_name, context)


class TestHuman(object):
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
