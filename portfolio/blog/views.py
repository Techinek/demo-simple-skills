from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def all_blogs(request):
    posts = BlogPost.objects.order_by('-created_at')
    return render(request, 'blog/all_blogs.html', {'posts': posts})

def detail_post(request, post_slug):
    post = get_object_or_404(BlogPost, slug=post_slug)
    return render(request, 'blog/detail.html', {'post': post})
