from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import (
    ForkliftListView,
    ForkliftDetailView,
    ForkliftUpdateView,
    VehicleListView,
    ForkliftRepairListView,
    ForkliftRepairDetailView,
    ForkliftRepairUpdateView,
    ForkliftRepairCreateView,
    ForkliftCreateView,
    ForkliftMaintDetailView,
    ForkliftMaintUpdateView,
    ForkliftMaintListView,
    ForkliftMaintCreateView,
    ForkliftAnnualInspectionListView,
    ForkliftAnnualInspectionCreateView,
    ForkliftAnnualInspectionDetailView,
    ForkliftAnnualInspectionUpdateView,
    VehicleDetailView,
    VehicleInspectionListView,
    VehicleInspectionDetailView,
    VehicleInspectionCreateView,
    VehicleInspectionUpdateView,
    DriverListView,
    DriverDetailView,
    TransportationKPIListDisplayView,
    TransportationKPIListEditView,
    TransportationKPICreateView,
    TransportationKPIDetailView,  
    TransportationKPIUpdateView,

    TransportSecurityView,
)

urlpatterns = [
    url(r'^transportsec$', TransportSecurityView.as_view(), name='transport_security'),  

    url(r'^vehicle$', VehicleListView.as_view(), name='vehicle_list'),  
    url(r'^vehicle/detail/(?P<pk>\d+)/$', VehicleDetailView.as_view(), name='vehicle_detail'),    
    url(r'^vehicle/inspection$', VehicleInspectionListView.as_view(), name='vehicle_inspection_list'),  
    url(r'^vehicle/inspection/create$', VehicleInspectionCreateView.as_view(), name='vehicle_inspection_create'),  
    url(r'^vehicle/inspection/detail/(?P<pk>\d+)/$', VehicleInspectionDetailView.as_view(), name='vehicle_inspection_detail'),
    url(r'^vehicle/inspection/update/(?P<pk>\d+)/$', VehicleInspectionUpdateView.as_view(), name='vehicle_inspection_update'),

    url(r'^driver$', DriverListView.as_view(), name='driver_list'),  
    url(r'^driver/detail/(?P<pk>\d+)/$', DriverDetailView.as_view(), name='driver_detail'),    

    url(r'^transportaionkpi$', TransportationKPIListDisplayView.as_view(), name='transportationkpi_list_display'),  
    url(r'^transportaionkpi/edit$', TransportationKPIListEditView.as_view(), name='transportationkpi_list_edit'),      
    url(r'^transportaionkpi/detail/(?P<pk>\d+)/$', TransportationKPIDetailView.as_view(), name='transportationkpi_detail'),   
    url(r'^transportaionkpi/update/(?P<pk>\d+)/$', TransportationKPIUpdateView.as_view(), name='transportationkpi_update'),   
    url(r'^transportaionkpi/create/(?P<year>\d+)/(?P<month>\d+)/(?P<project>\w+)/$', TransportationKPICreateView.as_view(), name='transportationkpi_create'),   
    
    url(r'^forklift$', ForkliftListView.as_view(), name='forklift_list'),  
    url(r'^forklift/create$', ForkliftCreateView.as_view(), name='forklift_create'),  
    url(r'^forklift/detail/(?P<pk>\d+)/$', ForkliftDetailView.as_view(), name='forklift_detail'),    
    url(r'^forklift/update/(?P<pk>\d+)/$', ForkliftUpdateView.as_view(), name='forklift_update'),    
    url(r'^forkliftrepair$', ForkliftRepairListView.as_view(), name='forklift_repair_list'), 
    url(r'^forkliftrepair/create$', ForkliftRepairCreateView.as_view(), name='forklift_repair_create'), 
    url(r'^forkliftrepair/detail/(?P<pk>\d+)/$', ForkliftRepairDetailView.as_view(), name='forklift_repair_detail'), 
    url(r'^forkliftrepair/update/(?P<pk>\d+)/$', ForkliftRepairUpdateView.as_view(), name='forklift_repair_update'), 
    url(r'^forkliftmaint/detail/(?P<pk>\d+)/$', ForkliftMaintDetailView.as_view(), name='forklift_maint_detail'), 
    url(r'^forkliftmaint/update/(?P<pk>\d+)/$', ForkliftMaintUpdateView.as_view(), name='forklift_maint_update'),     
    url(r'^forkliftmaint/$', ForkliftMaintListView.as_view(), name='forklift_maint_list'),  
    url(r'^forkliftmaint/create$', ForkliftMaintCreateView.as_view(), name='forklift_maint_create'),  
    url(r'^forkliftannualinspection$', ForkliftAnnualInspectionListView.as_view(), name='forklift_annual_inspection_list'),  
    url(r'^forkliftannualinspection/create$', ForkliftAnnualInspectionCreateView.as_view(), name='forklift_annual_inspection_create'),  
    url(r'^forkliftannualinspection/detail/(?P<pk>\d+)/$', ForkliftAnnualInspectionDetailView.as_view(), name='forklift_annual_inspection_detail'),    
    url(r'^forkliftannualinspection/update/(?P<pk>\d+)/$', ForkliftAnnualInspectionUpdateView.as_view(), name='forklift_annual_inspection_update'),      
]