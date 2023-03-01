from django import forms
from .models import Profile_User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile_User
        fields = [
            'fname',
            'lname',
            'technology',
            'email',
            'display_picture'
        ]
