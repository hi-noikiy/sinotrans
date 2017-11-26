from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views.generic.base import View, TemplateResponseMixin, ContextMixin, TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin, ModelFormMixin
from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage
from django_filters import FilterSet, CharFilter, NumberFilter, BooleanFilter, DateFilter, MethodFilter
import csv
import codecs

from .models import  (
    EquipmentInspection,
    EquipmentType,
    Equipment,
    SprayPumpRoomInspection,
    )

from .forms import (
    EquipmentInspectionForm, equipment_inspection_model_formset,
    EquipmentInspectiontFilterForm,
)

from .forms import (
    SprayPumpRoomInspectionForm,spray_pumproom_inspection_model_formset, SprayPumproomInspectionFilterForm,

)

# Create your views here.
# https://www.douban.com/note/350934079/
# http://blog.csdn.net/xyp84/article/details/7945094
# http://caibaojian.com/simple-responsive-table.html


class EquipmentInsepctionFilter(FilterSet):
    category_id = CharFilter(name='equipment__type__id', lookup_type='exact', distinct=True)
    use_condition = CharFilter(name='use_condition', lookup_type='exact', distinct=True)
    inspector = CharFilter(name='inspector', lookup_type='exact', distinct=True)
    date_of_inspection_start = DateFilter(name='date_of_inspection', lookup_type='gte', distinct=True)
    date_of_inspection_end = DateFilter(name='date_of_inspection', lookup_type='lte', distinct=True)

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
        qs  = self.model.objects.all()
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

        response = HttpResponse(content_type='text/csv')        
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        response.write(codecs.BOM_UTF8) # add bom header
        writer = csv.writer(response)

        row = []
        for field in self.model._meta.get_fields():
            print field.verbose_name
            row.append(field.verbose_name)
        writer.writerow(row)

        for obj in f.qs:
            row = []
            for field in self.model._meta.get_fields():
                #row.append(field.value_to_string(obj).encode('utf8'))
                value = "%s" %  (obj._get_FIELD_display(field))
                row.append(value.encode('utf8'))
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

class EquipmentInspectionCreateView(CreateView):
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
        instance = form.save()
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

class EquipmentInspectionUpdateView(UpdateView):
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

        return context

    def dispatch(self, *args, **kwargs):
        self.item_id = kwargs['pk']
        return super(EquipmentInspectionUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        item = EquipmentInspection.objects.get(id=self.item_id)
        return HttpResponse(render_to_string('equipment/equipment_inspection_edit_form_success.html', {'object': item, "is_create_view" : 0 }))        


class SprayPumproomInspectionDetailView(DetailView):
    model = SprayPumpRoomInspection
    template_name = "equipment/spray_pump_room_inspection_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SprayPumproomInspectionDetailView, self).get_context_data(*args, **kwargs)

        context["fields"] = [field for field in self.model._meta.get_fields() if not field.name=="id"]
        context["spraypumproominspection_year"] = self.request.session["spraypumproominspection_year"]

        return context


    def get_success_url(self):
        return reverse("spraypumproominspection_list_display", kwargs={})

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_("Spray Pump Room Inspection"), reverse("spraypumproominspection_list_display", kwargs={})),            
            (self.get_object(), request.path_info),
        ])
        return super(SprayPumproomInspectionDetailView, self).dispatch(request,args,kwargs)      

class SprayPumproomInspectionUpdateView(UpdateView):
    model = SprayPumpRoomInspection
    template_name = "equipment/spray_pump_room_inspection_update.html"
    form_class = SprayPumpRoomInspectionForm

    def get_success_url(self):
        return reverse("spraypumproominspection_detail", kwargs={"pk":self.get_object().pk})

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_("Spray Pump Room Inspection"), reverse("spraypumproominspection_list_display", kwargs={})),            
            (self.get_object(), request.path_info),
        ])
        return super(SprayPumproomInspectionUpdateView, self).dispatch(request,args,kwargs)      

class SprayPumproomInspectionCreateView(CreateView):
    model = SprayPumpRoomInspection
    template_name = "equipment/spray_pump_room_inspection_create.html"
    form_class = SprayPumpRoomInspectionForm

    def get_context_data(self, *args, **kwargs):
        context = super(SprayPumproomInspectionCreateView, self).get_context_data(*args, **kwargs)
        context["year"] = self.kwargs.get('year')
        context["form"] = self.form_class(self.request.POST or None, self.request.GET or None, initial={'year':self.kwargs.get('year')})

        return context

    def get_success_url(self):
        return reverse("spraypumproominspection_list_display", kwargs={})

class SprayPumproomInspectionFilter(FilterSet):
    year = CharFilter(name='year', lookup_type='exact', distinct=True)

    class Meta:
        model = SprayPumpRoomInspection
        fields = [
            'year',
        ]


