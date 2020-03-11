from django.shortcuts import render


def all_blogs(requests):
    return render(requests, 'blog/all_blog.html', {})
