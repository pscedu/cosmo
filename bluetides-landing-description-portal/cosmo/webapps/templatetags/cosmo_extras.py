from django import template
register = template.Library()
from django.urls import reverse

@register.simple_tag
def is_active(request, url):
    # Main idea is to check if the url and the current path is a match
    if request.path == reverse(url) or request.path == 'cosmo/':
        return "active"
    return ""