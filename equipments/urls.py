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
    url(r'^spraypumproominspection/create/(?P<year>\d+)/$', SprayPumproomInspectionCreateView.as_view(), name='spraypumproominspection_create'),    
]