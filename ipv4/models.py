# Create your models here.
from django.core import validators
from django.db import models
from datetime import datetime


# Create your models here.
class IpAddrV4(models.Model):
    address = models.CharField(max_length=10, default=None, null=True, blank=True,
                               validators=[validators.RegexValidator(
                                   regex=u'^[0-9]+$',
                                   message='input digits only',
                               )]
                               )
    address_until = models.CharField(max_length=10, default=None, null=True,
                                     validators=[validators.RegexValidator(
                                     regex=u'^[0-9]+$',
                                     message='input digits only',
                                     )]
                                     )
    country = models.CharField(max_length=2, default=None, null=True, blank=True,)
    region = models.CharField(max_length=63, default=None, null=True, blank=True,)
    category = models.CharField(max_length=63, default=None, null=True, blank=True,)
    count = models.IntegerField(blank=True, null=True, default=0,)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'ipaddrv4'
        verbose_name_plural = 'ipaddrv4'


class Country(models.Model):
    country = models.CharField(max_length=2, default=None, null=True,)
    name = models.CharField(max_length=63, default=None, null=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'
