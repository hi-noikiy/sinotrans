from django.contrib import admin
from inspection.admin import my_admin_site

from .models import (
    Equipment, 
    EquipmentType,
    EquipmentInspection,
    )

from .forms import (
    EquipmentInspectionForm,
)

# Register your models here.
class EquipmentTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_editable = ["name"]
    list_filter = [ "name"]

    class Meta:
        model = EquipmentType

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ["name","type"]
    list_editable = ["name", "type"]
    list_filter = [ "type"]

    class Meta:
        model = Equipment

class EquipmentInspectionAdmin(admin.ModelAdmin):
    list_display = ["equipment","use_condition","inspector","date_of_inspection","updated"]
    list_editable = ["use_condition","inspector"]
    list_filter = ["equipment","use_condition","inspector","date_of_inspection"]
    form = EquipmentInspectionForm

    class Meta:
        model = EquipmentInspection

    class Media:
        css = {
            "all": ("css/model_admin.css","css/equipment.css")
        }
        js = ("js/jquery.min.js","js/model_admin.js",)



admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(EquipmentType, EquipmentTypeAdmin)
admin.site.register(EquipmentInspection, EquipmentInspectionAdmin)

my_admin_site.register(Equipment, EquipmentAdmin)
my_admin_site.register(EquipmentType, EquipmentTypeAdmin)
my_admin_site.register(EquipmentInspection, EquipmentInspectionAdmin)        