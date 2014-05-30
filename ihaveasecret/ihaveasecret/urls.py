from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ihaveasecret.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^web/', include('website.urls', namespace="web")),
    url(r'^admin/', include(admin.site.urls)),
    
)
