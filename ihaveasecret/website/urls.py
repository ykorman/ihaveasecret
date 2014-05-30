from django.conf.urls import patterns, url

from website import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^view/$', views.view_messages, name='view_messages'),
    url(r'^message/(?P<message_id>\d+)/$', views.view_message, name='view_message'),
    url(r'^write/$', views.write_message, name='write_message'),
)