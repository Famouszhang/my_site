from django.conf.urls import url
from django.contrib import admin
from blog import views
from django.urls import path

app_name = 'blog'
urlpatterns = [
 path(r'', views.home_page, name='home_page'),
]