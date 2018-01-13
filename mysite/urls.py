from django.conf.urls import url, include
from django.contrib import admin
admin.autodiscover()

from mysite import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('^$', views.Login),
    url(r'^books/', include('books.urls')),
    #url('^Homepage/$', views.Homepage),
]