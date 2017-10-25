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

from .models import  (
    ElectricalEquipmentInspection,
    EquipmentType,
    Equipment,
    )

from .forms import (
    ElectricalEquipmentInspectionForm, electrical_equipment_inspection_model_formset,
)

# Create your views here.
# https://www.douban.com/note/350934079/
# http://blog.csdn.net/xyp84/article/details/7945094
# http://caibaojian.com/simple-responsive-table.html


class EquipmentInspectionListView(ListView):
    model = ElectricalEquipmentInspection
    queryset = ElectricalEquipmentInspection.objects.get_this_day()
    #object_list = queryset
    template_name = "equipment/equipment_inspection_list.html"

    # def get_queryset(self, *args, **kwargs):
    #     return self.queryset

    def get_context_data(self, *args, **kwargs):
        context = super(EquipmentInspectionListView, self).get_context_data(*args, **kwargs)

        queryset = ElectricalEquipmentInspection.objects.all()
        category_id = self.request.GET.get("category_id", None)
        if category_id:
            queryset = ElectricalEquipmentInspection.objects.all().filter(equipment__type__id=category_id)

        paginator = Paginator(queryset, 2)

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
        context["object_list"] = qs
        return context

    def get_success_url(self, *args, **kwargs):
        return reverse("equipmentinsepction_list", kwargs={})

class EquipmentInspectionDetailView(DetailView):
    model = ElectricalEquipmentInspection
    template_name = "equipment/equipment_inspection_detail.html"

class EquipmentInspectionCreateView(CreateView):
    model = ElectricalEquipmentInspection
    form_class = ElectricalEquipmentInspectionForm
    template_name = "equipment/equipment_inspection_create_form.html"

    def form_valid(self, form):
        instance = form.save()
        return HttpResponse(render_to_string('equipment/equipment_inspection_edit_form_success.html', {'object': instance}))  

class EquipmentInspectionQuickUpdateView(ListView):
    model = ElectricalEquipmentInspection
    queryset = ElectricalEquipmentInspection.objects.get_this_day()
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

class ElectricalEquipmentInspectionUpdateView(UpdateView):
    model = ElectricalEquipmentInspection
    form_class = ElectricalEquipmentInspectionForm
    template_name = 'equipment/equipment_inspection_edit_form.html'

    def dispatch(self, *args, **kwargs):
        self.item_id = kwargs['pk']
        return super(ElectricalEquipmentInspectionUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        item = ElectricalEquipmentInspection.objects.get(id=self.item_id)
        return HttpResponse(render_to_string('equipment/equipment_inspection_edit_form_success.html', {'object': item}))        