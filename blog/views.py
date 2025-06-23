from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def view_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/view_post.html', {'post': post})
