from django import template
import re, phonenumbers

register = template.Library()

### pip install phonenumbers  || for be able to manipulate numbers

@register.filter(name='secret_phone')
def secret_phone(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        national_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        
        parts = national_number.split()
        
        for i in range(1, len(parts) - 1):
            parts[i] = '*' * len(parts[i])
        
        censored_number = ' '.join(parts)
        
        return f"{censored_number}"
    
    except phonenumbers.phonenumberutil.NumberParseException:

        return phone_number