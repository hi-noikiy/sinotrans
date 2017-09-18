from django.contrib import admin
from .models import (OfficeInspection, DailyInspection, forklift_maint, forklift, 
    forklift_image, forklift_repair, forklift_annual_inspection, forklift_annual_inspection_image, shelf, shelf_inspection, shelf_inspection_record)
from .forms import DailyInspectionForm

# Register your models here.
class OfficeInspectionAdmin(admin.ModelAdmin):
    list_display = ["location", "plug",'timestamp']
    class Meta:
        model = OfficeInspection

class DailyInspectionAdmin(admin.ModelAdmin):
    list_display = ["category", "rectification_status",'owner']
    form = DailyInspectionForm
    
    class Meta:
        model = DailyInspection
        
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
    list_display = ["type", "warehouse",'compartment','group','number','is_gradient_measurement_mandatory']
    
    class Meta:
        model = shelf

class shelf_inspection_recordInline(admin.TabularInline):
    model = shelf_inspection_record
    extra = 0
    #max_num = 10

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

admin.site.register(DailyInspection, DailyInspectionAdmin)

admin.site.register(OfficeInspection, OfficeInspectionAdmin)

admin.site.register(forklift, forkliftAdmin)

admin.site.register(shelf, shelfAdmin)

#admin.site.register(shelf_inspection_record, shelf_inspection_recordAdmin)

admin.site.register(shelf_inspection, shelf_inspectionAdmin)