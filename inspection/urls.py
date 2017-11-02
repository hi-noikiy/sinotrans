from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import (
    OfficeInspectionListView,
    OfficeInspectionDetailView,
    OfficeInspectionCreateView,
    DailyInspectionListView,
    DailyInspectionUpdateView,
    DailyInspectionDetailView,
    DailyInspectionCreateView,
    DailyInspectionDeleteView,
    shelf_inspection_StatView,
    shelf_inspection_ListView,
    shelf_inspection_DetailView,
    shelf_inspection_CreateView,
    ShelfDetailView,
    ShelfListView,
    ShelfInspectionRecordDetailView,

)

urlpatterns = [
    url(r'^officeinspection$', OfficeInspectionListView.as_view(), name='OfficeInspection_list'),
    url(r'^officeinspection/create$', OfficeInspectionCreateView.as_view(), name='OfficeInspection_create'),
    url(r'^officeinspection/(?P<pk>\d+)/$', OfficeInspectionDetailView.as_view(), name='OfficeInspection_detail'), 

    url(r'^dailyinspection$', DailyInspectionListView.as_view(), name='dailyinspection_list'),
    url(r'^dailyinspection/create$', DailyInspectionCreateView.as_view(), name='dailyinspection_create'),
    url(r'^dailyinspection/(?P<pk>\d+)/$', DailyInspectionDetailView.as_view(), name='dailyinspection_detail'),  
    url(r'^dailyinspection/update/(?P<pk>\d+)/$', DailyInspectionUpdateView.as_view(), name='dailyinspection_update'),
    url(r'^dailyinspection/(?P<pk>\d+)/delete/$', DailyInspectionDeleteView.as_view(), name='dailyinspection_delete'),

    url(r'^shelfinspectionlist$', shelf_inspection_ListView.as_view(), name='shelf_inspection_list'),  
    url(r'^shelfinspectiondetail/(?P<pk>\d+)/$', shelf_inspection_DetailView.as_view(), name='shelf_inspection_detail'),  
    url(r'^shelfinspectioncreate$', shelf_inspection_CreateView.as_view(), name='shelf_inspection_create'),  
    url(r'^shelfinspectionstat$', shelf_inspection_StatView.as_view(), name='shelf_inspection_stat'),   

    url(r'^shelfinspectionrecorddetail/(?P<pk>\d+)/$', ShelfInspectionRecordDetailView.as_view(), name='shelf_inspection_record_detail'),  

    url(r'^shelfdetail/(?P<pk>\d+)/$', ShelfDetailView.as_view(), name='shelf_detail'),  
    url(r'^shelflist$', ShelfListView.as_view(), name='shelf_list'),



]