from django.contrib import admin
from .models import Product, Artist, Label, Colour, Format, Genre

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'artist',
        'label',
        'colour',
        'format',
        'release_year',
        'price',
        'rating',
        'image',
        'tracklist',
    )

    ordering = ('sku',)


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
class LabelAdmin(admin.ModelAdmin):
    list_display = (
    'friendly_name',
    'name',
)

class ColourAdmin(admin.ModelAdmin):
    list_display = (
    'friendly_name',
    'name',
)

class FormatAdmin(admin.ModelAdmin):
    list_display = (
    'friendly_name',
    'name',
)


admin.site.register(Product, ProductAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(Colour, ColourAdmin)
admin.site.register(Format, FormatAdmin)
