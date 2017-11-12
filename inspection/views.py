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
from django_filters import FilterSet, CharFilter, NumberFilter, BooleanFilter, MethodFilter, MultipleChoiceFilter
from django.db.models import Q
from django.http import HttpResponse, Http404
import json
from PIL import Image
import os
from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage
from .mixins import StaffRequiredMixin
from django.db.models.fields.related import (
    ForeignObjectRel, ManyToOneRel, OneToOneField, add_lazy_relation,
)
# Create your views here.
from .models import (
    OfficeInspection, 
    DailyInspection, 
    shelf_inspection_record, shelf_inspection, shelf,
    Rehearsal,
    )
from .forms import (
    OfficeInspectionForm, 
    DailyInspectionForm, InspectionFilterForm, 
    ShelfInspectionRecordForm, ShelfFilterForm, ShelfInspectionForm, ShelfUploadForm,
    )
from .forms import shelf_inspection_record_Formset


from .models import image_upload_to_dailyinspection

# Create your views here.


class TableListMixin(object):
    field_display = []

    field_display_options = []
    field_files = []

    def get_context_data(self, *args, **kwargs):
        context = super(TableListMixin, self).get_context_data(*args, **kwargs)
        context["fields"] = self.field_display
        context["fields_option"] = self.field_display_options
        context["field_files"] = self.field_files
        
        return context

class TableDetailMixin(object):
    fieldsets = [("title",{"fields":("",)}), ]
    model_sets = [("model name", None, []),]  # model name, object_list, list_display

    field_display_options = []
    field_files = []

    def get_context_data(self, *args, **kwargs):
        context = super(TableDetailMixin, self).get_context_data(*args, **kwargs)
        context["fieldsets"] = self.fieldsets
        context["model_sets"] = self.model_sets

        context["fields_option"] = self.field_display_options
        context["field_files"] = self.field_files
        
        return context

class RehearsalListView(TableListMixin, ListView): 
    model = Rehearsal
    template_name = "rehersal/rehearsal_list.html"
    from .admin import RehearsalAdmin
    field_display = RehearsalAdmin.list_display
    field_files = ["attachment"]

    def get_context_data(self, *args, **kwargs):
        context = super(RehearsalListView, self).get_context_data(*args, **kwargs)
        
        return context       

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('rehearsal'),request.path_info),
        ])
        return super(RehearsalListView, self).dispatch(request,args,kwargs)   

class RehearsalDetailView(TableDetailMixin, DetailView): 
    model = Rehearsal
    template_name = "rehersal/rehearsal_detail.html"
    fieldsets = [(_("Base Information"),{"fields":("title","date","attachment",)}), ]
    field_files = ["attachment"]

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


def save_and_get_image(form, fieldname, instance, obj):
    in_mem_image_file = form.cleaned_data[fieldname] # new image file
    instance_file = getattr(instance,fieldname, None)  # original file

    if in_mem_image_file:
        # delete original file
        if instance and instance_file:
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

        save_and_get_image(form, 'image_before', instance, obj)

        save_and_get_image(form, 'image_after', instance, obj)

        obj.save()

        return HttpResponseRedirect(self.get_success_url())

class DailyInspectionCreateView(StaffRequiredMixin, ThumbnailMixin, CreateView):
    form_class = DailyInspectionForm
    model = DailyInspection
    template_name = "dailyinspection/dailyinspection_create.html"

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, _("daily inspection create successfully"), extra_tags='capfirst')
        form = super(DailyInspectionCreateView, self).form_valid(form, *args, **kwargs)
        return form

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


    # def get_object(self, *args, **kwargs):
    #     reuse SingleObjectMixin::get_object
    #     dailyinspection_pk = self.kwargs.get("pk")
    #     dailyinspection = None
    #     if dailyinspection_pk:
    #         dailyinspection = get_object_or_404(DailyInspection, pk=dailyinspection_pk)
    #     return dailyinspection


    def post(self, request, *args, **kwargs):
        form = self.get_form()
        # self.object = self.get_object(*args, **kwargs)

        if form.is_valid():
            messages.success(request, _("daily inspection updated successfully"), extra_tags='capfirst')
            messages.info(request, _("check content please"))
            return self.form_valid(form)
        else:
            messages.success(request, _("daily inspection updated fail"))
            return self.form_invalid(form)

        return super(DailyInspectionUpdateView, self).post(request, *args, **kwargs) 

    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_("Daily Inspection"),reverse("dailyinspection_list", kwargs={})),
            (instance,request.path_info),
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
    owner = CharFilter(name='owner', lookup_type='icontains', distinct=True)

    class Meta:
        model = DailyInspection
        fields = [
            'category',
            'owner',
            'rectification_status',
            
        ]

    def category_filter(self, queryset, value):

        qs = queryset
        for category in value:
            print category
            qs = qs.filter(category=category)

        return qs.distinct()

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
        if ordering:
            qs = qs.order_by(ordering)
        filter_class = self.filter_class
        if filter_class:
            f = filter_class(self.request.GET, queryset=qs)
            context["object_list"] = f
        return context

