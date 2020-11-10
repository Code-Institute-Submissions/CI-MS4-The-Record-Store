from django import forms
from .models import Product, Artist, Genre, Label, Colour, Format, Tag

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        artist = Artist.objects.all()
        friendly_names = [(a.id, a.get_friendly_name()) for a in artist]
        self.fields['artist'].choices = friendly_names
        self.fields['artist'].widget.attrs['class'] = 'single-dynamic form-control'

        genre = Genre.objects.all()
        friendly_names = [(g.id, g.get_friendly_name()) for g in genre]
        self.fields['genre'].choices = friendly_names
        self.fields['genre'].widget.attrs['class'] = 'single-dynamic form-control'

        label = Label.objects.all()
        friendly_names = [(l.id, l.get_friendly_name()) for l in label]
        self.fields['label'].choices = friendly_names
        self.fields['label'].widget.attrs['class'] = 'single-dynamic form-control'

        colour = Colour.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in colour]
        self.fields['colour'].choices = friendly_names
        self.fields['colour'].widget.attrs['class'] = 'single-dynamic form-control'

        format = Format.objects.all()
        friendly_names = [(f.id, f.get_friendly_name()) for f in format]
        self.fields['format'].choices = friendly_names
        self.fields['format'].widget.attrs['class'] = 'single-dynamic form-control'

        tag = Tag.objects.all()
        friendly_names = [(t.id, t.get_friendly_name()) for t in tag]
        self.fields['tags'].choices = friendly_names
        self.fields['tags'].widget.attrs['class'] = 'single-dynamic form-control'
        self.fields['tags'].widget.attrs['multiple'] = 'multiple'

        self.fields['tracklist'].widget = forms.HiddenInput()
        self.fields['sku'].widget = forms.HiddenInput()
        
        