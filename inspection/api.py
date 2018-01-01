from .models import DailyInspection, PI, WHPI, RTPI
from equipments.models import EquipmentInspection, SprayPumpRoomInspection, SprayWarehouseInspection

import time, datetime
from datetime import timedelta
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.db.models import Q

import calendar

def get_last_times():
    year = timezone.now().year
    times = [[i, year] for i in range(1,13)]
    times = times + [["",year],]
    return times

def get_model_queryset(model, category,rectification_status, year,month):

    q = None

    if year and month:
        q = q & Q(created__startswith="{0}-{1:0>2d}-".format(year,month)) if q else Q(created__startswith="{0}-{1:0>2d}-".format(year,month))
    else:
        q = q & Q(created__startswith="{0}-".format(year)) if q else Q(created__startswith="{0}-".format(year))
    if category:
        q = q & Q(category__exact=category) if q else Q(category__exact=category)
    if rectification_status:
        q = q & Q(rectification_status__exact=rectification_status) if q else Q(rectification_status__exact=rectification_status)

    qs = model.objects.filter(q) if q else model.objects.all()

    return qs

def get_model_url(category,rectification_status, year,month):
    url = reverse("dailyinspection_list", kwargs={}) 
    q = None
    if category[0]:
        q = "?category={0}".format(category[0])
    if year and month:
        q = "{0}&start={1}-{2}-01&end={1}-{2}-{3}".format(q,year,month,calendar.monthrange(year, month)[1]) if q else\
            "?start={0}-{1}-01&end={0}-{1}-{2}".format(year,month,calendar.monthrange(year, month)[1])
    else:
        q = "{0}&start={1}-01-01&end={1}-12-31".format(q,year) if q else\
            "?start={0}-01-01&end={0}-12-31".format(year)        
    if rectification_status:
        q = "{0}&rectification_status={1}".format(q,rectification_status) if q else\
            "?rectification_status={0}".format(rectification_status)

    return "{0}{1}".format(url, q)

def get_daily_inspection_rows():
    return DailyInspection.daily_insepction_category + (('', _('Total')),)


def get_daily_inspection_total():
    return [[get_model_queryset(DailyInspection, category[0],"",year,month).count()\
                for month, year in get_last_times()] \
                    for category in get_daily_inspection_rows()]

def get_daily_inspection_uncompleted():
    return [[get_model_queryset(DailyInspection, category[0],"uncompleted",year,month).count()\
                for month, year in get_last_times()] \
                    for category in get_daily_inspection_rows()]

    return [[DailyInspection.objects.filter(category=category[0], rectification_status="uncompleted",created__startswith="{0}-{1:0>2d}-".format(year,month)).count() if category[0] else\
            DailyInspection.objects.filter(rectification_status="uncompleted",created__startswith="{0}-{1:0>2d}-".format(year,month)).count()\
                for month, year in get_last_times()] \
                    for category in get_daily_inspection_rows()]             

def get_daily_inspection_total_url():
    return [[get_model_url(category,'',year,month) \
                for month, year in get_last_times()] \
                    for category in get_daily_inspection_rows()]   

    url = reverse("dailyinspection_list", kwargs={}) 
    return [["{0}?category={1}&start={2}-{3}-01&end={2}-{3}-{4}".format(url, category[0],year,month,calendar.monthrange(year, month)[1]) if category[0] else\
            "{0}?start={1}-{2}-01&end={1}-{2}-{3}".format(url, year,month,calendar.monthrange(year, month)[1])\
                for month, year in get_last_times()] \
                    for category in get_daily_inspection_rows()]    

def get_daily_inspection_completed():
    return [[get_model_queryset(DailyInspection, category[0],"completed",year,month).count()\
                for month, year in get_last_times()] \
                    for category in get_daily_inspection_rows()]

def get_daily_inspection_uncompleted_url():

    return [[get_model_url(category,'uncompleted',year,month) \
                for month, year in get_last_times()] \
                    for category in get_daily_inspection_rows()]   

    url = reverse("dailyinspection_list", kwargs={}) 
    return [["%s?q=&category=%s&rectification_status=uncompleted&start=%s-%s-01&end=%s-%s-%s" % (url, category[0],year,month,year,month,calendar.monthrange(year, month)[1]) if category[0] else\
            "%s?q=&rectification_status=uncompleted&start=%s-%s-01&end=%s-%s-%s" % (url,year,month,year,month,calendar.monthrange(year, month)[1]) \
                for month, year in get_last_times()] \
                    for category in get_daily_inspection_rows()]    

