from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return  render(request,"login.html")


# Create your views here.
def register(request):
    if request.method == 'POST':
        uname = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"username already taken")
                return redirect ('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect ('register')
            else:

                 user = User.objects.create_user(username=uname,password=password,first_name=fname,last_name=lname,email=email)
                 user.save();
                 return redirect('login')

        else:
            messages.info(request, "password not matched")
            return redirect('register')
        return redirect('/')

    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')