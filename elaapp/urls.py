from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^about/', views.about),
    url(r'^analy/', views.analy),
    url(r'^integration/', views.integration),
    url(r'^market/', views.market),
    url(r'^track/', views.track),
    url(r'^careers/', views.careers),
]