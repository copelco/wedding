from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        name='auth_login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        name='auth_logout'),
    url(r'^$', 'rsvp.views.rsvp', name='rsvp'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^locations/', include('poi.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
