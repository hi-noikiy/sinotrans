# -*- coding:utf-8 -*-
from django import template
from django.utils import translation
from django.conf import settings

LANGUAGES = []
for lang_code in settings.LANGUAGES_SUPPORTED:
	LANGUAGES.append(translation.get_language_info(lang_code))

	
register = template.Library()

@register.inclusion_tag('languages_select_part.html')
def language_select(default, request):
	return {'languages':LANGUAGES, 'default':default, 'request':request}

@register.filter(name="strip_lang")
def strip_lang(value):
    lang = translation.get_language()
    #strip_url = '/%s' % value.lstrip('/%s/' % lang)	
    strip_url = value.replace('/{0}/'.format(lang), '/')
    return strip_url

@register.filter(name="get_lang")
def get_lang(value):
    return '/'+ value.split('/')[0]    