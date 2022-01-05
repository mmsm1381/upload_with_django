from django import forms
from .models import Flile


class UploadFileForm(forms.ModelForm):

    class Meta:
        model = Flile
        fields = ("name","body")

    def save(self,*args,**kwargs):
        user = kwargs.pop("user")
        size = kwargs.pop("size")
        self.instance.user = user
        self.instance.size = size
        return super().save(*args,**kwargs)