from django.conf import settings
from pprint import pprint
import os
from django.templatetags.static import static
from importlib import import_module, util
import json
from django.core.cache import cache


# Core theme class
class QTRKSTheme:
    defaultCompanyName = ''


    def init():
        QTRKSTheme.defaultCompanyName = ''


    def getCompanyName():
        return settings.QTRKS_DEFAULT_COMPANY_NAME

    def getCompanyAuthDefaults():
        return settings.QTRKS_COMPANY_AUTH_DEFAULTS
