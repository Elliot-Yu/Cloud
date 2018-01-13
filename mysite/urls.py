from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

admin.autodiscover()

from mysite import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('^$', RedirectView.as_view(url='/books')),
    url(r'^books/', include('books.urls')),
    #url('^Homepage/$', views.Homepage),
]