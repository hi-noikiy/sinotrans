from django import template

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
        return getattr(inst, fieldname)
    return None

# field value for display ( options, i18n)
@register.filter(name='my_get_field_display')
def my_get_field_display(inst, fieldname):
    if hasattr(inst, fieldname):
        field = inst._meta.get_field(fieldname)
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