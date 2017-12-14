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
from django_filters import FilterSet, CharFilter, NumberFilter, BooleanFilter, DateFilter, MethodFilter
from django.utils import timezone

from .models import (
	Forklift, 
    ForkliftMaint, 
    ForkliftRepair,

    Vehicle, 
    Driver, 
    VehicleInspection,
    VehicleTransportationKPI,

    option_value_convertion
	)
from .forms import (
    vehicle_transportation_kpi_model_formset, VehicleTransportationKPIForm,
    VehicleTransportationKPIFilterForm,
    )

from trainings.models import TrainingTranscript

from inspection.mixins import TableDetailViewMixin, TableListViewMixin

class TransportSecurityView(TemplateView):
    template_name = "transport_security.html"

    def get_context_data(self, *args, **kwargs):
        context = super(TransportSecurityView, self).get_context_data(*args, **kwargs)
        context["year"] = timezone.now().year
        
        return context
        
# Create your views here.
class ForkliftListView(TableListViewMixin, ListView): 
    model = Forklift
    template_name = "forklift/forklift_list.html"

    from .admin import ForkliftAdmin
    #fields = [field for field in model._meta.get_fields() if field.name in ForkliftAdmin.list_display]
    fields = ForkliftAdmin.list_display
    foreign_fields_images = ["forkliftimage_set",]

    def get_context_data(self, *args, **kwargs):
        context = super(ForkliftListView, self).get_context_data(*args, **kwargs)
        context["object_list"] = self.model.objects.all()
        return context       

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('Forklift'),request.path_info),
        ])
        return super(ForkliftListView, self).dispatch(request,args,kwargs)   

class ForkliftDetailView(TableDetailViewMixin, DetailView): 
    model = Forklift
    template_name = "forklift/forklift_detail.html"

    fieldsets = [
            ("",
                {"fields":(
                    "internal_car_number",
                    "internal_plate_number",
                    "model",
                    "sn",
                    "category",
                    "manufacturer",
                    )}), 
            ("",
                {"fields":(
                    "tip_height",
                    "carrying_capacity",
                    "self_weight",
                    "turning_radius",
                    "front_tyre_size",
                    "back_tyre_size",
                    "width",
                    "length",
                    "forklift_length",
                    "maximum_velocity",
                    )}), 

            ]

    def get_context_data(self, *args, **kwargs):
        context = super(ForkliftDetailView, self).get_context_data(*args, **kwargs)
        context["object"] = self.get_object()

        context["fields"] = [self.model._meta.get_field(field.name) for field in self.model._meta.fields  if not field.name in [self.model._meta.pk.attname,]]

        context["fields_safe_content"] = ["",]   
        context["fields_display"] = ["training_qualified",] 

        exclude = {
        'id','updated','created','forklift'
        }
        forklift_maint_objects = ForkliftMaint.objects.filter(forklift=self.get_object())
        for forklift_maint_object in forklift_maint_objects:
            from .models import RESULT_OPTION
            forklift_maint_object.fields = dict((field.verbose_name, option_value_convertion(RESULT_OPTION, field.value_to_string(forklift_maint_object))) 
                for field in forklift_maint_object._meta.fields if not field.name in exclude)
        context["forklift_maint_objects"] = forklift_maint_objects
        
        from admin import ForkliftRepairAdmin
        context["fields_foreign_forkliftrepair"] = ForkliftRepairAdmin.list_display
        if "forklift" in context["fields_foreign_forkliftrepair"]:
            context["fields_foreign_forkliftrepair"].remove("forklift")
        context["fields_foreign_display_forkliftrepair"] = [
            "repaired",
        ]
        return context       

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_("Forklift"),reverse("forklift_list", kwargs={})),            
            (self.get_object(), request.path_info),
        ])
        return super(ForkliftDetailView, self).dispatch(request,args,kwargs)  

class ForkliftRepairListView(TableListViewMixin, ListView): 
    model = ForkliftRepair
    template_name = "forklift/forklift_repair_list.html"

    from .admin import ForkliftRepairAdmin
    #fields = [model._meta.get_field(field) for field in ForkliftRepairAdmin.list_display]
    fields = ForkliftRepairAdmin.list_display
    fields_display = ["repaired",]
   
    def get_queryset(self, *args, **kwargs):
        return self.model.objects.filter(repaired="no")

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('Forklift'),reverse("forklift_list", kwargs={})),
            (_('forklift repair'),request.path_info),
        ])
        return super(ForkliftRepairListView, self).dispatch(request,args,kwargs)   

