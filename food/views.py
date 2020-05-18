from django.http import HttpResponse
from .models import veg
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect


def index(request):
    all_foods = veg.objects.all()
    html = ''
    for v in all_foods:
        url = 'food/' + str(v.id) + '/'
        html += '<a href = " ' + url + '">' + v.recipe + '</a><br>'
    return HttpResponse(html)
def detail(request,food_id):
    return HttpResponse("<h2>Details for food id : " + str(food_id) + "</h2>")


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
    if form.is_valid():
        return HttpResponseRedirect('/thanks/')


    else:
        form = AuthenticationForm()
    return render(request,'food/login.html',{'form':form})
