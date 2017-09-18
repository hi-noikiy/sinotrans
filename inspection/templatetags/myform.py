from django import template

register = template.Library()

#register.filter('render_field',render_field)
@register.filter(name='render_field')
def render_field(value):
    if value.__len__() > 30:
        return '%s......'% value[0:30]
    else:
        return value

@register.filter(name='get_field_value')
def get_field_value(inst, fieldname):
    if hasattr(inst, fieldname):
        return inst.get_field_value(fieldname)
    return None