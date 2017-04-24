#coding:utf-8
from django.conf.urls import include, url
from root.cls import index

urlpatterns = [
	url(r'^$', index.Index.as_view()),
]
