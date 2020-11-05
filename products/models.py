from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator
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


class Product(models.Model):
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
    name = models.CharField(max_length=254, default='')
    release_year = models.PositiveIntegerField(validators=[MaxValueValidator(9999)], default=0000)
    tracklist = ArrayField(models.CharField(
        max_length=200, blank=True), default=list)
    description = models.TextField(default='')
    tags = models.ManyToManyField(Tag)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
