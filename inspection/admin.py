from django.contrib import admin
from .models import (
    OfficeInspection,
    DailyInspection,
    shelf, shelf_inspection, shelf_inspection_record, ShelfAnnualInspection, ShelfAnnualInspectionImage, ShelfImport,
    Rehearsal, PI, WHPI, RTPI,
    )
    
from .forms import (
    DailyInspectionForm,
    ShelfInspectionRecordForm,
)
from django.core.urlresolvers import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.translation import ugettext_lazy as _

from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = 'SINOTRANS'
    site_title = "SINOTRANS"
    #site_url = None
    index_title = _("SINOTRANS Management")
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
# class OfficeInspectionAdmin(admin.ModelAdmin):
#     list_display = ["location", "plug",'timestamp']
#     class Meta:
#         model = OfficeInspection

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
        

    def view_on_site(self, obj):
        url = reverse('dailyinspection_detail', kwargs={'pk': obj.pk})
        return url

class ShelfAnnualInspectionImageInline(admin.TabularInline):
    model = ShelfAnnualInspectionImage  
    extra = 0

        
class ShelfAnnualInspectionInline(admin.TabularInline):
    model = ShelfAnnualInspection  
    extra = 0

class ShelfAnnualInspectionAdmin(admin.ModelAdmin):
    list_display = ["shelf","date","next_date",]

    view_on_site = False

    inlines = [
        ShelfAnnualInspectionImageInline,
    ]
    
    class Meta:
        model = ShelfAnnualInspection  


class ShelfInspectionRecordInline(admin.TabularInline):
    model = shelf_inspection_record
    extra = 0
    max_num = 10

    def get_max_num(self, request, obj=None, **kwargs):
        max_num = 10
        # if obj and obj.parent:
        #     return max_num - 5
        return max_num

"""
    def view_on_site(self, obj):
        url = reverse('shelf_inspection_detail_and_record_list_edit', kwargs={'pk': obj.pk})        
        #return get_current_site(self.request) + url
        return 'https://sinotran.applinzi.com' + url
"""

class ShelfInspectionRecordAdmin(admin.ModelAdmin):
    list_display = [
        "shelf", 
        # "shelf_inspection",
        "use_condition",
        "is_locked",
        "check_person",
        "owner",
        "gradient",
        'check_date',
        "forecast_complete_time",
        "completed_time",
        ]

    list_editable = [
        # "shelf", 
        # "shelf_inspection__check_date",
        "use_condition",
        "is_locked",
        "owner",
        "gradient",
        "forecast_complete_time",
        ]

    search_fields = [
        # "shelf", 
        # "shelf_inspection__check_date",
        "use_condition",
        "is_locked",
        "check_person",
        "gradient",
        # "forecast_complete_time",
        "comments"]

    list_filter = [
        "shelf__is_gradient_measurement_mandatory",
        "shelf_inspection",
        "use_condition",
        "check_person",
        "forecast_complete_time",
        ]

    ordering = ['shelf']
    list_per_page = 20
    list_max_show_all = 100

    view_on_site = False

    form = ShelfInspectionRecordForm

    class Meta:
        model = shelf_inspection_record

    class Media:
        css = {
            "all": ("css/model_admin.css","css/inspection.css")
        }
        js = ("js/jquery.min.js","js/model_admin.js",)

class ShelfInspectionAdmin(admin.ModelAdmin):
    list_display = ('check_date',)

    view_on_site = False


from .uploads import import_shelf
class ShelfImportAdmin(admin.ModelAdmin):
    list_display = ('shelf_import_file',)

    def save_model(self, request, obj, form, change):

        re = super(ShelfImportAdmin,self).save_model(request, obj, form, change)
        import_shelf(self, request, obj, change)
        return re

class ShelfAdmin(admin.ModelAdmin):
    list_display = ['id',"type", "warehouse",'compartment','warehouse_channel', 'group','number','is_gradient_measurement_mandatory']
    list_editable = ["type", "warehouse",'compartment','warehouse_channel','group','number','is_gradient_measurement_mandatory']
    list_filter = ["type", "warehouse",'compartment','warehouse_channel','group','is_gradient_measurement_mandatory']
    search_fields = ["type", "warehouse",'compartment','warehouse_channel','group','number']
    list_display_links = ['id']
    list_per_page = 10
    list_max_show_all = 80
    ordering = ["warehouse",'compartment','group','number']

    inlines = [
        ShelfAnnualInspectionInline,
        ShelfInspectionRecordInline,
    ]

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


class RehearsalAdmin(admin.ModelAdmin):
    list_display = ['title',"date","attachment","image"]
    list_search = ['title',"date",]

    view_on_site = False

    class Meta:
        model = Rehearsal

class PIAdmin(admin.ModelAdmin):
    list_display = [
        "reporter",
        "company_of_reporter",
        "department_of_reporter",
        "area",
        "category",
        "direct_reason",
        "root_cause",
        "feedback_person",
        "rectification_measures",
        "planned_complete_date",
        "image_before"
        ]
    list_search = [
        "reporter",
        "company_of_reporter",
        "department_of_reporter",
        "area",
        "category",
        "direct_reason",
        "root_cause",
        "feedback_person",
        "rectification_measures",
        ]

    list_filter = [
        "reporter",
        "company_of_reporter",
        "department_of_reporter",
        "area",
        "category",
        "direct_reason",
        "root_cause",
        "feedback_person",
        "rectification_measures",
        ]
    view_on_site = False

    class Meta:
        model = WHPI

class RTPIAdmin(PIAdmin):
    class Meta:
        model = RTPI

admin.site.register(DailyInspection, DailyInspectionAdmin)
# admin.site.register(OfficeInspection, OfficeInspectionAdmin)
admin.site.register(shelf, ShelfAdmin)
admin.site.register(ShelfImport, ShelfImportAdmin)
admin.site.register(shelf_inspection, ShelfInspectionAdmin)
admin.site.register(shelf_inspection_record, ShelfInspectionRecordAdmin)
admin.site.register(ShelfAnnualInspection, ShelfAnnualInspectionAdmin)
admin.site.register(Rehearsal, RehearsalAdmin)
admin.site.register(WHPI, PIAdmin)
admin.site.register(RTPI, RTPIAdmin)

my_admin_site.register(DailyInspection, DailyInspectionAdmin)
# my_admin_site.register(OfficeInspection, OfficeInspectionAdmin)
my_admin_site.register(shelf, ShelfAdmin)
my_admin_site.register(ShelfImport, ShelfImportAdmin)
my_admin_site.register(shelf_inspection, ShelfInspectionAdmin)
my_admin_site.register(shelf_inspection_record, ShelfInspectionRecordAdmin)
my_admin_site.register(ShelfAnnualInspection, ShelfAnnualInspectionAdmin)
my_admin_site.register(Rehearsal, RehearsalAdmin)
my_admin_site.register(WHPI, PIAdmin)
my_admin_site.register(RTPI, RTPIAdmin)

