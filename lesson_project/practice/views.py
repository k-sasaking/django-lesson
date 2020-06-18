from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template_name = "practice.html"
    context = {}
    return render(request, template_name, context)
