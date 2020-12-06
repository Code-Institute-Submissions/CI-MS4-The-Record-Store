from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

# Create your models here.


class Genre(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Artist(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Label(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Colour(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Format(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Tag(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    artist = models.ForeignKey(
        'Artist', null=True, blank=True, on_delete=models.SET_NULL)
    label = models.ForeignKey(
        'Label', null=True, blank=True, on_delete=models.SET_NULL)
    genre = models.ForeignKey(
        'Genre', null=True, blank=True, on_delete=models.SET_NULL)
    format = models.ForeignKey(
        'Format', null=True, blank=True, on_delete=models.SET_NULL)
    colour = models.ForeignKey(
        'Colour', null=True, blank=True, on_delete=models.SET_NULL)
    release_year = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(1930),
                                            max_value_current_year])
    price = models.DecimalField(max_digits=5, decimal_places=2, default=00.00)
    tags = models.ManyToManyField(Tag, blank=True)
    description = models.TextField(default='')
    image = models.ImageField(null=True, blank=True,)
    tracklist = ArrayField(models.CharField(
        max_length=254, null=True, blank=True), default=list, null=True,
        blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)

    def save(self, *args, **kwargs):
        sku = ("L"+str(self.label.pk) + '/'+"A"+str(self.artist.pk) +
               '/'+str(self.name)[0:3]+'/'+str(self.colour)[0:3] +
               '/'+str(self.format)[0:5])

        sku = sku.upper()
        self.sku = sku
        super().save(*args, **kwargs)

    def __str__(self):
        return self.artist.friendly_name + " : " + self.name
