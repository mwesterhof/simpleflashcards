from django import forms


class CardForm(forms.Form):
    card_id = forms.IntegerField()
    answer = forms.CharField(required=False)
