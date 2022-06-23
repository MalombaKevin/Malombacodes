from django import forms
from .models import malombacodes_Profile

class Profile_Form(forms.ModelForm):
    class Meta:
        model=malombacodes_Profile
        fields=['name','bio','email','github','linkedin','twitter','phone_number']
        exclude=['user']