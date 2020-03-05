from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Rintu',
        'title': 'Python Programing',
        'content': 'First Post',
        'date_posted': 'March 3,2019'
    },
    {
        'author': 'Rijo',
        'title': 'CA ',
        'content': 'Second Post',
        'date_posted': 'March 4,2019'
    }
]


def home(request):
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


def about(request):
    return render(request, 'blog/about.html')
