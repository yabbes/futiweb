from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^en/', views.en, name="en"),
    url(r'^de/', views.de, name="de"),
    url(r'^fr/', views.fr, name="fr"),
    url(r'^es/', views.es, name="es"),
    url(r'^it/', views.it, name="it"),
    url(r'^$', views.main, name="main")
]
