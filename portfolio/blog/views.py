from django.shortcuts import render
from .models import BlogPost

def all_blogs(request):
    posts = BlogPost.objects.order_by('-created_at')
    return render(request, 'blog/all_blogs.html', {'posts': posts})
