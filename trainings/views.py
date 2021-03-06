# Create your views here.
from django.views.generic.list import ListView
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django_filters import FilterSet, CharFilter, NumberFilter, BooleanFilter, DateFilter, MethodFilter
from django.utils import timezone

from .models import (
        AnnualTraningPlan, 
        TrainingRecord, 
        TrainingCourse,
        TrainingTranscript
        )
from .forms import AnnualTrainingPlanFilterForm, AnnualTraningPlanForm,TrainingRecordForm #, TransportationAnnualTraningPlanForm, WarehouseAnnualTraningPlanForm
from inspection.mixins import TableDetailViewMixin, TableListViewMixin, UpdateViewMixin, CreateViewMixin, StaffRequiredMixin
from django.forms import models as model_forms
from django.db.models import Q
from django.db import models

class TrainingRecordDetailView(TableDetailViewMixin, DetailView):
    model = TrainingRecord
    template_name = "trainings/trainingrecord_detail.html"

    fields_files = ["sign_sheet", ]

    def get_context_data(self, *args, **kwargs):
        context = super(TrainingRecordDetailView, self).get_context_data(*args, **kwargs)

        """ 
        fields = [
            "training_course",
            "date",
            "location",
            "trainer",
            "audiences",
            "sign_sheet",
        ]

        context["fields"] = [self.model._meta.get_field(fieldname) for fieldname in fields]
        """

        from .admin import TrainingTranscriptAdmin
        fields_training_transcript = TrainingTranscriptAdmin.list_display
        if "training_record" in fields_training_transcript:
            fields_training_transcript.remove("training_record")
        context["fields_training_transcript"] = fields_training_transcript
        context["fields_training_transcript_display"] = ["work_position",] 

        if self.request.session.get("shortcut_back_url_saved"): # navigate from Annual Training Plan
            context["back_url"] = self.request.session["shortcut_back_url_saved"]
        else:
            context["back_url"] = None
        
        return context

    def dispatch(self, request, *args, **kwargs):
        # navigate from training course, not navigate from training transcription
        if self.request.session.get("shortcut_back_url") and not self.request.session.get("shortcut_back_url") == request.get_full_path() and \
                not self.request.session.get("shortcut_back_url_saved", None): 
            self.request.session["shortcut_back_url_saved"] = self.request.session["shortcut_back_url"]
        self.request.session["shortcut_back_url"] = request.get_full_path()    
        self.request.session["shortcut_create_pk"] = self.get_object().pk
        
        # request.breadcrumbs([
        #     (_("Home"),reverse("home", kwargs={})),
        #     (_("annual training plan"), reverse("annualtrainingplan_list", kwargs={})),            
        #     (self.get_object(), request.path_info),
        # ])
        return super(TrainingRecordDetailView, self).dispatch(request,args,kwargs)    

class TrainingCourseDetailView(TableDetailViewMixin, DetailView):
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

        context["course_class"] = self.request.GET.get("class") or self.request.session.get("course_class")

        return context

    def dispatch(self, request, *args, **kwargs):
        self.request.session["shortcut_back_url"] = request.get_full_path()
        self.request.session["shortcut_create_pk"] = self.get_object().pk

        if self.request.session.get("shortcut_back_url_saved"):
            del self.request.session["shortcut_back_url_saved"]
    
        # request.breadcrumbs([
        #     (_("Home"),reverse("home", kwargs={})),
        #     (_("annual training plan"), reverse("annualtrainingplan_list", kwargs={})),            
        #     (self.get_object(), request.path_info),
        # ])
        return super(TrainingCourseDetailView, self).dispatch(request,args,kwargs)    

class AnnualTrainingPlanFilter(FilterSet):
    year = CharFilter(name='year', lookup_type='exact', distinct=True)
    start = CharFilter(name='planned_date', lookup_type='gte', distinct=True)
    end = CharFilter(name='planned_date', lookup_type='lte', distinct=True)
    uncompleted = MethodFilter(name='actual_date', action='uncompleted_custom_filter', distinct=True)

    def uncompleted_custom_filter(self, queryset, value):
        if 'True' == value:
            print "haha"
            qs  = queryset.filter(**{
                'actual_date': None,
            })

            return qs.distinct()
        
        return queryset
        
    class Meta:
        model = AnnualTraningPlan
        fields = [
            'year',
            'start',
            'end',
        ]


        
