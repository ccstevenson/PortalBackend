from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'portal_backend.views.home', name='home'),
                       url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),

                       # REST framework login and logout views.
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
