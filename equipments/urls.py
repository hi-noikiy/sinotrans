from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import (
    EquipmentInspectionListView,
    EquipmentInspectionDetailView,
    EquipmentInspectionCreateView,
    ElectricalEquipmentInspectionUpdateView,
    EquipmentInspectionQuickUpdateView,
)

urlpatterns = [

    url(r'^equipmentinspection/quickupdate/$', EquipmentInspectionQuickUpdateView.as_view(), name='equipmentinsepction_quickupdate'),
    url(r'^equipmentinspection/list/$', EquipmentInspectionListView.as_view(), name='equipmentinsepction_list'),
    url(r'^equipmentinspection/detail/(?P<pk>\d+)/$', EquipmentInspectionDetailView.as_view(), name='equipmentinsepction_detail'),
    url(r'^equipmentinspection/update/(?P<pk>\d+)/$', ElectricalEquipmentInspectionUpdateView.as_view(), name='equipmentinsepction_update'),
    url(r'^equipmentinspection/create/$', EquipmentInspectionCreateView.as_view(), name='equipmentinsepction_create'),

]