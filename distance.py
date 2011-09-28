# -*- coding: utf-8 -*-

import math

class DistanceMixin:
    """
    Search for nearby objects

    Example:

    class Supermarket(DistanceMixin, models.Model):
        lng = models.FloatField()
        lat = models.FloatField()
        name = models.CharField(max_length=100)

    # All McDonald's 200 meters from the supermarket
    supermarket = Supermarket.objects.get(name=u"Монетка").distance(200).filter(name="McDonald's")
    """
    lng_name = 'lng'
    lat_name = 'lat'
    manager_name = 'objects'

    def distance(self, meters):
        lng = getattr(self, self.lng_name, None)
        lat = getattr(self, self.lat_name, None)
        manager = getattr(self.__class__, self.manager_name)
        if not (lng and lat):
            return manager.none()
        miles = float(meters)/1609.344
        dist_lng = miles/abs(math.cos(math.radians(lat))*69)
        lng1 = lng-dist_lng
        lng2 = lng+dist_lng
        lat1 = lat-(miles/69)
        lat2 = lat+(miles/69)
        kwargs = {'%s__gte' % self.lng_name: lng1,
                  '%s__lte' % self.lng_name: lng2,
                  '%s__gte' % self.lat_name: lat1,
                  '%s__lte' % self.lat_name: lat2
        }
        return manager.filter(**kwargs).exclude(pk=self.pk)