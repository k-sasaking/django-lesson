from django.urls import path

from . import views

app_name = 'hello'
urlpatterns = [
    path('', views.index, name='hello_django'),
    path('test/template', views.hello_template, name='hello_template'),
    path('test/param/', views.hello_param, name='hello_param'),
]