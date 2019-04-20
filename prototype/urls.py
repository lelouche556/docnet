from django.conf.urls import include, url
from django.urls import path, include
from healthnet import urls
from django.contrib import admin

admin.autodiscover()

urlpatterns =[
    # Examples:
    # url(r'^$', 'prototype.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^healthnet/', include('healthnet.urls', namespace='healthnet')),
    # url(r'^admin/', include(admin.site.urls)),
    path('admin/', admin.site.urls),
    path('',include(urls)),

]
