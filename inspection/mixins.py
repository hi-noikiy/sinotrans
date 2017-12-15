from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.db import models
from django.forms import models as model_forms

class StaffRequiredMixin(object):
    @classmethod
    def as_view(self, *args, **kwargs):
        view = super(StaffRequiredMixin, self).as_view(*args, **kwargs)
        return login_required(view)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
        else:
            #raise Http404
            #return HttpResponseRedirect(reverse('home',kwargs={}))
            return render(request, "dailyinspection/permission_alert.html", {})

class SuperRequiredMixin(StaffRequiredMixin):

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_superuser:
			return super(SuperRequiredMixin, self).dispatch(request, *args, **kwargs)
		else:
			raise Http404

class LoginRequiredMixin(object):
	@classmethod
	def as_view(self, *args, **kwargs):
		view = super(LoginRequiredMixin, self).as_view(*args, **kwargs)
		return login_required(view)

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

class TableListViewMixin(object):
    template_name = "default/list.html"
    
    fields = []
    fields_display = []
    fields_files = []
    fields_images = []

    foreign_fields_images = []

    def get_context_data(self, *args, **kwargs):
        context = super(TableListViewMixin, self).get_context_data(*args, **kwargs)
        context["fields"] = self.fields
        context["fields_display"] = self.fields_display
        context["fields_files"] = self.fields_files
        context["fields_images"] = self.fields_images

        context["foreign_fields_images"] = self.foreign_fields_images
        
        return context

    def dispatch(self, request, *args, **kwargs):
        self.request.session["list_url"] = request.get_full_path()	
    
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (self.model._meta.verbose_name,request.path_info),
        ])
        return super(TableListViewMixin, self).dispatch(request,args,kwargs)   

# from django.db.models.fields import ManyToOneRel
from django.db import models
class TableDetailViewMixin(object):

    template_name = "default/detail.html"
    
    # fieldsets = [("title",{"fields":("",)}), ]
    fieldsets = []
    fields = []
    fields_display = []
    fields_files = []
    fields_images = []

    model = None

    model_sets = [("model name", None, []),]  # model name, object_list, list_display
    
    def get_context_data(self, *args, **kwargs):
        context = super(TableDetailViewMixin, self).get_context_data(*args, **kwargs)
        if not self.fieldsets:
            context["fields"] = [field for field in self.model._meta.get_fields() if not field.name in [self.model._meta.pk.attname,] and not isinstance(field, models.ManyToOneRel)] \
                    if not self.fields else self.fields
        # lookup_field
        # _get_non_gfk_field
        # need time to learning
        # pagination :: items_for_result
        context["fieldsets"] = self.fieldsets
        context["fields_display"] = self.fields_display
        context["fields_files"] = self.fields_files
        context["fields_images"] = self.fields_images
        
        context["model_sets"] = self.model_sets
        
        return context        

    def dispatch(self, request, *args, **kwargs):
        list_url=""
        try:
            list_url = self.get_object().get_absolute_url_list()
        except:
            pass

        self.request.session["detail_url"] = request.get_full_path()	
            
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (self.model._meta.verbose_name, list_url),
            (self.get_object(),request.path_info),
        ])
        return super(TableDetailViewMixin, self).dispatch(request,args,kwargs)    


# fields = ModelFormMixin::fields 

# form_class
# form_class = ModelFormMixin::get_form_class << model_forms.modelform_factory(model, fields=self.fields)
# form_class = FormMixin::get_form_class << self.form_class

# form = FormMixin::get_form()

# kwargs : ModelFormMixin::get_form_kwargs
#       instance :  self.object
# kwargs : FormMixin::get_form_kwargs
#       initial :  self.get_initial()
#       prefix :  self.get_prefix()
#       data : self.request.POST
#       files : self.request.FILES

# success_url : 
#       ModelFormMixin::get_success_url
#       FormMixin::get_success_url

# get_context_data
#       form : FormMixin::get_context_data
class UpdateViewMixin(object):
    template_name = "default/update.html"

    # model = models.Model
    fields = None # is defined in ModelFormMixin
    # fields = [field.name for field in model._meta.get_fields() if not field.name in [model._meta.pk.attname,] and not isinstance(field, models.ManyToOneRel)]

    def get_form_class(self):
        if not self.form_class:
            if self.fields:
                self.form_class = model_forms.modelform_factory(self.model, fields=self.fields, )
            else:
                self.form_class = model_forms.modelform_factory(self.model, exclude=["",], )
        return self.form_class
            
    def get_success_url(self):
        return self.get_object().get_absolute_url() # if not self.request.session.get("current_url", None) else self.request.session["current_url"]
        
    def get_context_data(self, *args, **kwargs):
        context = super(UpdateViewMixin, self).get_context_data(*args, **kwargs) 
        context["title"] = self.get_object()

        return context

    # HERE just for learning, it was implemented in base classed
    def post(self, request, *args, **kwargs):
        self.object = self.get_object() # must call in advace # called in  BaseUpdateView::post

        form = self.get_form()  # called in FormMixin::get_form
        # form = self.form_class(self.request.POST or None, self.request.FILES or None)        

        if form.is_valid():
            return self.form_valid(form)
        else:            
            return self.form_invalid(form)

        return super(UpdateViewMixin, self).post(request, *args, **kwargs)  

    # copy from FormMixin
    # def form_valid(self, form):
    #     return HttpResponseRedirect(self.get_success_url())

    # def form_invalid(self, form):
    #     return self.render_to_response(self.get_context_data())

    def get_fields(self, *args, **kwargs):
        return self.fields

        
    def dispatch(self, request, *args, **kwargs):
        if not self.fields and not self.get_fields() and not self.form_class:
            self.fields = [field.name for field in self.model._meta.get_fields() if not field.name in [self.model._meta.pk.attname,] and not isinstance(field, models.ManyToOneRel)]

        list_url=""
        try:
            list_url = self.get_object().get_absolute_url_list()
        except:
            pass
            
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (self.model._meta.verbose_name, list_url),
            (self.get_object(),request.path_info),
        ])
        return super(UpdateViewMixin, self).dispatch(request,args,kwargs)           

class CreateViewMixin(object):
    template_name = "default/create.html"

    def get_form_class(self):
        if not self.form_class:
            if self.fields:
                self.form_class = model_forms.modelform_factory(self.model, fields=self.fields, )
            else:
                self.form_class = model_forms.modelform_factory(self.model, exclude=["",], )
        return self.form_class
        
    def get_success_url(self):
        #return self.model().get_absolute_url_list()
        return self.object.get_absolute_url()  # default function

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (self.model._meta.verbose_name,self.model().get_absolute_url_list()),
            (_("Create"),request.path_info),
        ])
        return super(CreateViewMixin, self).dispatch(request,args,kwargs)                
