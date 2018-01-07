from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View, TemplateResponseMixin, ContextMixin, TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin, ModelFormMixin
from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage
from django_filters import FilterSet, CharFilter, NumberFilter, BooleanFilter, DateFilter, MethodFilter
from django.utils.encoding import force_str, force_text
from django.db import models
import csv
import codecs
from django.utils import timezone
from inspection.mixins import StaffRequiredMixin
from inspection.utils import gen_csv

from .models import  (
    EquipmentInspection,
    EquipmentType,
    Equipment,
    SprayPumpRoomInspection,
    SprayWarehouseInspection,
    HSSEKPI,
    )

from .forms import (
    EquipmentInspectionForm, equipment_inspection_model_formset,
    EquipmentInspectiontFilterForm,
)

from .forms import (
    SprayPumpRoomInspectionForm,
    spray_pumproom_inspection_model_formset, 
    SprayInspectionFilterForm,
    SprayWarehouseInspectionForm,
    spray_warehouse_inspection_model_formset,
    HSSEKPIForm,
    hssekpi_model_formset,

)

from inspection.utils import get_exist_option_items
from inspection.models import month_choice

# Create your views here.
# https://www.douban.com/note/350934079/
# http://blog.csdn.net/xyp84/article/details/7945094
# http://caibaojian.com/simple-responsive-table.html


class EquipmentInsepctionFilter(FilterSet):
    category_id = CharFilter(name='equipment__type__id', lookup_type='exact', distinct=True)
    use_condition = CharFilter(name='use_condition', lookup_type='exact', distinct=True)
    inspector = CharFilter(name='inspector', lookup_type='exact', distinct=True)
    date_of_inspection_start = DateFilter(name='check_date', lookup_type='gte', distinct=True)
    date_of_inspection_end = DateFilter(name='check_date', lookup_type='lte', distinct=True)

    class Meta:
        model = EquipmentInspection
        fields = [
            'category_id',
            'use_condition',
            'inspector',
            'date_of_inspection_start',
            'date_of_inspection_end',
        ]

class FilterMixin(object):
    filter_class = None
    search_ordering_param = "ordering"

    def get_queryset(self, *args, **kwargs):
        try:
            qs = super(FilterMixin, self).get_queryset(*args, **kwargs)
            return qs
        except:
            raise ImproperlyConfigured("You must have a queryset in order to use the FilterMixin")

    def get_context_data(self, *args, **kwargs):
        context = super(FilterMixin, self).get_context_data(*args, **kwargs)
        qs = self.get_queryset()
        ordering = self.request.GET.get(self.search_ordering_param, '-updated')
        if ordering:
            qs = qs.order_by(ordering)
        filter_class = self.filter_class
        if filter_class:
            f = filter_class(self.request.GET, queryset=qs)
            context["object_list"] = f
        return context



