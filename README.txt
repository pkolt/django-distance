Returns the objects in the vicinity

Example:

    class Supermarket(DistanceMixin, models.Model):
        lng = models.FloatField()
        lat = models.FloatField()
        name = models.CharField(max_length=100)

    # All McDonald's 200 meters from the supermarket
    supermarket = Supermarket.objects.get(name=u"Монетка").distance(200).filter(name="McDonald's")