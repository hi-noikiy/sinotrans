from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.views.generic.base import View, TemplateResponseMixin, ContextMixin, TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin, ModelFormMixin
from chartjs.views.lines import (JSONView, BaseLineChartView)
from django.http import HttpResponseRedirect
from django.conf import settings
from django.utils.translation import ugettext as _
from django_filters import FilterSet, CharFilter, NumberFilter, BooleanFilter, MethodFilter, MultipleChoiceFilter
from django.db.models import Q
from django.http import HttpResponse, Http404
import json
import time, datetime
from datetime import timedelta
from django.utils import timezone
from PIL import Image
import os
from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage
from .mixins import StaffRequiredMixin, TableListViewMixin, TableDetailViewMixin, UpdateViewMixin, CreateViewMixin
from django.db.models.fields.related import (
    ForeignObjectRel, ManyToOneRel, OneToOneField, add_lazy_relation,
)
from django.forms import models as model_forms

# Create your views here.
from .models import (
    OfficeInspection,     
    DailyInspection, 
    DailyInspectionLog,
    shelf_inspection_record, 
    shelf_inspection, 
    shelf,
    ShelfAnnualInspection,
    Rehearsal,
    PI,
    ShelfAnnualInspectionImage,

    image_upload_to_dailyinspection,
    )
from .forms import (
    OfficeInspectionForm, 
    DailyInspectionForm, 
    InspectionFilterForm, 
    ShelfInspectionRecordForm, 
    ShelfFilterForm, 
    ShelfInspectionForm, 
    ShelfUploadForm,
    PIForm,

    shelf_inspection_record_Formset, 
    shelf_gradient_inspection_Formset,
    )


# Create your views here.


class StorageSecurityView(TemplateView):
    template_name = "storage_security.html"

    def get_context_data(self, *args, **kwargs):
        context = super(StorageSecurityView, self).get_context_data(*args, **kwargs)
        context["year"] = timezone.now().year
        
        return context

class RehearsalListView(TableListViewMixin, ListView): 
    model = Rehearsal
    template_name = "rehersal/rehearsal_list.html"
    from .admin import RehearsalAdmin
    fields = RehearsalAdmin.list_display
    fields_files = ["attachment"]
    fields_images = ["image",]

    def get_context_data(self, *args, **kwargs):
        context = super(RehearsalListView, self).get_context_data(*args, **kwargs)
        
        return context       

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('rehearsal'),request.path_info),
        ])
        return super(RehearsalListView, self).dispatch(request,args,kwargs)   

class RehearsalDetailView(TableDetailViewMixin, DetailView): 
    model = Rehearsal
    template_name = "rehersal/rehearsal_detail.html"
    fieldsets = [("",{"fields":("title","date","attachment","image",)}), ]
    fields_files = ["attachment"]
    fields_images = ["image",]

    def get_context_data(self, *args, **kwargs):
        context = super(RehearsalDetailView, self).get_context_data(*args, **kwargs)
        
        return context       

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('rehearsal'),reverse("rehearsal_list", kwargs={})),            
            (self.get_object(),request.path_info),
        ])
        return super(RehearsalDetailView, self).dispatch(request,args,kwargs)   




def gen_qrcode(link):
    import qrcode
    qr=qrcode.QRCode(
         version = 2,
         error_correction = qrcode.constants.ERROR_CORRECT_L,
         box_size=10,
         border=10,)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image()
    #img.show()

    photopath = os.path.join(settings.MEDIA_ROOT, "inspection")
    if not os.path.exists(photopath):
        os.makedirs(photopath)
    path = os.path.join(photopath, 'create.jpg')
    img.save(path)
    return path

class OfficeInspectionCreateView(CreateView):
    form_class = OfficeInspectionForm
    template_name = "inspection/officeinspection_create.html"

    def form_valid(self, form, *args, **kwargs):
        form = super(OfficeInspectionCreateView, self).form_valid(form, *args, **kwargs)
        return form

    def get_success_url(self, *args, **kwargs):
        return reverse("OfficeInspection_list", kwargs={}) 


class OfficeInspectionDetailView(ModelFormMixin, DetailView):
    
    model = OfficeInspection
    template_name = "inspection/officeinspection_detail.html"
    form_class = OfficeInspectionForm

    def get_context_data(self, *args, **kwargs):
        context = super(OfficeInspectionDetailView, self).get_context_data(*args, **kwargs)
        context["object"] = self.get_object()
        context["form"] = self.form_class(instance = self.get_object()) 
        return context        

    def get_object(self, *args, **kwargs):
        officeinspection_pk = self.kwargs.get("pk")
        officeinspection = None
        if officeinspection_pk:
            print officeinspection_pk
            officeinspection = get_object_or_404(OfficeInspection, pk=officeinspection_pk)
        return officeinspection 

    def get(self, request, *args, **kwargs):
        return super(OfficeInspectionDetailView, self).get(request, *args, **kwargs) 

    def post(self, request, *args, **kwargs):
        form = self.get_form() 
        self.object = self.get_object(*args, **kwargs)

        if form.is_valid():
            return self.form_valid(form)
        else:            
            return self.form_invalid(form)

        return super(OfficeInspectionDetailView, self).post(request, *args, **kwargs) 

    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_("Inspection"),reverse("OfficeInspection_list", kwargs={})),
            (instance,request.path_info),
        ])
        return super(OfficeInspectionDetailView, self).dispatch(request,args,kwargs)   

    def get_success_url(self):
        return reverse("OfficeInspection_list", kwargs={}) 

    def form_valid(self, form, *args, **kwargs):
        #form.instance = self.get_object(*args, **kwargs)  # without this, form will create another new object
        obj = form.save(commit = False)
        instance = self.get_object()
        obj.id = instance.id
        obj.timestamp = instance.timestamp
        obj.image = gen_qrcode(self.request.get_host() + reverse("OfficeInspection_create", kwargs={}))
        obj.save()

        return HttpResponseRedirect(self.get_success_url())

class OfficeInspectionListView(ListView): 
    model = OfficeInspection
    template_name = "dailyinspection/officeinspection_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(OfficeInspectionListView, self).get_context_data(*args, **kwargs)
        context["objects"] = OfficeInspection.objects.all()
        context["objects_sort"] = OfficeInspection.objects.order_by('-updated')
        
        return context       

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('Inspection'),request.path_info),
        ])
        return super(OfficeInspectionListView, self).dispatch(request,args,kwargs)   


THUMBNAIL_WIDTH = 768 # 1024
THUMBNAIL_HEIGHT = 725 # 1000