class ForkliftRepairDetailView(TableDetailViewMixin, DetailView): 
    model = ForkliftRepair
    template_name = "forklift/forklift_repair_detail.html"

    fields = [field for field in model._meta.get_fields() if not field.name in [model._meta.pk.attname,]]
    fields_display = ["repaired",]

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_("forklift repair"),reverse("forklift_repair_list", kwargs={})),            
            (self.get_object(), request.path_info),
        ])
        return super(ForkliftRepairDetailView, self).dispatch(request,args,kwargs)  

class DriverListView(ListView): 
    model = Driver
    template_name = "transportation/driver_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DriverListView, self).get_context_data(*args, **kwargs)
        context["object_list"] = self.model.objects.all()

        from .admin import DriverAdmin
        fields = DriverAdmin.list_display

        context["object_list"] = self.model.objects.all()
        context["fields"] = [field for field in self.model._meta.get_fields() if field.name in fields]
        context["fields_display"] = ["",] 

        return context       

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('driver'),request.path_info),
        ])
        return super(DriverListView, self).dispatch(request,args,kwargs)   

class DriverDetailView(DetailView): 
    model = Driver
    template_name = "transportation/driver_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DriverDetailView, self).get_context_data(*args, **kwargs)
        context["object"] = self.get_object()

        context["fields"] = [self.model._meta.get_field(field.name) for field in self.model._meta.fields  if not field.name in [self.model._meta.pk.attname, ]]
        context["fields_safe_content"] = ["",]   
        context["fields_display"] = ["training_qualified",] 

        from trainings.admin import TrainingTranscriptAdmin
        fields_training_transcript = TrainingTranscriptAdmin.list_display
        context["fields_training_transcript"] = fields_training_transcript
        context["fields_training_transcript_display"] = ["work_position",]
        context["driver_training_transcripts"] = TrainingTranscript.objects.filter(work_position='driver', trainee=self.get_object().name)  # later maybe need add Driver ForeignKey to TrainingTranscript to avoid dup name

        return context        

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_("driver"),reverse("driver_list", kwargs={})),            
            (self.get_object(), request.path_info),
        ])
        return super(DriverDetailView, self).dispatch(request,args,kwargs)           

class VehicleListView(ListView): 
    model = Vehicle
    template_name = "transportation/vehicle_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(VehicleListView, self).get_context_data(*args, **kwargs)

        from .admin import VehicleAdmin
        fields = VehicleAdmin.list_display

        context["object_list"] = self.model.objects.all()
        context["fields"] = [field for field in self.model._meta.get_fields() if field.name in fields]
        context["fields_display"] = ["",] 


        return context       

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('vehicle'),request.path_info),
        ])
        return super(VehicleListView, self).dispatch(request,args,kwargs)   

class VehicleDetailView(TableDetailViewMixin, DetailView): 
    model = Vehicle
    template_name = "transportation/vehicle_detail.html"

    from admin import VehicleAdmin
    fieldsets = VehicleAdmin.fieldsets
    fields_display = [
        "service_content",
        "GPS",
        "ABS",
        "antiroll_protection",
        "reversing_alarm",
        "side_edge_and_low_location_collision_guard_bar",
        "car_seat_headrest",
        "three_point_belt",
        "IVMS_or_VDR",
        "anti_drop_equipment",
    ]

    def get_context_data(self, *args, **kwargs):
        context = super(VehicleDetailView, self).get_context_data(*args, **kwargs)
        context["object"] = self.get_object()

        # context["fieldsets"] = fieldsets

        # from admin import DriverAdmin
        # fields_dirver = DriverAdmin.list_display
        # context["fields_dirver"] = fields_dirver

        from admin import VehicleInspectionAdmin
        fields_vehicle_inspection = VehicleInspectionAdmin.list_display
        if "vehicle" in fields_vehicle_inspection:
            fields_vehicle_inspection.remove("vehicle")
        context["fields_vehicle_inspection"] = fields_vehicle_inspection
        fields_vehicle_inspection_display = [
                    "load_or_unload",
                    "rectification_qualified",
                    "hardware_inspection_disqualification",        
                    "no_driver_code_of_conduct",
                    "overload_or_LSR_violation",
                    "safety_policy_violation",
                    "no_journey_plan_or_log",
                    "vehichle_not_register",
                    "no_vehicle_inspection_record",
                    "no_DDC_certificate"
            ]
        context["fields_vehicle_inspection_display"] = fields_vehicle_inspection_display
        
        return context       

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_("vehicle"),reverse("vehicle_list", kwargs={})),            
            (self.get_object(), request.path_info),
        ])
        return super(VehicleDetailView, self).dispatch(request,args,kwargs)    

