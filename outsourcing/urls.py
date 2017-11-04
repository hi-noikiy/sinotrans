from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import (
    ForkliftListView,
    ForklifDetailView,
    TransportationKPIListDisplayView,
)

urlpatterns = [
    url(r'^forkliftlist$', ForkliftListView.as_view(), name='forklift_list'),  
    url(r'^forkliftdetail/(?P<pk>\d+)/$', ForklifDetailView.as_view(), name='forklift_detail'),
    url(r'^transportaionkpilistdisplay$', TransportationKPIListDisplayView.as_view(), name='transportationkpi_list_display'),  
]