def get_dailyinspection_path():
    if settings.USE_SAE_BUCKET: #'SERVER_SOFTWARE' in os.environ: 
        return 'dailyinspection'
    else:
        insepection_path = os.path.join(settings.MEDIA_ROOT, 'dailyinspection')
        if not os.path.exists(insepection_path):
            os.makedirs(insepection_path)
        return insepection_path


def save_and_get_image(form, fieldname, instance, obj, required=False):
    in_mem_image_file = form.cleaned_data[fieldname] # new image file
    instance_file = getattr(instance,fieldname, None)  # original file

    if in_mem_image_file:
        # delete original file
        if instance and instance_file and not in_mem_image_file == instance_file:
            instance_file.delete(save=True)       

        if getattr(form, 'clear_' + fieldname, None)():
            # clear original filename
            setattr(obj,fieldname,None)
        else:            
            img = Image.open(in_mem_image_file)
            if img.size[0] > THUMBNAIL_WIDTH or img.size[1] > THUMBNAIL_HEIGHT:
                newWidth = THUMBNAIL_WIDTH
                newHeight = float(THUMBNAIL_WIDTH) / img.size[0] * img.size[1]
                img.thumbnail((newWidth,newHeight),Image.ANTIALIAS)
                filename = image_upload_to_dailyinspection(instance if instance else obj, in_mem_image_file.name)
                filepath = os.path.join(settings.MEDIA_ROOT, filename)
                if not os.path.exists(os.path.dirname(filepath)):
                    os.makedirs(os.path.dirname(filepath))                
                img.save(filepath)
                # set new filename
                setattr(obj,fieldname,filename)
    else:
        if instance: # for update only
            if getattr(form, 'clear_' + fieldname, None)() is None:
                setattr(obj,fieldname,instance_file)  #keep original value
            else:    
                instance_file.delete(save=True) # clear original file

class ThumbnailMixin(object):
    """docstring for ThumbnailMixin"""
    def form_valid(self, form, *args, **kwargs):
        #form.instance = self.get_object(*args, **kwargs)  # without this, form will create another new object
        obj = form.save(commit = False)
        instance = None
        try:
            instance = self.get_object()
        except:
            pass

        if instance: #for update
            obj.id = instance.id
            obj.created = instance.created
            obj.inspector = instance.inspector
            inspection_completed = False
            if obj.image_after and obj.image_after.url:
                inspection_completed = True
                if not instance.image_after or instance.image_after.url is None or not instance.image_after.url == obj.image_after.url:                    
                    log = '{0}-{1} {2}'.format(datetime.datetime.now().strftime('%b-%d-%y %H:%M:%S'),self.request.user,_("uploaded image to complete the inspector").encode("utf-8")) 
                    DailyInspectionLog(dailyinspection=instance,log=log).save()


            if inspection_completed:
                obj.completed_time = timezone.now()
                obj.rectification_status = 'completed'
            else:
                obj.completed_time = instance.completed_time
                obj.rectification_status = instance.rectification_status


        save_and_get_image(form, 'image_before', instance, obj, required=True)

        save_and_get_image(form, 'image_after', instance, obj)

        obj.save()

        return HttpResponseRedirect(self.get_success_url())

class DailyInspectionCreateView(StaffRequiredMixin, ThumbnailMixin, CreateView):
    form_class = DailyInspectionForm
    model = DailyInspection
    template_name = "dailyinspection/dailyinspection_create.html"

    # def form_valid(self, form, *args, **kwargs):
    #     messages.success(self.request, _("daily inspection create successfully"), extra_tags='capfirst')
    #     form = super(DailyInspectionCreateView, self).form_valid(form, *args, **kwargs)
    #     return form

    def form_valid(self, form, *args, **kwargs):
        obj = form.save(commit = False)
        obj.inspector = self.request.user
        obj.save()

        messages.success(self.request, _("daily inspection create successfully"), extra_tags='capfirst')

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self, *args, **kwargs):
        return reverse("dailyinspection_list", kwargs={}) 

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_("Daily Inspection"),reverse("dailyinspection_list", kwargs={})),
            (_('Create'),request.path_info),
        ])
        return super(DailyInspectionCreateView, self).dispatch(request,args,kwargs)   
        

class DailyInspectionDetailView( DetailView):
    model = DailyInspection
    template_name = "dailyinspection/dailyinspection_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DailyInspectionDetailView, self).get_context_data(*args, **kwargs)
        context["fields"] = [field for field in self.model._meta.get_fields() if not field.name in [self.model._meta.pk.attname] and not isinstance(field, ManyToOneRel)]
        context["image_fields"] = ["image_before","image_after"]
        context["display_fields"] = ["category","rectification_status","location"]
        context["fields_exclude"] = []
        context["fields_multichoice"] = ["impact"]
        context["logs"] = DailyInspectionLog.objects.filter(dailyinspection=self.get_object())

        return context

    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()

        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_("Daily Inspection"),reverse("dailyinspection_list", kwargs={})),
            (instance,request.path_info),
        ])
        return super(DailyInspectionDetailView, self).dispatch(request,args,kwargs)   
        
class DailyInspectionUpdateView(StaffRequiredMixin, ThumbnailMixin, UpdateView): #ModelFormMixin
    
    model = DailyInspection
    template_name = "dailyinspection/dailyinspection_update.html"
    form_class = DailyInspectionForm

    def get_context_data(self, *args, **kwargs):
        context = super(DailyInspectionUpdateView, self).get_context_data(*args, **kwargs)
        object = self.get_object()
        context["object"] =object 
        #selected = [item for item in object.impact]
        #initial=selected
        form = kwargs.get('form',None) # called in form_invalid
        if form is None:
            form = self.form_class(self.request.POST or None, self.request.FILES or None, instance = self.get_object())
        context["form"] = form
        #context["media"] = settings.MEDIA_URL
        return context        

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        # self.object = self.get_object(*args, **kwargs)

        if form.is_valid():
            messages.success(request, _("daily inspection updated successfully"), extra_tags='capfirst')
            messages.info(request, _("check content please"))

            return self.form_valid(form)
        else:
            messages.error(request, _("daily inspection updated fail"), extra_tags='alert-error')
            return self.form_invalid(form)

        return super(DailyInspectionUpdateView, self).post(request, *args, **kwargs) 

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_("Daily Inspection"),reverse("dailyinspection_list", kwargs={})),
            (self.object,request.path_info),
        ])
        return super(DailyInspectionUpdateView, self).dispatch(request,args,kwargs)   

    def get_success_url(self):
        return reverse("dailyinspection_detail", kwargs={'pk':self.kwargs.get("pk")})

