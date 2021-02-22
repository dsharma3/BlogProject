from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def index(request):  
    posts = Post.objects.all()      
    return render(request,'blog/posts.html',context={'posts':posts})

def post_details(request, pk):
    post = Post.objects.get(pk = pk)
    print(post)
    return render(request, 'blog/posts-detail.html', context={'post':post})


class PostList(generic.ListView):
    template_name = 'blog/posts.html'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context

class PostDetail(generic.DetailView):
    model = Post
    template_name='blog/posts-detail.html'
    login_url = '/login/'

class CreatePost(generic.CreateView, LoginRequiredMixin):
    template_name = 'blog/posts-create.html'
    model = Post
    fields = ("title","content")
    login_url = '/login/'
    redirect_field_name ='blog/post-detail.html'