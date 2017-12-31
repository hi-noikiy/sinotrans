from .models import DailyInspection

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
        q = q & Q(created__startswith="{0}-{1}-".format(year,month)) if q else Q(created__startswith="{0}-{1}-".format(year,month))
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

    return [[DailyInspection.objects.filter(category=category[0], rectification_status="uncompleted",created__startswith="{0}-{1}-".format(year,month)).count() if category[0] else\
            DailyInspection.objects.filter(rectification_status="uncompleted",created__startswith="{0}-{1}-".format(year,month)).count()\
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
            # completed_qs = DailyInspection.objects.filter(category=category[0], rectification_status="completed", created__startswith="{0}-{1}-".format(year,month)) if category[0] else\
            #         DailyInspection.objects.filter(rectification_status="completed", created__startswith="{0}-{1}-".format(year,month))
            for instance in completed_qs:
                time_consumings = time_consumings + instance.time_consuming()
            efficiency_array[i][j]= time_consumings / completed_qs.count() if completed_qs.count() else '-'
    return efficiency_array