class DailyInspectionDeleteView( StaffRequiredMixin, DeleteView):
    model = DailyInspection
    template_name = "dailyinspection/dailyinspection_delete.html"

    def get_success_url(self):
        return reverse("dailyinspection_list", kwargs={})

'''
operators = {
        'exact': '= %s',
        'iexact': 'LIKE %s',
        'contains': 'LIKE BINARY %s',
        'icontains': 'LIKE %s',
        'regex': 'REGEXP BINARY %s',
        'iregex': 'REGEXP %s',
        'gt': '> %s',
        'gte': '>= %s',
        'lt': '< %s',
        'lte': '<= %s',
        'startswith': 'LIKE BINARY %s',
        'endswith': 'LIKE BINARY %s',
        'istartswith': 'LIKE %s',
        'iendswith': 'LIKE %s',
    }
'''



class InsepctionFilter(FilterSet):
    #cateory = CharFilter(name='category', lookup_type='icontains', distinct=True)
    category = MultipleChoiceFilter(name='category', choices=DailyInspection.daily_insepction_category, distinct=True)
    #category = MethodFilter(name='category', action='category_filter', distinct=True)
    #category_id = CharFilter(name='categories__id', lookup_type='icontains', distinct=True)
    rectification_status = CharFilter(name='rectification_status', lookup_type='exact', distinct=True)
    # due_date = MethodFilter(name='due_date', action='overdue_filter', distinct=True)
    owner = CharFilter(name='owner', lookup_type='icontains', distinct=True)

    start = CharFilter(name='created', lookup_type='gte', distinct=True)
    end = CharFilter(name='created', lookup_type='lte', distinct=True)

    class Meta:
        model = DailyInspection
        fields = [
            'category',
            'owner',
            'rectification_status',
            'created'
            
        ]

    def category_filter(self, queryset, value):

        qs = queryset
        for category in value:
            print category
            qs = qs.filter(category=category)

        return qs.distinct()

    # def overdue_filter(self, queryset, value):

    #     qs = queryset
    #     for due_date in value:
    #         qs = qs.filter(due_date__lt=due_date)

    #     return qs.distinct()

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
        ordering = self.request.GET.get(self.search_ordering_param, '-created')
        if qs and ordering:
            qs = qs.order_by(ordering)
        filter_class = self.filter_class
        if qs and filter_class:
            f = filter_class(self.request.GET, queryset=qs)
            context["object_list"] = f.qs # f also works
            context["object_list_count"] = f.qs.count()
        return context

class ChartMixin(object):

    def get_context_data(self, *args, **kwargs):
        context = super(ChartMixin, self).get_context_data(*args, **kwargs)
        object_list = context["object_list"]
        data = { 
            'datasets': [{
                # 'label': '# of Votes',
                'data': [object_list.filter(category=category[0]).count() if not object_list is None else 0 for category in DailyInspection.daily_insepction_category],
                'backgroundColor': [
                    'rgba(255, 0, 0, 0.2)',
                    'rgba(0, 255, 0, 0.2)',
                    'rgba(0, 0, 255, 0.2)',
                    'rgba(220, 0, 255, 0.2)',
                    'rgba(0, 220, 255, 0.2)',
                ]            
            }],

            # These labels appear in the legend and in the tooltips when hovering different arcs
            'labels': [_(category[1]) for category in DailyInspection.daily_insepction_category_view], # why ugettext in models.py didn't work?
        };
        context["data"] = json.dumps(data)
        
        return context

class DailyInspectionListView(ChartMixin, FilterMixin, ListView): 
    model = DailyInspection
    template_name = "dailyinspection/dailyinspection_list.html"
    filter_class = InsepctionFilter

    def get_context_data(self, *args, **kwargs):
        context = super(DailyInspectionListView, self).get_context_data(*args, **kwargs)
        # context["objects_list"] = DailyInspection.objects.order_by('-updated')
        context["objects_sort"] = DailyInspection.objects.order_by('-updated')[:10]
        context["query"] = self.request.GET.get("q")
        context["InspectionFilterForm"] = InspectionFilterForm(data=self.request.GET or None)        
        context["categories"] = DailyInspection.daily_insepction_category

        print context['data']
        return context       

    def get_queryset(self, *args, **kwargs):
        qs = super(DailyInspectionListView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")
        overdue = self.request.GET.get("overdue")

        qs  = None
        if not self.request.user.is_staff and not self.request.user.is_superuser:
            qs =  self.model.objects.external()
        else:
            qs =  self.model.objects.all()

        # for over due only
        if overdue:
            qs = qs.filter(due_date__lt=timezone.now()).filter(rectification_status="uncompleted")
            return qs
        
        if query:
            qs = qs.filter(
                Q(impact__icontains=query) |
                Q(rectification_measures__icontains=query) |
                Q(owner__icontains=query) |
                Q(category__icontains=query) |
                Q(inspection_content__icontains=query)
                )
            try:
                qs2 = qs.filter(
                    Q(rectification_status=query)
                )
                qs = (qs | qs2).distinct()
            except:
                pass
        return qs

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('Daily Inspection'),request.path_info),
        ])
        return super(DailyInspectionListView, self).dispatch(request,args,kwargs)   

# https://github.com/novafloss/django-chartjs
class LineChartColorMixin(object):
    def get_context_data(self):
        data = super(LineChartColorMixin, self).get_context_data()
        backgroundColors =[
                    'rgba(255, 0, 0, 0.2)',
                    'rgba(0, 255, 0, 0.2)',
                    'rgba(0, 0, 255, 0.2)',
                    'rgba(220, 0, 255, 0.2)',
                    'rgba(0, 220, 255, 0.2)',                    
                ]

        borderColors =[
                    'rgba(255, 0, 0, 0.1)',
                    'rgba(0, 255, 0, 0.1)',
                    'rgba(0, 0, 255, 0.1)',
                    'rgba(220, 0, 255, 0.1)',
                    'rgba(0, 220, 255, 0.1)',                    
                ]                

        for i in range(0,len(self.get_providers())):
        #for i, color in enumerate(backgroundColors)
            data['datasets'][i]['backgroundColor'] = backgroundColors[i]
            data['datasets'][i]['borderColor'] = borderColors[i]

        # print data
        return data 

