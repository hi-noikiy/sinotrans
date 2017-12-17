# Create your views here.
from django.views.generic.list import ListView
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django_filters import FilterSet, CharFilter, NumberFilter, BooleanFilter, DateFilter, MethodFilter

from .models import (
        AnnualTraningPlan, 
        TrainingRecord, 
        TrainingCourse,
        TrainingTranscript
        )
from .forms import AnnualTrainingPlanFilterForm
from inspection.mixins import TableDetailViewMixin, TableListViewMixin, UpdateViewMixin, CreateViewMixin, StaffRequiredMixin



class TrainingRecordDetailView(TableDetailViewMixin, DetailView):
    model = TrainingRecord
    template_name = "trainings/trainingrecord_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(TrainingRecordDetailView, self).get_context_data(*args, **kwargs)

        field = [
            "training_course",
            "date",
            "location",
            "trainer",
            "audiences",
        ]

        context["fields"] = [self.model._meta.get_field(fieldname) for fieldname in field]

        from .admin import TrainingTranscriptAdmin
        fields_training_transcript = TrainingTranscriptAdmin.list_display
        if "training_record" in fields_training_transcript:
            fields_training_transcript.remove("training_record")
        context["fields_training_transcript"] = fields_training_transcript
        context["fields_training_transcript_display"] = ["work_position",] 

        return context

    def dispatch(self, request, *args, **kwargs):
        self.request.session["shortcut_back_url"] = request.get_full_path()    
        self.request.session["shortcut_create_pk"] = self.get_object().pk
        
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_("annual training plan"), reverse("annualtrainingplan_list", kwargs={})),            
            (self.get_object(), request.path_info),
        ])
        return super(TrainingRecordDetailView, self).dispatch(request,args,kwargs)    

class TrainingCourseDetailView(DetailView):
    model = TrainingCourse
    template_name = "trainings/trainingcourse_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(TrainingCourseDetailView, self).get_context_data(*args, **kwargs)

        field = [
            "training_class",
            "topic",
            "category",
            "content",
        ]

        context["fields"] = [self.model._meta.get_field(fieldname) for fieldname in field]
        context["fields_safe_content"] = ["content",]
        context["fields_display"] = ["training_class","category",]

        from .admin import TrainingRecordAdmin
        fields_training_record = TrainingRecordAdmin.list_display
        if "training_course" in fields_training_record:
            fields_training_record.remove("training_course")
        context["fields_training_record"] = fields_training_record
        context["fields_training_record_display"] = ["",] 

        from .admin import AnnualTraningPlanAdmin
        fields_annual_training_plan = AnnualTraningPlanAdmin.list_display
        if "training_course" in fields_annual_training_plan:
            fields_annual_training_plan.remove("training_course")
        context["fields_annual_training_plan"] = fields_annual_training_plan
        context["fields_annual_training_plan_display"] = ["",] 

        return context

    def dispatch(self, request, *args, **kwargs):
        self.request.session["shortcut_back_url"] = request.get_full_path()
        self.request.session["shortcut_create_pk"] = self.get_object().pk
    
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_("annual training plan"), reverse("annualtrainingplan_list", kwargs={})),            
            (self.get_object(), request.path_info),
        ])
        return super(TrainingCourseDetailView, self).dispatch(request,args,kwargs)    

class AnnualTrainingPlanFilter(FilterSet):
    year = CharFilter(name='year', lookup_type='exact', distinct=True)

    class Meta:
        model = AnnualTraningPlan
        fields = [
            'year',
        ]


class AnnualTrainingPlanListView(ListView): 
    model = AnnualTraningPlan
    #template_name = "trainings/annualtrainingplan_list.html"
    filter_class = AnnualTrainingPlanFilter

    def get_context_data(self, *args, **kwargs):
        context = super(AnnualTrainingPlanListView, self).get_context_data(*args, **kwargs)

        qs = self.get_queryset()
        queryset = self.filter_class(self.request.GET, queryset=qs)
        if self.request.GET.get("class"):
            queryset = queryset.qs.filter(training_course__training_class=self.request.GET.get("class"))
        context["object_list"] = queryset if self.request.GET else None

        context["top_filter_form"] = AnnualTrainingPlanFilterForm(data=self.request.GET or None) 

        context["project_name"] = _("training")

        from inspection.models import month_choice

        header1 = [
            [
                (_("training"),3,1),
                (_("Q1"),1,6), 
                (_("Q2"),1,6),
                (_("Q3"),1,6),
                (_("Q4"),1,6),
            ],
        ]
        header2 = [
            [ [month[1],1,2] for month in month_choice ]
        ]
        header3 = [[
            (_("plan"),1,1),
            (_("actual"),1,1),
            ]*12]

        context["headers"] = header1 + header2 + header3

        objects = []
        initial = ["",""]*12
        for object in queryset:
        	row = [object.training_course] + initial
        	row[object.planned_date.month * 2 - 1] = (object.training_record,"P") #object.planned_date
        	if object.actual_date:
        		row[object.actual_date.month * 2] = (object.training_record,"A") #object.actual_date
        	objects.append(row)

        context["objects"] = objects
        
        return context       

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('annual training plan'),request.path_info),
        ])
        return super(AnnualTrainingPlanListView, self).dispatch(request,args,kwargs)   

