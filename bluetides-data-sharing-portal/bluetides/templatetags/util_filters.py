from django import template
register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def pretty_print_bytes(bytes):
    for unit in ['B', 'K', 'M', 'G']:
        if bytes < 1024.0:
            return "{}{}".format(round(bytes, 2), unit)
        bytes /= 1024.0
    return "{}{}".format(round(bytes, 2), "T")
