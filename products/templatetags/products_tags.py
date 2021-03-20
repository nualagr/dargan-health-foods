from django import template

register = template.Library()


# Split Filter Tag found at:
# https://roytuts.com/creating-custom-template-tags-and-filter-in-django/
@register.filter(name='split')
def split(str, delimiter):
    return str.split(delimiter)


@register.filter
def to_ampersand(value):
    return value.replace("_N_", " & ").replace("_", " ")
