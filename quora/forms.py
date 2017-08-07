from django import forms
from .models import query
from django.utils.translation import ugettext_lazy as _


class queryForm(forms.ModelForm):

    class Meta:

        model = query
        fields = ('ques',)
        labels = {
            'ques': _(''),
        }