class StatMixin(object):

    # ['category']['date']['count']
    # {'people',{'2017-08-01':'0','2017-08-02':'1'}}

    def get_dates(self):
        #dates = list([ ins.created.strftime("%Y-%m-%d") for ins in DailyInspection.objects.order_by('-updated')])        
        dates = list([ ins.get_created_date() for ins in DailyInspection.objects.order_by('-updated')[:30]])
        dates = list(set(dates))
        dates.sort()
        return dates

    def get_dates_value(self):
        dates = list([ ins.created for ins in DailyInspection.objects.order_by('-updated')[:30]])
        dates = list(set(dates))
        dates.sort()
        return dates

    def get_catetory(self):
        categories = list([ ins[1] for ins in DailyInspection.daily_insepction_category])
        return categories

    def get_catetory_value(self):
        categories = list([ ins[0] for ins in DailyInspection.daily_insepction_category])
        return categories

    def get_chart_counts(self):
        counts = []
        dates = self.get_dates()
        categories = self.get_catetory_value()
        for category in categories:
            count  = [DailyInspection.objects.filter(created__range=(\
                            datetime.datetime( datetime.datetime.strptime(date,'%Y-%m-%d').year, datetime.datetime.strptime(date,'%Y-%m-%d').month,datetime.datetime.strptime(date,'%Y-%m-%d').day,0,0,0),\
                            datetime.datetime(datetime.datetime.strptime(date,'%Y-%m-%d').year, datetime.datetime.strptime(date,'%Y-%m-%d').month,datetime.datetime.strptime(date,'%Y-%m-%d').day,23,59,59)))\
                                             .filter(category=category).count() for date in dates ]
            if counts == None:
                counts = [count]
            else:
                counts.append(count)
        return counts


    def get_counters_sorted(self):
        llcounterperdaypercategory = {}
        for category in self.get_catetory():
            #llcounterperdaypercategory.update({category:{}})
            llcounterperdaypercategory[category] = {}
            for date in self.get_dates():
                llcounterperdaypercategory[category].update({date:0})

        return self.get_counters(llcounterperdaypercategory)

    def get_counters(self, llcounterperdaypercategory):
        #llcounterperdaypercategory = {}
        for inspect in DailyInspection.objects.all():
            created = inspect.get_created_date()
            category = inspect.my_get_field_display('category')
            if llcounterperdaypercategory.get(category, None) is None:
                llcounterperdaypercategory.update({category: {created : 1}})
            else:                
                if llcounterperdaypercategory[category].get(created, None):
                    llcounterperdaypercategory[category][created] = llcounterperdaypercategory[category].get(created, None) + 1
                else:
                    llcounterperdaypercategory[category].update({created:1})

        return llcounterperdaypercategory


#class ShelfInspectionStatView(TemplateView):
class DailyInspectionStatView(StatMixin, TemplateResponseMixin, ContextMixin, View):
    template_name = "dailyinspection/dailyinspection_stat.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DailyInspectionStatView, self).get_context_data(*args, **kwargs)
        context["objects_list"] = DailyInspection.objects.order_by('-updated')
        context["dates"] = self.get_dates()
        context["categories"] = self.get_catetory()
        context["counters"] = self.get_counters_sorted()
        return context   

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('Inspection List'),reverse("dailyinspection_list", kwargs={})),
            (_('Inspection Statistic'),request.path_info),
        ])
        return super(DailyInspectionStatView, self).dispatch(request,args,kwargs)  

class LineChartJSONView(StatMixin, LineChartColorMixin, BaseLineChartView):
    def get_labels(self):
        """Return labels for the x-axis."""
        return self.get_dates()

    def get_providers(self):
        """Return names of datasets."""
        return self.get_catetory()

    def get_data(self):
        """Return 3 datasets to plot."""
        return self.get_chart_counts()


# var data = {
#     labels : ["January","February","March","April","May","June","July"],
#     datasets : [
#         {
#             fillColor : "rgba(220,220,220,0.5)",
#             strokeColor : "rgba(220,220,220,1)",
#             data : [65,59,90,81,56,55,40]
#         },
#         {
#             fillColor : "rgba(151,187,205,0.5)",
#             strokeColor : "rgba(151,187,205,1)",
#             data : [28,48,40,19,96,27,100]
#         }
#     ]
# }

class OverdueChartJSONView(JSONView):

    def get_context_data(self):
        data = { 
            'datasets': [{
                # 'label': '# of Votes',
                'data': [DailyInspection.objects.filter(rectification_status="uncompleted", due_date__lt=timezone.now(), category=category[0]).count() for category in DailyInspection.daily_insepction_category],
                'backgroundColor': [
                    'rgba(255, 0, 0, 0.2)',
                    'rgba(0, 255, 0, 0.2)',
                    'rgba(0, 0, 255, 0.2)',
                    'rgba(220, 0, 255, 0.2)',
                    'rgba(0, 220, 255, 0.2)',
                ]            
            }],

            # These labels appear in the legend and in the tooltips when hovering different arcs
            'labels': [category[1] for category in DailyInspection.daily_insepction_category],
        };

        return data

class LastsChartJSONView(LineChartColorMixin, BaseLineChartView):
    def get_time_range(self):
        times =  [timezone.now(), timezone.now() - timedelta(weeks=1)]
        return times
               
    def get_labels(self):
        """Return labels for the x-axis."""
        return [category[1] for category in DailyInspection.daily_insepction_category]

    def get_providers(self):
        """Return names of datasets."""
        providers =  [ "{0}  ~  {1}".format(self.get_time_range()[1].date(), self.get_time_range()[0].date()), ]
        return providers

    def get_data(self):
        data =  [[DailyInspection.objects.filter(category=category[0], created__gte=self.get_time_range()[1]).count()\
                     for category in DailyInspection.daily_insepction_category],]
        return data

class CompareChartJSONView(LineChartColorMixin, BaseLineChartView):
    def get_last_times(self):
        #  RuntimeWarning: DateTimeField DailyInspection.created received a naive datetime (2017-12-02 23:59:59) while time zone support is active.
        year = timezone.now().year #time.localtime()[0]
        month = timezone.now().month #time.localtime()[1]        
        return [[month-i or 12, year if month > i else year-1] for i in reversed(range(0,3))]
               
    def get_labels(self):
        """Return labels for the x-axis."""
        return [category[1] for category in DailyInspection.daily_insepction_category]

    def get_providers(self):
        """Return names of datasets."""
        return [            
            "{0}-{1}".format(year,month) for month,year in self.get_last_times()
        ]

    def get_data(self):
        data =  [[DailyInspection.objects.filter(category=category[0], created__month=month, created__year=year).count() for category in DailyInspection.daily_insepction_category] \
                    for month, year in self.get_last_times()]
        return data


    # def get_context_data(self):
    #     data = super(CompareChartJSONView, self).get_context_data()
    #     backgroundColors =[
    #                 'rgba(255, 0, 0, 0.2)',
    #                 'rgba(0, 255, 0, 0.2)',
    #                 'rgba(0, 0, 255, 0.2)',
    #             ]

    #     borderColors =[
    #                 'rgba(255, 0, 0, 0.1)',
    #                 'rgba(0, 255, 0, 0.1)',
    #                 'rgba(0, 0, 255, 0.1)',
    #             ]                

    #     for i, color in enumerate(backgroundColors):
    #         data['datasets'][i]['backgroundColor'] = backgroundColors[i]
    #         data['datasets'][i]['borderColor'] = borderColors[i]

    #     return data

