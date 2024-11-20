from django.views.generic import TemplateView
from django.conf import settings
from _keenthemes.__init__ import KTLayout, auth_templates
from _keenthemes.libs.theme import KTTheme
from django.conf import settings
from django.urls import resolve

auth_js = {
    'signin' : 'js/custom/authentication/sign-in/general.js',
    'signup' : 'js/custom/authentication/sign-up/general.js',
    'two-factor' : 'js/custom/authentication/sign-in/two-factor.js',
    'reset-password' : 'js/custom/authentication/reset-password/reset-password.js',
    'new-password' : 'js/custom/authentication/reset-password/new-password.js',
}


class AuthView(TemplateView):
    template_name = 'pages/auth/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = KTLayout.init(context)

        url_name = resolve(self.request.path_info).url_name

        KTTheme.addJavascriptFile(auth_js[f'{url_name}'])

        context.update({
            'layout': KTTheme.setLayout(f'auth/{auth_templates[settings.QTRKS_COMPANY_DEFAULTS["auth_template"]]}.html', context),
        })

        if url_name == 'two-factor':
            context.update({
                'auth_member_phone' : '+905355554433',
            })

        return context