class SprayPumproomInspectionListDisplayView(ListView):
    model = SprayPumpRoomInspection
    template_name = "equipment/spray_pump_room_inspection_list_display.html"
    filter_class = SprayPumproomInspectionFilter

    def get_context_data(self, *args, **kwargs):
        context = super(SprayPumproomInspectionListDisplayView, self).get_context_data(*args, **kwargs)
        #context["object_list"] = self.model.objects.all()

        qs = self.get_queryset()
        queryset = self.filter_class(self.request.GET, queryset=qs)
        context["object_list"] = queryset if self.request.GET else None

        excludes = [
            'id',
            'year',
        ]

        indicator = [
        ]

        groups =[
            ('month', "",1),
            ('voltage_and_power_normal', _("power distribution cabinet"),3),
            ('no_corrosion_inside_and_foundation_bolt_not_loose', _("spray pump"),3),
            ('no_corrosion_and_damage', _("valve"),4),
            ('water_level_normal_and_moisturizing_well', _("pool"),3),
            ('no_sundries_in_pump_house', _("sanitation"),2),
            ('inspector', _("Inspector"),2),

        ]

        rows = [field for field in self.model._meta.get_fields() if field.name not in excludes]
        if indicator:
            rows = zip(rows,indicator)
        else:
            rows = zip(rows, list("na"*len(rows)))
        print rows
        
        from inspection.utils import get_exist_option_items
        from inspection.models import month_choice
        context["columns"] = get_exist_option_items(month_choice, self.get_queryset(), 'month')
        context["column_key"] = "month"
        context["columns_exist"] = [ obj.month for obj in queryset.qs ]
        context["groups"] = groups
        context["indicator"] = indicator
        context["rows"] = rows # row th display
        context["hidden_fields"] = excludes

        context["top_filter_form"] = SprayPumproomInspectionFilterForm(data=self.request.GET or None) 

        context["project_name"] = "Spray Pump Room Inspection"

        self.request.session["spraypumproominspection_year"] = self.request.GET.get('year')        

        if self.request.GET.get('year'):
            context["create_url"] = reverse("spraypumproominspection_create", kwargs={'year':self.request.GET.get('year'), })
        
        return context       

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset() # copy from BaseListView::get
        context = self.get_context_data()
        return self.render_to_response(context)

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('Spray Pump Room Inspection'),request.path_info),
        ])
        return super(SprayPumproomInspectionListDisplayView, self).dispatch(request,args,kwargs)   

class SprayPumproomInspectionListEditView(ListView):
    model = SprayPumpRoomInspection
    queryset = SprayPumpRoomInspection.objects.all() #queryset_ordered()
    filter_class = SprayPumproomInspectionFilter

    template_name = "equipment/spray_pump_room_inspection_list_edit.html"

    def get_queryset(self, *args, **kwargs):  # queryset has cache
        return SprayPumpRoomInspection.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(SprayPumproomInspectionListEditView, self).get_context_data(*args, **kwargs)

        excludes = [
            'id',
            'year',
        ]

        qs = self.get_queryset(*args, **kwargs)
        queryset = self.filter_class(self.request.GET, queryset=qs).qs 
        context["object_list"] = queryset if self.request.GET else None
        formset = spray_pumproom_inspection_model_formset(queryset=queryset) if self.request.GET else None
        context["formset"] = formset

        context["rows_fields"] = formset[0] if formset and len(formset) else SprayPumpRoomInspectionForm(instance=self.model.objects.all().first())
        from inspection.utils import get_exist_option_items
        from inspection.models import month_choice
        context["columns"] = get_exist_option_items(month_choice, self.get_queryset(), 'month')
        context["column_key"] = "month"
        context["project_name"] = "Spray Pump Room Inspection"
        context["hidden_fields"] = excludes
        context["date_field_list"] = ["date_of_inspection"]


        context["top_filter_form"] = SprayPumproomInspectionFilterForm(data=self.request.GET or None) 

        return context

    def post(self, request, *args, **kwargs):
        formset = spray_pumproom_inspection_model_formset(request.POST or None, request.FILES or None)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.save()
            messages.success(request, "Your list has been updated.")
            return redirect(reverse("spraypumproominspection_list_edit",  kwargs={}))

        self.object_list = self.get_queryset() # copy from BaseListView::get
        context = self.get_context_data()
        context['formset'] = formset
        return self.render_to_response(context)

    def get_success_url(self, *args, **kwargs):
        return reverse("spraypumproominspection_list_edit", kwargs={})        

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('Spray Pump Room Inspection'),request.path_info),
        ])
        return super(SprayPumproomInspectionListEditView, self).dispatch(request,args,kwargs)           