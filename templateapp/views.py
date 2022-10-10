from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>this is home page</h1>')

def House(request):
    return render(request,'app/home.html')

def death(request):
    context={'name':'prashanth'}
    return render(request,'app/prasad.html',context)