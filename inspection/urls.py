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
    DashboardViewDailyInspection,

    ShelfInspectionListView,
    ShelfInspectionDetailAndRecordListDisplayView,
    ShelfInspectionDetailAndRecordListEditView,
    ShelfInspectionCreateView,
    ShelfGradientInspectionView,
    ShelfDetailView,
    ShelfListView,
    ShelfInspectionRecordDetailView,
    ShelfInspectionRecordUpdateView,
    ShelfInspectionRecordListView,
    ShelfAnnualInspectionListView,
    ShelfAnnualInspectionDetailView,
    ShelfAnnualInspectionCreateView,
    ShelfAnnualInspectionUpdateView,
    ShelfInspectionRecordBatchCreateView,

    RehearsalListView,
    RehearsalDetailView,
    RehearsalUpdateView,
    RehearsalCreateView,

    PIListView,
    PICreateView,
    PIDetailView,
    PIUpdateView,
    WHPIListView,
    WHPICreateView,
    WHPIDetailView,
    WHPIUpdateView,
    RTPIListView,
    RTPICreateView,
    RTPIDetailView,
    RTPIUpdateView,

    ExtinguisherInspectionListView,
    ExtinguisherInspectionCreateView,
    ExtinguisherInspectionDetailView,
    ExtinguisherInspectionUpdateView,

    HydrantInspectionListView,
    HydrantInspectionCreateView,
    HydrantInspectionDetailView,
    HydrantInspectionUpdateView,

    StorageSecurityView,

)

