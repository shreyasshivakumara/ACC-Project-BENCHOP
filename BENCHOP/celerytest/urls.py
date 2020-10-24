"""celerytest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from hello import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('index/',views.index),
    path ('index/pa1', views.pa1),
    path ('index/pb1', views.pb1),
    path ('index/pc1', views.pc1),
    path ('index/pa2', views.pa2),
    path ('index/pb2', views.pb2),
    path ('index/pc2', views.pc2),

]
