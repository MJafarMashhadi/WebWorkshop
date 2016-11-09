from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

from user_manager.models import Member


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        password_field = self.fields['password']
        username_field = self.fields['username']

        username_field.widget.attrs = {'class': 'inputA'}
        username_field.label = ''

        password_field.widget.attrs = {'class': 'inputA'}
        password_field.label = ''


class RegisterForm(UserCreationForm):

    def clean_phone(self):
        phone_number = self.cleaned_data['phone']
        if len(phone_number) == 0:
            raise ValidationError('Phone number is required')

        if phone_number[0] != '0':
            raise ValidationError('Phone number should begin with a zero')

        return phone_number

    class Meta:
        model = Member
        fields = ['username', 'phone', 'profile_picture', 'email']
        help_texts = {
            'password': 'لطفا گذرواژهٔ امنی انتخاب کنید',
            'bio': 'شرح حال کوتاهی از خود بنویسید',
        }
        labels = {
            'phone': 'شماره همراه',
        }
