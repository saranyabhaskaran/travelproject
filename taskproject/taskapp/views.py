from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from . models import Place
from .models import team


def home(request):
    obj=Place.objects.all()
    tm=team.objects.all()
    return render(request,"index.html",{'result':obj,'res':tm})

#def operations(request):'num2'])
  #  a=x+y
  #  b=x-y
  # c=x*y
   # d=x/y
  #  x=int(request.GET['num1'])
  #  y=int(request.GET[
    #return render(request,"result.html",{'add':a,'sub':b,'mul':c,'div':d})




