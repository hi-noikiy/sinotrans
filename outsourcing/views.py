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
	Forklift
	)
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
        
        return context       

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_("Forklift"),reverse("forklift_list", kwargs={})),            
            (self.get_object(), request.path_info),
        ])
        return super(ForklifDetailView, self).dispatch(request,args,kwargs)           