class ShelfInspectionListView(ListView): 
    model = shelf_inspection
    template_name = "shelf/shelf_inspection_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ShelfInspectionListView, self).get_context_data(*args, **kwargs)

        #queryset = shelf_inspection.objects.all()

        records_list = [(object, \
            object.shelf_inspection_record_set.filter(use_condition=2).count(), \
            object.shelf_inspection_record_set.filter(is_locked=True).count(), \
            object.shelf_inspection_record_set.filter(gradient__gt=1.4).count()) for object in shelf_inspection.objects.all()]

        paginator = Paginator(records_list, 20)

        records = None

        page = self.request.GET.get('page')
        try:
            records = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            records = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            records = paginator.page(paginator.num_pages)

        #context["object_list"] = queryset
        context["records"] = records

        # context["uncompleted_shelf_inspection_record"] = shelf_inspection_record.objects.filter(
        #         Q(use_condition=2) |
        #         Q(is_locked = True) |
        #         Q(gradient__gt = 1.4)
        #     ).distinct().order_by("shelf_inspection")

        # from .admin import ShelfInspectionRecordAdmin
        # context["fields_shelf_inspection_record"] = [field.name for field in shelf_inspection_record._meta.get_fields() if field.name in ShelfInspectionRecordAdmin.list_display]

        # context["fields_shelf_inspection_record_display"] = [
        #     "use_condition",
        #     "is_locked",
        # ]
        # context["field_display_links"] = ["shelf",]
        # context["title"] = _("abnormal") + _("shelf inspection record")

        # if self.request.session.get("shelf_inspection_pk"):
        #     del self.request.session["shelf_inspection_pk"]

        return context       


    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('Shelf Inspection List'),request.path_info),
        ])
        return super(ShelfInspectionListView, self).dispatch(request,args,kwargs)       

class ShelfInspectionRecordFilter(FilterSet):
    #is_gradient_measurement_mandatory = BooleanFilter(name='shelf__is_gradient_measurement_mandatory', method='gradient_custom_filter', distinct=True) # this is for latest version
    is_gradient_measurement_mandatory = MethodFilter(name='shelf__is_gradient_measurement_mandatory', action='gradient_custom_filter', distinct=True)
    type = CharFilter(name='shelf__type', lookup_expr='iexact', distinct=True)  #shelf is elem name of shelf_inspection_record
    warehouse = CharFilter(name='shelf__warehouse', lookup_type='exact', distinct=True)
    compartment = CharFilter(name='shelf__compartment', lookup_type='exact', distinct=True)
    warehouse_channel = CharFilter(name='shelf__warehouse_channel', lookup_type='exact', distinct=True)
    use_condition = CharFilter(name='use_condition', lookup_type='exact', distinct=True)
    is_locked = CharFilter(name='is_locked', lookup_type='exact', distinct=True)
    is_overdue = MethodFilter(name='forecast_complete_time', action='overdue_filter', distinct=True)

    class Meta:
        model = shelf_inspection_record
        fields = [
            'is_gradient_measurement_mandatory',
            'type',
            'warehouse',
            'compartment',
            'warehouse_channel',
            'use_condition',
            'is_locked',
            'forecast_complete_time'
        ]

    #def gradient_custom_filter(self, queryset, name, value): # this is for latest version
    def gradient_custom_filter(self, queryset, value):
        if 'on' == value:
            qs1 = queryset.filter(**{
                'shelf__is_gradient_measurement_mandatory': True,
            })
            qs = qs1

            # for ins in qs1:
            #     qs2 = queryset.filter(**{
            #     'shelf__warehouse_channel': ins.shelf.warehouse_channel,})
            #     qs = (qs | qs2)
            return qs.distinct()
        
        return queryset

    def overdue_filter(self, queryset, value):
        if 'on' == value:
            qs = queryset.filter(**{
                'forecast_complete_time__lte': timezone.now(),
            })
            return qs.distinct()
        
        return queryset

class ShelfInspectionDetailAndRecordListDisplayView(DetailView):  # Per Inspection
    model = shelf_inspection
    template_name = "shelf/shelf_inspection_detail_and_record_list_display.html"
    filter_class = ShelfInspectionRecordFilter

    def get_record_queryset(self, *args, **kwargs):
        pk = self.kwargs.get('pk', None)
        if pk:
            shelf_inspection_instance = get_object_or_404(shelf_inspection, pk=pk)
            queryset =  shelf_inspection_record.objects.filter(shelf_inspection__id = pk).order_by('shelf__id')
            filter_class = self.filter_class
            if filter_class and kwargs.get('filter'):
                queryset = filter_class(self.request.GET, queryset=queryset).qs
            return queryset
        return None

    def get_context_data(self, *args, **kwargs):
        context = super(ShelfInspectionDetailAndRecordListDisplayView, self).get_context_data(*args, **kwargs)
        context["shelf_inspection_record_set"] = self.get_record_queryset(filter=True)
        from inspection.admin import ShelfInspectionRecordAdmin
        #context["fields_shelf_inspection_record"] = [field for field in shelf_inspection_record._meta.get_fields() if field.name in ShelfInspectionRecordAdmin.list_display]
        context["fields_shelf_inspection_record"] = ShelfInspectionRecordAdmin.list_display

        context["fields_shelf_inspection_record_display"] = [
            "use_condition",
            "is_locked",
        ]
        context["field_display_links"] = []
        context["title"] = _("shelf inspection record")
        context["shelfFilterForm"] = ShelfFilterForm(data=self.request.GET or None) 

        self.request.session["shelf_inspection_pk"] = self.get_object().pk

        return context       


    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('Shelf Inspection List'),reverse("shelf_inspection_list", kwargs={})),
            (_('Shelf Inspection Detail'),request.path_info),
        ])

        return super(ShelfInspectionDetailAndRecordListDisplayView, self).dispatch(request,args,kwargs)


