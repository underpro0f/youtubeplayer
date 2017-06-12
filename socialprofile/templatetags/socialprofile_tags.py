"""Template tags for the socialprofile module"""

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.translation import ugettext as _

from django.contrib.auth.models import User

register = template.Library()

@register.simple_tag
def get_username_from_userid(user_id):
    try:
        return User.objects.get(id=user_id).username
    except User.DoesNotExist:
        return 'Unknown'
    

@register.filter
@stringfilter
def social_provider_name(provider_slug):
    """Decode name of Social Auth Provider to Friendly Name"""
    if provider_slug == 'google-oauth2':
        return _("Google")

    if provider_slug == 'twitter':
        return _("Twitter")

    if provider_slug == 'facebook':
        return _("Facebook")

    if provider_slug == 'vk-oauth2':
        return _("VKontakte")

    if provider_slug == 'odnoklassniki-oauth2':
        return _("Odnoklassniki")

