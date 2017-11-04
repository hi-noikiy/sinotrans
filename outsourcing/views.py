from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.views.generic.base import View, TemplateResponseMixin, ContextMixin, TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin, ModelFormMixin
from django.http import HttpResponseRedirect
from django.conf import settings
from django.utils.translation import ugettext as _
from django.contrib import messages

from .models import (
	Forklift, ForkliftMaint, 
    VehicleTransportationKPI,
	)
from .forms import (
    vehicle_transportation_kpi_model_formset
    )

from .models import option_value_convertion

# Create your views here.
class ForkliftListView(ListView): 
    model = Forklift
    template_name = "forklift/forklift_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ForkliftListView, self).get_context_data(*args, **kwargs)
        context["object_list"] = Forklift.objects.all()
        
        return context       

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('Forklift'),request.path_info),
        ])
        return super(ForkliftListView, self).dispatch(request,args,kwargs)   

class ForklifDetailView(DetailView): 
    model = Forklift
    template_name = "forklift/forklift_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ForklifDetailView, self).get_context_data(*args, **kwargs)
        context["object"] = self.get_object()

        exclude = {
        'id','updated','created','forklift'
        }
        forklift_maint_objects = ForkliftMaint.objects.filter(forklift=self.get_object())
        for forklift_maint_object in forklift_maint_objects:
        	from .models import RESULT_OPTION
        	forklift_maint_object.fields = dict((field.verbose_name, option_value_convertion(RESULT_OPTION, field.value_to_string(forklift_maint_object))) for field in forklift_maint_object._meta.fields if not field.name in exclude)
        context["forklift_maint_objects"] = forklift_maint_objects
        
        return context       

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_("Forklift"),reverse("forklift_list", kwargs={})),            
            (self.get_object(), request.path_info),
        ])
        return super(ForklifDetailView, self).dispatch(request,args,kwargs)           

class TransportationKPIListDisplayView(ListView):
    model = VehicleTransportationKPI
    template_name = "kpi/transportionkpi_list_display.html"

    def get_context_data(self, *args, **kwargs):
        context = super(TransportationKPIListDisplayView, self).get_context_data(*args, **kwargs)
        context["object_list"] = self.model.objects.all()

        fields = [
            'safe_mileages',
            'safe_labor_hours',
            'LSR_violation_cases',
            'safety_accident_cases',
            'yearly_plan_executing_rate',
            'vehicle_qualification_rate',
            'journey_management_rules_implemented_rate',
            'safe_loading_violation_cases',
            'departure_count',
            'departure_tones',
            'monthly_delivery_plan_completion_rate',
            'AOG_on_time_rate',
            'POD_on_time_rate',
            'POD_accuracy',
            'customer_satisfaction_rate',
            'customer_complaint_cases',
        ]

        rows = [(field, self.model._meta.get_field(field).verbose_name) for field in fields ]

        from inspection.utils import get_exist_option_items
        context["columns"] = get_exist_option_items(VehicleTransportationKPI.TRANSPORTATION_PROJECT_OPTION, self.get_queryset(), 'transportation_project')        
        context["rows"] = rows
        context["project_name"] = _("vehicle tranportation KPI")
        context["hidden_fields"] = ["id",]
        
        return context       

    def post(self, request, *args, **kwargs):
        formset = vehicle_transportation_kpi_model_formset(request.POST or None, request.FILES or None)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.save()
            messages.success(request, "Your list has been updated.")
            return redirect(reverse("transportationkpi_list_edit",  kwargs={}))

        self.object_list = self.get_queryset() # copy from BaseListView::get
        context = self.get_context_data()
        context['formset'] = formset
        return self.render_to_response(context)

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('vehicle tranportation KPI'),request.path_info),
        ])
        return super(TransportationKPIListDisplayView, self).dispatch(request,args,kwargs)   

class TransportationKPIListEditView(ListView):
    model = VehicleTransportationKPI
    template_name = "kpi/transportionkpi_list_edit.html"

    def get_context_data(self, *args, **kwargs):
        context = super(TransportationKPIListEditView, self).get_context_data(*args, **kwargs)
        context["object_list"] = self.model.objects.all()
        formset = vehicle_transportation_kpi_model_formset(queryset=self.get_queryset(*args, **kwargs))
        context["formset"] = formset

        from inspection.utils import get_exist_option_items
        context["columns"] = get_exist_option_items(VehicleTransportationKPI.TRANSPORTATION_PROJECT_OPTION, self.get_queryset(), 'transportation_project')
        context["project_name"] = "vehicle tranportation KPI"
        context["hidden_fields"] = ["id",]
        context["date_field_list"] = [""]
        
        return context       

    def post(self, request, *args, **kwargs):
        formset = vehicle_transportation_kpi_model_formset(request.POST or None, request.FILES or None)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.save()
            messages.success(request, "Your list has been updated.")
            return redirect(reverse("transportationkpi_list_edit",  kwargs={}))

        self.object_list = self.get_queryset() # copy from BaseListView::get
        context = self.get_context_data()
        context['formset'] = formset
        return self.render_to_response(context)

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('vehicle tranportation KPI'),request.path_info),
        ])
        return super(TransportationKPIListEditView, self).dispatch(request,args,kwargs)   
        