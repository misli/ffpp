# -*- coding: utf-8 -*-

"""
Django settings for ffpp project.
"""

from django.utils.translation import ugettext_lazy as _
from cms_site.settings import *

# Application definition
INSTALLED_APPS = INSTALLED_APPS + [
    'cmsplugin_iframe2',
    'cmsplugin_container',
]

CMS_TEMPLATES = (
    ('default.html', _('Default')),
)

CMS_PLACEHOLDER_CONF = {
    'content': {
        'name': _('Content'),
    },
}

GANALYTICS_TRACKING_CODE = 'UA-32025357-2'

CONTAINER_TEMPLATES = {
    'container': {
        'label':    _('container'),
        'template': 'container',
        'class': 'white',
    },
    'green': {
        'label':    _('green container'),
        'template': 'container',
        'class': 'green',
    },
    'carousel': {
        'label':    _('carousel'),
        'template': 'carousel',
    },
}
