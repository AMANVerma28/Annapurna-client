from django import template
register = template.Library()

@register.filter(name='splitlng')
def splitlng(value, key):
#    Returns the value turned into a list.
    print(value.split(key)[0])
    return value.split(key)[0]

@register.filter(name='splitlat')
def splitlat(value, key):
#        Returns the value turned into a list.
    return value.split(" ")[1]