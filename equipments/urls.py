from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import (
    EquipmentInspectionListView,
    EquipmentInspectionDetailView,
    EquipmentInspectionCreateView,
    EquipmentInspectionUpdateView,
    EquipmentInspectionQuickUpdateView,

    SprayPumproomInspectionListEditView,
    SprayPumproomInspectionListDisplayView,
    SprayPumproomInspectionDetailView,
    SprayPumproomInspectionUpdateView,
    SprayPumproomInspectionCreateView,

    SprayWarehouseInspectionListEditView,
    SprayWarehouseInspectionListDisplayView,
    SprayWarehouseInspectionDetailView,
    SprayWarehouseInspectionUpdateView,
    SprayWarehouseInspectionCreateView,     

    HSSEKPIListEditView,
    HSSEKPIListDisplayView,
    HSSEKPIDetailView,
    HSSEKPIUpdateView,
    HSSEKPICreateView,       
)

urlpatterns = [

    url(r'^equipmentinspection/quickupdate/$', EquipmentInspectionQuickUpdateView.as_view(), name='equipmentinsepction_quickupdate'),
    #url(r'^equipmentinspection/export/$', EquipmentInspectionQuickUpdateView.as_view(), name='equipmentinsepction_export'),
    url(r'^equipmentinspection/list/$', EquipmentInspectionListView.as_view(), name='equipmentinsepction_list'),
    url(r'^equipmentinspection/detail/(?P<pk>\d+)/$', EquipmentInspectionDetailView.as_view(), name='equipmentinsepction_detail'),
    url(r'^equipmentinspection/update/(?P<pk>\d+)/$', EquipmentInspectionUpdateView.as_view(), name='equipmentinsepction_update'),
    url(r'^equipmentinspection/create/(?P<cat>\d+)/$', EquipmentInspectionCreateView.as_view(), name='equipmentinsepction_create'),

    url(r'^spraypumproominspection/listedit/$', SprayPumproomInspectionListEditView.as_view(), name='spraypumproominspection_list_edit'),
    url(r'^spraypumproominspection/listdisplay/$', SprayPumproomInspectionListDisplayView.as_view(), name='spraypumproominspection_list_display'),
    url(r'^spraypumproominspection/detail/(?P<pk>\d+)/$', SprayPumproomInspectionDetailView.as_view(), name='spraypumproominspection_detail'),
    url(r'^spraypumproominspection/update/(?P<pk>\d+)/$', SprayPumproomInspectionUpdateView.as_view(), name='spraypumproominspection_update'),
    url(r'^spraypumproominspection/create/(?P<year>\d+)/(?P<month>\d+)/$', SprayPumproomInspectionCreateView.as_view(), name='spraypumproominspection_create'),   

    url(r'^spraywarehouseinspection/listedit/$', SprayWarehouseInspectionListEditView.as_view(), name='spraywarehouseinspection_list_edit'),
    url(r'^spraywarehouseinspection/listdisplay/$', SprayWarehouseInspectionListDisplayView.as_view(), name='spraywarehouseinspection_list_display'),
    url(r'^spraywarehouseinspection/detail/(?P<pk>\d+)/$', SprayWarehouseInspectionDetailView.as_view(), name='spraywarehouseinspection_detail'),
    url(r'^spraywarehouseinspection/update/(?P<pk>\d+)/$', SprayWarehouseInspectionUpdateView.as_view(), name='spraywarehouseinspection_update'),
    url(r'^spraywarehouseinspection/create/(?P<year>\d+)/(?P<month>\d+)/$', SprayWarehouseInspectionCreateView.as_view(), name='spraywarehouseinspection_create'),    

    url(r'^hssekpi/listedit/$', HSSEKPIListEditView.as_view(), name='hssekpi_list_edit'),
    url(r'^hssekpi/listdisplay/$', HSSEKPIListDisplayView.as_view(), name='hssekpi_list_display'),
    url(r'^hssekpi/detail/(?P<pk>\d+)/$', HSSEKPIDetailView.as_view(), name='hssekpi_detail'),
    url(r'^hssekpi/update/(?P<pk>\d+)/$', HSSEKPIUpdateView.as_view(), name='hssekpi_update'),
    url(r'^hssekpi/create/(?P<year>\d+)/(?P<month>\d+)/$', HSSEKPICreateView.as_view(), name='hssekpi_create'),   
]