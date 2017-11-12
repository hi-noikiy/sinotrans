from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import (
    AnnualTrainingPlanListView, TrainingRecordDetailView,TrainingCourseDetailView,
)

urlpatterns = [
    url(r'^annualtrainingplan/list/$', AnnualTrainingPlanListView.as_view(), name='annualtrainingplan_list'),
    url(r'^trainingrecord/detail/(?P<pk>\d+)/$', TrainingRecordDetailView.as_view(), name='trainingrecord_detail'),
    url(r'^trainingcourse/detail/(?P<pk>\d+)/$', TrainingCourseDetailView.as_view(), name='trainingcourse_detail'),
    # url(r'^electronicalequipmentinspection/create/$', ElectricalEquipmentInspectionCreateView.as_view(), name='electronialequipmentinsepction_create'),
]