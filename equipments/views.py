from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _


from django.views.generic.base import View, TemplateResponseMixin, ContextMixin, TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin, ModelFormMixin
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


class ElectricalEquipmentInspectionListView(ListView):
    model = ElectricalEquipmentInspection
    queryset = ElectricalEquipmentInspection.objects.get_this_day()
    #object_list = queryset
    template_name = "equipment/electronical_equipment_inspection_list.html"

    # def get_queryset(self, *args, **kwargs):
    #     return self.queryset

    def get_context_data(self, *args, **kwargs):
        context = super(ElectricalEquipmentInspectionListView, self).get_context_data(*args, **kwargs)

        formset = electrical_equipment_inspection_model_formset(queryset=self.model.objects.get_this_day(),
            initial=[{'use_condition': _('Normal'),}])
        context["formset"] = formset
        # context["objects_list"] = self.model.objects.get_this_day()
        qs = Equipment.objects.all()
        category_id = self.request.GET.get("category_id", None)
        if category_id:
            qs = Equipment.objects.all().filter(type__id=category_id)
        context["categories"] = EquipmentType.objects.all()
        context["current_category"] = category_id
        context["object_list"] = qs
        return context

    def post(self, request, *args, **kwargs):
        #postresult = super(ElectricalEquipmentInspectionListView, self).post(request, *args, **kwargs)

        formset = electrical_equipment_inspection_model_formset(request.POST or None, request.FILES or None)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.save()
            messages.success(request, "Your list has been updated.")
            return redirect(reverse("electronialequipmentinsepction_list",  kwargs={}))

        self.object_list = self.get_queryset() # copy from BaseListView::get
        context = self.get_context_data()
        context['formset'] = formset
        return self.render_to_response(context)

    def get_success_url(self, *args, **kwargs):
        return reverse("electronialequipmentinsepction_list", kwargs={})

class ElectricalEquipmentInspectionDetailView(DetailView):
    model = ElectricalEquipmentInspection
    template_name = "equipment/electronical_equipment_inspection_detail.html"

class ElectricalEquipmentInspectionCreateView(CreateView):
    model = ElectricalEquipmentInspection
    form_class = ElectricalEquipmentInspectionForm
    template_name = "equipment/electronical_equipment_inspection_create.html"