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
