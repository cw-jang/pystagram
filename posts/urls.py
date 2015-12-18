from django.conf.urls import url

from .import views


urlpatterns = [

    url(r'^(?P<pk>[0-9]+)/$', views.view_post, name='view_post'),
    url(r'^list/$', views.list_posts, name='list_posts'),
    url(r'^create/$', views.create_post, name='create_post'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.edit_post, name='edit_post'),
]