#coding:utf-8
from django.conf.urls import include, url
from api.cls import index

urlpatterns = [
	url(r'^$', index.Index.as_view()),
]
