from django import forms
from .models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image_url', 'thumb_url', )



class SearchForm(forms.Form):
    search = forms.CharField()