def get_daily_inspection_efficiency():
    efficiency_array = get_daily_inspection_completed()

    for i, category in enumerate(get_daily_inspection_rows()):
        for j, [month, year] in enumerate(get_last_times()):            
            time_consumings = 0
            completed_qs = get_model_queryset(DailyInspection, category[0],"completed",year,month)
            # completed_qs = DailyInspection.objects.filter(category=category[0], rectification_status="completed", created__startswith="{0}-{1:0>2d}-".format(year,month)) if category[0] else\
            #         DailyInspection.objects.filter(rectification_status="completed", created__startswith="{0}-{1:0>2d}-".format(year,month))
            for instance in completed_qs:
                time_consumings = time_consumings + instance.time_consuming()
            efficiency_array[i][j]= time_consumings / completed_qs.count() if completed_qs.count() else '-'
    return efficiency_array

# >>>>>>>>>>>>>>>
def get_pi_rows():
    # return (('WH PI/NM', _('WH PI/NM')),) + (('RT PI/NM', _('RT PI/NM')),) + (('', _('Total')),)
    return (('WHPI', _('WH PI/NM')),) + (('RTPI', _('RT PI/NM')),) #+ (('', _('Total')),)

def get_pi_model_queryset(category,rectification_status, year,month):

    model = PI
    if category == "WHPI":
        model = WHPI
    elif category == "RTPI":
        model = RTPI

    q = None

    if year and month:
        q = q & Q(created__startswith="{0}-{1:0>2d}-".format(year,month)) if q else Q(created__startswith="{0}-{1:0>2d}-".format(year,month))
    else:
        q = q & Q(created__startswith="{0}-".format(year)) if q else Q(created__startswith="{0}-".format(year))

    if rectification_status:
        q = q & Q(rectification_status__exact=rectification_status) if q else Q(rectification_status__exact=rectification_status)

    qs = model.objects.filter(q) if q else model.objects.all()

    return qs

def get_whpi_total():
    return [[get_pi_model_queryset(category[0],"",year,month).count()\
                for month, year in get_last_times()] \
                    for category in get_pi_rows()]

def get_whpi_uncompleted():
    return [[get_pi_model_queryset(category[0],"uncompleted",year,month).count()\
                for month, year in get_last_times()] \
                    for category in get_pi_rows()]

def get_whpi_efficiency():
    efficiency_array = get_whpi_uncompleted()

    for i, category in enumerate(get_pi_rows()):
        for j, [month, year] in enumerate(get_last_times()):            
            time_consumings = 0
            completed_qs = get_pi_model_queryset(category[0],"completed",year,month)
            for instance in completed_qs:
                time_consumings = time_consumings + instance.time_consuming()
            efficiency_array[i][j]= time_consumings / completed_qs.count() if completed_qs.count() else '-'
    return efficiency_array

def get_pi_model_url(category,rectification_status, year,month):
    url = reverse("pi_list", kwargs={}) 
    if category == "WHPI":
        url = reverse("whpi_list", kwargs={}) 
    elif category == "RTPI":
        url = reverse("rtpi_list", kwargs={}) 

    q = None

    if year and month:
        q = "{0}&start={1}-{2}-01&end={1}-{2}-{3}".format(q,year,month,calendar.monthrange(year, month)[1]) if q else\
            "?start={0}-{1}-01&end={0}-{1}-{2}".format(year,month,calendar.monthrange(year, month)[1])
    else:
        q = "{0}&start={1}-01-01&end={1}-12-31".format(q,year) if q else\
            "?start={0}-01-01&end={0}-12-31".format(year)        
    if rectification_status:
        q = "{0}&rectification_status={1}".format(q,rectification_status) if q else\
            "?rectification_status={0}".format(rectification_status)

    return "{0}{1}".format(url, q)

def get_pi_total_url():
    return [[get_pi_model_url(category[0],'',year,month) \
                for month, year in get_last_times()] \
                    for category in get_pi_rows()]       

def get_pi_uncompleted_url():

    return [[get_pi_model_url(category[0],'uncompleted',year,month) \
                for month, year in get_last_times()] \
                    for category in get_pi_rows()] 

# >>>>>>>>>>>>>>>>>>>>>>>>>>
def get_spray_rows():
    return (('SprayPumpRoomInspection', _('Spray Pump Room')),) + (('SprayWarehouseInspection', _('Spray Warehouse')),) #+ (('', _('Total')),)

def get_spary_model_queryset(model_name,rectification_status, year,month):

    model = None
    from equipments import models
    model = getattr(models,model_name)()

    q = None

    if year and month:
        q = q & Q(year=year,month="{0:0>2d}".format(month)) if q else Q(year=year,month="{0:0>2d}".format(month))
    else:
        q = q & Q(year=year) if q else Q(year=year)

    if rectification_status:
        q = q & Q(rectification_status__exact=rectification_status) if q else Q(rectification_status__exact=rectification_status)

    qs = model.__class__.objects.filter(q) if q else model.objects.all()

    return qs

def get_spray_total():
    return [[get_spary_model_queryset(model_name[0],"",year,month).count()\
                for month, year in get_last_times()] \
                    for model_name in get_spray_rows()]

