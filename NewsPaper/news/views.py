from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


class PostList(ListView):
    model = Post
    ordering = '-created'
    template_name = 'PostList.html'
    context_object_name = 'post'


class PostDetail(DetailView):
    model = Post
    template_name = 'PostDetail.html'
    context_object_name = 'post_detail'