class AnnualTrainingPlanListView(TableListViewMixin, ListView): 
    model = AnnualTraningPlan
    template_name = "trainings/annualtrainingplan_list.html"
    filter_class = AnnualTrainingPlanFilter

    def get_context_data(self, *args, **kwargs):
        context = super(AnnualTrainingPlanListView, self).get_context_data(*args, **kwargs)

        qs = self.get_queryset()
        queryset = self.filter_class(self.request.GET, queryset=qs)
        
        # retrieve course class
        course_class = None
        if self.request.GET.get("class"):
            course_class = self.request.GET.get("class")
            self.request.session["course_class"] = course_class
        elif self.request.session.get("course_class"):
            course_class = self.request.session.get("course_class")

        if course_class:
            queryset = queryset.qs.filter(training_course__training_class=course_class)
            
        object_list = queryset if self.request.GET or course_class else None

        context["object_list"] = object_list
            
        context["object_list_overdue"] = queryset.filter(actual_date=None,planned_date__lte=timezone.now())
            
        context["top_filter_form"] = AnnualTrainingPlanFilterForm(data=self.request.GET or None) 

        context["course_class"] = course_class if course_class else ""
        
        context["project_name"] = _("training")

        from .admin import AnnualTraningPlanAdmin
        fields = AnnualTraningPlanAdmin.list_display
        context["fields"] = [field.name for field in self.model._meta.get_fields() if field.name in fields]

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
        	row[object.planned_date.month * 2 - 1] = (object.training_record,"P",object) #object.planned_date
        	if object.actual_date:
        		row[object.actual_date.month * 2] = (object.training_record,"A",object) #object.actual_date
        	objects.append(row)

        context["objects"] = objects
        
        return context       

    def post(self, *args, **kwargs):
        qs = self.get_queryset()
        f = self.filter_class(self.request.GET, queryset=qs)

        fields_display = [] 
        fields_fk = ["training_record","training_course"]
        fields_datetime = []
        excludes = [field.name for field in self.model._meta.get_fields() if isinstance(field, models.ManyToOneRel)] 
        fields_multiple = ["",]

        from inspection.utils import gen_csv
        return gen_csv(self.model, f.qs, "annual_training_plan_export.csv", fields_display, fields_fk, fields_datetime, excludes, fields_multiple)

        
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
                context["form"] = self.get_form_class()(
                    self.request.GET or None, 
                    initial={"training_course": self.model.objects.filter(pk=self.request.session.get("shortcut_create_pk")).first()})

        return context
        
class TrainingRecordCreateView(StaffRequiredMixin, CreateViewMixin, CreateView): 
    model = TrainingRecord
    form_class = TrainingRecordForm

    def get_form_kwargs(self):
        kwargs = super(TrainingRecordCreateView, self).get_form_kwargs()
        kwargs.update({
                'request': self.request,
            })
        return kwargs

    def get_context_data(self, *args, **kwargs):
        context = super(TrainingRecordCreateView, self).get_context_data(*args, **kwargs)

        if  self.request.session.get("shortcut_create_pk"):
            if self.request.method == "GET":
                context["form"] = self.get_form_class()(
                    self.request.GET or None, 
                    request = self.request,                    
                    initial={"training_course": self.model.objects.filter(pk=self.request.session.get("shortcut_create_pk")).first()})

        return context
        
class TrainingTranscriptCreateView(StaffRequiredMixin, CreateViewMixin, CreateView): 
    model = TrainingTranscript    

    def get_context_data(self, *args, **kwargs):
        context = super(TrainingTranscriptCreateView, self).get_context_data(*args, **kwargs)

        if  self.request.session.get("shortcut_create_pk"):
            if self.request.method == "GET":
                context["form"] = self.get_form_class()(
                    self.request.GET or None, 
                    initial={"training_record": self.model.objects.filter(pk=self.request.session.get("shortcut_create_pk")).first()})

        return context
        
class AnnualTraningPlanCreateView(StaffRequiredMixin, CreateViewMixin, CreateView): 
    model = AnnualTraningPlan    

    form_class = AnnualTraningPlanForm #model_forms.modelform_factory(AnnualTraningPlan, exclude=["actual_date",], queryset)

    def get_form_kwargs(self):
        kwargs = super(AnnualTraningPlanCreateView, self).get_form_kwargs()
        kwargs.update({
                'request': self.request,
            })
        return kwargs

    def get_context_data(self, *args, **kwargs):
        context = super(AnnualTraningPlanCreateView, self).get_context_data(*args, **kwargs)

        if  self.request.session.get("shortcut_create_pk"):
            if self.request.method == "GET":
                context["form"] = self.get_form_class()(
                    self.request.GET or None, 
                    request=self.request,
                    initial={"training_course": self.model.objects.filter(pk=self.request.session.get("shortcut_create_pk")).first()})

        return context
        
