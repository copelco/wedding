from django import forms

from rsvp.models import Guest


class GuestForm(forms.ModelForm):

    class Meta(object):
        model = Guest
