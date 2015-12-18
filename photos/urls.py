from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^import/$', views.import_photo, name='import_photo'),
    url(r'^search/$', views.search_photo, name='search_photo'),
    url(r'^list/$', views.list_photos, name='list_photos'),
    url(r'^delete/$', views.delete_photos, name='delete_photos'),
]