from django import forms
from .models import Response_message

class signUp(forms.Form):
    ROLES_CHOICES = (
        ('one', '1'),
        ('two', '2'),
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'Passwordinput', 'placeholder': 'First Name'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'Passwordinput', 'placeholder': 'Last Name'}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'Passwordinput', 'placeholder': 'User Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'Passwordinput', 'placeholder': 'Email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'Passwordinput', 'placeholder': 'Password'}))
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'Passwordinput', 'placeholder': 'Confirm Password'}))
    role = forms.CharField(widget=forms.Select(attrs={'class': 'Passwordinput'},choices=ROLES_CHOICES))

class loginform(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'Passwordinput', 'placeholder': 'Email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'Passwordinput', 'placeholder': 'Password'}))

class message_date_filterform(forms.Form):
    start_date = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control m-input border-dark validateInput','id':'start_date', 'placeholder': 'start date',}))
    end_date = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control m-input border-dark validateInput','id':'end_date', 'placeholder': 'end date', })
        )

class Response_messages_form(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'id':'title','class': 'form-control m-input border-dark validateInput', 'placeholder': 'title'}))
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={'id':'description','class': 'form-control m-input border-dark validateInput', 'placeholder': 'desciption'}))
    message = forms.CharField(
        widget=forms.TextInput(
            attrs={'id':'message','class': 'form-control m-input border-dark validateInput', 'placeholder': 'message'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'id':'image','class': 'form-control m-input border-dark validateInput'}), required=True)

    class Meta:
        model = Response_message
        fields = ('title', 'description', 'message', 'image')