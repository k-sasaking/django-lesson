from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, Djnago!!")


def hello_template(request):
    template_name = "hello.html"
    context = {}
    return render(request, template_name, context)
