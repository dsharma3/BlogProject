from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post
# Create your views here.

def index(request):  
    posts = Post.objects.all()      
    return render(request,'blog/posts.html',context={'posts':posts})

class PostList(generic.ListView):
    template_name = 'blog/posts.html'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context
    