class DailyInspectionListView(FilterMixin, ListView): 
    model = DailyInspection
    template_name = "dailyinspection/dailyinspection_list.html"
    filter_class = InsepctionFilter

    def get_context_data(self, *args, **kwargs):
        context = super(DailyInspectionListView, self).get_context_data(*args, **kwargs)
        # context["objects_list"] = DailyInspection.objects.order_by('-updated')
        context["objects_sort"] = DailyInspection.objects.order_by('-updated')
        context["query"] = self.request.GET.get("q")
        context["InspectionFilterForm"] = InspectionFilterForm(data=self.request.GET or None)        
        context["categories"] = DailyInspection.daily_insepction_category
        return context       

    def get_queryset(self, *args, **kwargs):
        qs = super(DailyInspectionListView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")

        qs  = self.model.objects.all()
        if not self.request.user.is_staff and not self.request.user.is_superuser:
            qs =  self.model.objects.external()

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

class StatMixin(object):

    # ['category']['date']['count']
    # {'people',{'2017-08-01':'0','2017-08-02':'1'}}

    def get_dates(self):
        #dates = list([ ins.created.strftime("%Y-%m-%d") for ins in DailyInspection.objects.order_by('-updated')])        
        dates = list([ ins.get_created_date() for ins in DailyInspection.objects.order_by('-updated')])
        dates = list(set(dates))
        dates.sort()
        return dates

    def get_catetory(self):
        categories = list([ ins[1] for ins in DailyInspection.daily_insepction_category])
        return categories

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
class ShelfInspectionStatView(StatMixin, TemplateResponseMixin, ContextMixin, View):
    template_name = "dailyinspection/dailyinspection_stat.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ShelfInspectionStatView, self).get_context_data(*args, **kwargs)
        context["objects_list"] = DailyInspection.objects.order_by('-updated')
        context["dates"] = self.get_dates()
        context["categories"] = self.get_catetory()
        context["counters"] = self.get_counters_sorted()
        return context   

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

class ShelfInspectionListView(ListView): 
    model = shelf_inspection
    template_name = "shelf/shelf_inspection_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ShelfInspectionListView, self).get_context_data(*args, **kwargs)

        queryset = shelf_inspection.objects.all()

        records_list = [(object, \
            object.shelf_inspection_record_set.filter(use_condition=1).count(), \
            object.shelf_inspection_record_set.filter(is_locked=False).count(), \
            object.shelf_inspection_record_set.filter(gradient__gt=1.4).count()) for object in shelf_inspection.objects.all()]

        paginator = Paginator(records_list, 2)

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

        context["object_list"] = queryset
        context["records"] = records
        print records
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

    class Meta:
        model = shelf_inspection_record
        fields = [
            'is_gradient_measurement_mandatory',
            'type',
            'warehouse',
            'compartment',
            'warehouse_channel'
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


class ShelfInspectionDetailView(DetailView): 
    model = shelf_inspection
    template_name = "shelf/shelf_inspection_detail.html"
    filter_class = ShelfInspectionRecordFilter

    def get_record_queryset(self, *args, **kwargs):
        pk = self.kwargs.get('pk', None)
        if pk:
            shelf_inspection_instance = get_object_or_404(shelf_inspection, pk=pk)
            queryset =  shelf_inspection_record.objects.filter(shelf_inspection__id = pk).order_by('shelf__id')
            filter_class = self.filter_class
            if filter_class and kwargs.get('filter'):
                queryset = filter_class(self.request.GET, queryset=queryset)
            return queryset
        return None

    def get_context_data(self, *args, **kwargs):
        context = super(ShelfInspectionDetailView, self).get_context_data(*args, **kwargs)
        context["object_list"] = self.get_record_queryset(filter=True)
        context["shelfFilterForm"] = ShelfFilterForm(data=self.request.GET or None) 
        formset = shelf_inspection_record_Formset(queryset=self.get_record_queryset(filter=True).qs,
            initial=[{'use_condition': _('Normal'),}])    
        context["formset"] = formset

        return context       


    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('Shelf Inspection List'),reverse("shelf_inspection_list", kwargs={})),
            (_('Shelf Inspection Detail'),request.path_info),
        ])

        return super(ShelfInspectionDetailView, self).dispatch(request,args,kwargs)


    def post(self, request, *args, **kwargs):
        #print request.is_ajax()
        #print 'request.POST >>>>>>>>>>'
        #print request.POST
        if request.is_ajax():
            form_id = request.POST.get('form_id')
            prefix = form_id.replace('id_', '')
            form = ShelfInspectionRecordForm(request.POST, prefix=prefix)
            #print form.errors
            if form.is_valid():
                instance_id = form.clean_id()
                try:
                    instance = shelf_inspection_record.objects.get(pk=instance_id)
                    form.save(commit=False)
                    #form.save()
                    json_data = {
                        'message': 'valid form!',
                        'valid':True,
                        'form_id': form_id,
                    }                    
                    for fieldname in shelf_inspection_record._meta.get_all_field_names():
                        if not ( fieldname in ShelfInspectionRecordForm.Meta.exclude or fieldname in ShelfInspectionRecordForm.Meta.hidden_form):
                            if form.cleaned_data.get(fieldname, None) is not None: # be careful for False
                                setattr(instance, fieldname, form.cleaned_data.get(fieldname))
                                json_data.update({fieldname: instance.my_get_field_display(fieldname)})
                    instance.save()
                    return HttpResponse(json.dumps(json_data))
                    '''
                    return render(request,"shelf/shelf_inspection_detail.html",self.get_context_data(*args, **kwargs))
                    return render(request,"shelf/response_form.html",context)                
                    form.instance = instance
                    context = {
                        'form' : form,
                        'form_id' : form_id
                    }  
                    '''              
                except:
                    raise Http404
            return HttpResponse(json.dumps({'message': 'invalid form!','valid':False,'form_id': form_id}))
        else:
            raise Http404

