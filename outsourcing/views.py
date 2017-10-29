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

from .models import (
	Forklift, ForkliftMaint, 
	)

def option_value_convertion(tuple_enum,key):
	dict_enum = dict(tuple_enum)
	if key in dict_enum.keys():
		return dict_enum[key]
	else:
		return None

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

