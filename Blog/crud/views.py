from typing import Reversible
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from requests import post
from .models import Post
from .forms import BlogForm


class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"


class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"


class AddPost(CreateView):
    model = Post
    template_name = "add_post.html"
    success_url = "/show"
    fields = ["title", "author", "content", "status", "created_on"]


class DeletePost(DeleteView):
    model = Post
    template_name = "delete.html"
    success_url = "/show"


class UpdatePost(UpdateView):
    model = Post
    fields = ["title", "author", "content", "status"]
    template_name = "update.html"
    success_url = "/show"
    initial = {}

    def get_initial(self) -> dict:
        global initial
        initial = super(UpdatePost, self).get_initial()
        print("initial data", initial)

        # retrieve current object
        habit_object = self.get_object()

        initial["title"] = habit_object.title
        initial["author"] = habit_object.author
        initial["content"] = habit_object.content
        initial["status"] = habit_object.status
        print(initial)
        return initial
    
    def get_context_data(self, **kwargs):
        context = super(UpdatePost, self).get_context_data(**kwargs)
        context.update(self.get_initial())
        return context


class Myview(ListView):
    model = Post
    template_name = "show.html"

    def get_queryset(self, *args, **kwargs):
        return Post.objects.all()


class SearchView(ListView):
    model = Post
    template_name = "show.html"

    def get_queryset(self, *args, **kwargs):
        title = self.request.GET.get("post")
        if title:
            result = Post.objects.filter(title=title)
            if len(result) == 0:
                return Post.objects.all()
        else:
            result = Post.objects.all()

        return result
