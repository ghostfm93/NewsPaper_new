from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .filters import PostFilter
from .forms import PostForm
from .models import *


class PostList(ListView):
    model = Post
    ordering = '-created'
    template_name = 'PostList.html'
    context_object_name = 'post'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'PostDetail.html'
    context_object_name = 'post_detail'


class PostSearch(ListView):
    model = Post
    ordering = '-created'
    template_name = 'PostSearch.html'
    context_object_name = 'post'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'PostEdit.html'


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'PostEdit.html'

class PostDelete(DeleteView):
    model = Post
    template_name = 'PostDelete.html'
    success_url = reverse_lazy('post_list')

