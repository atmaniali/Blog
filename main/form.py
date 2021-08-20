from django.forms import ModelForm
from django import forms
from .models import *
class PostForm(ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Title'})
    )
    text = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Post
        fields = '__all__'

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'        