class EquipmentInspectionListView(FilterMixin, ListView):
    model = EquipmentInspection
    queryset = EquipmentInspection.objects.get_this_day()
    #object_list = queryset
    template_name = "equipment/equipment_inspection_list.html"
    filter_class = EquipmentInsepctionFilter

    def get_queryset(self, *args, **kwargs):
        #qs = super(EquipmentInspectionListView, self).get_queryset(*args, **kwargs)
        qs  = self.model.objects.all() if self.request.user.is_staff else self.model.objects.filter(use_condition='normal')
        return qs

    def get_context_data(self, *args, **kwargs):

        context = super(EquipmentInspectionListView, self).get_context_data(*args, **kwargs)

        queryset = context["object_list"].qs # filtered qs
        category_id = self.request.GET.get("category_id", None)

        if category_id and int(category_id) > 0:
            queryset = queryset.filter(equipment__type__id=category_id)
        else:
            category_id = ""

        paginator = Paginator(queryset, 10)

        qs = None
        page = self.request.GET.get('page')
        try:
            qs = paginator.page(page)
        except PageNotAnInteger: # If page is not an integer, deliver first page.
            qs = paginator.page(1)
        except EmptyPage:        # If page is out of range (e.g. 9999), deliver last page of results.
            qs = paginator.page(paginator.num_pages)

        context["categories"] = EquipmentType.objects.all()
        context["current_category"] = category_id
        context["object_list"] = qs
        context["object_list_overdue"] = queryset.filter(use_condition="breakdown", due_date__lt=timezone.now()) if queryset and self.request.user.is_staff else None 
        from .admin import EquipmentInspectionAdmin
        fields = EquipmentInspectionAdmin.list_display
        context["fields"] = [field.name for field in self.model._meta.get_fields() if field.name in fields]
        context["fields"].remove('completed_time')
        context["fields_display"] = ["use_condition",]
        context["filter_form"] = EquipmentInspectiontFilterForm(data=self.request.GET or None) 

        filter_use_condition = self.request.GET.get("use_condition", "")
        filter_inspector = self.request.GET.get("inspector", "")
        filter_date_of_inspection_start = self.request.GET.get("date_of_inspection_start", "")
        filter_date_of_inspection_end = self.request.GET.get("date_of_inspection_end", "")

        filter_str = "use_condition=%s&inspector=%s&date_of_inspection_start=%s&date_of_inspection_end=%s" % (filter_use_condition, filter_inspector, filter_date_of_inspection_start, filter_date_of_inspection_end)
        context["filter_str"] = filter_str

        return context


    def post(self, *args, **kwargs):
        qs = self.get_queryset()
        f = EquipmentInsepctionFilter(self.request.GET, queryset=qs)

        fields_display = [ "use_condition", ]
        fields_fk = ["equipment",  ]
        fields_datetime = ["updated","completed_time", ]
        excludes = ["",]
        
        return gen_csv(self.model, f.qs, "equipment_export.csv", fields_display, fields_fk, fields_datetime, excludes)

        response = HttpResponse(content_type='text/csv')        
        response['Content-Disposition'] = 'attachment; filename="equipment_export.csv"'
        response.write(codecs.BOM_UTF8) # add bom header
        writer = csv.writer(response)

        row = []
        for field in self.model._meta.get_fields():
            row.append(field.verbose_name)
        writer.writerow(row)

        for obj in f.qs:
            row = []
            for field in self.model._meta.get_fields():
                #row.append(field.value_to_string(obj).encode('utf8'))
                value = getattr(obj, field.name) 
                if value:
                    if field.name in fields_datetime:
                        value = value.strftime('%Y-%m-%d %H:%M:%S')             
                    elif field.name in fields_display:
                        value = obj._get_FIELD_display(field)
                    elif field.name in fields_fk:
                        value = force_text(value, strings_only=True)
                    value = "%s" %  (value)
                    row.append(value.encode('utf8'))
                else:
                    row.append("")
            writer.writerow(row)    

        return response


    def get_success_url(self, *args, **kwargs):
        return reverse("equipmentinsepction_list", kwargs={})

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_("Equipmentinsepction List"),  request.path_info),            
        ])
        return super(EquipmentInspectionListView, self).dispatch(request,args,kwargs)      


class EquipmentInspectionDetailView(DetailView):
    model = EquipmentInspection
    template_name = "equipment/equipment_inspection_detail.html"

class EquipmentInspectionCreateView(StaffRequiredMixin, CreateView):
    model = EquipmentInspection
    form_class = EquipmentInspectionForm
    template_name = "equipment/equipment_inspection_create_form.html"

    def get_context_data(self, *args, **kwargs):
        context = super(EquipmentInspectionCreateView, self).get_context_data(*args, **kwargs)

        form = self.get_form()
        cat = self.kwargs.get('cat',None)
        if cat and int(cat)>0:
            form.fields['equipment'].queryset = Equipment.objects.filter(type__id=cat)

        context["form"] = form
        context["is_create_view"] = True

        return context

    def form_valid(self, form):
        instance = form.save(commit = False)
        instance.inspector = self.request.user
        instance.save()
        return HttpResponse(render_to_string('equipment/equipment_inspection_edit_form_success.html', {'object': instance, "is_create_view" : 1 }))  

