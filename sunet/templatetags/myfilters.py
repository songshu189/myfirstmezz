from django import template

register = template.Library()

@register_filter(name="filterbr")
def filterbr(value):
    '''removes all breaks from the given string'''
    return value.replace('<br>', ' ')
