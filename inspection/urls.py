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
    DailyInspectionStatView,
    LineChartJSONView,
    OverdueChartJSONView,
    LastsChartJSONView,
    CompareChartJSONView,
    ShelfInspectionListView,
    ShelfInspectionDetailView,
    ShelfInspectionDetailDisplayView,
    ShelfInspectionCreateView,
    ShelfGradientInspectionView,
    ShelfDetailView,
    ShelfListView,
    ShelfInspectionRecordDetailView,
    RehearsalListView,
    RehearsalDetailView,

    StorageSecurityView,

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
    url(r'^dailyinspectionstat$', DailyInspectionStatView.as_view(), name='daily_inspection_stat'),   
    url(r'^linechartjason/$', LineChartJSONView.as_view(), name='line_chart_json'),   
    url(r'^linechartjasonoverdue$', OverdueChartJSONView.as_view(), name='line_chart_json_overdue'),   
    url(r'^linechartjasonlasts$', LastsChartJSONView.as_view(), name='line_chart_json_lasts'),   
    url(r'^linechartjasoncompare$', CompareChartJSONView.as_view(), name='line_chart_json_compare'),   

    url(r'^storagesec$', StorageSecurityView.as_view(), name='storage_sec'),

    url(r'^shelfinspectionlist$', ShelfInspectionListView.as_view(), name='shelf_inspection_list'),  
    url(r'^shelfinspectiondetail/(?P<pk>\d+)/$', ShelfInspectionDetailView.as_view(), name='shelf_inspection_detail'),  
    url(r'^shelfinspectiondetaildisplay/(?P<pk>\d+)/$', ShelfInspectionDetailDisplayView.as_view(), name='shelf_inspection_detail_display'),
    url(r'^shelfinspectioncreate$', ShelfInspectionCreateView.as_view(), name='shelf_inspection_create'),  

    url(r'^shelfgradientinspection/(?P<pk>\d+)/$', ShelfGradientInspectionView.as_view(), name='shelf_gradient_inspection'),  

    url(r'^shelfinspectionrecorddetail/(?P<pk>\d+)/$', ShelfInspectionRecordDetailView.as_view(), name='shelf_inspection_record_detail'),  

    url(r'^shelfdetail/(?P<pk>\d+)/$', ShelfDetailView.as_view(), name='shelf_detail'),  
    url(r'^shelflist$', ShelfListView.as_view(), name='shelf_list'),

    url(r'^rehearsallist$', RehearsalListView.as_view(), name='rehearsal_list'),
    url(r'^rehearsaldetail/(?P<pk>\d+)/$', RehearsalDetailView.as_view(), name='rehearsal_detail'),  

]