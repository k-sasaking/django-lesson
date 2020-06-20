from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Post
from .forms import PostCreateForm


def index(request):
    template_name = "index.html"
    context = {}
    return render(request, template_name, context)


class PostCreateView(CreateView):
    form_class = PostCreateForm
    template_name = "post/post_form.html"
    success_url = reverse_lazy('post:index')


class PostListView(ListView):
    model = Post
    template_name = 'index.html'


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostCreateForm
    template_name = "post/post_form.html"
    success_url = reverse_lazy('post:index')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/delete_confirm.html'
    success_url = reverse_lazy('post:index')
