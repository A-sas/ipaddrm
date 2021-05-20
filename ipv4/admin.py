from django.contrib import admin

# Register your models here.
from .models import IpAddrV4, Country

""" Django 管理サイト名変更 """
# admin.site.site_header = "Krasavkana"


@admin.register(IpAddrV4)
class IpAddrV4Admin(admin.ModelAdmin):
    list_display = ('id', 'address', 'address_until', 'country', 'region', 'category', 'count')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'name',)
