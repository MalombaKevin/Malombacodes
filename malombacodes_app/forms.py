from django import forms
from .models import malombacodes_Post, malombacodes_Profile

class Profile_Form(forms.ModelForm):
    class Meta:
        model=malombacodes_Profile
        fields=['name','bio','profile_photo','email','github','linkedin','twitter','phone_number']
        exclude=['user']

class Post_Form(forms.ModelForm):
    class Meta:
        model=malombacodes_Post
        fields=['post_title','post_description','post_url']
        exclude=['user']