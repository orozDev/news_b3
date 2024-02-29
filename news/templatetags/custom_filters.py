from django import template

register = template.Library()


@register.filter(name='capital')
def capital(value, arg):
    print(value, arg)
    return value[0].upper() + value[1: len(value)]