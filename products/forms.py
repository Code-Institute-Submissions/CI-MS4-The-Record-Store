from django import forms
from .models import Product, Artist, Genre, Label, Colour, Format, Tag


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        artists = Artist.objects.all()
        friendly_names = ([(artist.id, artist.get_friendly_name())
                           for artist in artists])
        self.fields['artist'].choices = friendly_names
        self.fields['artist'].widget.attrs['class'] = (
            'single-dynamic form-control')

        genres = Genre.objects.all()
        friendly_names = ([(genre.id, genre.get_friendly_name())
                           for genre in genres])
        self.fields['genre'].choices = friendly_names
        self.fields['genre'].widget.attrs['class'] = (
            'single-dynamic form-control')

        labels = Label.objects.all()
        friendly_names = ([(label.id, label.get_friendly_name())
                           for label in labels])
        self.fields['label'].choices = friendly_names
        self.fields['label'].widget.attrs['class'] = (
            'single-dynamic form-control')

        colours = Colour.objects.all()
        friendly_names = ([(colour.id, colour.get_friendly_name())
                           for colour in colours])
        self.fields['colour'].choices = friendly_names
        self.fields['colour'].widget.attrs['class'] = (
            'single-dynamic form-control')

        formats = Format.objects.all()
        friendly_names = ([(_format.id, _format.get_friendly_name())
                           for _format in formats])
        self.fields['format'].choices = friendly_names
        self.fields['format'].widget.attrs['class'] = (
            'single-dynamic form-control')

        tags = Tag.objects.all()
        friendly_names = ([(tag.id, tag.get_friendly_name()) for tag in tags])
        self.fields['tags'].choices = friendly_names
        self.fields['tags'].widget.attrs['class'] = (
            'single-dynamic form-control')
        self.fields['tags'].widget.attrs['multiple'] = 'multiple'

        self.fields['tracklist'].widget = forms.HiddenInput()
        self.fields['sku'].widget = forms.HiddenInput()
