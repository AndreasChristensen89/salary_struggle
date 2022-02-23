from django import forms
from profiles.models import ActiveCharacter


class HomeCharmForm(forms.ModelForm):
    """
    To update charm for a character
    """
    class Meta:
        """ Specify model and fields"""
        model = ActiveCharacter
        fields = ['charm']


class SleepForm(forms.ModelForm):
    """
    To recharge energy for a character
    """
    class Meta:
        """ Specify model and fields"""
        model = ActiveCharacter
        fields = ['energy']


class HomeIntellectForm(forms.ModelForm):
    """
    To update coding for a character
    """
    class Meta:
        """ Specify model and fields"""
        model = ActiveCharacter
        fields = ['intellect']
