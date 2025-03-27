from django.urls import path
from .views import PostList, post_detail

urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path("post/<int:pk>/", post_detail, name="post_detail"),

]