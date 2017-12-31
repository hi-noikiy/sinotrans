from django.shortcuts import render
from django.core.urlresolvers import reverse
#from django.views.i18n import set_language
from django import http
from django.utils import translation
from django.utils.translation import (
    LANGUAGE_SESSION_KEY, check_for_language, get_language, to_locale,
)
from django.utils.http import is_safe_url

def set_language(request):
    #print request.META.get('HTTP_REFERER', None)
    next = request.POST.get('next', request.GET.get('next'))
    if not is_safe_url(url=next, host=request.get_host()):
        next = request.META.get('HTTP_REFERER', None)
        if not is_safe_url(url=next, host=request.get_host()):
            next = reverse("home", kwargs={})
    response = http.HttpResponseRedirect(next)

    lang_code = request.POST.get('language', None) if request.method == 'POST' else request.GET.get('language', None)
    if lang_code and check_for_language(lang_code):
        if hasattr(request, 'session'):
            request.session[LANGUAGE_SESSION_KEY] = lang_code
        else:
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code,
                max_age=settings.LANGUAGE_COOKIE_AGE,
                path=settings.LANGUAGE_COOKIE_PATH,
                domain=settings.LANGUAGE_COOKIE_DOMAIN)

    return response


def about(request):
    return render(request, "about.html", {})

def sitemap(request):
    return render(request, "map.html", {})	

# def CKEditorImageUpload(request):
#     if request.method == 'POST':  
#         callback = request.GET.get('CKEditorFuncNum')  
#         try:  
#             path = "static/upload/" + time.strftime("%Y%m%d%H%M%S",time.localtime())  
#             f = request.FILES["upload"]  
#             file_name = path + "_" + f.name  
#             des_origin_f = open(file_name, "wb+")    
#             for chunk in f.chunks():  
#                 des_origin_f.write(chunk)  
#             des_origin_f.close()  
#         except Exception, e:  
#             print e  
#         res = "<script>window.parent.CKEDITOR.tools.callFunction("+callback+",'/"+file_name+"', '');</script>"  
#         return HttpResponse(res)  
#     else:  
#         raise Http404()  

from inspection.models import month_choice
from inspection.models import DailyInspection
import time, datetime
from datetime import timedelta
from django.utils import timezone
from django.utils.translation import ugettext as _
from inspection.api import (get_daily_inspection_total,
    get_daily_inspection_uncompleted, 
    get_daily_inspection_efficiency, 
    get_daily_inspection_uncompleted_url,
    get_daily_inspection_total_url,
    get_daily_inspection_rows
    )

def get_last_times():
    year = timezone.now().year #time.localtime()[0]
    return [[i, year] for i in range(1,13)]

def DashboardViewSINO(request):

    row_groups = []

    indicators = []

    row_headers = DailyInspection.daily_insepction_category

    # (display, rowspan, columnspan)
    column_header1 = [
        [ [month[1],1,3] for month in month_choice + (('', _('total number')),) ]
    ]

    column_header2 = [[
        (_("total number"),1,1),
        (_("Uncompleted"),1,1),
        (_("efficiency"),1,1),
        ]*len(column_header1[0])]

    if row_groups:
        column_header1.insert(0,[_("category"),2,1])

    if indicators:
        column_header1.insert(0,[_("indicator"),2,1])

    column_header1[0].insert(0,[_("category"),2,1])

    context = {}   
    context["headers"] = column_header1 + column_header2 

    print context["headers"]

    data1 = get_daily_inspection_total()
    data2 = get_daily_inspection_uncompleted()
    data3 = get_daily_inspection_efficiency()
    data4 = get_daily_inspection_uncompleted_url()
    data5 = get_daily_inspection_total_url()

    data = [ zip(a,b,c,d,e) for a,b,c,d,e in zip(data1,data2,data3,data4,data5)]

    # print data
                                                       
    rows = get_daily_inspection_rows()
    indicator = ["na"]*len(rows)
    group = ["na"]*len(rows)
    context["rows_dailyinspection"] = zip(rows,indicator,group,data)


    return render(request,"dashboard_statistic.html",context)

def test(request):
    return render(request, "test.html", {})  