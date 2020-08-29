from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request, *args,  **kwargs):
    data = {
        'userinfo': request.user,
    }
    return render(request, "trydjango/index.html", data)