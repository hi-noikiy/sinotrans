from django.contrib import admin
from .models import (
    OfficeInspection,
    DailyInspection,
    shelf, shelf_inspection, shelf_inspection_record,
    SprayPumpRoomInspection)
    
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
            "all": ("css/inspection.css", "css/model_admin.css")
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
        return 'https://sinotran.applinzi.com' + url

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

class SprayPumpRoomInspectionAdmin(admin.ModelAdmin):
    list_display = ['month',"voltage_and_power_normal","indicator_and_instrument_normal"]
    list_editable = ["voltage_and_power_normal","indicator_and_instrument_normal"]

    class Meta:
        model = SprayPumpRoomInspection

admin.site.register(DailyInspection, DailyInspectionAdmin)
admin.site.register(OfficeInspection, OfficeInspectionAdmin)
admin.site.register(shelf, shelfAdmin)
admin.site.register(shelf_inspection, shelf_inspectionAdmin)
admin.site.register(SprayPumpRoomInspection, SprayPumpRoomInspectionAdmin)

my_admin_site.register(DailyInspection, DailyInspectionAdmin)
my_admin_site.register(OfficeInspection, OfficeInspectionAdmin)
my_admin_site.register(shelf, shelfAdmin)
my_admin_site.register(shelf_inspection, shelf_inspectionAdmin)
my_admin_site.register(SprayPumpRoomInspection, SprayPumpRoomInspectionAdmin)