class EquipmentInspectionQuickUpdateView(ListView):
    model = EquipmentInspection
    queryset = EquipmentInspection.objects.get_this_day()
    #object_list = queryset
    template_name = "equipment/equipment_inspection_quickupdate.html"

    def get_context_data(self, *args, **kwargs):
        context = super(EquipmentInspectionQuickUpdateView, self).get_context_data(*args, **kwargs)

        formset = equipment_inspection_model_formset(queryset=self.model.objects.get_this_day(),
            initial=[{'use_condition': _('Normal'),}])
        context["formset"] = formset
        context["extra_form_lg_one"] = True
        # context["objects_list"] = self.model.objects.get_this_day()
        return context

    def post(self, request, *args, **kwargs):
        #postresult = super(EquipmentInspectionQuickUpdateView, self).post(request, *args, **kwargs)

        formset = equipment_inspection_model_formset(request.POST or None, request.FILES or None)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.save()
            messages.success(request, "Your list has been updated.")
            return redirect(reverse("equipmentinsepction_quickupdate",  kwargs={}))

        self.object_list = self.get_queryset() # copy from BaseListView::get
        context = self.get_context_data()
        context['formset'] = formset
        return self.render_to_response(context)

    def get_success_url(self, *args, **kwargs):
        return reverse("equipmentinsepction_quickupdate", kwargs={})    

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_("Equipmentinsepction List"), reverse("equipmentinsepction_list", kwargs={})),            
            (_("Quick Update"), request.path_info),
        ])
        return super(EquipmentInspectionQuickUpdateView, self).dispatch(request,args,kwargs)      

class EquipmentInspectionUpdateView(StaffRequiredMixin, UpdateView):
    model = EquipmentInspection
    form_class = EquipmentInspectionForm
    template_name = 'equipment/equipment_inspection_edit_form.html'

    def get_context_data(self, *args, **kwargs):
        context = super(EquipmentInspectionUpdateView, self).get_context_data(*args, **kwargs)

        form = self.get_form()
        try:
            instance = EquipmentInspection.objects.filter(pk=self.kwargs.get('pk',None))[0]
            form.fields['equipment'].choices = ((instance.equipment.id, instance.equipment), )        
        except:
            pass

        context["form"] = form
        print context

        return context

    def dispatch(self, *args, **kwargs):
        self.item_id = kwargs['pk']
        return super(EquipmentInspectionUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = self.get_object()
        instance = form.save(commit=False)
        if obj.use_condition == "breakdown" and instance.use_condition == "normal":
            instance.completed_time = timezone.now() #.strftime('%Y-%m-%d %H:%M:%S')
        elif obj.use_condition == "normal" and instance.use_condition == "breakdown":
            instance.completed_time = None
        instance.save()
        item = EquipmentInspection.objects.get(id=self.item_id)
        return HttpResponse(render_to_string('equipment/equipment_inspection_edit_form_success.html', {'object': item, "is_create_view" : 0 }))        


class DashboardTableDetailView(DetailView):
    model = None
    template_name = "equipment/dashboard_table_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardTableDetailView, self).get_context_data(*args, **kwargs)

        context["fields"] = [field for field in self.model._meta.get_fields() if not field.name=="id"]
        context["year"] = self.request.session["filter_key"]

        return context

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (self.model._meta.verbose_name, self.get_object().get_list_display()),            
            (self.get_object(), request.path_info),
        ])
        return super(DashboardTableDetailView, self).dispatch(request,args,kwargs)   

    def get_success_url(self):
        return self.get_object().get_list_display()

class SprayPumproomInspectionDetailView(DashboardTableDetailView):
    model = SprayPumpRoomInspection

    def get_context_data(self, *args, **kwargs):
        context = super(SprayPumproomInspectionDetailView, self).get_context_data(*args, **kwargs)

        fields_display = {
            'voltage_and_power_normal',
            'indicator_and_instrument_normal',
            'switch_contactor_and_connection_normal',
            'no_corrosion_inside_and_foundation_bolt_not_loose',
            'motor_and_pump_connection_intact',
            'motor_sample_integrated',
            'no_corrosion_and_damage',
            'valve_normally_open',
            'one_way_valve_intact_and_no_leak_and_pressure_gage_normal',
            'pressure_maintaining_valve_intact',
            'water_level_normal_and_moisturizing_well',
            'water_level_cover_plate_and_no_abnormal_move',
            'pool_wall_dry_and_no_leak',
            'no_sundries_in_pump_house',
            'pump_house_clean_and_tidy',
            'rectification_status'
        }
        context["fields_display"] = fields_display

        return context



