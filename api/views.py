# Create your views here.
from rest_framework import viewsets
from logging import getLogger
from rest_framework.response import Response
import re
from ipv4.serializer import *

logger = getLogger(__name__)


class IpAddrV4ViewSet(viewsets.ModelViewSet):
    # queryset = TsWork.objects.order_by('date').reverse()[:5]
    queryset = IpAddrV4.objects.all()
    serializer_class = IpAddrV4Serializer
    filter_fields = ('id', 'category', 'region', 'count')


class IpAddrV4CountryViewSet(viewsets.ViewSet):

    def retrieve(self, request, pk=None):

        ipaddr_v4_pattern = re.compile(r'[0-9]{8,10}')

        if not ipaddr_v4_pattern.fullmatch(pk):
            print("invalid parameter format(pk): {}".format(pk))
            return

        # b_10d_addr, e_10d_addr = self._get_pk_ranged(pk)
        pk_10d_addr = self._get_pk_10d(pk)

        # ipaddrv4_ranged = IpAddrV4.objects.filter(address__range=[b_10d_addr, e_10d_addr])
        # queryset = ipaddrv4_ranged.filter(address__lt=pk_10d_addr).filter(address_until__gt=pk_10d_addr)[:1]
        queryset = IpAddrV4.objects.filter(address__lt=pk_10d_addr).filter(address_until__gt=pk_10d_addr)[:1]

        # if queryset:
        #    logger.debug(sqlparse.format(str(queryset.query), reindent=True))

        serializer = IpAddrV4SerializerForAPI(queryset, many=True)
        return Response(serializer.data)

    @staticmethod
    def _get_pk_ranged(pk):
        if len(pk) == 8:
            return "00" + pk[0:2] + "000000", "00" + pk[0:2] + "999999"
        elif len(pk) == 9:
            return "0" + pk[0:3] + "000000", "0" + pk[0:3] + "999999"
        elif len(pk) == 10:
            return pk[0:4] + "000000", pk[0:4] + "999999"

    @staticmethod
    def _get_pk_10d(pk):
        if len(pk) == 8:
            return "00" + pk
        elif len(pk) == 9:
            return "0" + pk
        elif len(pk) == 10:
            return pk
