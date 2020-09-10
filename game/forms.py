from django import forms
from .models import Game


class GameForm(forms.Form):
    number = forms.IntegerField(required=True)


class GameCreateForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ['number']