class SprayWarehouseInspectionDetailView(DashboardTableDetailView):
    model = SprayWarehouseInspection

    def get_context_data(self, *args, **kwargs):
        context = super(SprayWarehouseInspectionDetailView, self).get_context_data(*args, **kwargs)
        fields_display = {
            "valve_normal",
            "valve_open_signal_transmission_normal",
            "valve_no_corrosion",
            "water_testing_normal",
            "valve_switch_in_close_status",
            "pipe_network_pressure_normal",
            "pipe_valve_in_open_status",
            "pipe_connection_no_leakage",
            "spray_head_no_leakage",
            "rectification_status"
        }
        context["fields_display"] = fields_display

        return context

class HSSEKPIDetailView(DashboardTableDetailView):
    model = HSSEKPI

    def get_context_data(self, *args, **kwargs):
        context = super(HSSEKPIDetailView, self).get_context_data(*args, **kwargs)
        fields_display = {
        }
        context["fields_display"] = fields_display

        return context

class DashboardTableUpdateView(StaffRequiredMixin, UpdateView):
    model = None
    form_class = None
    template_name = "equipment/dashboard_table_update.html"
    

    def get_success_url(self):
        return self.get_object().get_absolute_url()

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (self.model._meta.verbose_name, self.get_object().get_list_display()),             
            (self.get_object(), request.path_info),
        ])
        return super(DashboardTableUpdateView, self).dispatch(request,args,kwargs)  


class SprayPumproomInspectionUpdateView(DashboardTableUpdateView):
    model = SprayPumpRoomInspection
    form_class = SprayPumpRoomInspectionForm

class SprayWarehouseInspectionUpdateView(DashboardTableUpdateView):
    model = SprayWarehouseInspection
    form_class = SprayWarehouseInspectionForm    

class HSSEKPIUpdateView(DashboardTableUpdateView):
    model = HSSEKPI
    form_class = HSSEKPIForm    

class DashboardTableCreateView(StaffRequiredMixin, CreateView):
    model = None
    form_class = None
    template_name = "equipment/dashboard_table_create.html"    

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardTableCreateView, self).get_context_data(*args, **kwargs)
        context["year"] = self.kwargs.get('year')
        context["form"] = self.form_class(self.request.POST or None, self.request.GET or None, initial={'year':self.kwargs.get('year'),'month':self.kwargs.get('month')})

        return context

    def form_valid(self, form, *args, **kwargs):
        obj = form.save(commit = False)
        obj.inspector = self.request.user
        obj.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return self.model().get_list_display()+"?year="+self.request.session["filter_key"]

class SprayPumproomInspectionCreateView(DashboardTableCreateView):
    model = SprayPumpRoomInspection
    form_class = SprayPumpRoomInspectionForm

class SprayWarehouseInspectionCreateView(DashboardTableCreateView):
    model = SprayWarehouseInspection
    form_class = SprayWarehouseInspectionForm

class HSSEKPICreateView(DashboardTableCreateView):
    model = HSSEKPI
    form_class = HSSEKPIForm

class DashboardTableListDisplayView(ListView):
    model = None
    filter_class = None
    filter_form = None
    template_name = "equipment/dashboard_table_list_display.html"    

    # group format
    groups =[
    ]

    # indicator for each item or KPIs if exist
    indicator = [
    ]

    # hidden fields
    excludes = [
        'id',
        'year',
        'updated',
    ]

    fields_display = [
        'rectification_status'
    ]

    column_key = 'month'  # default
    filter_key_name = 'year'

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardTableListDisplayView, self).get_context_data(*args, **kwargs)

        qs = self.get_queryset()
        queryset = self.filter_class(self.request.GET, queryset=qs) if self.request.GET.get(self.filter_key_name) else None
        context["object_list"] = queryset

        rows = [field for field in self.model._meta.get_fields() if field.name not in self.excludes]
        if self.indicator:
            rows = zip(rows,self.indicator)
        else:
            rows = zip(rows, list("na"*len(rows)))
        
        context["column_key"] = self.column_key
        if 0: # only show exist month in db
            context["columns"] = get_exist_option_items(month_choice, self.get_queryset(), context["column_key"])
        else:
            context["columns"] = month_choice         
        
        context["columns_exist"] = [ obj.month for obj in queryset.qs ] if queryset else None
        # 
        context["groups"] = self.groups
        context["indicator"] = self.indicator
        context["rows"] = rows # row th display
        context["hidden_fields"] = self.excludes
        context["fields_display"] = self.fields_display
        context["top_filter_form"] = self.filter_form(data=self.request.GET or None) 
        context["project_name"] = self.model._meta.verbose_name
        context["model_name"] = str(self.model.__name__)

        self.request.session["filter_key"] = self.request.GET.get(self.filter_key_name)        

        if self.request.GET.get(self.filter_key_name):
            temp_object = self.model.objects.first()
            if not temp_object:
                temp_object = self.model()
            context["create_url"] = temp_object.get_create_url(self.request.GET.get(self.filter_key_name),"00")[:-3]
        
        return context       

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset() # copy from BaseListView::get
        context = self.get_context_data()
        return self.render_to_response(context)

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (self.model._meta.verbose_name,request.path_info),
        ])
        return super(DashboardTableListDisplayView, self).dispatch(request,args,kwargs)   


