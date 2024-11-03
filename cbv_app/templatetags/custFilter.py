from django import template
register = template.Library()

@register.filter(name='myLower')
def custLower(value):
    result = value[:3].lower()
    return result

@register.filter(name='myAppend')
def custAppend(value,arg):
    res = str(arg)+value
    return res