from pybird.models import BaseNamed
from locations.models import Zone
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save


class Author(models.Model):
    user = models.OneToOneField(User)
    equipment = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.user.username


def create_author(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(user=instance)


post_save.connect(create_author, sender=User)


class Brand(BaseNamed):
    web = models.URLField(blank=True, null=True)


class Camera(BaseNamed):
    brand = models.ForeignKey(Brand)
    reflex = models.BooleanField()
    digital = models.BooleanField()


class Lens(BaseNamed):
    brand = models.ForeignKey(Brand)
    flength_min = models.IntegerField(
            validators=[MinValueValidator(1), MaxValueValidator(1000)])
    flength_max = models.IntegerField(
            validators=[MinValueValidator(1), MaxValueValidator(1000)])
    aperture_min = models.FloatField(
            validators=[MinValueValidator(1), MaxValueValidator(1000)])
    aperture_max = models.FloatField(
            validators=[MinValueValidator(1), MaxValueValidator(1000)])
    macro = models.BooleanField(default=False)

    def clean(self):
        mina, maxa = self.aperture_min, self.aperture_max
        if mina > maxa:
            raise ValidationError(
                    'Max Aperture ' + str(maxa) +
                    ' lower than Min Aperture ' + str(mina)
            )
        minf, maxf = self.flength_min, self.flength_max
        if minf > maxf:
            raise ValidationError(
                    'Max Focal ' + str(maxa) +
                    ' lower than Min Focal ' + str(mina)
            )


class Media(BaseNamed):
    digital = models.BooleanField()
    brand = models.ForeignKey(Brand)


class Roll(BaseNamed):
    date = models.DateField()
    media = models.ForeignKey(Media)
    iso = models.IntegerField(
            blank=True,
            null=True,
            validators=[MinValueValidator(1), MaxValueValidator(1000)]
    )


class Photo(BaseNamed):
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    date = models.DateTimeField()
    author = models.ForeignKey(Author,  blank=True, null=True)
    number = models.IntegerField()
    roll = models.ForeignKey(Roll)
    camera = models.ForeignKey(Camera)
    lens = models.ForeignKey(Lens, blank=True, null=True)
    focal = models.IntegerField()
    aperture = models.FloatField()
    speed = models.FloatField()
    iso = models.IntegerField(blank=True, null=True)
    position = models.PointField(geography=True, blank=True, null=True)
    zone = models.ForeignKey(Zone, blank=True, null=True)

    def clean(self):
        if self.position and self.zone:
            pass
