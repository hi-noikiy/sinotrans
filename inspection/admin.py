from django.contrib import admin
from .models import (
    OfficeInspection,
    DailyInspection,
    shelf, shelf_inspection, shelf_inspection_record,
    Rehearsal, PI,
    )
    
from .forms import (
    DailyInspectionForm,
)
from django.core.urlresolvers import reverse
from django.contrib.sites.shortcuts import get_current_site


from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = 'SINOTRANS'
    site_title = "SINOTRANS"
    #site_url = None
    index_title = "SINOTRANS Management"
    """        index_template
    app_index_template
    empty_value_display
    login_template
    login_form
    logout_template
    password_change_template
    password_change_done_template
    """

my_admin_site = MyAdminSite(name='sinotrans')

# Register your models here.
class OfficeInspectionAdmin(admin.ModelAdmin):
    list_display = ["location", "plug",'timestamp']
    class Meta:
        model = OfficeInspection

class DailyInspectionAdmin(admin.ModelAdmin):
    list_display = ['inspection_content', "category","rectification_status",'owner','due_date','created','updated','location']
    list_editable = ["category","rectification_status",'owner','location']
    list_filter = ["category", "rectification_status",'owner','location']
    search_fields = ["category", 'inspection_content',"rectification_status",'owner','due_date','created','updated','location']
    list_display_links = ['inspection_content']
    ordering = ['-created']
    list_per_page = 10
    list_max_show_all = 80

    form = DailyInspectionForm
    
    class Meta:
        model = DailyInspection

    class Media:
        css = {
            "all": ("css/model_admin.css", "css/inspection.css", )
        }
        js = ("js/jquery.min.js","js/model_admin.js",)
        



class shelfAdmin(admin.ModelAdmin):
    list_display = ['id',"type", "warehouse",'compartment','warehouse_channel', 'group','number','is_gradient_measurement_mandatory']
    list_editable = ["type", "warehouse",'compartment','warehouse_channel','group','number','is_gradient_measurement_mandatory']
    list_filter = ["type", "warehouse",'compartment','warehouse_channel','group','is_gradient_measurement_mandatory']
    search_fields = ["type", "warehouse",'compartment','warehouse_channel','group','number']
    list_display_links = ['id']
    list_per_page = 10
    list_max_show_all = 80
    ordering = ["warehouse",'compartment','group','number']

    
    class Meta:
        model = shelf

    class Media:
        css = {
            "all": ("css/model_admin.css",)
        }
        js = ("js/jquery.min.js","js/model_admin.js",)

    def view_on_site(self, obj):
        url = reverse('shelf_detail', kwargs={'pk': obj.pk})
        #print get_current_site(self.request)
        #return 'http://127.0.0.1:8000' + url
        return url

class shelf_inspection_recordInline(admin.TabularInline):
    model = shelf_inspection_record
    extra = 0
    #max_num = 10

    def view_on_site(self, obj):
        url = reverse('shelf_inspection_detail', kwargs={'pk': obj.pk})        
        #return get_current_site(self.request) + url
        return 'https://sinotran.applinzi.com' + url

'''
class shelf_inspection_recordAdmin(admin.ModelAdmin):
    list_display = ["use_condition", "check_person",'gradient','forecast_complete_time','is_locked']
    
    class Meta:
        model = shelf_inspection_record
'''

class shelf_inspectionAdmin(admin.ModelAdmin):
    list_display = ["check_date"]
    
    class Meta:
        model = shelf_inspection  

    inlines = [
        shelf_inspection_recordInline,
    ]

class RehearsalAdmin(admin.ModelAdmin):
    list_display = ['title',"date",]
    list_search = ['title',"date",]

    class Meta:
        model = Rehearsal

class PIAdmin(admin.ModelAdmin):
    list_display = ['date',"reporter","company_of_reporter","department_of_reporter","PI_area","category","direct_reason","root_cause","feedback_person","rectification_measures",]
    list_search = ['date',"reporter","company_of_reporter","department_of_reporter","PI_area","category","direct_reason","root_cause","feedback_person","rectification_measures",]

    class Meta:
        model = PI


admin.site.register(DailyInspection, DailyInspectionAdmin)
admin.site.register(OfficeInspection, OfficeInspectionAdmin)
admin.site.register(shelf, shelfAdmin)
admin.site.register(shelf_inspection, shelf_inspectionAdmin)
admin.site.register(Rehearsal, RehearsalAdmin)
admin.site.register(PI, PIAdmin)

my_admin_site.register(DailyInspection, DailyInspectionAdmin)
my_admin_site.register(OfficeInspection, OfficeInspectionAdmin)
my_admin_site.register(shelf, shelfAdmin)
my_admin_site.register(shelf_inspection, shelf_inspectionAdmin)
my_admin_site.register(Rehearsal, RehearsalAdmin)
my_admin_site.register(PI, PIAdmin)

