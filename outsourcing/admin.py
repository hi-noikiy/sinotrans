from django.contrib import admin
from django.contrib.admin import AdminSite
from inspection.admin import my_admin_site
from django.utils.translation import ugettext_lazy as _

# Register your models here.
from .models import (
    ForkliftMaint, Forklift,ForkliftImage, ForkliftRepair, ForkliftAnnualInspection, ForkliftAnnualInspectionImage,
    Driver, Vehicle, VehicleInspection, VehicleTransportationKPI,
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
    list_display = ["created", "updated"]
    search_fields = ("created", "updated" )
    list_filter = ("created", "updated" )
    ordering = ("created", "updated") 

class ForkliftAdmin(admin.ModelAdmin):
    list_display = ["internal_car_number", "internal_plate_number",'sn']
    list_editable = ["internal_car_number","internal_plate_number",'sn',]
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

    class Media:
        css = {
            "all": ("css/model_admin.css", )
        }
        js = ("js/jquery.min.js","js/model_admin.js",)

class DriverAdmin(admin.ModelAdmin):
    list_display = ["name", "driver_ID","driver_license_type","contact_phone"]
    search_fields = ("name", "driver_ID","driver_license_type","contact_phone" )
    list_filter = ("driver_license_type",)
    ordering = ("driver_ID",) 

    class Meta:
        model = Driver    

class VehicleInspectionInline(admin.TabularInline):
    model = VehicleInspection
    extra = 0
    #max_num = 10    

class VehicleAdmin(admin.ModelAdmin):
    list_display = [
                        "service_content", 
                        "motorcade",
                        "relevant_license_plate",
                        'vehicle_inspection_valid_until',
                        "vehicle_type",
                        'relevant_trailer_number',
                        'trailer_inspection_valid_until',
                        'maximum_loadable_tonnage',
                        'green_mark_valid_until',
                        'insurance_policy_valid_until',
                        ]
    search_fields = (
                        "service_content", 
                        "motorcade",
                        "relevant_license_plate",
                        'vehicle_inspection_valid_until',
                        "vehicle_type",
                        'relevant_trailer_number',
                        'trailer_inspection_valid_until',
                        'maximum_loadable_tonnage',
                        'green_mark_valid_until',
                        'insurance_policy_valid_until',
                        )
    list_filter = ("motorcade","service_content", )
    ordering = ("relevant_license_plate",) 

    inlines = [
        VehicleInspectionInline,
    ]

    fieldsets= [
        (None,{
             'fields':
                (
                 'service_content',
                 'motorcade',
                 'relevant_license_plate',
                 'vehicle_inspection_valid_until',
                 'vehicle_type',
                 'relevant_trailer_number',
                 'trailer_inspection_valid_until',
                 'maximum_loadable_tonnage',
                 'green_mark_valid_until',
                 'insurance_policy_valid_until',
                 )}),
        (None,{
             'fields':
                 (
                 'GPS',                 
                 'ABS',                                  
                 'antiroll_protection',
                 'reversing_alarm',
                 'side_edge_and_low_location_collision_guard_bar',
                 'car_seat_headrest',
                 'three_point_belt',   
                 'IVMS_or_VDR',
                 'anti_drop_equipment',
                 )}),]   

    class Meta:
        model = Vehicle    

    class Media:
        css = {
            "all": ("css/model_admin.css", )
        }
        js = ("js/jquery.min.js","js/model_admin.js",)


class VehicleInspectionAdmin(admin.ModelAdmin):
    list_display = ["vehicle", "driver","date_of_inspection","inspector","carrier","rectification_qualified",]
    search_fields = ("vehicle", "driver","date_of_inspection","inspector","carrier","rectification_qualified","disqualification_comments" )
    list_filter = ("vehicle","driver","inspector", "carrier",  "rectification_qualified",)
    ordering = ("vehicle","date_of_inspection",) 

    class Meta:
        model = VehicleInspection    

class VehicleTransportationKPIAdmin(admin.ModelAdmin):
    list_display = ["transportation_project", "year","month",]
    search_fields = ("transportation_project", "year","month", )
    list_filter = ("transportation_project", "year","month", )
    ordering = ("transportation_project", "year","month",) 

    class Meta:
        model = VehicleTransportationKPI    

admin.site.register(Forklift, ForkliftAdmin)
admin.site.register(ForkliftRepair, ForkliftRepairAdmin)
admin.site.register(ForkliftMaint, ForkliftMaintAdmin)
admin.site.register(ForkliftAnnualInspection, ForkliftAnnualInspectionAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(VehicleInspection, VehicleInspectionAdmin)
admin.site.register(VehicleTransportationKPI, VehicleTransportationKPIAdmin)

my_admin_site.register(Forklift, ForkliftAdmin)
my_admin_site.register(ForkliftRepair, ForkliftRepairAdmin)
my_admin_site.register(ForkliftMaint, ForkliftMaintAdmin)
my_admin_site.register(ForkliftAnnualInspection, ForkliftAnnualInspectionAdmin)
my_admin_site.register(Driver, DriverAdmin)
my_admin_site.register(Vehicle, VehicleAdmin)
my_admin_site.register(VehicleInspection, VehicleInspectionAdmin)
my_admin_site.register(VehicleTransportationKPI, VehicleTransportationKPIAdmin)
        