class ShelfInspectionDetailAndRecordListEditView(DetailView): 
    model = shelf_inspection
    template_name = "shelf/shelf_inspection_detail_and_record_list_edit.html"
    filter_class = ShelfInspectionRecordFilter

    def get_record_queryset(self, *args, **kwargs):
        pk = self.kwargs.get('pk', None)
        if pk:
            shelf_inspection_instance = get_object_or_404(shelf_inspection, pk=pk)
            queryset =  shelf_inspection_record.objects.filter(shelf_inspection__id = pk).order_by('shelf__id')
            filter_class = self.filter_class
            if filter_class and kwargs.get('filter'):
                queryset = filter_class(self.request.GET, queryset=queryset).qs
            return queryset
        return None

    def get_context_data(self, *args, **kwargs):
        context = super(ShelfInspectionDetailAndRecordListEditView, self).get_context_data(*args, **kwargs)
        context["object_list"] = self.get_record_queryset(filter=True)
        context["shelfFilterForm"] = ShelfFilterForm(data=self.request.GET or None) 
        formset = shelf_inspection_record_Formset(queryset=self.get_record_queryset(filter=True),
            initial=[{'use_condition': _('Normal'),}])    
        context["formset"] = formset

        self.request.session["shelf_inspection_pk"] = self.request.GET.get(self.get_object().pk)  

        return context       


    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('Shelf Inspection List'),reverse("shelf_inspection_list", kwargs={})),
            (_('Shelf Inspection Detail'),request.path_info),
        ])

        return super(ShelfInspectionDetailAndRecordListEditView, self).dispatch(request,args,kwargs)


    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form_id = request.POST.get('form_id')
            prefix = form_id.replace('id_', '')
            form = ShelfInspectionRecordForm(request.POST, prefix=prefix)
            
            if form.is_valid():
                instance_id = form.clean_id()                
                try:
                    instance = shelf_inspection_record.objects.get(pk=instance_id)
                    obj = form.save(commit=False)
                    if obj.turn_normal(instance):
                        instance.completed_time = timezone.now()       
                    elif obj.turn_abnormal(instance):
                        instance.completed_time = None                                  
                    #form.save()
                    json_data = {
                        'message': 'valid form!',
                        'valid':True,
                        'form_id': form_id,
                    }                    
                    for fieldname in shelf_inspection_record._meta.get_all_field_names():
                        if not ( fieldname in ShelfInspectionRecordForm.Meta.exclude or fieldname in ShelfInspectionRecordForm.Meta.display_with_field_hiden):
                            if form.cleaned_data.get(fieldname, None) is not None: # be careful for False
                                setattr(instance, fieldname, form.cleaned_data.get(fieldname))
                                json_data.update({fieldname: instance.my_get_field_display(fieldname)})

                    instance.save()
                    return HttpResponse(json.dumps(json_data))
                    '''
                    return render(request,"shelf/shelf_inspection_detail_and_record_list_edit.html",self.get_context_data(*args, **kwargs))
                    return render(request,"shelf/response_form.html",context)                
                    form.instance = instance
                    context = {
                        'form' : form,
                        'form_id' : form_id
                    }  
                    '''              
                except:
                    raise Http404
            
            return HttpResponse(json.dumps({'message': form.errors,'valid':False,'form_id': form_id}))
        else:
            raise Http404

class ShelfInspectionCreateView(CreateView):
    #model = shelf
    template_name = "shelf/shelf_inspection_create.html"
    form_class = ShelfInspectionForm
    success_url = "inspection/shelfinspectionlist" #reverse("shelf_inspection_list")

    def get_context_data(self, *args, **kwargs):
        context = super(ShelfInspectionCreateView, self).get_context_data(*args, **kwargs)
        context["form"] = ShelfInspectionForm(self.request.POST or None, self.request.GET or None)  # without paramter, error will not be displayed
        return context

    def get_form(self, *args, **kwargs):
        form = super(ShelfInspectionCreateView, self).get_form(*args, **kwargs)

        #form.fields['categories'].queryset  = Category.objects.all()
        #form.fields['default'].queryset  = Category.objects.all()

        return form

    def post(self, request, *args, **kwargs):

        form = ShelfInspectionForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            for shelf_instance in shelf.objects.all():
                shelf_inspection_record_instance = shelf_inspection_record()
                shelf_inspection_record_instance.shelf = shelf_instance
                shelf_inspection_record_instance.shelf_inspection = obj
                shelf_inspection_record_instance.use_condition = 1                
                shelf_inspection_record_instance.is_locked = False
                shelf_inspection_record_instance.gradient = 0
                shelf_inspection_record_instance.create_date = timezone.now()
                # shelf_inspection_record_instance.forecast_complete_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
                shelf_inspection_record_instance.save()            

            return redirect(reverse("shelf_inspection_detail_and_record_list_edit", kwargs={'pk': obj.id}))

        return super(ShelfInspectionCreateView, self).post(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('Shelf Inspection List'),reverse("shelf_inspection_list", kwargs={})),
            (_('Create'),request.path_info),
        ])
        return super(ShelfInspectionCreateView, self).dispatch(request,args,kwargs)    

class ShelfDetailView(DetailView):
    model = shelf
    template_name = "shelf/shelf_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ShelfDetailView, self).get_context_data(*args, **kwargs)
        print self.model._meta.get_fields()
        context["fields"] = [field for field in self.model._meta.get_fields() if not field.name in [self.model._meta.pk.attname] and not isinstance(field, ManyToOneRel)]
        context["fields_display"] = ["is_gradient_measurement_mandatory", ]
        # ManyToOneRel are in field.rel or field.remote_field, can be investigated later
        context["detail_view_title"] = _("Shelf")
        context["related_inspection"] = shelf_inspection_record.objects.filter(shelf=self.get_object())

        return context    

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('Shelf List'),reverse("shelf_list", kwargs={})),
            (self.get_object(),request.path_info),
        ])
        return super(ShelfDetailView, self).dispatch(request,args,kwargs)    

class ShelfListView(ListView):
    model = shelf
    template_name = "shelf/shelf_list.html"

    def get_queryset(self,*args,**kwargs):
        query = self.request.GET.get('q')
        qs = self.model.objects.all()

        if query:
            qs = qs.filter(
                Q(type__icontains=query) |
                Q(warehouse__icontains = query) |
                Q(compartment__icontains = query) |
                Q(warehouse_channel__icontains = query) |
                Q(number__icontains = query)
            ).distinct()
        return qs


    def get_context_data(self, *args, **kwargs):
        context = super(ShelfListView, self).get_context_data(*args, **kwargs)
        context["ShelfUploadForm"] = ShelfUploadForm          
        context["field_exclude"] = ["shelf_inspection_record","shelfannualinspection",]  

        return context    

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('Shelf List'),request.path_info),
        ])
        return super(ShelfListView, self).dispatch(request,args,kwargs)     

