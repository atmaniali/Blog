from django.forms import ModelForm
from django import forms
from .models import *
from django.forms.widgets import NumberInput
# from .widgets import BootstrapDateTimePickerInput
class PostForm(ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Title'})
    )
    text = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Post
        fields = '__all__'

class UserForm(ModelForm):

    first_name = forms.CharField(
        widget=forms.TextInput(attrs = {'placeholder' : 'First Name'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs = {'placeholder' : 'Last Name'})
    )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(ModelForm):
    bio = forms.CharField(
        widget= forms.Textarea(attrs={'rows':3})
    )
    location = forms.CharField(
        widget=forms.TextInput(attrs = {'placeholder' : 'Location'})
    )
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    class Meta:
        model = Profile
        fields = ('bio','location','birth_date','avatar')        