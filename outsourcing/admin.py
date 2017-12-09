from django.contrib import admin
from django.contrib.admin import AdminSite
from inspection.admin import my_admin_site
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.utils import timezone

# Register your models here.
from .models import (
    ForkliftMaint, Forklift,ForkliftImage, ForkliftRepair, ForkliftAnnualInspection, ForkliftAnnualInspectionImage,
    Driver, Vehicle, VehicleInspection, VehicleTransportationKPI,
    )

from .forms import (
    VehicleInspectionForm, 
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
    # pk_field = ForkliftAnnualInspectionImage

    fieldsets= [
        ("",{
             'fields':
                (
                 'forklift',
                 'date',
                 'next_date',
                 # 'forkliftannualinspectionimage_set',
                 )}),]    

class ForkliftAnnualInspectionImageInline(admin.TabularInline):
    model = ForkliftAnnualInspectionImage
    extra = 0
    max_num = 10    

class ForkliftAnnualInspectionAdmin(admin.ModelAdmin):
    list_display = ["date", "next_date",]
    search_fields = ('date', 'next_date')
    list_filter = ('date',)
    ordering = ('date',) 

    view_on_site = False

    inlines = [
        ForkliftAnnualInspectionImageInline,            
    ]

class ForkliftRepairAdmin(admin.ModelAdmin):
    list_display = ["forklift", "damage_reason", "accessories_name","accessories_num","repaired","repaire_date",]
    search_fields = ("damage_reason", "accessories_name","accessories_num","repaired","repaire_date",)
    list_filter = ("damage_reason", "repaired","repaire_date",)
    ordering = ('repaire_date',) 

    view_on_site = False

class ForkliftMaintAdmin(admin.ModelAdmin):
    list_display = ["created", "updated"]
    search_fields = ("created", "updated" )
    list_filter = ("created", "updated" )
    ordering = ("created", "updated") 

    view_on_site = False

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

    def view_on_site(self, obj):
        url = reverse('forklift_detail', kwargs={'pk': obj.pk})
        return url

class DriverAdmin(admin.ModelAdmin):
    list_display = ["name", "driver_ID","driver_license_type","contact_phone","motorcade",]
    search_fields = ("name", "driver_ID","driver_license_type","contact_phone" ,"motorcade",)
    list_filter = ("driver_license_type","motorcade",)
    ordering = ("driver_ID",) 

    view_on_site = False

    class Meta:
        model = Driver    

class VehicleInspectionInline(admin.TabularInline):
    model = VehicleInspection
    extra = 0
    #max_num = 10    

class VehicleAdmin(admin.ModelAdmin):
    list_display = [
                        "service_content",                         
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
                        "relevant_license_plate",
                        'vehicle_inspection_valid_until',
                        "vehicle_type",
                        'relevant_trailer_number',
                        'trailer_inspection_valid_until',
                        'maximum_loadable_tonnage',
                        'green_mark_valid_until',
                        'insurance_policy_valid_until',
                        )
    list_filter = ("service_content", )
    ordering = ("relevant_license_plate",) 

    inlines = [
        VehicleInspectionInline,
    ]

    fieldsets= [
        (None,{
             'fields':
                (
                 'service_content',
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

    view_on_site = False

    class Meta:
        model = Vehicle    

    class Media:
        css = {
            "all": ("css/model_admin.css", )
        }
        js = ("js/jquery.min.js","js/model_admin.js",)


class VehicleInspectionAdmin(admin.ModelAdmin):
    form = VehicleInspectionForm

    list_display = [
                "vehicle", 
                "date_of_inspection",
                "driver",                
                "inspector",
                "owner",
                "disqualification_comments",
                "carrier",
                "load_or_unload",
                "rectification_qualified",
                "hardware_inspection_disqualification",
                "no_driver_code_of_conduct",
                "overload_or_LSR_violation",
                "safety_policy_violation",
                "no_journey_plan_or_log",
                "vehichle_not_register",
                "no_vehicle_inspection_record",
                "no_DDC_certificate",
                "due_date",
                "completed_time"
        ]
    search_fields = (
                "vehicle", 
                "driver",
                "date_of_inspection",
                "inspector",
                "carrier",
                "rectification_qualified",
                "disqualification_comments" 
                )
    list_filter = (
                "vehicle",
                "driver",
                "inspector", 
                "carrier",  
                "rectification_qualified",
                )
    ordering = (
                "vehicle",
                "date_of_inspection",
                ) 

    view_on_site = False

    def save_model(self, request, obj, form, change):        
        if not change:
            obj.inspector = request.user.get_full_name()
        if obj.rectification_qualified == "yes" and VehicleInspection.objects.filter(pk=obj.pk).first().rectification_qualified == "no":
            obj.completed_time = timezone.now()
        obj.save()

        re = super(VehicleInspectionAdmin,self).save_model(request, obj, form, change)
        return re

    class Meta:
        model = VehicleInspection            

class VehicleTransportationKPIAdmin(admin.ModelAdmin):
    list_display = [
                "transportation_project", 
                "year",
                "month",
                'safe_mileages',
                'safe_labor_hours',
                'LSR_violation_cases',
                'safety_accident_cases',
                'yearly_plan_executing_rate',
                'vehicle_qualification_rate',
                'journey_management_rules_implemented_rate',
                'safe_loading_violation_cases',
                'departure_count',
                'departure_tones',
                'monthly_delivery_plan_completion_rate',
                'AOG_on_time_rate',
                'POD_on_time_rate',
                'POD_accuracy',
                'customer_satisfaction_value',
                'customer_complaint_cases',
                ]

    list_editable = [
                'safe_mileages',
                'safe_labor_hours',
                'LSR_violation_cases',
                'safety_accident_cases',
                'yearly_plan_executing_rate',
                'vehicle_qualification_rate',
                'journey_management_rules_implemented_rate',
                'safe_loading_violation_cases',
                'departure_count',
                'departure_tones',
                'monthly_delivery_plan_completion_rate',
                'AOG_on_time_rate',
                'POD_on_time_rate',
                'POD_accuracy',
                'customer_satisfaction_value',
                'customer_complaint_cases',
                ]

    search_fields = ("transportation_project", "year","month", )
    list_filter = ("transportation_project", "year","month", )
    ordering = ( "year","month", "transportation_project",) 

    view_on_site = False


    class Meta:
        model = VehicleTransportationKPI    

    class Media:
        css = {
            "all": ("css/model_admin.css", "css/outsourcing.css",)
        }
        js = ("js/jquery.min.js","js/model_admin.js",)

    # def view_on_site(self, obj):
    #     url = reverse('person-detail', kwargs={'slug': obj.slug})
    #     return 'https://example.com' + url        
        
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
        