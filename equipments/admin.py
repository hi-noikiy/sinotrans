from django.contrib import admin
from inspection.admin import my_admin_site

from .models import (
    Equipment, 
    EquipmentType,
    EquipmentInspection,
    SprayPumpRoomInspection,
    SprayWarehouseInspection,
    )

from .forms import (
    EquipmentInspectionForm,
)

# Register your models here.
class EquipmentTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_editable = ["name"]
    list_filter = [ "name"]

    view_on_site = False

    class Meta:
        model = EquipmentType

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ["name","type"]
    list_editable = [ "type"]
    list_filter = [ "type"]

    view_on_site = False

    class Meta:
        model = Equipment

class EquipmentInspectionAdmin(admin.ModelAdmin):
    list_display = ["equipment","use_condition","inspector","date_of_inspection","updated","owner","due_date","completed_time"]
    list_editable = ["use_condition","inspector"]
    list_filter = ["equipment","use_condition","inspector","date_of_inspection"]
    form = EquipmentInspectionForm

    view_on_site = False

    class Meta:
        model = EquipmentInspection

    class Media:
        css = {
            "all": ("css/model_admin.css","css/equipment.css")
        }
        js = ("js/jquery.min.js","js/model_admin.js",)


class SprayPumpRoomInspectionAdmin(admin.ModelAdmin):
    list_display = ['year','month',
        "voltage_and_power_normal",
        "indicator_and_instrument_normal",
        "switch_contactor_and_connection_normal",
        "no_corrosion_inside_and_foundation_bolt_not_loose",
        "motor_and_pump_connection_intact",
        "motor_sample_integrated",
        "no_corrosion_and_damage",
        "valve_normally_open",
        "one_way_valve_intact_and_no_leak_and_pressure_gage_normal",
        "pressure_maintaining_valve_intact",
        "water_level_normal_and_moisturizing_well",
        "water_level_cover_plate_and_no_abnormal_move",
        "pool_wall_dry_and_no_leak",
        "no_sundries_in_pump_house",
        "pump_house_clean_and_tidy",
        ]
    list_editable = ["voltage_and_power_normal",
        "indicator_and_instrument_normal",
        "switch_contactor_and_connection_normal",
        "no_corrosion_inside_and_foundation_bolt_not_loose",
        "motor_and_pump_connection_intact",
        "motor_sample_integrated",
        "no_corrosion_and_damage",
        "valve_normally_open",
        "one_way_valve_intact_and_no_leak_and_pressure_gage_normal",
        "pressure_maintaining_valve_intact",
        "water_level_normal_and_moisturizing_well",
        "water_level_cover_plate_and_no_abnormal_move",
        "pool_wall_dry_and_no_leak",
        "no_sundries_in_pump_house",
        "pump_house_clean_and_tidy",]
        
    list_filter = ['year','month',]

    view_on_site = False

    class Meta:
        model = SprayPumpRoomInspection

    class Media:
        css = {
            "all": ("css/model_admin.css","css/equipment.css")
        }
        js = ("js/jquery.min.js","js/model_admin.js",)

class SprayWarehouseInspectionAdmin(admin.ModelAdmin):
    list_display = ['year','month',
        "valve_normal",
        "valve_open_signal_transmission_normal",
        "valve_no_corrosion",
        "water_testing_normal",
        "valve_switch_in_close_status",
        "pipe_network_pressure_normal",
        "pipe_valve_in_open_status",
        "pipe_connection_no_leakage",
        "spray_head_no_leakage",
        "inspector",
        "date_of_inspection",
        ]
    list_editable = [
        "valve_normal",
        "valve_open_signal_transmission_normal",
        "valve_no_corrosion",
        "water_testing_normal",
        "valve_switch_in_close_status",
        "pipe_network_pressure_normal",
        "pipe_valve_in_open_status",
        "pipe_connection_no_leakage",
        "spray_head_no_leakage",
        ]
        
    list_filter = ['year','month',]

    view_on_site = False

    class Meta:
        model = SprayWarehouseInspection

    class Media:
        css = {
            "all": ("css/model_admin.css","css/equipment.css")
        }
        js = ("js/jquery.min.js","js/model_admin.js",)

admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(EquipmentType, EquipmentTypeAdmin)
admin.site.register(EquipmentInspection, EquipmentInspectionAdmin)
admin.site.register(SprayPumpRoomInspection, SprayPumpRoomInspectionAdmin)
admin.site.register(SprayWarehouseInspection, SprayWarehouseInspectionAdmin)

my_admin_site.register(Equipment, EquipmentAdmin)
my_admin_site.register(EquipmentType, EquipmentTypeAdmin)
my_admin_site.register(EquipmentInspection, EquipmentInspectionAdmin)    
my_admin_site.register(SprayPumpRoomInspection, SprayPumpRoomInspectionAdmin)    
my_admin_site.register(SprayWarehouseInspection, SprayWarehouseInspectionAdmin)