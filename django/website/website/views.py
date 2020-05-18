from django.http import HttpResponse
from django.shortcuts import render

def register(request):
    #return HttpResponse('register')
    return render(request,'register.html')


def login(request):
    #return HttpResponse("login")
    return render(request,'login.html')

def fitness(request):
    return render(request,'fitness.html')
