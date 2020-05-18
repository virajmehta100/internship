from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^login/$',views.login_view,name="login"),
   #/food/
    url(r'^$', views.index, name='index'),
   #/food/1/
    url(r'^(?P<food_id>[0-9]+)/$',views.detail,name='detail'),
]

