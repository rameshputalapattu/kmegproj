from django import forms
from .models import KmegImage


class FileUpload(forms.ModelForm):
    class Meta:
        model = KmegImage
        fields = ('jpeg_picture', 'title', 'colors')
