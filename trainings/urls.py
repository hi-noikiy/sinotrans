from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import (
    AnnualTrainingPlanListView, 
    AnnualTraningPlanCreateView,
    AnnualTraningPlanUpdateView,
    AnnualTraningPlanDetailView,

    TrainingRecordDetailView,
    TrainingRecordCreateView,
    TrainingRecordUpdateView,
    TrainingRecordListView,

    TrainingCourseDetailView,
    TrainingCourseCreateView,
    TrainingCourseUpdateView,
    TrainingCourseListView,

    TrainingTranscriptCreateView,
    TrainingTranscriptUpdateView,
    TrainingTranscriptDetailView,
)

urlpatterns = [
    url(r'^annualtrainingplan/$', AnnualTrainingPlanListView.as_view(), name='annualtrainingplan_list'),
    url(r'^annualtrainingplan/create$', AnnualTraningPlanCreateView.as_view(), name='annualtrainingplan_create'),
    url(r'^annualtrainingplan/update/(?P<pk>\d+)/$', AnnualTraningPlanUpdateView.as_view(), name='annualtrainingplan_update'),
    url(r'^annualtrainingplan/detail/(?P<pk>\d+)/$', AnnualTraningPlanDetailView.as_view(), name='annualtrainingplan_detail'),
    
    url(r'^trainingrecord/create', TrainingRecordCreateView.as_view(), name='trainingrecord_create'),
    url(r'^trainingrecord/$', TrainingRecordListView.as_view(), name='trainingrecord_list'),
    url(r'^trainingrecord/detail/(?P<pk>\d+)/$', TrainingRecordDetailView.as_view(), name='trainingrecord_detail'),
    url(r'^trainingrecord/update/(?P<pk>\d+)/$', TrainingRecordUpdateView.as_view(), name='trainingrecord_update'),

    url(r'^trainingcourse/$', TrainingCourseListView.as_view(), name='trainingcourse_list'),
    url(r'^trainingcourse/detail/(?P<pk>\d+)/$', TrainingCourseDetailView.as_view(), name='trainingcourse_detail'),
    url(r'^trainingcourse/update/(?P<pk>\d+)/$', TrainingCourseUpdateView.as_view(), name='trainingcourse_update'),
    
    url(r'^trainingtranscript/create', TrainingTranscriptCreateView.as_view(), name='trainingtranscript_create'),
    url(r'^trainingtranscript/detail/(?P<pk>\d+)/$', TrainingTranscriptDetailView.as_view(), name='trainingtranscript_detail'),
    url(r'^trainingtranscript/update/(?P<pk>\d+)/$', TrainingTranscriptUpdateView.as_view(), name='trainingtranscript_update'),
    
]