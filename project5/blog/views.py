
from django.views.generic import ListView  # new
from .models import Post
from django.shortcuts import get_object_or_404, render

class PostList(ListView):  # new
    model = Post
    template_name = "home.html"

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post_detail.html", {"post": post})