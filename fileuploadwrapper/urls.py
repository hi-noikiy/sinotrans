from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import upload_file, upload_status

urlpatterns = [

    url(r'^uploadfile', upload_file, name='upload_file'),
    url(r'^upload_status$', upload_status, name='upload_status'),

]