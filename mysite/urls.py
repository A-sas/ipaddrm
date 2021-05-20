"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import views
# from api.views import IpAddrV4CountryViewSet
from api.views import *


#
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


#
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r'ipaddrv4', IpAddrV4ViewSet)
# router.register(r'ipv4country', IpAddrV4CountryViewSet, basename='ipv4country-detail')
router.register(r'ipaddrv4country', IpAddrV4CountryViewSet, basename='ipaddrv4country')
# router.register(r'ipv4country', IpAddrV4CountryViewSet, basename='ipv4')
# router.register(r'users', UserViewSet)

urlpatterns = [
    # url('^ipv4/', include('ipv4.urls', namespace='ipv4')),
    url('^admin/', admin.site.urls),
    url('^api/', include(router.urls)),
    url('^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^api-token-auth/', views.obtain_auth_token),
]