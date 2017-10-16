from django.contrib import admin
from inspection.admin import my_admin_site

from .models import  TrainingCourse, AnnualTraningPlan

class TrainingCourseAdmin(admin.ModelAdmin):
    list_display = ['date', "location", "topic", 'type', 'content']
    list_editable = [ "location", "topic", 'type', 'content']
    list_filter = ["date", "location", ]
    search_fields = ["topic", 'content', ]
    list_display_links = ['date']
    ordering = ['-date']
    list_per_page = 10
    list_max_show_all = 80

    class Meta:
        model = TrainingCourse

    # class Media:
    #     css = {
    #         "all": ("css/model_admin.css",)
    #     }
    #     js = ("js/jquery.min.js", "js/model_admin.js",)

admin.site.register(TrainingCourse, TrainingCourseAdmin)

my_admin_site.register(TrainingCourse, TrainingCourseAdmin)