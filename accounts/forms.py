from django import forms
from .models import user

class loginform(forms.ModelForm):
    
     class Meta:
        model = user
        fields = ('username','password') 