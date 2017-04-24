#coding:utf-8
"""notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from home.cls import index #首页

from root import root_url
from home import home_url
from api import api_url
from logs import logs_url

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', index.Index.as_view()),
	url(r'^root/', include(root_url)),
	url(r'^home/', include(home_url)),
	url(r'^api/', include(api_url)),
	url(r'^logs/', include(logs_url)),
]
