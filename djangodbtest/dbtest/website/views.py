from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        'author': 'first author',
        'title': 'first title',
        'content': "first content",
        'date': 'Aug. 27th, 2020'
    },
    {
        'author': 'second author',
        'title': 'second title',
        'content': "second content",
        'date': 'Aug. 30th, 2020'
    }
]

info = [
    {
        'myinfo': 'dad',
        'second': 'mom'
    }
]


def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'website/index.html', context)

def api(request):
    return render(request, 'website/api.html')
