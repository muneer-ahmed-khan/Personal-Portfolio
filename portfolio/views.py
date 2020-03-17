from django.shortcuts import render

from .models import Project


def home(requests):
    project = Project.objects.all()
    urls = ['core:corehome', 'portfolio:home', 'todohome']
    projects = zip(project, urls)
    return render(requests, 'portfolio/home.html', {'projects': projects})
