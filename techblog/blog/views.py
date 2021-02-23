from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
# Create your views here.

def index(request):  
    posts = Post.objects.all()      
    return render(request,'blog/posts.html',context={'posts':posts})

def post_details(request, pk):
    post = Post.objects.get(pk = pk)
    print(post)
    return render(request, 'blog/posts-detail.html', context={'post':post})

class MyPostList(generic.ListView):
    template_name = 'blog/myposts.html'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(user = self.request.user)
        return context

class PostList(generic.ListView):
    template_name = 'blog/posts.html'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(approvals = True)
        return context

class PostDetail(generic.DetailView):
    model = Post
    template_name='blog/posts-detail.html'
    login_url = '/login/'

class CreatePost(generic.CreateView, LoginRequiredMixin):
    template_name = 'blog/posts-create.html'
    model = Post
    #fields = ("title","content")
    form_class = PostForm
    login_url = '/login/'
    redirect_field_name ='blog/post-detail.html'

    def form_valid(self, form):
        print(form.instance)
        form.instance.user = self.request.user
        return super(CreatePost, self).form_valid(form)

class UpdatePost(generic.UpdateView, LoginRequiredMixin):
    template_name = 'blog/posts-create.html'
    model = Post
    #fields = ("title","content")
    form_class = PostForm
    login_url = '/login/'
    redirect_field_name ='blog/post-detail.html'

    def form_valid(self, form):
        print(form.instance)
        form.instance.user = self.request.user
        return super(UpdatePost, self).form_valid(form)