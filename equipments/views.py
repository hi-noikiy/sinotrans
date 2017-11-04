from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string

from django.views.generic.base import View, TemplateResponseMixin, ContextMixin, TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin, ModelFormMixin
from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage
from django_filters import FilterSet, CharFilter, NumberFilter, BooleanFilter, DateFilter, MethodFilter

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
    SprayPumpRoomInspectionForm,spray_pumproom_inspection_model_formset,
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

    def get_success_url(self, *args, **kwargs):
        return reverse("equipmentinsepction_list", kwargs={})

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

        formset = electrical_equipment_inspection_model_formset(queryset=self.model.objects.get_this_day(),
            initial=[{'use_condition': _('Normal'),}])
        context["formset"] = formset
        # context["objects_list"] = self.model.objects.get_this_day()
        return context

    def post(self, request, *args, **kwargs):
        #postresult = super(EquipmentInspectionQuickUpdateView, self).post(request, *args, **kwargs)

        formset = electrical_equipment_inspection_model_formset(request.POST or None, request.FILES or None)
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




class SprayPumproomInspectionListView(ListView):
    model = SprayPumpRoomInspection
    queryset = SprayPumpRoomInspection.objects.all() #queryset_ordered()
    #filter_class = SprayPumproomInsepctionFilter

    template_name = "equipment/spray_pump_room_inspection.html"

    def get_queryset(self, *args, **kwargs):  # queryset has cache
        return SprayPumpRoomInspection.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(SprayPumproomInspectionListView, self).get_context_data(*args, **kwargs)

        formset = spray_pumproom_inspection_model_formset(queryset=self.get_queryset(*args, **kwargs))
        context["formset"] = formset
        months_exist = [_.month for _ in self.get_queryset()]
        from inspection.models import month_choice
        months = [_ for _ in month_choice if _[0] in months_exist]
        context["months"] = months

        return context

    def post(self, request, *args, **kwargs):
        formset = spray_pumproom_inspection_model_formset(request.POST or None, request.FILES or None)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.save()
            messages.success(request, "Your list has been updated.")
            return redirect(reverse("spraypumproominspection_list",  kwargs={}))

        self.object_list = self.get_queryset() # copy from BaseListView::get
        context = self.get_context_data()
        context['formset'] = formset
        return self.render_to_response(context)

    def get_success_url(self, *args, **kwargs):
        return reverse("spraypumproominspection_list", kwargs={})        