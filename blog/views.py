from django.shortcuts import render, get_list_or_404

from .models import Blog


def all_blogs(requests):
    all_blog = Blog.objects.all()
    return render(requests, 'blog/all_blog.html', {'all_blog': all_blog})


def details(requests, blog_id):
    blog = get_list_or_404(Blog, pk=blog_id)
    return render(requests, 'blog/details.html', {'blog': blog[0]})
