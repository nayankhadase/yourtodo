from django.shortcuts import redirect, render
from .models import Task
from django.contrib.auth.models import User , auth
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

def Loadlogin(request):
    return render(request,'login.html')

def Login(request):
    if request.method == "POST":
        vuser = request.POST.get('user')
        vpass = request.POST.get('password')
        login_user = auth.authenticate(username=vuser, password=vpass)
        if login_user is not None:
            auth.login(request,login_user)
            return redirect("/home")
        else:
            return redirect("/")
    else:
        return HttpResponse("404 Error...")


def Userlogout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect("/")
    else:
        return HttpResponse("404 Error...")

def Loadsignup(request):
    return render(request,'signup.html')

def Signup(request):
    if request.method == "POST":
        vuser = request.POST.get('user')
        vfname = request.POST.get('fname')
        vlname = request.POST.get('lname')
        vpass = request.POST.get('password')
        vemail = request.POST.get('email')
        if User.objects.filter(username=vuser).exists():
            messages.info(request,"Username is already exits")
            return redirect("/signuppage")
        else:
            new_user=User.objects.create_user(username=vuser,first_name=vfname,last_name=vlname,password=vpass,email=vemail)
            new_user.save()
            messages.info(request,"Account created successfully")
            return redirect('/')
    else:
        return HttpResponse("404 Error...")



def Home(request):
    if request.user.is_authenticated:
        objtask=Task.objects.all()
        return render(request,'home.html',{'task':objtask})
    else:
        return redirect("/")

def Inserttask(request):
    if request.user.is_authenticated :
        if request.method == "POST":
            vtask=request.POST.get('task')
            userdata=request.POST.get('user_data')
            objtask=Task()
            objtask.task=vtask
            objtask.user_data=userdata
            objtask.save()
            objtask=Task.objects.all()
            return render(request,'usertask.html',{'task':objtask})
        else:
            return HttpResponse("404 Error...")
    else:
        return redirect("/")



def Delete(request,sid):
    if request.user.is_authenticated :
        objtask=Task.objects.get(id=sid)
        objtask.delete()
        return redirect('/home')
    else:
        return redirect("/")



def Edit(request,sid):
    if request.user.is_authenticated :
        objtask=Task.objects.get(id=sid)
        return render(request,'edittask.html',{'task':objtask})
    else:
        return redirect("/")

def Update(request,sid):
    if request.user.is_authenticated :
        if request.method == "POST":
            vtask=request.POST.get('task')
            objtask=Task.objects.get(id=sid)
            objtask.task=vtask
            objtask.save()
            return redirect('/home')
        else:
            return HttpResponse("404 Error...")
    else:
        return redirect("/")