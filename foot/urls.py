from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^en/', views.en, name="en"),
    url(r'^$', views.main, name="start")
]
