from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import (
    ForkliftListView,
    ForklifDetailView,
    VehicleInpspectionListView,
    VehicleInpspectionDetailView,
    TransportationKPIListDisplayView,
    TransportationKPIListEditView,
    TransportationKPICreateView,
    TransportationKPIDetailView,  
    TransportationKPIUpdateView,
)

urlpatterns = [
    url(r'^forkliftlist$', ForkliftListView.as_view(), name='forklift_list'),  
    url(r'^forkliftdetail/(?P<pk>\d+)/$', ForklifDetailView.as_view(), name='forklift_detail'),
    url(r'^vehiclelist$', VehicleInpspectionListView.as_view(), name='vehicle_inspection_list'),  
    url(r'^vehicledetail/(?P<pk>\d+)/$', VehicleInpspectionDetailView.as_view(), name='vehicle_inspection_detail'),    
    url(r'^transportaionkpilistdisplay$', TransportationKPIListDisplayView.as_view(), name='transportationkpi_list_display'),  
    url(r'^transportaionkpilistedit$', TransportationKPIListEditView.as_view(), name='transportationkpi_list_edit'),      
    url(r'^transportaionkpidetail/(?P<pk>\d+)/$', TransportationKPIDetailView.as_view(), name='transportationkpi_detail'),   
    url(r'^transportaionkpiupdate/(?P<pk>\d+)/$', TransportationKPIUpdateView.as_view(), name='transportationkpi_update'),   
    url(r'^transportaionkpicreate/(?P<year>\d+)/(?P<month>\d+)/$', TransportationKPICreateView.as_view(), name='transportationkpi_create'),   
]