from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.core.paginator import Paginator

from .models import Post
from .forms import PostCreateForm


DEFAULT_PAGE_SIZE = 5
DEFAULT_PAGE = 1


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

    def get_queryset(self):
        page = self.request.GET.get('page', DEFAULT_PAGE)
        post_list = Post.objects.all()
        object_list = Paginator(post_list, DEFAULT_PAGE_SIZE).get_page(page)
        return object_list


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostCreateForm
    template_name = "post/post_form.html"
    success_url = reverse_lazy('post:index')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/delete_confirm.html'
    success_url = reverse_lazy('post:index')


class PostSearchView(ListView):
    model = Post
    template_name = 'index.html'

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        page = self.request.GET.get('page', DEFAULT_PAGE)
        if q_word:
            post_list = Post.objects.filter(text__icontains=q_word)
        else:
            post_list = Post.objects.all()
        object_list = Paginator(post_list, DEFAULT_PAGE_SIZE).get_page(page)
        return object_list
