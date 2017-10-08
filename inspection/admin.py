from django.contrib import admin
from .models import (
    OfficeInspection,
    DailyInspection,
    forklift_maint, forklift,forklift_image, forklift_repair, forklift_annual_inspection, forklift_annual_inspection_image,
    shelf, shelf_inspection, shelf_inspection_record,
    equipment, ElectricalEquipmentInspection)
from .forms import (
    DailyInspectionForm,
    ElectricalEquipmentInspectionForm,
)
from django.core.urlresolvers import reverse
from django.contrib.sites.shortcuts import get_current_site


from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = 'SINOTRANS'

my_admin_site = MyAdminSite(name='SINOTRANS')

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
            "all": ("css/model_admin.css",)
        }
        js = ("js/jquery.min.js","js/model_admin.js",)
        
class forklift_imageInline(admin.TabularInline):
    model = forklift_image
    extra = 0
    max_num = 10

class forkliftAdmin(admin.ModelAdmin):
    list_display = ["internal_car_number", "internal_plate_number",'sn']
    search_fields = ('internal_car_number',)
    list_filter = ('category',)
    ordering = ('sn',)

    fieldsets= [
        ('Information',{
             'fields':
                (
                 'internal_car_number',
                 'internal_plate_number',
                 'model',
                 'sn',
                 'category',
                 'width',
                 'length'
                 )}),
        ("Record",{
             'fields':
                 (
                 'manufacturer',                 
                 'tip_height',                                  
                 'carrying_capacity',
                 'self_weight',
                 'turning_radius',
                 'front_tyre_size',
                 'back_tyre_size',   
                 'fork_length',
                 'maximum_velocity'
                 )}),]    

    #readonly_fields = ('internal_car_number',)

    inlines = [
        forklift_imageInline,
    ]

    class Meta:
        model = forklift


class shelfAdmin(admin.ModelAdmin):
    list_display = ['id',"type", "warehouse",'compartment','group','number','is_gradient_measurement_mandatory']
    list_editable = ["type", "warehouse",'compartment','group','number','is_gradient_measurement_mandatory']
    list_filter = ["type", "warehouse",'compartment','group','is_gradient_measurement_mandatory']
    search_fields = ["type", "warehouse",'compartment','group','number']
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


class equipmentAdmin(admin.ModelAdmin):
    list_display = ["name","type"]
    list_editable = ["name", "type"]

    class Meta:
        model = equipment

class ElectricalEquipmentInspectionAdmin(admin.ModelAdmin):
    list_display = ["equipment","use_condition","inspector","date_of_inspection","updated"]
    list_editable = ["use_condition","inspector"]
    form = ElectricalEquipmentInspectionForm

    class Meta:
        model = ElectricalEquipmentInspection

    class Media:
        css = {
            "all": ("css/model_admin.css","css/equipment.css")
        }
        js = ("js/jquery.min.js","js/model_admin.js",)

admin.site.register(DailyInspection, DailyInspectionAdmin)
admin.site.register(OfficeInspection, OfficeInspectionAdmin)
admin.site.register(forklift, forkliftAdmin)
admin.site.register(shelf, shelfAdmin)
admin.site.register(shelf_inspection, shelf_inspectionAdmin)
admin.site.register(equipment, equipmentAdmin)
admin.site.register(ElectricalEquipmentInspection, ElectricalEquipmentInspectionAdmin)

my_admin_site.register(DailyInspection, DailyInspectionAdmin)
my_admin_site.register(OfficeInspection, OfficeInspectionAdmin)
my_admin_site.register(forklift, forkliftAdmin)
my_admin_site.register(shelf, shelfAdmin)
my_admin_site.register(shelf_inspection, shelf_inspectionAdmin)
my_admin_site.register(equipment, equipmentAdmin)
my_admin_site.register(ElectricalEquipmentInspection, ElectricalEquipmentInspectionAdmin)


