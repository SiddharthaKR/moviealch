from django.db.models import query
from django.db.models.query import RawQuerySet
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .decorators import *



@csrf_exempt
def loginuser(request):
    context={}
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
           messages.info(request,"Username or password incorrect")             
     
    return render(request,'login.html',context)


def logoutUser(request):
    logout(request)
    return redirect("/")



    
@authenticated_user
def index(request):
    s=movies.objects.all()
    v=watchlist.objects.get(user=request.user)
    t=v.watchlist1.all()
    print(s)
    return render(request,'home.html',{"s":s,"t":t})

    

@csrf_exempt
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        
        s=User.objects.create_user(username,email,password)
        
        s.save()
        watch=watchlist(user=s)
        watch.save()
        return redirect('/login')
    return render(request,'signup.html')


def addwatchlist(request,pk):
    s=watchlist.objects.get(user=request.user)
    m=movies.objects.get(id=pk)
    s.watchlist1.add(m)
    s.save()
    return redirect('/')



def search(request):
    if request.method=="GET":
        query=request.GET["query"]
        s=movies.objects.filter(name__contains=query)
        return render(request,"search.html",{"hello":s})

    return render(request,"home.html")