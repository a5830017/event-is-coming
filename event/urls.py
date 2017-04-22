from django.conf.urls import url

from . import views

app_name = 'event'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^new_event$', views.new_event, name='new_event'),
]
