from django import template

register = template.Library()


@register.filter
def keyvalue(dict, key):
    if(key.name in dict):
        return dict[key.name]
    else:
        return None
