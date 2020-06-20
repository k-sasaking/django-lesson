from django.urls import path

from . import views

app_name = 'post'
urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.PostDeleteView.as_view(), name='delete'),
    path('search/', views.PostSearchView.as_view(), name='post_search'),
]
