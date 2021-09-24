"""ringly URL Configuration

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

from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),


    path('',login_page),
    path('dashboard/',dashboard_page, name='dashboard'),
    path('user/add',create_user_page, name='adduser'),
    # path('user/details/<uid>/',user_details,name='detial_user'),
    path('delete/<uid>/<key>/<url>/',delete_obj, name='delete'),    

    path('ringtones/',list_ringtone, name='list_ringtone'),
    path('ringtone/add/',add_ringtone, name='addringtone'),

    

]
