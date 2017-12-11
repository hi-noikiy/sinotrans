from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import (
    ForkliftListView,
    ForkliftDetailView,
    VehicleListView,
    ForkliftRepairListView,
    ForkliftRepairDetailView,
    VehicleDetailView,
    VehicleInspectionListView,
    VehicleInspectionDetailView,
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
    url(r'^vehicle/inspection/detail/(?P<pk>\d+)/$', VehicleInspectionDetailView.as_view(), name='vehicle_inspection_detail'),
    url(r'^driver$', DriverListView.as_view(), name='driver_list'),  
    url(r'^driver/detail/(?P<pk>\d+)/$', DriverDetailView.as_view(), name='driver_detail'),    
    url(r'^transportaionkpi$', TransportationKPIListDisplayView.as_view(), name='transportationkpi_list_display'),  
    url(r'^transportaionkpi/edit$', TransportationKPIListEditView.as_view(), name='transportationkpi_list_edit'),      
    url(r'^transportaionkpi/detail/(?P<pk>\d+)/$', TransportationKPIDetailView.as_view(), name='transportationkpi_detail'),   
    url(r'^transportaionkpi/update/(?P<pk>\d+)/$', TransportationKPIUpdateView.as_view(), name='transportationkpi_update'),   
    url(r'^transportaionkpi/create/(?P<year>\d+)/(?P<month>\d+)/$', TransportationKPICreateView.as_view(), name='transportationkpi_create'),   
    url(r'^forklift$', ForkliftListView.as_view(), name='forklift_list'),  
    url(r'^forklift/detail/(?P<pk>\d+)/$', ForkliftDetailView.as_view(), name='forklift_detail'),    
    url(r'^forkliftrepair$', ForkliftRepairListView.as_view(), name='forklift_repair_list'), 
    url(r'^forkliftrepair/detail/(?P<pk>\d+)/$', ForkliftRepairDetailView.as_view(), name='forklift_repair_detail'), 
]