class VehicleInspectionListView(ListView): 
    model = VehicleInspection
    template_name = "transportation/vehicle_inspection_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(VehicleInspectionListView, self).get_context_data(*args, **kwargs)

        from .admin import VehicleInspectionAdmin
        
        context["object_list"] = self.model.objects.filter(rectification_qualified='no')
        #context["fields"] = [field for field in self.model._meta.get_fields() if field.name in VehicleInspectionAdmin.list_display]
        context["fields"] = VehicleInspectionAdmin.list_display
        context["fields_display"] = [
                    "load_or_unload",
                    "rectification_qualified",
                    "hardware_inspection_disqualification",        
                    "no_driver_code_of_conduct",
                    "overload_or_LSR_violation",
                    "safety_policy_violation",
                    "no_journey_plan_or_log",
                    "vehichle_not_register",
                    "no_vehicle_inspection_record",
                    "no_DDC_certificate"
            ]


        return context       

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_("vehicle"),reverse("vehicle_list", kwargs={})),    
            (_('vehicle inspection'),request.path_info),
        ])
        return super(VehicleInspectionListView, self).dispatch(request,args,kwargs)   

class VehicleInspectionDetailView(DetailView): 
    model = VehicleInspection
    template_name = "transportation/vehicle_inspection_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(VehicleInspectionDetailView, self).get_context_data(*args, **kwargs)
        context["fields_display"] = [
                    "load_or_unload",
                    "rectification_qualified",
                    "hardware_inspection_disqualification",        
                    "no_driver_code_of_conduct",
                    "overload_or_LSR_violation",
                    "safety_policy_violation",
                    "no_journey_plan_or_log",
                    "vehichle_not_register",
                    "no_vehicle_inspection_record",
                    "no_DDC_certificate"
            ]
        context["detail_view_title"] = _("vehicle inspection")
        context["fields"] = [field for field in self.model._meta.get_fields() if not field.name in [self.model._meta.pk.attname, ]]   

        return context    

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_("vehicle"),reverse("vehicle_list", kwargs={})),            
            (self.get_object(), request.path_info),
        ])
        return super(VehicleInspectionDetailView, self).dispatch(request,args,kwargs)    

class VehicleTransportationKPIFilter(FilterSet):
    year = CharFilter(name='year', lookup_type='exact', distinct=True)
    month = CharFilter(name='month', lookup_type='exact', distinct=True)

    class Meta:
        model = VehicleTransportationKPI
        fields = [
            'year',
            'month',
        ]

class TransportationKPIDetailView(DetailView):
    model = VehicleTransportationKPI
    template_name = "kpi/transportationkpi_detail.html"
    #success_url = reverse("transportationkpi_list_display", kwargs={})

    def get_context_data(self, *args, **kwargs):
        context = super(TransportationKPIDetailView, self).get_context_data(*args, **kwargs)

        context["fields"] = [field for field in self.model._meta.get_fields() if not field.name=="id"]
        context["transport_kpi_year"] = self.request.session["transport_kpi_year"]
        context["transport_kpi_month"] = self.request.session["transport_kpi_month"]
        return context


    def get_success_url(self):
        return reverse("transportationkpi_list_display", kwargs={})

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_("vehicle tranportation KPI"), reverse("transportationkpi_list_display", kwargs={})),            
            (self.get_object(), request.path_info),
        ])
        return super(TransportationKPIDetailView, self).dispatch(request,args,kwargs)      

class TransportationKPIUpdateView(UpdateView):
    model = VehicleTransportationKPI
    template_name = "kpi/transportationkpi_update.html"
    form_class = VehicleTransportationKPIForm

    def get_success_url(self):
        return reverse("transportationkpi_detail", kwargs={"pk":self.get_object().pk})

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_("vehicle tranportation KPI"), reverse("transportationkpi_list_display", kwargs={})),            
            (self.get_object(), request.path_info),
        ])
        return super(TransportationKPIUpdateView, self).dispatch(request,args,kwargs)      

class TransportationKPICreateView(CreateView):
    model = VehicleTransportationKPI
    template_name = "kpi/transportationkpi_create.html"
    form_class = VehicleTransportationKPIForm

    def get_context_data(self, *args, **kwargs):
        context = super(TransportationKPICreateView, self).get_context_data(*args, **kwargs)
        context["year"] = self.kwargs.get('year')
        context["month"] = self.kwargs.get('month')
        context["form"] = self.form_class(self.request.POST or None, self.request.GET or None, initial={'year':self.kwargs.get('year'),'month': self.kwargs.get('month'),'transportation_project': self.kwargs.get('project')})

        return context

    def get_success_url(self):
        return reverse("transportationkpi_list_display", kwargs={})

