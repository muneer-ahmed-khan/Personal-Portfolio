from django.shortcuts import render

from .models import Blog


def all_blogs(requests):
    all_blog = Blog.objects.all()
    return render(requests, 'blog/all_blog.html', {'all_blog': all_blog})
