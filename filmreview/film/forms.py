from django import forms
from film.models import Movie

class MovieForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Movie Title")
    director = forms.CharField(max_length=128, help_text="Movie Director", required=False)
    release_date = forms.DateField(required=False, help_text="Release Date")
    cover_art = forms.ImageField(required=False, help_text="Movie Poster Upload")
    
    class Meta:
        model= Movie
        fields = ['name', 'director', 'release_date', 'cover_art']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'director': forms.TextInput(attrs={'class':'form-control'}),
            'release_date': forms.DateInput(attrs={'class':'form-control'}),
            'cover_art': forms.FileInput(attrs={'class':'form-control'}),
        }