class TransportationKPIListDisplayView(ListView):
    model = VehicleTransportationKPI
    template_name = "kpi/transportationkpi_list_display.html"
    filter_class = VehicleTransportationKPIFilter

    def get_context_data(self, *args, **kwargs):
        context = super(TransportationKPIListDisplayView, self).get_context_data(*args, **kwargs)
        #context["object_list"] = self.model.objects.all()

        qs = self.get_queryset()
        queryset = self.filter_class(self.request.GET, queryset=qs)
        context["object_list"] = queryset if self.request.GET else None

        excludes = [
            'id',
            'year',
            'month',
        ]

        indicator = [
            "-",
            "NA",
            "NA",
            "0",
            "0",
            "100%",
            "95%",
            "100%",
            "0",
            "NA",
            "NA",
            "100%",
            "99%",
            "100%",
            "100%",
            "8.5",
            "0",
        ]

        fields_display = [
            'transportation_project',
        ]    
        
        rows = [field for field in self.model._meta.get_fields() if field.name not in excludes]
        rows = zip(rows,indicator)
        
        from inspection.utils import get_exist_option_items
        context["columns"] = get_exist_option_items(VehicleTransportationKPI.TRANSPORTATION_PROJECT_OPTION, self.get_queryset(), 'transportation_project')   
        context["column_key"] = "transportation_project"  # for cell matching
        context["columns_exist"] = [ _.transportation_project for _ in queryset.qs ]
        context["indicator"] = indicator
        context["rows"] = rows # row th display
        context["hidden_fields"] = excludes
        context["fields_display"] = fields_display
        
        context["top_filter_form"] = VehicleTransportationKPIFilterForm(data=self.request.GET or None) 

        context["project_name"] = "vehicle tranportation KPI"

        self.request.session["transport_kpi_year"] = self.request.GET.get('year')
        self.request.session["transport_kpi_month"] = self.request.GET.get('month')

        #if self.request.GET.get('year') and self.request.GET.get('month'):
        #    context["create_url"] = reverse("transportationkpi_create", kwargs={'year':self.request.GET.get('year'), 'month':self.request.GET.get('month')})

        if self.request.GET.get('year') and self.request.GET.get('month'):
            temp_object = self.model.objects.first()
            if not temp_object:
                temp_object = self.model()
            context["create_url"] = temp_object.get_create_url(self.request.GET.get('year'), self.request.GET.get('month'), "01")[:-3]
            
        return context       

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset() # copy from BaseListView::get
        context = self.get_context_data()
        return self.render_to_response(context)

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('vehicle tranportation KPI'),request.path_info),
        ])
        return super(TransportationKPIListDisplayView, self).dispatch(request,args,kwargs)   

class TransportationKPIListEditView(ListView):
    model = VehicleTransportationKPI
    template_name = "kpi/transportationkpi_list_edit.html"
    filter_class = VehicleTransportationKPIFilter

    def get_context_data(self, *args, **kwargs):

        excludes = [
            'id',
            'year',
            'month',
        ]

        context = super(TransportationKPIListEditView, self).get_context_data(*args, **kwargs)
        #context["object_list"] = self.model.objects.all()
        qs = self.get_queryset(*args, **kwargs)
        queryset = self.filter_class(self.request.GET, queryset=qs).qs 
        context["object_list"] = queryset if self.request.GET else None
        formset = vehicle_transportation_kpi_model_formset(queryset=queryset) if self.request.GET else None
        context["formset"] = formset

        context["rows_fields"] = formset[0] if formset and len(formset) else VehicleTransportationKPIForm(instance=VehicleTransportationKPI.objects.all().first())
        #print [field for name, field in VehicleTransportationKPIForm().fields.items() if not name in excludes ]
        from inspection.utils import get_exist_option_items
        context["columns"] = get_exist_option_items(VehicleTransportationKPI.TRANSPORTATION_PROJECT_OPTION, self.get_queryset(), 'transportation_project')
        context["column_key"] = "transportation_project"
        context["project_name"] = "vehicle tranportation KPI"
        context["hidden_fields"] = excludes
        context["date_field_list"] = [""]

        context["top_filter_form"] = VehicleTransportationKPIFilterForm(data=self.request.GET or None) 

        return context       

    def post(self, request, *args, **kwargs):
        print request.GET
        formset = vehicle_transportation_kpi_model_formset(request.POST or None, request.FILES or None)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.save()
            messages.success(request, "Your list has been updated.")
            return redirect(reverse("transportationkpi_list_edit",  kwargs={}) + "?" + request.META['QUERY_STRING'])

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
        