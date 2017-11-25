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

from chartjs.views.lines import BaseLineChartView

from .forms import PickingBillScanForm, WaybillScanForm
from .models import Waybill, PickingBill
# Create your views here.

class PickingbillAssignView(FormMixin, ListView) :
    template_name = "picking/pickingbill_assign.html"
    model = PickingBill
    form_class = PickingBillScanForm

    def get_context_data(self, *args, **kwargs):
        context = super(PickingbillAssignView, self).get_context_data(*args, **kwargs)
        context["pickingbill_scan_form"] = PickingBillScanForm()        
        context["pickingbill_objects_unassigned"] = PickingBill.objects.all()
        field_exclude = ["id","waybill"]
        context["fields"] = [field for field in self.model._meta.get_fields() if not field.name in field_exclude]
        
        return context      

class WaybillCompleteView(FormMixin, ListView) :
    template_name = "picking/waybill_complete.html"
    model = Waybill
    form_class = WaybillScanForm

    def get_context_data(self, *args, **kwargs):
        context = super(WaybillCompleteView, self).get_context_data(*args, **kwargs)
        context["waybill_scan_form"] = WaybillScanForm(self.request.GET or None, self.request.POST or None )
        context["waybill_objects_unassigned"] = Waybill.objects.all()
        field_exclude = ["id","pickingbill"]
        context["fields"] = [field for field in self.model._meta.get_fields() if not field.name in field_exclude]
        
        return context          


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return labels for the x-axis."""
        # return self.get_dates()
        return ['2017-11-1', '2017-11-2', '2017-11-3', '2017-11-4', '2017-11-5']

    def get_providers(self):
        """Return names of datasets."""
        # return self.get_catetory()
        return ['Tom', 'Jerry', 'Haro', 'Boto']

    def get_data(self):
        """Return 3 datasets to plot."""
        # return self.get_chart_counts()
        return [["1.73","1.9","2.0","1.7"], ["1.83","1.774","1.8","1.8"], ["1.93","1.9","1.9","1.9"], ["2.13","1.4","2.5","2.0"],]  # per provider

class PickingbillStatView(ListView) :
    template_name = "picking/pickingbill_stat.html"
    model = PickingBill

    def get_context_data(self, *args, **kwargs):
        context = super(PickingbillStatView, self).get_context_data(*args, **kwargs)     
        context["x-axis"] = ['2017-11-1', '2017-11-2', '2017-11-3', '2017-11-4']
        context["y-axis"] = ['Tom', 'Jerry', 'Haro', 'Boto']
        context["values"] = [["1.73","1.774","1.5","2.0"], ["1.73","1.774","1.5","2.0"], ["1.73","1.774","1.5","2.0"], ["1.73","1.774","1.5","2.0"],]
        
        return context                
