from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render

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

class TableListMixin(object):
    fields_display = []
    fields_files = []
    fields_images = []

    def get_context_data(self, *args, **kwargs):
        context = super(TableListMixin, self).get_context_data(*args, **kwargs)
        context["fields"] = self.fields_display
        context["fields_files"] = self.fields_files
        context["fields_images"] = self.fields_images
        
        return context

class TableDetailMixin(object):
    fieldsets = [("title",{"fields":("",)}), ]
    fields_display = []
    fields_files = []
    fields_images = []

    model_sets = [("model name", None, []),]  # model name, object_list, list_display
    
    def get_context_data(self, *args, **kwargs):
        context = super(TableDetailMixin, self).get_context_data(*args, **kwargs)
        context["fieldsets"] = self.fieldsets
        context["fields_display"] = self.fields_display
        context["fields_files"] = self.fields_files
        context["fields_images"] = self.fields_images
        
        context["model_sets"] = self.model_sets
        
        return context        