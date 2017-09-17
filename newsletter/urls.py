from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import ArticleListView, ArticleDetailView

urlpatterns = [

    url(r'^$', ArticleListView.as_view(), name='ArticleListView'),
    #url(r'^create$', CrowdfundingCreateView.as_view(), name='Article_create'),
    url(r'^(?P<pk>\d+)/$', ArticleDetailView.as_view(), name='Article_detail'), 
]