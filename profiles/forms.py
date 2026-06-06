from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    """Form for creating a new profile, including gender field."""

    class Meta:
        model = Profile
        exclude = ['user', 'completed', 'created_at']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'bio': forms.Textarea(attrs={'rows': 4})
        }

class ProfileEditForm(forms.ModelForm):
    """Form for editing existing profiles. Gender is locked after initial creation."""

    class Meta:
        model = Profile
        exclude = ['user', 'completed', 'created_at', 'gender']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'bio': forms.Textarea(attrs={'rows': 4})
        }