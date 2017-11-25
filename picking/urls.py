from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import (
        PickingbillAssignView,
        WaybillCompleteView,
        LineChartJSONView,
        PickingbillStatView,
)

urlpatterns = [
    url(r'^pickingbillassign$', PickingbillAssignView.as_view(), name='pickingbill_assign'),  
    url(r'^waybillcomplete$', WaybillCompleteView.as_view(), name='waybill_assign'),  
    url(r'^pickingbillstat$', PickingbillStatView.as_view(), name='pickingbill_stat'),  
    url(r'^linechartjason$', LineChartJSONView.as_view(), name='line_chart_json'),   
    # url(r'^transportaionkpilistdisplay$', TransportationKPIListDisplayView.as_view(), name='transportationkpi_list_display'),  
    # url(r'^transportaionkpilistedit$', TransportationKPIListEditView.as_view(), name='transportationkpi_list_edit'),      
    # url(r'^transportaionkpidetail/(?P<pk>\d+)/$', TransportationKPIDetailView.as_view(), name='transportationkpi_detail'),   
    # url(r'^transportaionkpiupdate/(?P<pk>\d+)/$', TransportationKPIUpdateView.as_view(), name='transportationkpi_update'),   
    # url(r'^transportaionkpicreate/(?P<year>\d+)/(?P<month>\d+)/$', TransportationKPICreateView.as_view(), name='transportationkpi_create'),   
    # url(r'^forkliftlist$', ForkliftListView.as_view(), name='forklift_list'),  
    # url(r'^forkliftdetail/(?P<pk>\d+)/$', ForklifDetailView.as_view(), name='forklift_detail'),    
]