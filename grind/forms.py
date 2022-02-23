from django import forms
from profiles.models import ActiveCharacter


class HomeCharmForm(forms.ModelForm):
    """
    To update stats for a character
    """
    class Meta:
        """ Specify model and fields"""
        model = ActiveCharacter
        fields = ['charm']


class SleepForm(forms.ModelForm):
    """
    To update stats for a character
    """
    class Meta:
        """ Specify model and fields"""
        model = ActiveCharacter
        fields = ['energy']
