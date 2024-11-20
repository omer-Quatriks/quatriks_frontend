from django.views.generic import TemplateView, ListView
from django.utils.translation import gettext_lazy as _
from _keenthemes.libs.theme import KTTheme
from _keenthemes.__init__ import KTLayout, template_background, error_templates, modal_templates
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.conf import settings
from django.urls import resolve
from django.shortcuts import redirect, render
from pprint import pprint

from _BASE.models import Member

"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to dashboards/urls.py file for more pages.
"""

# class DashboardsView(LoginRequiredMixin, TemplateView):
class DashboardView(TemplateView):
    template_name = 'pages/dashboards/index.html'
    login_url = "/signin/"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context = KTLayout.init(context)

        url_name = resolve(self.request.path_info).url_name
        page = self.kwargs.get('page', 'index')
        content = self.kwargs.get('slug', 'default')

        if url_name == 'index':
            KTTheme.addVendors(['amcharts', 'amcharts-maps', 'amcharts-stock'])
            context.update(
                self.get_index_view_contexts(page=page, content=content)
            )
        elif url_name == 'list':
            KTTheme.addJavascriptFile('js/custom/apps/ecommerce/customers/listing/listing.js')
            KTTheme.addJavascriptFile('js/custom/apps/ecommerce/customers/listing/export.js')
            KTTheme.addJavascriptFile('js/custom/apps/ecommerce/customers/listing/add.js')
            KTTheme.addJavascriptFile('js/custom/widgets.js')
            context.update(
                self.get_list_view_contexts(page=page, content=content)
            )
        elif url_name == 'create':
            context.update(
                self.get_edit_view_contexts(page=page, content=content)
            )
        elif url_name == 'edit':
            context.update(
                self.get_edit_view_contexts(page=page, content=content)
            )
        elif url_name == 'error':
            context.update({
                'layout': KTTheme.setLayout('system.html', context),
            })
            context.update(
                self.get_error_view_contexts(page=page, content=content)
            )

        return context
    
        
    def get_index_view_contexts(self, page, content):

        return {
            'page_title' : _('Home'),
            'toolbar_url' : 'dashboard:index',
        }
        
    def get_error_view_contexts(self, page, content):

        return {
            'page_title' : _('System Error') if str.startswith(content, "5") else _('Not Found'),
            'error_title' : _('System Error') if str.startswith(content, "5") else _('Oops!'),
            'error_text' : _('Something went wrong! Please try again later.') if str.startswith(content, "5") else _("We can't find that page."),
            'error_image' : error_templates['500'] if str.startswith(content, "5") else error_templates['404'],
            'error_image_dark' : error_templates['500-dark'] if str.startswith(content, "5") else error_templates['404-dark'],
            'error_button_text' : 'Return Home',
            'error_button_url' : 'dashboard:index',
            'background' : template_background[settings.QTRKS_COMPANY_DEFAULTS["error_background"]],
            'background_dark' : template_background[settings.QTRKS_COMPANY_DEFAULTS["error_background_dark"]],
        }
        
    def get_list_view_contexts(self, page, content):

        content = member_listing_test_data() if page == 'member' else member_listing_test_data()
         
        return {
            'page_title' : _(f'{page} List'),
            'toolbar_url' : 'dashboard:list',
            'add_modal' : modal_templates['add_member'],
            'toolbar_url_parameter' : f'{page}',
            'table_headers': settings.QTRKS_COMPANY_LIST_VIEW[f'{page}']['table_headers'],
            'table_body': [],
            'content': content,
        }
        
    def get_create_view_contexts(self, page, content):

        if page == 'product':
            return {
                'page_title': f'Edit Product {content}',
                'toolbar_url' : 'dashboard:view',
                'toolbar_url_parameter' : f'{page}',
                'content': f'Editing {content} for Product',
            }
        
        elif page == 'category':
            return {
                'page_title': 'Edit Category',
                'toolbar_url' : 'dashboard:view',
                'toolbar_url_parameter' : f'{page}',
                'content': f'Editing {content} for Category',
            }
        else:
            return {
                'page_title': 'Edit Page',
                'toolbar_url' : 'dashboard:view',
                'toolbar_url_parameter' : f'{page}',
                'content': f'Editing {content} for {page}',
            }
        
    def get_edit_view_contexts(self, page, content):

        if page == 'product':
            return {
                'page_title': f'Edit Product {content}',
                'content': f'Editing {content} for Product',
            }
        
        elif page == 'category':
            return {
                'page_title': 'Edit Category',
                'content': f'Editing {content} for Category',
            }
        else:
            return {
                'page_title': 'Edit Page',
                'content': f'Editing {content} for {page}',
            }
        
    
    def logout_view(request):
        logout(request)


def member_listing_test_data():
    return {
        'quatriks_oguzhan' : {
            'Customer Name' : 'Oğuzhan Akkol',
            'Phone' : '+905422642042',
            'E-Mail' : 'oguzhan.akkol@quatriks.com',
            'Status' : 'Active',
            'Created Date' : '2024-08-03 13:17:34.927742+00',
        }
    }