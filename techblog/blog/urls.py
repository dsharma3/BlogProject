from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/(?P<pk>\d+)/detail',views.PostDetail.as_view(),name='post-detail'),
    path('accounts/', include("django.contrib.auth.urls")),
    path("post/create", views.CreatePost.as_view(),name='createpost')
]