class ShelfInspectionRecordDetailView(DetailView):
    model = shelf_inspection_record
    template_name = "shelf/shelf_inspection_record_detail.html"    

    def get_context_data(self, *args, **kwargs):
        context = super(ShelfInspectionRecordDetailView, self).get_context_data(*args, **kwargs)
        context["fields_display"] = ["use_condition","is_locked",]
        context["detail_view_title"] = _("shelf inspection record")
        context["fields"] = [field for field in self.model._meta.get_fields() if not field.name in [self.model._meta.pk.attname, ]]   

        shelf_inspection_pk = self.request.session.get("shelf_inspection_pk")        
        shelf_inspection_instance = shelf_inspection.objects.get(pk=shelf_inspection_pk) if shelf_inspection_pk else None
        if shelf_inspection_instance:
            context["shelf_inspection_instance"] = shelf_inspection_instance

        return context    


    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('Shelf Inspection List'),reverse("shelf_inspection_list", kwargs={})),
            (self.get_object(),request.path_info),
        ])
        return super(ShelfInspectionRecordDetailView, self).dispatch(request,args,kwargs)     

class ShelfInspectionRecordUpdateView(StaffRequiredMixin, UpdateView):
    model = shelf_inspection_record
    form_class = ShelfInspectionRecordForm
    template_name = "shelf/shelf_inspection_record_update.html"   

    def form_valid(self, form, *args, **kwargs):
        obj = form.save(commit = False)
        if not obj.check_person:
            obj.check_person = self.request.user.get_full_name()
        instance = self.model.objects.get(pk=obj.pk)
        if obj.turn_normal(instance):
            obj.completed_time = timezone.now()  
        if obj.turn_abnormal(instance):
            obj.completed_time = None     
        obj.save()

        return HttpResponseRedirect(self.get_success_url())    

    def get_success_url(self):
        return self.get_object().get_absolute_url()

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('Shelf Inspection List'), reverse("shelf_inspection_list", kwargs={})),             
            (self.get_object(), request.path_info),
        ])
        return super(ShelfInspectionRecordUpdateView, self).dispatch(request,args,kwargs)  


class ShelfInspectionRecordListView(ListView):
    model = shelf_inspection_record
    template_name = "shelf/shelf_inspection_record_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ShelfInspectionRecordListView, self).get_context_data(*args, **kwargs)    
        context["uncompleted_shelf_inspection_record"] = shelf_inspection_record.objects.filter(
                Q(use_condition=2) |
                Q(is_locked = True) |
                Q(gradient__gt = 1.4)
            ).distinct().order_by("shelf_inspection")

        from .admin import ShelfInspectionRecordAdmin
        context["fields_shelf_inspection_record"] = [field.name for field in shelf_inspection_record._meta.get_fields() if field.name in ShelfInspectionRecordAdmin.list_display]

        context["fields_shelf_inspection_record_display"] = [
            "use_condition",
            "is_locked",
        ]
        context["field_display_links"] = ["shelf",]
        context["title"] = _("abnormal") + _("shelf inspection record")

        if self.request.session.get("shelf_inspection_pk"):
            del self.request.session["shelf_inspection_pk"]

        return context

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('Shelf Inspection List'),reverse("shelf_inspection_list", kwargs={})),
            (_('Shelf Inspection Record List'), request.path_info),
        ])
        return super(ShelfInspectionRecordListView, self).dispatch(request,args,kwargs)       


from itertools import chain

class ShelfGradientInspectionView(DetailView): 
    model = shelf_inspection
    template_name = "shelf/shelf_gradient_inspection.html"
    #filter_class = ShelfInspectionRecordFilter

    def get_groups(self, *args, **kwargs):
        qs = shelf_inspection_record.objects.filter(shelf_inspection=self.get_object())
        groups = []
        for object in qs:
            group_id = object.shelf.get_group_id()
            if groups == None or len(groups)==0:
                groups = [group_id]
            else:
                if not group_id in groups:
                    groups.append(group_id)

        return groups



    def get_context_data(self, *args, **kwargs):
        context = super(ShelfGradientInspectionView, self).get_context_data(*args, **kwargs)

        qs = shelf_inspection_record.objects.filter(shelf_inspection=self.get_object())
        qs_upright = qs.filter(shelf__is_gradient_measurement_mandatory=True)
        qs_not_upright = qs.filter(shelf__is_gradient_measurement_mandatory=False)

        queryset = None

        for group in self.get_groups():
            queryset0 = qs_upright.relevant(group_id=group)
            queryset1 = qs_not_upright.relevant(group_id=group)

            formsets = [shelf_gradient_inspection_Formset(prefix="".join(list(queryset0[0].shelf.get_group_id()))+"upright", queryset=shelf_inspection_record.objects.filter(pk__in=[x.pk for x in queryset0])),
                        shelf_gradient_inspection_Formset(prefix="".join(list(queryset0[0].shelf.get_group_id()))+"noupright",queryset=shelf_inspection_record.objects.filter(pk__in=[x.pk for x in queryset1])),]

            if queryset is None:
                queryset = [formsets]
            else:
                queryset.append(formsets)

        context["formset_queryset"] = queryset

        return context       

    def post(self, request, *args, **kwargs):
        qs = shelf_inspection_record.objects.filter(shelf_inspection=self.get_object())
        qs_upright = qs.filter(shelf__is_gradient_measurement_mandatory=True)
        qs_not_upright = qs.filter(shelf__is_gradient_measurement_mandatory=False)

        queryset = None

        for group in self.get_groups():
            queryset0 = qs_upright.relevant(group_id=group)
            queryset1 = qs_not_upright.relevant(group_id=group)

            formsets = [shelf_gradient_inspection_Formset(self.request.POST or None, self.request.FILES or None, prefix="".join(list(queryset0[0].shelf.get_group_id()))+"upright"),]

            if not queryset1 is None:
                formsets.append(shelf_gradient_inspection_Formset(self.request.POST or None, self.request.FILES or None, prefix="".join(list(queryset0[0].shelf.get_group_id()))+"noupright"))
            
            if queryset is None:
                queryset = [formsets]
            else:
                queryset.append(formsets)

        is_valid = True
        for formsets in queryset:
            for formset in formsets:
                if formset.is_valid() == False:
                    is_valid = False
                    break
            if False == is_valid:
                break

        if True == is_valid:
            for formsets in queryset:
                for formset in formsets:            
                    instances = formset.save(commit=False)
                    for instance in instances:
                        instance.save()
            messages.success(request, _("Your list has been updated."))
            return redirect(reverse("shelf_gradient_inspection",  kwargs={"pk":self.get_object().id}))

        #self.object_list = self.get_queryset() # copy from BaseListView::get
        context = self.get_context_data()
        context['formset_queryset'] = queryset
        return self.render_to_response(context)

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('Shelf Inspection List'),reverse("shelf_inspection_list", kwargs={})),
            (_('Shelf Inspection Detail'),reverse("shelf_inspection_detail_and_record_list_edit", kwargs={"pk":self.get_object().id})),
            (_('shelf gradient inspection'),request.path_info),
        ])

        return super(ShelfGradientInspectionView, self).dispatch(request,args,kwargs)

