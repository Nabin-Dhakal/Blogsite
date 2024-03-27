from django.shortcuts import render, redirect  
from django.contrib import messages  
from .models import blogs  

def index(request):
    posts = blogs.objects.all()  
    return render(request, "index.html", {'posts': posts}) 

def create(request):
    return render(request, "create.html")

def save(request):
    if request.method == "POST":
        title = request.POST.get('title')  
        desc = request.POST.get('desc')
        form = blogs.objects.create(Title=title,Desc=desc)  
        form.save()
    return render(request, "create.html")

def post(request,pk):
    posts = blogs.objects.get(id=pk)
    return render(request,"post.html",{'posts': posts})