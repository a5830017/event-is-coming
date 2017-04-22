from django.conf.urls import include, url

from event import views

urlpatterns = [
    url(r'^', include('event.urls')),
]