class PIListView(TableListViewMixin, ListView): 
    model = PI
    template_name = "pi/pi_list.html"
    from .admin import PIAdmin
    fields = PIAdmin.list_display
    fields_display = [
        "company_of_reporter",
        "department_of_reporter",
        "area",
        "category",
        "direct_reason",
        "root_cause",
        "rectification_status",
        ]
    fields_files = [""]
    fields_images = ["image_before","image_after",]

    def get_context_data(self, *args, **kwargs):
        context = super(PIListView, self).get_context_data(*args, **kwargs)
        object_list = context["object_list"]

        if self.request.GET.get('uncompleted') and self.request.GET.get('overdue'):
            object_list = self.model.objects.filter(rectification_status="uncompleted", planned_complete_date__lte=timezone.now())
        elif self.request.GET.get('uncompleted'):
            object_list = self.model.objects.filter(rectification_status="uncompleted")
        context["object_list"] = object_list                   

        return context 

class PIDetailView(TableDetailViewMixin, DetailView): 
    model = PI
    template_name = "pi/pi_detail.html"
    fields_images = ["image_before","image_after",]
    fields_display = [
        "company_of_reporter",
        "department_of_reporter",
        "area",
        "category",
        "direct_reason",
        "root_cause",
        "rectification_status",
        ]

class PICreateView(CreateViewMixin, CreateView): 
    model = PI
    form_class = PIForm
    template_name = "pi/pi_create.html"

class PIUpdateView(UpdateViewMixin, UpdateView): 
    model = PI
    form_class = PIForm 
    template_name = "pi/pi_update.html"

    def form_valid(self, form, *args, **kwargs):
        obj = form.save(commit = False)
        instance = self.model.objects.filter(pk=form.instance.pk).first()
        if obj.is_rectification_completed() and not instance.is_rectification_completed():
            obj.completed_time = timezone.now()
            obj.close_person = self.request.user.get_full_name()
            obj.rectification_status = "completed"
            obj.save()
        elif not obj.is_rectification_completed() and instance.is_rectification_completed():
            obj.completed_time = None
            obj.close_person = None
            obj.rectification_status = "uncompleted"
            obj.save()

        return super(PIUpdateView, self).form_valid(form, *args, **kwargs)
        return HttpResponseRedirect(self.get_success_url())    

class ShelfAnnualInspectionListView(TableListViewMixin, ListView): 
    model = ShelfAnnualInspection
    template_name = "shelf/shelf_annual_inspection_list.html"
    from .admin import ShelfAnnualInspectionAdmin
    fields = ShelfAnnualInspectionAdmin.list_display

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ShelfAnnualInspectionListView, self).get_context_data(*args, **kwargs)

    #     object_list = context["object_list"]
    #     if self.request.GET.get('uncompleted') and self.request.GET.get('overdue'):
    #         object_list = self.model.objects.filter(rectification_status="uncompleted", planned_complete_date__lte=timezone.now())
    #     elif self.request.GET.get('uncompleted'):
    #         object_list = self.model.objects.filter(rectification_status="uncompleted")
    #     context["object_list"] = object_list                   

    #     return context 

class ShelfAnnualInspectionDetailView(TableDetailViewMixin, DetailView): 
    model = ShelfAnnualInspection
    template_name = "shelf/shelf_annual_inspection_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ShelfAnnualInspectionDetailView, self).get_context_data(*args, **kwargs) 
        context["fields_foreign_shelfannualinspection"] = ["image",]
        context["fields_foreign_shelfannualinspection_image"] = ["image",]
        return context

class ShelfAnnualInspectionCreateView(CreateViewMixin, CreateView): 
    model = ShelfAnnualInspection
    # form_class = ShelfAnnualInspectionForm
    template_name = "shelf/shelf_annual_inspection_create.html"
    from .admin import ShelfAnnualInspectionAdmin
    fields = ShelfAnnualInspectionAdmin.list_display

from django.forms.models import modelformset_factory, inlineformset_factory, BaseModelFormSet, BaseInlineFormSet
from .forms import ShelfAnnualInspectionImageForm, ImageFileInput
class ShelfAnnualInspectionUpdateView(UpdateViewMixin, UpdateView): 
    model = ShelfAnnualInspection
    template_name = "shelf/shelf_annual_inspection_update.html"

    def get_foreign_form_class(self):
        # method #1
        return model_forms.modelform_factory(ShelfAnnualInspectionImage, fields=["image",], widgets={"image":ImageFileInput(),})
        # method #2
        return ShelfAnnualInspectionImage

    def get_foreign_formset_class(self):
        return modelformset_factory(
                                    ShelfAnnualInspectionImage, 
                                    formset=BaseModelFormSet, 
                                    form=self.get_foreign_form_class(), 
                                    can_delete=True,
                                    extra=1)

    def get_inine_foreign_formset_class(self):
        return inlineformset_factory(
                                    ShelfAnnualInspection, 
                                    ShelfAnnualInspectionImage,  
                                    form=self.get_foreign_form_class(), 
                                    can_delete=True,
                                    extra=1)

    def get_context_data(self, *args, **kwargs):
        context = super(ShelfAnnualInspectionUpdateView, self).get_context_data(*args, **kwargs) 

        # context["form_foreign_image"] = self.get_foreign_form_class()(self.request.GET or None,self.request.POST or None, self.request.FILES or None )

        # method #1
        # context["formset"] = self.get_foreign_formset_class()(queryset=ShelfAnnualInspectionImage.objects.filter(shelf_annual_inspection=self.object))
        # method #2
        context["formset"] = self.get_inine_foreign_formset_class()(instance=self.object)

        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object() 

        form = self.get_form() 
        form_foreign_image = self.get_foreign_form_class()(self.request.POST, self.request.FILES )
        formset = self.get_inine_foreign_formset_class()(self.request.POST, self.request.FILES, instance=self.object )

        if form.is_valid():
            if form_foreign_image.is_valid():
                image = form_foreign_image.save(commit=False)
                image.shelf_annual_inspection = self.object
                image.save()
            if formset.is_valid():
                formset.save()             
            form.save()

            return HttpResponseRedirect(self.get_success_url())
        else:            
            return self.form_invalid(form)

        return super(UpdateViewMixin, self).post(request, *args, **kwargs)       