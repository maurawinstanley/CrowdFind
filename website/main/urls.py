from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.lost, name="lost"),
    url(r'^found/', views.found, name="found"),
    url(r'^lost/', views.lost, name="lost"),
    url(r'^postItem/', views.postItem, name="postItem")
]