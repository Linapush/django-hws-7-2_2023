from django.forms import ChoiceField, Form, DecimalField, CharField, EmailField
from .config import DECIMAL_MAX_DIGITS, DECIMAL_PLACES, CF_DEFAULT, EMAIL_LENGTH
from django.contrib.auth import forms as auth_forms, models as auth_models
from django import forms
from .models import Artists, Tracks


class AddFundsForm(Form):
    money = DecimalField(
        label='Amount',
        max_digits=DECIMAL_MAX_DIGITS,
        decimal_places=DECIMAL_PLACES,
    )
    def validate(self):
        # self.money = self.cleaned_data.get('money')
        if self.money is not None and self.money <= 0:
            raise forms.ValidationError("Enter a value equal or greater than 0")
        return self.money


class RegistrationForm(auth_forms.UserCreationForm):
    first_name = CharField(max_length=CF_DEFAULT, required=True)
    last_name = CharField(max_length=CF_DEFAULT, required=True)
    email = EmailField(max_length=EMAIL_LENGTH, required=True)

    class Meta:
        model = auth_models.User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

class ArtistPostForm(Form):
    class Meta:
        model = Artists
        fields = ('name', 'birth_date', 'country', 'education')

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
        'birth_date': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
        'country': forms.Select(attrs={'class': 'form-control'}),
        'education': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
    }

class SubscriptionForm(forms.Form):
    username = forms.CharField(label='ФИО')
    email = forms.EmailField(label='Email')

class AddTracksForm(forms.Form):
    tracks = forms.ModelMultipleChoiceField(queryset=Tracks.objects.all(), widget=forms.CheckboxSelectMultiple())