class ShelfInspectionCreateView(CreateView):
    #model = shelf
    template_name = "shelf/shelf_inspection_create.html"
    form_class = ShelfInspectionForm
    success_url = "inspection/shelfinspectionlist" #reverse("shelf_inspection_list")

    def get_context_data(self, *args, **kwargs):
        context = super(ShelfInspectionCreateView, self).get_context_data(*args, **kwargs)
        context["form"] = ShelfInspectionForm()
        return context

    def get_form(self, *args, **kwargs):
        form = super(ShelfInspectionCreateView, self).get_form(*args, **kwargs)

        #form.fields['categories'].queryset  = Category.objects.all()
        #form.fields['default'].queryset  = Category.objects.all()

        return form

    def post(self, request, *args, **kwargs):
        postresult = super(ShelfInspectionCreateView, self).post(request, *args, **kwargs)

        form = ShelfInspectionForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            for shelf_instance in shelf.objects.all():
                shelf_inspection_record_instance = shelf_inspection_record()
                shelf_inspection_record_instance.shelf = shelf_instance
                shelf_inspection_record_instance.shelf_inspection = obj
                shelf_inspection_record_instance.is_locked = False
                import time
                shelf_inspection_record_instance.forecast_complete_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
                shelf_inspection_record_instance.save()            

            return redirect(reverse("shelf_inspection_detail", kwargs={'pk': obj.id}))

        return postresult

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
        print self.model._meta.get_fields()
        context["display_fields"] = ["use_condition",]
        context["detail_view_title"] = _("shelf inspection record")
        context["fields"] = [field for field in self.model._meta.get_fields() if not field.name in [self.model._meta.pk.attname, ]]        

        return context    


    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_('Shelf Inspection List'),reverse("shelf_inspection_list", kwargs={})),
            (self.get_object(),request.path_info),
        ])
        return super(ShelfInspectionRecordDetailView, self).dispatch(request,args,kwargs)     