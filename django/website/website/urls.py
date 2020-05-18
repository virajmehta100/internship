from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^calculator/',include('calculator.urls')),
    url(r'^login/$',views.login),
    url(r'^fitness/$',views.fitness),
    url(r'^$',views.register),
]
