from django.contrib import admin
from inspection.admin import my_admin_site

from .models import  TrainingCourse, TrainingPerson, AnnualTraningPlan

class TrainingPersonInline(admin.TabularInline):
    model = TrainingPerson
    extra = 0

class TrainingPersonAdmin(admin.ModelAdmin):
    list_display = ['training_course', "trainee", "score", 'work_position']
    list_filter = [ "trainee", 'work_position' ]
    search_fields = ['training_course__content', "trainee", "score", 'work_position' ]
    list_display_links = ['training_course']
    ordering = ['training_course']
    list_per_page = 10
    list_max_show_all = 80

    class Meta:
        model = TrainingPerson

class AnnualTraningPlanInline(admin.TabularInline):
    model = AnnualTraningPlan
    extra = 0

class AnnualTraningPlanAdmin(admin.ModelAdmin):
    list_display = ['training_course', "planned_date", "actual_date",]
    list_filter = [ 'training_course', "planned_date", "actual_date", ]
    search_fields = ['training_course__content', "planned_date", "actual_date", ]
    list_display_links = ['training_course']
    ordering = ['training_course']
    list_per_page = 10
    list_max_show_all = 80

    class Meta:
        model = AnnualTraningPlan

class TrainingCourseAdmin(admin.ModelAdmin):
    list_display = [ "topic", "location", 'category', 'content']
    #list_editable = [ "location", "topic", 'category', ]
    list_filter = [ "location", ]
    search_fields = ["topic", 'content', ]
    list_display_links = ['topic']
    ordering = ['-date']
    list_per_page = 10
    list_max_show_all = 80

    inlines = [
        TrainingPersonInline,
        AnnualTraningPlanInline,
    ]

    class Meta:
        model = TrainingCourse

    # class Media:
    #     css = {
    #         "all": ("css/model_admin.css",)
    #     }
    #     js = ("js/jquery.min.js", "js/model_admin.js",)

admin.site.register(TrainingCourse, TrainingCourseAdmin)
admin.site.register(TrainingPerson, TrainingPersonAdmin)
admin.site.register(AnnualTraningPlan, AnnualTraningPlanAdmin)

my_admin_site.register(TrainingCourse, TrainingCourseAdmin)
my_admin_site.register(TrainingPerson, TrainingPersonAdmin)
my_admin_site.register(AnnualTraningPlan, AnnualTraningPlanAdmin)