class SprayPumproomInspectionFilter(FilterSet):
    year = CharFilter(name='year', lookup_type='exact', distinct=True)

    class Meta:
        model = SprayPumpRoomInspection
        fields = [
            'year',
        ]


class SprayPumproomInspectionListDisplayView(DashboardTableListDisplayView):
    model = SprayPumpRoomInspection
    template_name = "equipment/spray_pumproom_inspection_dashboard_table_list_display.html"    
    
    filter_class = SprayPumproomInspectionFilter
    filter_form = SprayInspectionFilterForm

    groups =[
        ('month', "",1),
        ('voltage_and_power_normal', _("power distribution cabinet"),3),
        ('no_corrosion_inside_and_foundation_bolt_not_loose', _("spray pump"),3),
        ('no_corrosion_and_damage', _("valve"),4),
        ('water_level_normal_and_moisturizing_well', _("pool"),3),
        ('no_sundries_in_pump_house', _("sanitation"),2),
        ('rectification_status', _("Inspector"),4),
    ]

    fields_display = [
        'month',
        'rectification_status'
    ]

    def post(self, *args, **kwargs):
        qs = self.get_queryset()
        f = self.filter_class(self.request.GET, queryset=qs)

        fields_display = [ "month", "rectification_status",  ]
        fields_fk = ["",  ]
        fields_datetime = ["check_date", "updated",]
        excludes = [field.name for field in self.model._meta.get_fields() if isinstance(field, models.ManyToOneRel)]
        fields_multiple = ["",]

        from inspection.utils import gen_csv
        return gen_csv(self.model, f.qs, "spray_pumproom_export.csv", fields_display, fields_fk, fields_datetime, excludes, fields_multiple)


class SprayWarehouseInspectionFilter(FilterSet):
    year = CharFilter(name='year', lookup_type='exact', distinct=True)

    class Meta:
        model = SprayWarehouseInspection
        fields = [
            'year',
        ]


class SprayWarehouseInspectionListDisplayView(DashboardTableListDisplayView):
    model = SprayWarehouseInspection
    template_name = "equipment/spray_pumproom_inspection_dashboard_table_list_display.html"    
    
    filter_class = SprayWarehouseInspectionFilter
    filter_form = SprayInspectionFilterForm

    groups =[
        ('month', "",1),
        ('valve_normal', _("The end test device"),5),  # left is align with model field
        ('pipe_network_pressure_normal', _("spray header and pipe network"),4),
        ('rectification_status', _("Inspector"),4),
    ]

    fields_display = [
        'month',
        'rectification_status'
    ]

    def post(self, *args, **kwargs):
        qs = self.get_queryset()
        f = self.filter_class(self.request.GET, queryset=qs)

        fields_display = [ "month", "rectification_status",  ]
        fields_fk = ["",  ]
        fields_datetime = ["check_date", "updated",]
        excludes = [field.name for field in self.model._meta.get_fields() if isinstance(field, models.ManyToOneRel)]
        fields_multiple = ["",]

        from inspection.utils import gen_csv
        return gen_csv(self.model, f.qs, "spray_warehouse_export.csv", fields_display, fields_fk, fields_datetime, excludes, fields_multiple)


class HSSEKPIFilter(FilterSet):
    year = CharFilter(name='year', lookup_type='exact', distinct=True)

    class Meta:
        model = HSSEKPI
        fields = [
            'year',
        ]


