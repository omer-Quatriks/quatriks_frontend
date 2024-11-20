from django.utils.translation import gettext_lazy as _
from django.db import models

from django.contrib.auth.models import User

######################### MEMBERS #########################
class Member(models.Model):
    user = models.OneToOneField(User, verbose_name=_("Kullanıcı"), on_delete=models.CASCADE, related_name="member_user")
    company = models.ForeignKey("Company", verbose_name=_("Şirket"), on_delete=models.CASCADE, related_name="company_members")

    username = models.CharField(verbose_name=_("Kullanıcı Adı"), max_length=1000, null=True, blank=True)
    firstname = models.CharField(verbose_name=_("Üye Adı"), max_length=1000)
    middlename = models.CharField(verbose_name=_("Üye Orta Adı"), max_length=1000, null=True, blank=True)
    lastname = models.CharField(verbose_name=_("Üye Soyadı"), max_length=1000)
    profile_picture = models.ImageField(verbose_name=_("Profil Resmi"), upload_to="members/profile_pictures", null=True, blank=True)

    member_type = models.ManyToManyField("MemberTypes", verbose_name=_("Üye Tipleri"), related_name="member_user_types", blank=True, help_text=_("Üye ile ilişkilendirilmiş üye tipleri"))
    member_role = models.ManyToManyField("MemberRoles", verbose_name=_("Üye Rolleri"), related_name="member_user_roles", blank=True, help_text=_("Üye ile ilişkilendirilmiş üye rolleri"))

    idtax_number = models.CharField(verbose_name=_("TC/Vergi No"), max_length=50, null=True, blank=True)
    tax_office = models.CharField(verbose_name=_("Vergi Dairesi"), max_length=50, null=True, blank=True)

    phone = models.CharField(verbose_name=_("Telefon"), max_length=50, null=True, blank=True)
    email = models.EmailField(verbose_name=_("E-Posta"), max_length=1000, null=True, blank=True)

    gender = models.CharField(verbose_name=_("Cinsiyet"), max_length=50, null=True, blank=True)
    birthdate = models.DateField(verbose_name=_("Doğum Tarihi"), null=True, blank=True)
    weight = models.DecimalField(verbose_name=_("Ağırlık"), max_digits=10, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(verbose_name=_("Boy"), max_digits=10, decimal_places=2, null=True, blank=True)

    ip_address = models.GenericIPAddressField(verbose_name=_("IP Adresi"), null=True, blank=True)
    member_tags = models.ManyToManyField("MemberTags", verbose_name=_("Kullanıcı Etiketleri"), related_name="member_user_tags", blank=True, help_text=_("Üye ile ilişkilendirilmiş kullanıcı etiketleri"))

    season = models.CharField(verbose_name=_("Sezon"), max_length=50, null=True, blank=True)
    registration_state = models.CharField(verbose_name=_("Kayıt Durumu"), max_length=50, null=True, blank=True)
    is_active = models.BooleanField(verbose_name=_("Aktif"), default=True)

    description = models.TextField(verbose_name=_("Açıklama"), null=True, blank=True)

    created_at = models.DateTimeField(verbose_name=_("Oluşturulma Tarihi"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("Güncellenme Tarihi"), auto_now=True)
    last_login = models.DateTimeField(verbose_name=_("Son Giriş"), null=True, blank=True)

    additional_data = models.JSONField(verbose_name=_("Ek Veri"), null=True, blank=True)

    def __str__(self):
        return f"{self.username}"
    
    class Meta:
        verbose_name = _("Üye")
        verbose_name_plural = _("Üyeler")

class MemberAddress(models.Model):
    member = models.ForeignKey("Member", on_delete=models.CASCADE, verbose_name=_("Üye"), related_name="member_addresses")
    type = models.CharField(max_length=100, choices=[('Delivery', 'Teslimat'), ('Invoice', 'Fatura')], default='Delivery', verbose_name=_("Adres Tipi"))
    
    recipient_name = models.CharField(max_length=255, verbose_name=_("Alıcı Adı"))
    recipient_lastname = models.CharField(max_length=255, verbose_name=_("Alıcı Soyadı"))

    country = models.CharField(max_length=100, default="Türkiye", verbose_name=_("Ülke"))
    city = models.CharField(max_length=100, verbose_name=_("Şehir"))
    district = models.CharField(max_length=100, verbose_name=_("İlçe"))
    full_address = models.TextField(verbose_name=_("Adres"))
    postal_code = models.PositiveIntegerField(null=True, blank=True, verbose_name=_("Posta Kodu"))

    phone = models.IntegerField(verbose_name=_("Telefon Numarası"))
    email = models.EmailField(verbose_name=_("E-Posta"))

    comp_name = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Şirket Adı"))
    tax_office = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Vergi Dairesi"))
    tax_no = models.PositiveBigIntegerField(null=True, blank=True, verbose_name=_("Vergi Numarası"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.recipient_name} {self.recipient_lastname}"

    class Meta:
        verbose_name = _("Üye Adresi")
        verbose_name_plural = _("Üye Adresleri")

class MemberTags(models.Model):
    company = models.ForeignKey("Company", verbose_name=_("Şirket"), on_delete=models.CASCADE, related_name="company_member_tags")

    tag = models.CharField(verbose_name=_("Etiket"), max_length=1000)
    category = models.CharField(verbose_name=_("Kategori"), max_length=1000, null=True, blank=True)
    visibility = models.BooleanField(verbose_name=_("Görünürlük"), default=True)

    is_active = models.BooleanField(verbose_name=_("Aktif"), default=True)

    created_at = models.DateTimeField(verbose_name=_("Oluşturulma Tarihi"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("Güncellenme Tarihi"), auto_now=True)

    def __str__(self):
        return f"{self.tag}"
    
    class Meta:
        verbose_name = _("Üye Etiketi")
        verbose_name_plural = _("Üye Etiketleri")

class MemberTypes(models.Model):
    name = models.CharField(verbose_name=_("Üye Tipi"), max_length=1000)
    category = models.CharField(verbose_name=_("Kategori"), max_length=1000, null=True, blank=True)
    description = models.TextField(verbose_name=_("Açıklama"), null=True, blank=True)

    is_active = models.BooleanField(verbose_name=_("Aktif"), default=True)
    is_public = models.BooleanField(verbose_name=_("Genel"), default=True)

    created_at = models.DateTimeField(verbose_name=_("Oluşturulma Tarihi"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("Güncellenme Tarihi"), auto_now=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = _("Üye Tipi")
        verbose_name_plural = _("Üye Tipleri")

class MemberRoles(models.Model):
    name = models.CharField(verbose_name=_("Üye Rolü"), max_length=1000)
    category = models.CharField(verbose_name=_("Kategori"), max_length=1000, null=True, blank=True)
    description = models.TextField(verbose_name=_("Açıklama"), null=True, blank=True)

    is_active = models.BooleanField(verbose_name=_("Aktif"), default=True)
    is_public = models.BooleanField(verbose_name=_("Genel"), default=True)

    created_at = models.DateTimeField(verbose_name=_("Oluşturulma Tarihi"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("Güncellenme Tarihi"), auto_now=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = _("Üye Rolü")
        verbose_name_plural = _("Üye Rolleri")



######################### COMPANIES #########################

class Company(models.Model):
    name = models.CharField(verbose_name=_("Şirket Adı"), max_length=1000)
    slug = models.SlugField(verbose_name=_("Şirket Slug"), max_length=256, unique=True)
    
    parent = models.ForeignKey('self', verbose_name=_("Bağlı Olduğu Şirket"), on_delete=models.SET_NULL, null=True, blank=True, related_name='sub_companies')
    bill_comp = models.ForeignKey('self', verbose_name=_("Fatura Şirketi"), on_delete=models.SET_NULL, null=True, blank=True, related_name='bill_companies')
    manager_comp = models.ForeignKey('self', verbose_name=_("Yönetim Şirketi"), on_delete=models.SET_NULL, null=True, blank=True, related_name='manager_companies')
    supplier_comp = models.ForeignKey('self', verbose_name=_("Tedarikçi Şirket"), on_delete=models.SET_NULL, null=True, blank=True, related_name='supplier_companies')
    is_branch = models.BooleanField(verbose_name=_("Şube Mi?"), default=False)

    type = models.CharField(verbose_name=_("Şirket Tipi"), max_length=1000, null=True, blank=True)
    hierarchy = models.PositiveIntegerField(verbose_name=_("Hiyerarşi"), default=0)

    valid_from = models.DateField(verbose_name=_("Geçerlilik Başlangıç Tarihi"), null=True, blank=True)
    valid_until = models.DateField(verbose_name=_("Geçerlilik Bitiş Tarihi"), null=True, blank=True)
    paid_amount = models.DecimalField(verbose_name=_("Ödenen Tutar"), max_digits=10, decimal_places=2, null=True, blank=True)
    paid_currency = models.CharField(verbose_name=_("Para Birimi"), max_length=3, null=True, blank=True)
    paid_services = models.ManyToManyField("CompanyServices", verbose_name=_("Ödenen Servisler"), related_name="paid_servies", blank=True)

    member_tags = models.ManyToManyField("MemberTags", verbose_name=_("Üye Etiketleri"), related_name="company_member_tags", blank=True, help_text=_("Şirket ile ilişkilendirilmiş üye etiketleri"))

    is_active = models.BooleanField(verbose_name=_("Aktif"), default=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Oluşturulma Tarihi"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Güncellenme Tarihi"))

    def __str__(self):
        return f"{self.name}"

    def get_sub_companies(self, level=0):
        sub_companies = []
        for sub_company in self.sub_companies.all():
            sub_companies.append((sub_company, level))
            sub_companies.extend(sub_company.get_sub_companies(level=level+1))
        return sub_companies

    def get_parent_companies(self, level=0):
        parent_companies = []
        parent = self.parent
        current_level = level
        while parent is not None:
            parent_companies.append((parent, current_level))
            parent = parent.parent
            current_level += 1
        return parent_companies
    
    def list_sub_companies(self):
        def format_sub_companies(company, level=0):
            sub_companies_str = ""
            for sub_company in company.sub_companies.all():
                sub_companies_str += f"{'|--' * level} {sub_company.name}<br>"
                sub_companies_str += format_sub_companies(sub_company, level + 1)
            return sub_companies_str
        return mark_safe(format_sub_companies(self).strip())

    def list_parent_companies(self):
        parent_companies = []
        parent = self.parent
        while parent is not None:
            parent_companies.append(parent)
            parent = parent.parent
        parent_companies.reverse()
        
        parent_companies_str = ""
        level = 0
        for parent in parent_companies:
            parent_companies_str += f"{'|--' * level} {parent.name}<br>"
            level += 1
        return mark_safe(parent_companies_str.strip())
    
    list_sub_companies.short_description = _("Alt Şirketler")
    list_parent_companies.short_description = _("Üst Şirketler")

    @classmethod
    def count_sub_companies(cls, company):
        sub_companies = company.sub_companies.all()
        count = sub_companies.count()
        for sub_company in sub_companies:
            count += cls.count_sub_companies(sub_company)
        return count

    class Meta:
        verbose_name = _("Şirket")
        verbose_name_plural = _("Şirketler")

class CompanyAdditionalInfo(models.Model):
    company = models.OneToOneField("Company", on_delete=models.CASCADE, related_name="company_additional_info")
    
    tax_number = models.CharField(verbose_name=_("Vergi Numarası"), max_length=50, null=True, blank=True)
    tax_office = models.CharField(verbose_name=_("Vergi Dairesi"), max_length=50, null=True, blank=True)
    mernis_no = models.CharField(verbose_name=_("Mernis Numarası"), max_length=50, null=True, blank=True)

    country = models.CharField(verbose_name=_("Ülke"), max_length=50, null=True, blank=True, default="Türkiye")
    city = models.CharField(verbose_name=_("Şehir"), max_length=50, null=True, blank=True)
    district = models.CharField(verbose_name=_("İlçe"), max_length=50, null=True, blank=True)
    address = models.TextField(verbose_name=_("Adres"), null=True, blank=True)
    zip_code = models.CharField(verbose_name=_("Posta Kodu"), max_length=10, null=True, blank=True)

    auth_firstname = models.CharField(verbose_name=_("Yetkili Kişi Adı"), max_length=100, null=True, blank=True)
    auth_lastname = models.CharField(verbose_name=_("Yetkili Kişi Syoadı"), max_length=100, null=True, blank=True)
    auth_phone = models.CharField(verbose_name=_("Yetkili Kişi Telefon"), max_length=20, null=True, blank=True)
    auth_email = models.EmailField(verbose_name=_("Yetkili Kişi E-Posta"), null=True, blank=True)

    def __str__(self):
        return f"{self.company.name}"

    class Meta:
        verbose_name = _("Şirket Ek Bilgisi")
        verbose_name_plural = _("Şirket Ek Bilgileri")

class CompanyServices(models.Model):
    SERVICE_CHOICES = [('Ecom', 'Ecom'), ('Dashboard', 'Dashboard')]

    company = models.ForeignKey("Company", on_delete=models.CASCADE, related_name="company_services")
    name = models.CharField(max_length=500, verbose_name=_("Servis Adı"))
    service = models.CharField(verbose_name=_("Servis"), max_length=255, choices=SERVICE_CHOICES)

    valid_from = models.DateField(verbose_name=_("Geçerlilik Tarihi"), null=True, blank=True)
    valid_until = models.DateField(verbose_name=_("Bitiş Tarihi"), null=True, blank=True)
    paid_amount = models.DecimalField(verbose_name=_("Ödenen Tutar"), max_digits=10, decimal_places=2, null=True, blank=True)
    paid_currency = models.CharField(verbose_name=_("Para Birimi"), max_length=3, null=True, blank=True)

    is_active = models.BooleanField(verbose_name=_("Aktif"), default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("Şirket Servisi")
        verbose_name_plural = _("Şirket Servisleri")

class CompanyServiceDomain(models.Model):
    company = models.ForeignKey("Company", on_delete=models.CASCADE, related_name="company_service_domain")
    company_service = models.ForeignKey(CompanyServices, on_delete=models.CASCADE, related_name="company_service_domain")

    domain = models.URLField(verbose_name="Domain")
    subdomain = models.CharField(verbose_name="Subdomain", max_length=50, null=True, blank=True, default="")
    directory = models.CharField(max_length=50, verbose_name=_("Yol"), null=True, blank=True, default="")

    complete_domain = models.URLField(max_length=255, editable=False)
    complete_path = models.URLField(max_length=255, editable=False, unique=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Oluşturulma Tarihi"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Güncellenme Tarihi"))

    def save(self, *args, **kwargs):
        self.complete_domain = f"{self.subdomain}.{str(self.domain).split('//')[1]}" if self.subdomain else self.domain
        self.complete_path = f"{self.complete_domain}/{self.directory}" if self.directory else self.complete_domain
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.complete_path}"

    class Meta:
        verbose_name = _("Şirket Servis Domaini")
        verbose_name_plural = _("Şirket Servis Domainleri")