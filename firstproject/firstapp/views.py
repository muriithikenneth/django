from django.shortcuts import render
from .models import Post
# Create your views here.
from django.http import HttpResponse

# def hello(request):
#     return HttpResponse('Hello world')

def home(request):
    context = {
        'title': 'homepage',
        'description':'welcome to the home page! Here you can find the latest update and feature of the website.',
        
    }
    return render(request, 'home.html',context)


def about(request):
    context = {
        'title': 'About Me',
        'description': 'Learn more about me on this page. I am passionate about web development and enjoy creating useful applications.',
        
    }
    return render(request, 'about.html', context)

def contact(request):
    context = {
         'title': 'Contact Me',
        'description': 'Feel free to contact me through the form below or reach out to me on social media.',
        
    }
    return render(request, 'contact.html',context)

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})