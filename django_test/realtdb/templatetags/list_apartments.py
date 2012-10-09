from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.inclusion_tag('realtdb/houses.html')
def list_apartments(obj_lists):
    pass