def get_spray_uncompleted():
    return [[get_spary_model_queryset(model_name[0],"uncompleted",year,month).count()\
                for month, year in get_last_times()] \
                    for model_name in get_spray_rows()]

def get_spray_efficiency():
    efficiency_array = get_spray_uncompleted()

    for i, model_name in enumerate(get_spray_rows()):
        for j, [month, year] in enumerate(get_last_times()):            
            time_consumings = 0
            completed_qs = get_spary_model_queryset(model_name[0],"completed",year,month)
            for instance in completed_qs:
                time_consumings = time_consumings + instance.time_consuming()
            efficiency_array[i][j]= time_consumings / completed_qs.count() if completed_qs.count() else '-'
    return efficiency_array

def get_spary_model_url(category,rectification_status, year,month):
    url = None
    if category == "SprayPumpRoomInspection":
        url = reverse("spraypumproominspection_list_display", kwargs={}) 
    elif category == "SprayWarehouseInspection":
        url = reverse("spraywarehouseinspection_list_display", kwargs={}) 

    q = None

    if year:
        q = "?year={0}".format(year) 
    else:
        q = ""   

    return "{0}{1}".format(url, q)

def get_spray_total_url():
    return [[get_spary_model_url(category[0],'',year,month) \
                for month, year in get_last_times()] \
                    for category in get_spray_rows()]       

def get_spray_uncompleted_url():

    return [[get_spary_model_url(category[0],'uncompleted',year,month) \
                for month, year in get_last_times()] \
                    for category in get_spray_rows()]                     

# >>>>>>>>>>>>>>>
def get_hydrant_rows():
    return (('ExtinguisherInspection', _('extinguisher')),) + (('HydrantInspection', _('hydrant')),) #+ (('', _('Total')),)

def get_hydrant_model_queryset(model_name,check_result, year,month, is_efficiency=False):

    model = None
    from inspection import models
    model = getattr(models,model_name)()

    q = None

    if year and month:
        q = q & Q(check_date__startswith="{0}-{1:0>2d}-".format(year,month)) if q else Q(check_date__startswith="{0}-{1:0>2d}-".format(year,month))
    else:
        q = q & Q(check_date__startswith="{0}-".format(year)) if q else Q(check_date__startswith="{0}-".format(year))

    if check_result:
        q = q & Q(check_result__exact=check_result) if q else Q(check_result__exact=check_result)

    if is_efficiency:
        q = q & Q(completed_time__gte="{0}-01-01".format(year)) if q else Q(check_result__exact="{0}-01-01".format(year))

    qs = model.__class__.objects.filter(q) if q else model.objects.all()

    return qs

def get_hydrant_total():
    return [[get_hydrant_model_queryset(model_name[0],"",year,month).count()\
                for month, year in get_last_times()] \
                    for model_name in get_hydrant_rows()]

def get_hydrant_uncompleted():
    return [[get_hydrant_model_queryset(model_name[0],"breakdown",year,month).count()\
                for month, year in get_last_times()] \
                    for model_name in get_hydrant_rows()]

def get_hydrant_efficiency():
    efficiency_array = get_whpi_uncompleted()

    for i, model_name in enumerate(get_hydrant_rows()):
        for j, [month, year] in enumerate(get_last_times()):            
            time_consumings = 0
            completed_qs = get_hydrant_model_queryset(model_name[0],"normal",year,month,is_efficiency=True)
            for instance in completed_qs:
                time_consumings = time_consumings + instance.time_consuming()
            efficiency_array[i][j]= time_consumings / completed_qs.count() if completed_qs.count() else '-'
    return efficiency_array

def get_hydrant_model_url(model_name,check_result, year,month):
    url = None
    if model_name == "ExtinguisherInspection":
        url = reverse("extinguisherinspection_list", kwargs={}) 
    elif model_name == "HydrantInspection":
        url = reverse("hydrantinspection_list", kwargs={}) 

    q = None

    if year and month:
        q = "{0}&start={1}-{2}-01&end={1}-{2}-{3}".format(q,year,month,calendar.monthrange(year, month)[1]) if q else\
            "?start={0}-{1}-01&end={0}-{1}-{2}".format(year,month,calendar.monthrange(year, month)[1])
    else:
        q = "{0}&start={1}-01-01&end={1}-12-31".format(q,year) if q else\
            "?start={0}-01-01&end={0}-12-31".format(year)        
    if check_result:
        q = "{0}&check_result={1}".format(q,check_result) if q else\
            "?check_result={0}".format(check_result)

    return "{0}{1}".format(url, q)

def get_hydrant_total_url():
    return [[get_hydrant_model_url(model_name[0],'',year,month) \
                for month, year in get_last_times()] \
                    for model_name in get_hydrant_rows()]       

def get_hydrant_uncompleted_url():

    return [[get_hydrant_model_url(model_name[0],'breakdown',year,month) \
                for month, year in get_last_times()] \
                    for model_name in get_hydrant_rows()] 
