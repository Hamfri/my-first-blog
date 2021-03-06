from django.conf.urls import patterns,url
from blog import views 

urlpatterns = [
    url(r'^$', views.post_list,name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]