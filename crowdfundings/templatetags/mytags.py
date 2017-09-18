from django import template
register = template.Library()


def str2int(value):
    if value.__len__() > 0:
        return int(value)
    else:
        return 0	

@register.filter(name='int2str')
def int2str(value):
    return str(value)

register.filter('str2int',str2int)



