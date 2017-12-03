from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.login, name="login"),
    url(r'^register/$', views.register, name="register"),
    url(r'^main/', include('main.urls'))
   # url(r'^register/$', views.register, name='register')
]