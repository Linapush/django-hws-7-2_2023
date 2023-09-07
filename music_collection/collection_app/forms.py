from django.forms import ChoiceField, Form, DecimalField, CharField, EmailField
from .config import DECIMAL_MAX_DIGITS, DECIMAL_PLACES, CF_DEFAULT, EMAIL_LENGTH
from django.contrib.auth import forms as auth_forms, models as auth_models
from django import forms
from .models import Artists
from django.core.exceptions import ValidationError
from datetime import timezone


class AddFundsForm(Form):
    money = DecimalField(
        label='Amount',
        max_digits=DECIMAL_MAX_DIGITS,
        decimal_places=DECIMAL_PLACES,
    )


class RegistrationForm(auth_forms.UserCreationForm):
    first_name = CharField(max_length=CF_DEFAULT, required=True)
    last_name = CharField(max_length=CF_DEFAULT, required=True)
    email = EmailField(max_length=EMAIL_LENGTH, required=True)

    class Meta:
        model = auth_models.User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

class LoginForm(auth_forms.UserCreationForm):
    username = CharField(max_length=CF_DEFAULT, required=True)
    password = CharField(max_length=CF_DEFAULT, required=True)

    class Meta:
        model = auth_models.User
        fields = ['username', 'password']

class SubscriptionForm(forms.Form):
    username = forms.CharField(label='ФИО')
    email = forms.EmailField(label='Email')
    amount = forms.IntegerField(label='Сумма подписки')

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount is not None and amount < 499:
            raise forms.ValidationError("Enter a value equal or greater 499")
        return amount
    
from django.contrib.auth.models import User

class TrackForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
    def clean(self):        
        cleaned_data = super().clean()        
        if self.user and self.user.subscription_expiry <= timezone.now():
            raise forms.ValidationError('У вас нет активной подписки')        
        return cleaned_data
    
from datetime import timedelta  
class SubscriptionForm(forms.Form):
    username = forms.CharField(label='ФИО')
    email = forms.EmailField(label='Email')
    amount = forms.IntegerField(label='Сумма подписки')


    def has_active_subscription(user):
        # Assuming you have a Subscription model associated with the user
        # and it has a field subscription_expiry representing the expiry date of the subscription

        subscription = user.subscription

        if subscription is None:
            return False
        
        # Assuming you have a field in your Subscription model indicating the status of the subscription
        # e.g. active or inactive
        if subscription.status != 'active':
            return False

        # Assuming you have a field subscription_expiry representing the expiry date of the subscription
        # and the expiry date is stored as a DateTimeField

        current_datetime = timezone.now()

        if subscription.subscription_expiry > current_datetime:
            return True

        return False

    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get('user')
        tracks = cleaned_data.get('tracks')

        if user and tracks is not None and tracks > 10 and not SubscriptionForm.has_active_subscription(user):
            self.add_error(None, 'Для добавления более 10 треков необходима активная подписка')

        return cleaned_data