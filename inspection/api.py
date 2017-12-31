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
    return [[i, year] for i in range(1,13)]

def get_daily_insepction_queryset(category,rectification_status, year,month):

    q = Q(created__startswith="{0}-{1}-".format(year,month))
    if category:
        q = q & Q(category__exact=category)
    if rectification_status:
        q = q & Q(rectification_status__exact=rectification_status)

    qs = DailyInspection.objects.filter(q)

    return qs


def get_rows():
    return DailyInspection.daily_insepction_category + (('', _('Total')),)


def get_daily_inspection_total():
    return [[get_daily_insepction_queryset(category[0],"",year,month).count()\
                for month, year in get_last_times()] \
                    for category in get_rows()]

def get_daily_inspection_uncompleted():
    return [[DailyInspection.objects.filter(category=category[0], rectification_status="uncompleted",created__startswith="{0}-{1}-".format(year,month)).count() if category[0] else\
            DailyInspection.objects.filter(rectification_status="uncompleted",created__startswith="{0}-{1}-".format(year,month)).count()\
                for month, year in get_last_times()] \
                    for category in get_rows()]             

def get_daily_inspection_total_url():
    url = reverse("dailyinspection_list", kwargs={}) 
    return [["{0}?category={1}&start={2}-{3}-01&end={2}-{3}-{4}".format(url, category[0],year,month,calendar.monthrange(year, month)[1]) if category[0] else\
            "{0}?start={1}-{2}-01&end={1}-{2}-{3}".format(url, year,month,calendar.monthrange(year, month)[1])\
                for month, year in get_last_times()] \
                    for category in get_rows()]    

def get_daily_inspection_completed():
    return [[DailyInspection.objects.filter(category=category[0], rectification_status="completed",created__startswith="{0}-{1}-".format(year,month)).count() if category[0] else\
            DailyInspection.objects.filter(rectification_status="completed",created__startswith="{0}-{1}-".format(year,month)).count() \
                for month, year in get_last_times()] \
                    for category in get_rows()]   

def get_daily_inspection_uncompleted_url():
    # url = ""
    # return [["{0}?q=&category={1}&rectification_status=uncompleted&start={2}-{3}-01&end={2}-{3}-{4}".format(url, category[0],year,month,calendar.monthrange(year, month)[1]) if category[0] else\
    #         "{0}?q=&rectification_status=uncompleted&start={1}-{2}-01&end={1}-{2}-{4}".format(url, year,month,calendar.monthrange(year, month)[1])\
    #             for month, year in get_last_times()] \
    #                 for category in get_rows()]    

    url = reverse("dailyinspection_list", kwargs={}) 
    return [["%s?q=&category=%s&rectification_status=uncompleted&start=%s-%s-01&end=%s-%s-%s" % (url, category[0],year,month,year,month,calendar.monthrange(year, month)[1]) if category[0] else\
            "%s?q=&rectification_status=uncompleted&start=%s-%s-01&end=%s-%s-%s" % (url,year,month,year,month,calendar.monthrange(year, month)[1]) \
                for month, year in get_last_times()] \
                    for category in get_rows()]    

def get_daily_inspection_efficiency():
    efficiency_array = get_daily_inspection_completed()

    for i, category in enumerate(get_rows()):
        for j, [month, year] in enumerate(get_last_times()):            
            time_consumings = 0
            completed_qs = DailyInspection.objects.filter(category=category[0], rectification_status="completed", created__startswith="{0}-{1}-".format(year,month)) if category[0] else\
                    DailyInspection.objects.filter(rectification_status="completed", created__startswith="{0}-{1}-".format(year,month))
            for instance in completed_qs:
                time_consumings = time_consumings + instance.time_consuming()
            efficiency_array[i][j]= time_consumings / completed_qs.count() if completed_qs.count() else '-'
    return efficiency_array