urlpatterns = [
    url(r'^officeinspection$', OfficeInspectionListView.as_view(), name='OfficeInspection_list'),
    url(r'^officeinspection/create$', OfficeInspectionCreateView.as_view(), name='OfficeInspection_create'),
    url(r'^officeinspection/(?P<pk>\d+)/$', OfficeInspectionDetailView.as_view(), name='OfficeInspection_detail'), 

    url(r'^dailyinspection$', DailyInspectionListView.as_view(), name='dailyinspection_list'),
    url(r'^dailyinspection/create$', DailyInspectionCreateView.as_view(), name='dailyinspection_create'),
    url(r'^dailyinspection/(?P<pk>\d+)/$', DailyInspectionDetailView.as_view(), name='dailyinspection_detail'),  
    url(r'^dailyinspection/(?P<pk>\d+)/update/$', DailyInspectionUpdateView.as_view(), name='dailyinspection_update'),
    url(r'^dailyinspection/(?P<pk>\d+)/delete/$', DailyInspectionDeleteView.as_view(), name='dailyinspection_delete'),
    url(r'^dailyinspection/stat$', DailyInspectionStatView.as_view(), name='daily_inspection_stat'),   
    url(r'^linechartjason/$', LineChartJSONView.as_view(), name='line_chart_json'),   
    url(r'^linechartjasonoverdue$', OverdueChartJSONView.as_view(), name='line_chart_json_overdue'),   
    url(r'^linechartjasonlasts$', LastsChartJSONView.as_view(), name='line_chart_json_lasts'),   
    url(r'^linechartjasoncompare$', CompareChartJSONView.as_view(), name='line_chart_json_compare'),   
    url(r'^dashboardview/api/dailyinspection/$', DashboardViewDailyInspection.as_view()),   

    url(r'^storagesec$', StorageSecurityView.as_view(), name='storage_sec'),

    url(r'^shelfinspection$', ShelfInspectionListView.as_view(), name='shelf_inspection_list'),      
    url(r'^shelfinspection/(?P<pk>\d+)/$', ShelfInspectionDetailAndRecordListDisplayView.as_view(), name='shelf_inspection_detail_and_record_list_display'),
    url(r'^shelfinspection/(?P<pk>\d+)/edit/$', ShelfInspectionDetailAndRecordListEditView.as_view(), name='shelf_inspection_detail_and_record_list_edit'),  
    url(r'^shelfinspection/create$', ShelfInspectionCreateView.as_view(), name='shelf_inspection_create'),  
    url(r'^shelfinspection/(?P<pk>\d+)/gradient/$', ShelfGradientInspectionView.as_view(), name='shelf_gradient_inspection'),  

    url(r'^shelfinspectionrecord/(?P<pk>\d+)/$', ShelfInspectionRecordDetailView.as_view(), name='shelf_inspection_record_detail'),  
    url(r'^shelfinspectionrecord/(?P<pk>\d+)/update/$', ShelfInspectionRecordUpdateView.as_view(), name='shelf_inspection_record_update'), 
    url(r'^shelfinspectionrecord/abnormal/$', ShelfInspectionRecordListView.as_view(), {'status':'abnormal'}, name='shelf_inspection_record_list_abnormal'),  
    url(r'^shelfinspectionrecord/$', ShelfInspectionRecordListView.as_view(), name='shelf_inspection_record_list'), 
    url(r'^shelfinspectionrecord/(?P<inspection_id>\d+)/create$', ShelfInspectionRecordBatchCreateView.as_view(), name='shelf_inspection_record_batch_create'), 

    

    url(r'^shelf$', ShelfListView.as_view(), name='shelf_list'),
    url(r'^shelf/(?P<pk>\d+)/$', ShelfDetailView.as_view(), name='shelf_detail'),  

    url(r'^shelfannualinspection$', ShelfAnnualInspectionListView.as_view(), name='shelf_annualinspectin_list'),   
    url(r'^shelfannualinspection/create$', ShelfAnnualInspectionCreateView.as_view(), name='shelf_annualinspectin_create'),  
    url(r'^shelfannualinspection/(?P<pk>\d+)/$', ShelfAnnualInspectionDetailView.as_view(), name='shelf_annualinspectin_detail'),  
    url(r'^shelfannualinspection/(?P<pk>\d+)/update/$', ShelfAnnualInspectionUpdateView.as_view(), name='shelf_annualinspectin_update'),  

    url(r'^rehearsal$', RehearsalListView.as_view(), name='rehearsal_list'),
    url(r'^rehearsal/create$', RehearsalCreateView.as_view(), name='rehearsal_create'),  
    url(r'^rehearsal/detail/(?P<pk>\d+)/$', RehearsalDetailView.as_view(), name='rehearsal_detail'),  
    url(r'^rehearsal/update/(?P<pk>\d+)/$', RehearsalUpdateView.as_view(), name='rehearsal_update'),  

    url(r'^pi$', PIListView.as_view(), name='pi_list'),
    url(r'^pi/create$', PICreateView.as_view(), name='pi_create'),
    url(r'^pi/(?P<pk>\d+)/$', PIDetailView.as_view(), name='pi_detail'),  
    url(r'^pi/update/(?P<pk>\d+)/$', PIUpdateView.as_view(), name='pi_update'),

    url(r'^whpi$', WHPIListView.as_view(), name='whpi_list'),
    url(r'^whpi/create$', WHPICreateView.as_view(), name='whpi_create'),
    url(r'^whpi/(?P<pk>\d+)/$', WHPIDetailView.as_view(), name='whpi_detail'),  
    url(r'^whpi/update/(?P<pk>\d+)/$', WHPIUpdateView.as_view(), name='whpi_update'),

    url(r'^rtpi$', RTPIListView.as_view(), name='rtpi_list'),
    url(r'^rtpi/create$', RTPICreateView.as_view(), name='rtpi_create'),
    url(r'^rtpi/(?P<pk>\d+)/$', RTPIDetailView.as_view(), name='rtpi_detail'),  
    url(r'^rtpi/update/(?P<pk>\d+)/$', RTPIUpdateView.as_view(), name='rtpi_update'),   

    url(r'^extinguisherinspection$', ExtinguisherInspectionListView.as_view(), name='extinguisherinspection_list'),
    url(r'^extinguisherinspection/create$', ExtinguisherInspectionCreateView.as_view(), name='extinguisherinspection_create'),
    url(r'^extinguisherinspection/(?P<pk>\d+)/$', ExtinguisherInspectionDetailView.as_view(), name='extinguisherinspection_detail'),  
    url(r'^extinguisherinspection/(?P<pk>\d+)/update/$', ExtinguisherInspectionUpdateView.as_view(), name='extinguisherinspection_update'),

    url(r'^hydrantinspection$', HydrantInspectionListView.as_view(), name='hydrantinspection_list'),
    url(r'^hydrantinspection/create$', HydrantInspectionCreateView.as_view(), name='hydrantinspection_create'),
    url(r'^hydrantinspection/(?P<pk>\d+)/$', HydrantInspectionDetailView.as_view(), name='hydrantinspection_detail'),  
    url(r'^hydrantinspection/(?P<pk>\d+)/update/$', HydrantInspectionUpdateView.as_view(), name='hydrantinspection_update'),  

]