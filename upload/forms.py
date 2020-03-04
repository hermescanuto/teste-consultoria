from django import forms
from .models import Document


class DocumentForm(forms.Form):
    file = forms.FileField()

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs['style'] = 'custom-file-input'
        self.fields['file'].widget.attrs['aria-describedby'] = 'inputGroupFileAddon01'

