from django import forms
from .models import Product, Artist, Genre, Label, Colour, Format, Tag



# search_fields = [
    #     "name__icontains",
    #     "friendly_name__icontains",
    # ]
    # def label_from_instance(obj):
    #     return str(obj.title).upper()


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = 'artist','label','genre', 'format','colour',

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        artist = Artist.objects.all()
        friendly_names = [(a.id, a.get_friendly_name()) for a in artist]
        self.fields['artist'].choices = friendly_names
        self.fields['artist'].widget.attrs['class'] = 'single-dynamic'

        genre = Genre.objects.all()
        friendly_names = [(g.id, g.get_friendly_name()) for g in genre]
        self.fields['genre'].choices = friendly_names
        self.fields['genre'].widget.attrs['class'] = 'single-dynamic'

        label = Label.objects.all()
        friendly_names = [(l.id, l.get_friendly_name()) for l in label]
        self.fields['label'].choices = friendly_names
        self.fields['label'].widget.attrs['class'] = 'single-dynamic'

        colour = Colour.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in colour]
        self.fields['colour'].choices = friendly_names
        self.fields['colour'].widget.attrs['class'] = 'single-dynamic'

        format = Format.objects.all()
        friendly_names = [(f.id, f.get_friendly_name()) for f in format]
        self.fields['format'].choices = friendly_names
        self.fields['format'].widget.attrs['class'] = 'single-dynamic'

        # tag = Tag.objects.all()
        # friendly_names = [(t.id, t.get_friendly_name()) for t in tag]
        # self.fields['tags'].choices = friendly_names
        # self.fields['tags'].widget.attrs['class'] = 'single-dynamic'
        # self.fields['tags'].widget.attrs['multiple'] = 'multiple123'
        
        