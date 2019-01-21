# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter(name='iconset_from_class')
@stringfilter
def iconset_from_class(value):
    """
    extracts the iconset from a class definition
    "fa-flask" -> "fa"
    :param value:
    """
    if '-' in value:
        return value.split('-')[0]
    return ''
