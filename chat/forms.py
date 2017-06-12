"""Django forms for the socialprofile application"""
from django import forms
from django.contrib.auth.models import User
from .models import PrivRoom, Room
from django.utils.html import strip_tags
import logging
from django.utils.translation import gettext_lazy as _

# pylint: disable=E1120,W0212

LOGGER = logging.getLogger(name='chat.forms')
'''

class UserForm(forms.ModelForm):
    """Form for editing the data that is part of the User model"""

    class Meta(object):
        """Configuration for the ModelForm"""
        model = User
        fields = {'username', 'first_name', 'last_name', 'email'}
'''

class PrivateRoomForm(forms.ModelForm):
    """Master form for editing the user's profile"""
    model = PrivRoom
    # label=u'Название' - for custom 'title'
    title = forms.CharField(required=True, label=u'Название', error_messages={'required': 'Введите название комнаты'})
    #members = forms.CharField()
    #members = forms.IntegerField(widget=forms.HiddenInput, required=True)
    #manually_edited = forms.BooleanField(widget=forms.HiddenInput, required=False, initial=True)
    #current_user = forms.IntegerField(widget=forms.HiddenInput, required=True)
    
    '''
    user = forms.IntegerField(widget=forms.HiddenInput, required=True)
    returnTo = forms.CharField(widget=forms.HiddenInput, required=False, initial='/')  # URI to Return to after save
    manually_edited = forms.BooleanField(widget=forms.HiddenInput, required=False, initial=True)

    avatar = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'ask-signup-avatar-input',}),
        required=False, label=u'Загрузите аватар'
    )
    '''
    '''
    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        #проверка на аватар
        
        if avatar is None:
            raise forms.ValidationError(u'Добавьте картинку')
        if 'image' not in avatar.content_type:
            raise forms.ValidationError(u'Неверный формат картинки')
        
        
        return avatar
    '''
    
    class Meta(object):
        """Configuration for the ModelForm"""
        model = PrivRoom

        fields = ['title', 'private',
                  #'members',
                  #'current_user',
                  #'manually_edited', 
                  #'description'
                  ]  # Don't let through for security reasons, user should be based on logged in user only


