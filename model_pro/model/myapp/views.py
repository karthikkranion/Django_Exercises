from django.shortcuts import render
# from django.contrib.auth.models import User
from .models import Page,Post,Song,User
# Create your views here.

def home(request):
    return render(request,'myapp/home.html')

def show_user_data(request):
    users =User.objects.all()
    users1 =User.objects.filter(email='raj@gmail.com')
    users2 =User.objects.filter(page__pcat='Money')
    return render(request,'myapp/user.html',{'users':users,'users1':users1,'users2':users2})

def show_page_data(request):
    pages =Page.objects.all()
    return render(request,'myapp/page.html',{'pages':pages})

def show_post_data(request):
    posts =Post.objects.all()
    return render(request,'myapp/post.html',{'posts':posts})

def show_song_data(request):
    songs =Song.objects.all()
    return render(request,'myapp/song.html',{'songs':songs})