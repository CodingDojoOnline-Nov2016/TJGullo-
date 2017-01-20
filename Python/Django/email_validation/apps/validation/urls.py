from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^validation$', views.validation),
    url(r'^success$', views.success),
]
