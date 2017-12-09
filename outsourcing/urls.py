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

    url(r'^vehiclelist$', VehicleListView.as_view(), name='vehicle_list'),  
    url(r'^vehicledetail/(?P<pk>\d+)/$', VehicleDetailView.as_view(), name='vehicle_detail'),    
    url(r'^vehicleinspectionlist$', VehicleInspectionListView.as_view(), name='vehicle_inspection_list'),  
    url(r'^vehicleinspectiondetail/(?P<pk>\d+)/$', VehicleInspectionDetailView.as_view(), name='vehicle_inspection_detail'),
    url(r'^driverlist$', DriverListView.as_view(), name='driver_list'),  
    url(r'^driverdetail/(?P<pk>\d+)/$', DriverDetailView.as_view(), name='driver_detail'),    
    url(r'^transportaionkpilistdisplay$', TransportationKPIListDisplayView.as_view(), name='transportationkpi_list_display'),  
    url(r'^transportaionkpilistedit$', TransportationKPIListEditView.as_view(), name='transportationkpi_list_edit'),      
    url(r'^transportaionkpidetail/(?P<pk>\d+)/$', TransportationKPIDetailView.as_view(), name='transportationkpi_detail'),   
    url(r'^transportaionkpiupdate/(?P<pk>\d+)/$', TransportationKPIUpdateView.as_view(), name='transportationkpi_update'),   
    url(r'^transportaionkpicreate/(?P<year>\d+)/(?P<month>\d+)/$', TransportationKPICreateView.as_view(), name='transportationkpi_create'),   
    url(r'^forkliftlist$', ForkliftListView.as_view(), name='forklift_list'),  
    url(r'^forkliftdetail/(?P<pk>\d+)/$', ForkliftDetailView.as_view(), name='forklift_detail'),    
    url(r'^forkliftrepairlist$', ForkliftRepairListView.as_view(), name='forklift_repair_list'), 
    url(r'^forkliftrepairdetail/(?P<pk>\d+)/$', ForkliftRepairDetailView.as_view(), name='forklift_repair_detail'), 
]