class TrainingCourseUpdateView(StaffRequiredMixin, UpdateViewMixin, UpdateView): 
    model = TrainingCourse

class TrainingRecordUpdateView(StaffRequiredMixin, UpdateViewMixin, UpdateView): 
    model = TrainingRecord
    form_class = TrainingRecordForm

    def get_form_kwargs(self):
        kwargs = super(TrainingRecordUpdateView, self).get_form_kwargs()
        kwargs.update({
                'request': self.request,
            })
        return kwargs

class TrainingTranscriptUpdateView(StaffRequiredMixin, UpdateViewMixin, UpdateView): 
    model = TrainingTranscript    

class AnnualTraningPlanUpdateView(StaffRequiredMixin, UpdateViewMixin, UpdateView): 
    model = AnnualTraningPlan        

    form_class = AnnualTraningPlanForm #model_forms.modelform_factory(AnnualTraningPlan, exclude=["actual_date",])

    def get_form_kwargs(self):
        kwargs = super(AnnualTraningPlanUpdateView, self).get_form_kwargs()
        kwargs.update({
                'request': self.request,
            })
        return kwargs

class TrainingTranscriptDetailView(TableDetailViewMixin, DetailView): 
    model = TrainingTranscript    

    fields_display = ["work_position",]

class AnnualTraningPlanDetailView(TableDetailViewMixin, DetailView): 
    model = AnnualTraningPlan    

class TrainingCourseFilter(FilterSet):
    training_class= CharFilter(name='training_class', lookup_type='exact', distinct=True)
    
    class Meta:
        model = TrainingCourse
        fields = [
            'training_class',
        ]
        
class TrainingCourseListView(TableListViewMixin, ListView): 
    model = TrainingCourse
    template_name = "trainings/trainingcourse_list.html"
    filter_class = TrainingCourseFilter

    from .admin import TrainingCourseAdmin
    fields = TrainingCourseAdmin.list_display
    fields_display = ["training_class","category", ]

    def get_context_data(self, *args, **kwargs):
        context = super(TrainingCourseListView, self).get_context_data(*args, **kwargs)

        if self.request.session.get("course_class"):
            context["object_list"] = self.model.objects.filter(training_class=self.request.session.get("course_class"))
        return context

    def post(self, *args, **kwargs):
        qs = self.get_queryset()
        f = self.filter_class(self.request.GET, queryset=qs)

        fields_display = ["training_class", "category"] 
        fields_fk = []
        fields_datetime = []
        excludes = [field.name for field in self.model._meta.get_fields() if isinstance(field, models.ManyToOneRel)] 
        fields_multiple = ["",]

        from inspection.utils import gen_csv
        return gen_csv(self.model, f.qs, "training_course_export.csv", fields_display, fields_fk, fields_datetime, excludes, fields_multiple)
        
class TrainingRecordFilter(FilterSet):
    start = CharFilter(name='date', lookup_type='gte', distinct=True) # =  check_date__gte=start
    end = CharFilter(name='date', lookup_type='lte', distinct=True)
    # rectification_qualified = CharFilter(name='rectification_qualified', lookup_type='exact', distinct=True)
    
    class Meta:
        model = TrainingRecord
        fields = [
            'start',
            'end',
            # 'rectification_qualified',
        ]
        
class TrainingRecordListView(TableListViewMixin, ListView): 
    model = TrainingRecord
    template_name = "trainings/trainingrecord_list.html"
    filter_class = TrainingRecordFilter
    
    from .admin import TrainingRecordAdmin
    fields = TrainingRecordAdmin.list_display
    fields_files = ["sign_sheet", ]    

    def get_context_data(self, *args, **kwargs):
        context = super(TrainingRecordListView, self).get_context_data(*args, **kwargs)

        if self.request.session.get("course_class"):
            context["object_list"] = self.model.objects.filter(training_course__training_class=self.request.session.get("course_class"))
        return context

    def post(self, *args, **kwargs):
        qs = self.get_queryset()
        f = self.filter_class(self.request.GET, queryset=qs)

        fields_display = [] 
        fields_fk = ["training_course" ]
        fields_datetime = []
        excludes = [field.name for field in self.model._meta.get_fields() if isinstance(field, models.ManyToOneRel)] 
        fields_multiple = ["",]

        from inspection.utils import gen_csv
        return gen_csv(self.model, f.qs, "training_record_export.csv", fields_display, fields_fk, fields_datetime, excludes, fields_multiple)

        
