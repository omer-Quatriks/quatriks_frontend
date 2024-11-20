from pprint import pprint
from _keenthemes.bootstrap import KTBootstrap
from _keenthemes.libs.theme import KTTheme
from django.conf import settings
import importlib.util
import sys

auth_templates = {
    'corporate' : 'auth-corporate',
    'creative' : 'auth-creative',
    'fancy' : 'auth-fancy',
    'overlay' : 'auth-overlay',
}

template_background = {
    'bg1' : 'media/auth/bg1.jpg',
    'bg1-dark' : 'media/auth/bg1-dark.jpg',
    'bg2' : 'media/auth/bg2.jpg',
    'bg2-dark' : 'media/auth/bg2-dark.jpg',
    'bg3' : 'media/auth/bg3.jpg',
    'bg3-dark' : 'media/auth/bg3-dark.jpg',
    'bg4' : 'media/auth/bg4.jpg',
    'bg4-dark' : 'media/auth/bg4-dark.jpg',
    'bg5' : 'media/auth/bg5.jpg',
    'bg5-dark' : 'media/auth/bg5-dark.jpg',
    'bg6' : 'media/auth/bg6.jpg',
    'bg6-dark' : 'media/auth/bg6-dark.jpg',
    'bg7' : 'media/auth/bg7.jpg',
    'bg7-dark' : 'media/auth/bg7-dark.jpg',
    'bg8' : 'media/auth/bg8.jpg',
    'bg8-dark' : 'media/auth/bg8-dark.jpg',
    'bg9' : 'media/auth/bg9.jpg',
    'bg9-dark' : 'media/auth/bg9-dark.jpg',
    'bg10' : 'media/auth/bg10.jpg',
    'bg10-dark' : 'media/auth/bg10-dark.jpg',
}

modal_templates = {
    'add_member' : '#kt_modal_add_customer',
    'add_product' : '#kt_modal_add_product',
    'add_category' : '#kt_modal_add_customer',
}

error_templates = {
    '404' : 'media/auth/404-error.png',
    '404-dark' : 'media/auth/404-error-dark.png',
    '500' : 'media/auth/500-error.png',
    '500-dark' : 'media/auth/500-error-dark.png',
    '505' : 'media/auth/505-error.png',
    '505-dark' : 'media/auth/505-error-dark.png',
}

class KTLayout:
    # Initialize the bootstrap files and page layout
    def init(context):
        # Init the theme API
        KTTheme.init()

        # Set a default layout globally. Can be set in the page level view file as well.
        # See example in dashboards/views.py
        context.update(
            {
                #'layout': KTTheme.setLayout('dashboard/default.html', context),
                'layout': KTTheme.setLayout('dashboard/dashboard-saas.html', context),
                # "layout": KTTheme.setLayout("default_header_layout.html", context),
                # "layout": KTTheme.setLayout("default_mini_sidebar_layout.html", context),
                # "layout": KTTheme.setLayout("default_overlay_layout.html", context),

                # AUTH Defaults
                'auth_background' : template_background[settings.QTRKS_COMPANY_DEFAULTS["auth_background"]],
                'auth_background_dark' : template_background[settings.QTRKS_COMPANY_DEFAULTS["auth_background_dark"]],
                'auth_logo' : settings.QTRKS_COMPANY_DEFAULTS["auth_logo"],
                'auth_form_position' : settings.QTRKS_COMPANY_DEFAULTS["auth_form_position"],

                # DASHBOARD Defaults
                'service' : 'E-Commerce',
                'sidebar_logo' : settings.QTRKS_COMPANY_DEFAULTS["sidebar_logo"],
                'sidebar_logo_dark' : settings.QTRKS_COMPANY_DEFAULTS["sidebar_logo_dark"],
                'sidebar_logo_small' : settings.QTRKS_COMPANY_DEFAULTS["sidebar_logo_small"],
                'toolbar_buttons' : settings.QRKS_COMPANY_TOOLBAR_BUTTONS,
            }
        )

        # Init the base theme settings
        KTBootstrap.init()

        # Return context
        return context
