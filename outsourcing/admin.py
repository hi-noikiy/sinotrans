from django.contrib import admin
from django.contrib.admin import AdminSite
from inspection.admin import my_admin_site
from django.utils.translation import ugettext_lazy as _

# Register your models here.
from .models import (
    ForkliftMaint, Forklift,ForkliftImage, ForkliftRepair, ForkliftAnnualInspection, ForkliftAnnualInspectionImage,
    )

class ForkliftImageInline(admin.TabularInline):
    model = ForkliftImage
    extra = 0
    max_num = 10

class ForkliftRepairInline(admin.TabularInline):
    model = ForkliftRepair
    extra = 0
    max_num = 10

class ForkliftMaintInline(admin.TabularInline):
    model = ForkliftMaint
    extra = 0
    max_num = 10    

class ForkliftAnnualInspectionInline(admin.StackedInline):
    model = ForkliftAnnualInspection
    extra = 0
    max_num = 10    

class ForkliftAnnualInspectionImageInline(admin.TabularInline):
    model = ForkliftAnnualInspectionImage
    extra = 0
    max_num = 10    

class ForkliftAnnualInspectionAdmin(admin.ModelAdmin):
    list_display = ["date", "next_date",]
    search_fields = ('date', 'next_date')
    list_filter = ('date',)
    ordering = ('date',) 

    inlines = [
        ForkliftAnnualInspectionImageInline,            
    ]

class ForkliftRepairAdmin(admin.ModelAdmin):
    list_display = ["damage_reason", "accessories_name","accessories_num","repaired","repaire_date",]
    search_fields = ("damage_reason", "accessories_name","accessories_num","repaired","repaire_date",)
    list_filter = ("damage_reason", "repaired","repaire_date",)
    ordering = ('repaire_date',) 

class ForkliftMaintAdmin(admin.ModelAdmin):
    list_display = ["clean_forklift", ]
    search_fields = ("clean_forklift", )
    list_filter = ("clean_forklift", )
    ordering = ('clean_forklift',) 

class ForkliftAdmin(admin.ModelAdmin):
    list_display = ["internal_car_number", "internal_plate_number",'sn']
    search_fields = ('internal_car_number',)
    list_filter = ('category',)
    ordering = ('sn',)

    fieldsets= [
        (_('Base Information'),{
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
        (_("Record"),{
             'fields':
                 (
                 'manufacturer',                 
                 'tip_height',                                  
                 'carrying_capacity',
                 'self_weight',
                 'turning_radius',
                 'front_tyre_size',
                 'back_tyre_size',   
                 'forklift_length',
                 'maximum_velocity'
                 )}),]    

    #readonly_fields = ('internal_car_number',)

    inlines = [
        ForkliftImageInline,
        ForkliftRepairInline,
        ForkliftMaintInline,        
        ForkliftAnnualInspectionInline,
    ]

    class Meta:
        model = Forklift

admin.site.register(Forklift, ForkliftAdmin)
admin.site.register(ForkliftRepair, ForkliftRepairAdmin)
admin.site.register(ForkliftMaint, ForkliftMaintAdmin)
admin.site.register(ForkliftAnnualInspection, ForkliftAnnualInspectionAdmin)
my_admin_site.register(Forklift, ForkliftAdmin)
my_admin_site.register(ForkliftRepair, ForkliftRepairAdmin)
my_admin_site.register(ForkliftMaint, ForkliftMaintAdmin)
my_admin_site.register(ForkliftAnnualInspection, ForkliftAnnualInspectionAdmin)
        