class HSSEKPIListDisplayView(DashboardTableListDisplayView):
    model = HSSEKPI
    filter_class = HSSEKPIFilter
    filter_form = SprayInspectionFilterForm
    template_name = "equipment/hssekpi_dashboard_list_display.html"  

    indicator =[
        '-',
        '0',
        '0',
        '0',
        '0',
        '0',
        '0',
        '0',
        '0',
        '>=21',
        '1',
        '95%',
        'NA',
        '95%',
        '100%',
        'NA',
    ]

    fields_display = [
        'month',
    ]    

    def get_context_data(self, *args, **kwargs):
        context = super(HSSEKPIListDisplayView, self).get_context_data(*args, **kwargs)

        context["indicator"] = self.indicator    
        
        return context      

    def post(self, *args, **kwargs):
        qs = self.get_queryset()
        f = self.filter_class(self.request.GET, queryset=qs)

        fields_display = [ "month",  ]
        fields_fk = ["",  ]
        fields_datetime = ["created",]
        excludes = [field.name for field in self.model._meta.get_fields() if isinstance(field, models.ManyToOneRel)]
        fields_multiple = ["",]

        from inspection.utils import gen_csv
        return gen_csv(self.model, f.qs, "hsse_kpi_export.csv", fields_display, fields_fk, fields_datetime, excludes, fields_multiple)

        
class DashboardTableListEditView(StaffRequiredMixin, ListView):
    model = None    
    filter_class = None
    filter_form = None
    formset_class = None
    form_class = None

    # queryset = self.model.objects.all() #queryset_ordered()

    template_name = "equipment/dashboard_table_list_edit.html"

    def get_queryset(self, *args, **kwargs):  # queryset has cache
        return self.model.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardTableListEditView, self).get_context_data(*args, **kwargs)

        excludes = [
            'id',
            'year',
            'inspector'
        ]

        qs = self.get_queryset(*args, **kwargs)
        queryset = self.filter_class(self.request.GET, queryset=qs).qs 
        context["object_list"] = queryset if self.request.GET else None
        formset = self.formset_class(queryset=queryset) if self.request.GET else None
        context["formset"] = formset
        context["fakeform"] = self.form_class() if not formset else None  # use this fakeform to get url

        context["rows_fields"] = formset[0] if formset and len(formset) else self.form_class(instance=self.model.objects.all().first())

        if 0:
            context["columns"] = get_exist_option_items(month_choice, self.get_queryset(), 'month')
        else:
            context["columns"] = month_choice
        context["column_key"] = "month"
        context["project_name"] = self.model._meta.verbose_name
        context["hidden_fields"] = excludes
        context["date_field_list"] = ["check_date"]

        context["top_filter_form"] = self.filter_form(data=self.request.GET or None) 

        return context

    def post(self, request, *args, **kwargs):
        formset = self.formset_class(request.POST or None, request.FILES or None)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.save()
            messages.success(request, _("Your list has been updated."))
            return redirect(self.model.objects.first().get_list_edit()+'?year='+self.request.GET.get('year'))

        self.object_list = self.get_queryset() # copy from BaseListView::get
        context = self.get_context_data()
        context['formset'] = formset
        return self.render_to_response(context)

    def get_success_url(self, *args, **kwargs):
        # return self.model.objects.first().get_list_edit()
        return self.model().get_list_edit()

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (self.model._meta.verbose_name,request.path_info),
        ])
        return super(DashboardTableListEditView, self).dispatch(request,args,kwargs)    


class SprayPumproomInspectionListEditView(DashboardTableListEditView):
    model = SprayPumpRoomInspection
    form_class = SprayPumpRoomInspectionForm
    formset_class = spray_pumproom_inspection_model_formset
    filter_class = SprayPumproomInspectionFilter
    filter_form = SprayInspectionFilterForm   

    queryset = SprayPumpRoomInspection.objects.all() #queryset_ordered() 

class SprayWarehouseInspectionListEditView(DashboardTableListEditView):
    model = SprayWarehouseInspection
    form_class = SprayWarehouseInspectionForm
    formset_class = spray_warehouse_inspection_model_formset
    filter_class = SprayWarehouseInspectionFilter
    filter_form = SprayInspectionFilterForm   

    queryset = SprayWarehouseInspection.objects.all() #queryset_ordered() 

class HSSEKPIListEditView(DashboardTableListEditView):
    model = HSSEKPI
    form_class = HSSEKPIForm
    formset_class = hssekpi_model_formset
    filter_class = HSSEKPIFilter
    filter_form = SprayInspectionFilterForm   

    queryset = HSSEKPI.objects.all() #queryset_ordered() 
