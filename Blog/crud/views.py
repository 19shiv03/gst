from typing import Reversible
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from .models import Post
from .forms import BlogForm

class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'

class AddPost(CreateView):
    model=Post
    template_name='add_post.html'
    success_url = '/show'
    fields=['title','author','content','status','created_on'] 
    
class DeletePost(DeleteView):
    model=Post
    template_name='delete.html'
    success_url='/show'
    
class UpdatePost(UpdateView):
    model=Post
    fields=['title','author','content','status']
    template_name='update.html'
    success_url='/show'


class Myview(ListView):
    model = Post
    template_name= 'show.html'
    
    def get_queryset(self, *args, **kwargs):
    
        return Post.objects.all()


# def SearchView(request):
#     query=request.POST.get('post')
#     print(query)
#     posts=Post.objects.filter(title__ic+ontains=query)
#     print(posts)
#     return render(request,'search.html',{'posts':posts})
    
class SearchView(ListView):
    model = Post
    template_name=  'show.html'
    
    def get_queryset(self, *args, **kwargs):
        title = self.request.GET.get('post')
        # print(f"title: {title}")
        # print( Post.objects.filter(title=title))
        return Post.objects.filter(title=title)

        
