from django.utils.translation import gettext_lazy as _


class QTRKS_Formatter():
    def __init__(self):
        self.comp = 'Quatriks'

    def member_formatter(self, *args, **kwargs):
        return {
            'profile_picture' : kwargs.profile_picture,
            'username' : kwargs.username,
            'firstname' : kwargs.firstname,
            'middlename' : kwargs.middlename,
            'lastname' : kwargs.lastname,
            'idtax_number' : kwargs.idtax_number,
            'phone' : kwargs.phone,
            'email' : kwargs.email,
            'gender' : kwargs.gender,
            'birthdate' : kwargs.birthdate,
            'ip_address' : kwargs.ip_address,
            'is_active' : kwargs.is_active,
        }
    
    def company_formatter(self, *args, **kwargs):
        return {
            'name' : kwargs.name,
            'slug' : kwargs.slug,
            'valid_from' : kwargs.valid_from,
            'valid_until' : kwargs.valid_until,
            'is_active' : kwargs.is_active,
        }
    
    def product_formatter(self, *args, **kwargs):
        return {
            'name' : kwargs.name,
            'web_name' : kwargs.web_name,
            'slug' : kwargs.slug,
            'type' : kwargs.type,
            'category' : kwargs.category,
            'is_set' : kwargs.is_set,
            'is_selectable' : kwargs.is_selectable,
            'is_active' : kwargs.is_active,
        }