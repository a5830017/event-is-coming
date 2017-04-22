from django.conf.urls import url

from event import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^create$', views.create_event, name='create_event'),
    #url(r'^add$', views.add_event, name='add_event'),
    # url(r'^admin/', include(admin.site.urls)),
]