class TrainingCourseCreateView(StaffRequiredMixin, CreateViewMixin, CreateView): 
    model = TrainingCourse

    def get_context_data(self, *args, **kwargs):
        context = super(TrainingCourseCreateView, self).get_context_data(*args, **kwargs)

        if  self.request.session.get("shortcut_create_pk"):
            if self.request.method == "GET":
                context["form"] = self.get_form_class()(self.request.GET or None, initial={"training_course": self.model.objects.filter(pk=self.request.session.get("shortcut_create_pk")).first()})

        return context
        
class TrainingRecordCreateView(StaffRequiredMixin, CreateViewMixin, CreateView): 
    model = TrainingRecord

    def get_context_data(self, *args, **kwargs):
        context = super(TrainingRecordCreateView, self).get_context_data(*args, **kwargs)

        if  self.request.session.get("shortcut_create_pk"):
            if self.request.method == "GET":
                context["form"] = self.get_form_class()(self.request.GET or None, initial={"training_course": self.model.objects.filter(pk=self.request.session.get("shortcut_create_pk")).first()})

        return context
        
class TrainingTranscriptCreateView(StaffRequiredMixin, CreateViewMixin, CreateView): 
    model = TrainingTranscript    

    def get_context_data(self, *args, **kwargs):
        context = super(TrainingTranscriptCreateView, self).get_context_data(*args, **kwargs)

        if  self.request.session.get("shortcut_create_pk"):
            if self.request.method == "GET":
                context["form"] = self.get_form_class()(self.request.GET or None, initial={"training_record": self.model.objects.filter(pk=self.request.session.get("shortcut_create_pk")).first()})

        return context
        
class AnnualTraningPlanCreateView(StaffRequiredMixin, CreateViewMixin, CreateView): 
    model = AnnualTraningPlan    

    def get_context_data(self, *args, **kwargs):
        context = super(AnnualTraningPlanCreateView, self).get_context_data(*args, **kwargs)

        if  self.request.session.get("shortcut_create_pk"):
            if self.request.method == "GET":
                context["form"] = self.get_form_class()(self.request.GET or None, initial={"training_course": self.model.objects.filter(pk=self.request.session.get("shortcut_create_pk")).first()})

        return context
        
class TrainingCourseUpdateView(StaffRequiredMixin, UpdateViewMixin, UpdateView): 
    model = TrainingCourse

class TrainingRecordUpdateView(StaffRequiredMixin, UpdateViewMixin, UpdateView): 
    model = TrainingRecord

class TrainingTranscriptUpdateView(StaffRequiredMixin, UpdateViewMixin, UpdateView): 
    model = TrainingTranscript    

class AnnualTraningPlanUpdateView(StaffRequiredMixin, UpdateViewMixin, UpdateView): 
    model = AnnualTraningPlan        

class TrainingTranscriptDetailView(TableDetailViewMixin, DetailView): 
    model = TrainingTranscript    

class AnnualTraningPlanDetailView(TableDetailViewMixin, DetailView): 
    model = AnnualTraningPlan    
    
class TrainingCourseListView(TableListViewMixin, ListView): 
    model = TrainingCourse

    from .admin import TrainingCourseAdmin
    fields = TrainingCourseAdmin.list_display
    fields_display = ["training_class","category", ]

class TrainingRecordListView(TableListViewMixin, ListView): 
    model = TrainingRecord

    from .admin import TrainingRecordAdmin
    fields = TrainingRecordAdmin.list_display
    # fields_display = ["training_class","category", ]    
    
