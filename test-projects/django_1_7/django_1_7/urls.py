from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_1_7.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Enable Slumber
    (r'^slumber/', include('slumber.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
