from django import template
from django.db import models
from django.utils.translation import ugettext as _

register = template.Library()

#register.filter('render_field',render_field)
@register.filter(name='render_field')
def render_field(value):
    if value.__len__() > 30:
        return '%s......'% value[0:30]
    else:
        return value

# field value in db
@register.filter(name='my_get_field_value')
def my_get_field_value(inst, fieldname):
    if hasattr(inst, fieldname):
        value = getattr(inst, fieldname)
        if None == value:
            value = ""
        else:
            pass
        return value

    return None


@register.filter(name='my_hasattr')
def my_hasattr(inst, fieldname):
    try:
        if hasattr(inst, fieldname):
            return True
    except:
        pass
    return False
    
# field value for display ( options, i18n)
@register.filter(name='my_get_field_display')
def my_get_field_display(inst, fieldname):
    if hasattr(inst, fieldname):
        field = inst._meta.get_field(fieldname)   
        value = getattr(inst, fieldname)
        if True == value:
            return  _("Yes")
        elif False == value:
            return  _("No")
        elif None == value:
            return  ""
        else:
            pass
        return "%s" % inst._get_FIELD_display(field)  
        #return inst.my_get_field_display(fieldname)
    return None
    
# field lable / verbose name
@register.filter(name='my_get_field_verbose_name')
def my_get_field_verbose_name(inst, fieldname):
    if hasattr(inst, fieldname):
        field = inst._meta.get_field(fieldname)
        return field.verbose_name
    return None

@register.filter(name='my_get_pk_name')
def my_get_pk_name(inst):
    meta = inst._meta
    return meta.pk.attname

"""
def get_pk_name(model):
    meta = model._meta.concrete_model._meta
    return _get_pk(meta).name
"""