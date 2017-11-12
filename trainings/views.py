# Create your views here.
from django.views.generic.list import ListView
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from .models import AnnualTraningPlan, TrainingRecord, TrainingCourse
from .forms import AnnualTrainingPlanFilterForm


class TrainingRecordDetailView(DetailView):
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

        return context

    def dispatch(self, request, *args, **kwargs):
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
            "topic",
            "category",
            "content",
        ]

        context["fields"] = [self.model._meta.get_field(fieldname) for fieldname in field]

        return context

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_("annual training plan"), reverse("annualtrainingplan_list", kwargs={})),            
            (self.get_object(), request.path_info),
        ])
        return super(TrainingCourseDetailView, self).dispatch(request,args,kwargs)    

class AnnualTrainingPlanListView(ListView): 
    model = AnnualTraningPlan
    #template_name = "trainings/annualtrainingplan_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(AnnualTrainingPlanListView, self).get_context_data(*args, **kwargs)
        qs = AnnualTraningPlan.objects.all()
        context["object_list"] = qs
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
        for object in qs:
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
