from django.contrib import admin
from inspection.admin import my_admin_site

from .models import  TrainingCourse, TrainingTranscript, AnnualTraningPlan, TrainingRecord
from .forms import AnnualTraningPlanForm

class TrainingTranscriptInline(admin.TabularInline):
    model = TrainingTranscript
    extra = 0

class TrainingTranscriptAdmin(admin.ModelAdmin):
    list_display = ['training_record', "trainee", "score", 'work_position']
    list_filter = [ "trainee", 'work_position' ]
    search_fields = ['training_course__content', "trainee", "score", 'work_position' ]
    list_display_links = ['training_record']
    ordering = ['training_record']
    list_per_page = 10
    list_max_show_all = 80

    view_on_site = False

    class Meta:
        model = TrainingTranscript


class TrainingRecordInline(admin.TabularInline):
    model = TrainingRecord
    extra = 0

class TrainingRecordAdmin(admin.ModelAdmin):
    list_display = ["training_course", "date", "location", "trainer", 'audiences']
    list_filter = [ "training_course",'location' ]
    search_fields = ["training_course", "date", "location", "trainer", 'audiences']
    list_display_links = ["training_course",]
    ordering = ["training_course",]
    list_per_page = 10
    list_max_show_all = 80

    view_on_site = False

    inlines = [
        TrainingTranscriptInline,
    ]

    class Meta:
        model = TrainingRecord



class AnnualTraningPlanInline(admin.TabularInline):
    model = AnnualTraningPlan
    form = AnnualTraningPlanForm
    extra = 0

class AnnualTraningPlanAdmin(admin.ModelAdmin):
    list_display = ['training_course', "planned_date", "actual_date",]
    list_filter = [ 'training_course', "planned_date", "actual_date", ]
    search_fields = ['training_course__content', "planned_date", "actual_date", ]
    list_display_links = ['training_course']
    ordering = ['training_course']
    list_per_page = 10
    list_max_show_all = 80

    view_on_site = False

    form = AnnualTraningPlanForm

    class Meta:
        model = AnnualTraningPlan
        

class TrainingCourseAdmin(admin.ModelAdmin):
    list_display = [ "training_class","topic", "category", "content"]
    #list_editable = [ "topic", 'category', ]
    list_filter = [ "training_class","category", ]
    search_fields = ["topic", 'content', ]
    list_display_links = ['topic']
    ordering = ["training_class",'topic']
    list_per_page = 10
    list_max_show_all = 80

    view_on_site = False

    inlines = [
        AnnualTraningPlanInline,
        TrainingRecordInline,
    ]

    class Meta:
        model = TrainingCourse

    # class Media:
    #     css = {
    #         "all": ("css/model_admin.css",)
    #     }
    #     js = ("js/jquery.min.js", "js/model_admin.js",)

admin.site.register(TrainingCourse, TrainingCourseAdmin)
admin.site.register(TrainingRecord, TrainingRecordAdmin)
admin.site.register(TrainingTranscript, TrainingTranscriptAdmin)
admin.site.register(AnnualTraningPlan, AnnualTraningPlanAdmin)

my_admin_site.register(TrainingCourse, TrainingCourseAdmin)
my_admin_site.register(TrainingRecord, TrainingRecordAdmin)
my_admin_site.register(TrainingTranscript, TrainingTranscriptAdmin)
my_admin_site.register(AnnualTraningPlan, AnnualTraningPlanAdmin)