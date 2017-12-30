from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth import views as auth_views


urlpatterns = [
 
    url(r'^logout/$', auth_views.logout, name='logout'), 
    url(r'^login/$', auth_views.login, name='login'), 
    url(r'^password/change/$', auth_views.password_change, {'post_change_redirect': reverse_lazy('auth_password_change_done2')}, name='auth_password_change2'), 
    url(r'^password/change/done/$', auth_views.password_change_done, name='auth_password_change_done2'), 
]