from django.contrib.postgres.fields import HStoreField, ArrayField
from django.contrib.gis.db import models

# Create your models here.
class Reactor(models.Model):
    name=models.CharField(max_length=50)
    latitude=models.FloatField()
    longitude=models.FloatField()
    plant=HStoreField(ArrayField(models.FloatField(), size=2))

    location=models.PointField(srid=4326, verbose_name='center')

    class Meta:
        managed = True

    def __str__(self):
        return self.name

    def 

class WindAPI(models.Model):
    
    KNOTS = '0'
    MPH = '1'
    KM_HOUR = '2'
    METERS_SEC = '3'
    SPEED_CHOICES  = [
        (KNOTS, 'kt'),
        (MPH, 'mph'),
        (KM_HOUR, 'km/h'),
        (METERS_SEC, 'm/s'),
    ]

    FT = '0'
    METERS = '1'
    HEIGHT_CHOICES = [
        (FT, 'x100ft'),
        (METERS, 'x100m'),
    ]

    _api_uri = models.TextField(
        default='http://forecast.weather.gov/MapClick.php?',
        editable=False,
        )
    _api_json = HStoreField()
    
    w3u = models.CharField(
        max_length =10,
        choices=SPEED_CHOICES,
        default=METERS_SEC,
        editable=False,
    )
    w13u= models.CharField(
        max_length =10,
        choices=HEIGHT_CHOICES,
        default=METERS,
        editable=False,
    )
    w16u = models.CharField(
        max_length =10,
        choices=SPEED_CHOICES,
        default=METERS_SEC,
        editable=False,
    )
    api_hour = HStoreField()
    bearing = HStoreField()

    def __str__(self):
        return self.name

