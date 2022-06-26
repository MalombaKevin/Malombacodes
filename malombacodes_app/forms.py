from django import forms
from .models import Memes, malombacodes_Post, malombacodes_Profile

class Profile_Form(forms.ModelForm):
    class Meta:
        model=malombacodes_Profile
        fields=['name','bio','profile_photo','email','github','linkedin','twitter','phone_number']
        exclude=['user']

class Post_Form(forms.ModelForm):
    class Meta:
        model=malombacodes_Post
        fields=['post_title','post_description','notes','site_name','site_url', 'youtube_url']
        exclude=['user']

class Meme_Form(forms.ModelForm):
    class Meta:
        model=Memes
        fields=['meme_title','meme_description','meme_image']
        exclude=['user']