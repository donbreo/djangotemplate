from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from . import views


urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.home),
	path('contact/', views.contact),
]
