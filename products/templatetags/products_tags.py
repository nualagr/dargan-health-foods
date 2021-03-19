from django import template

register = template.Library()


@register.filter(name='split')
def split(str, delimiter):
    return str.split(delimiter)
