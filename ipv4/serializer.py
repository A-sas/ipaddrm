from rest_framework import serializers
from .models import IpAddrV4


class IpAddrV4Serializer(serializers.ModelSerializer):
    class Meta:
        model = IpAddrV4
        fields = ('id', 'address', 'address_until', 'country', 'region', 'category', 'count', )


class IpAddrV4SerializerForAPI(serializers.ModelSerializer):
    class Meta:
        model = IpAddrV4
        fields = ('country', )
