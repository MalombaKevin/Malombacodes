from django.db import models
from django.contrib.auth.models import User

class malombacodes_Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    user= models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile_photo = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return self.name
    
    def malombacode_save(self):
        self.save()

class malombacodes_Post (models.Model): #introduce category field
    post_title=models.CharField(max_length=100)
    post_description=models.TextField(max_length=100, blank=True)
    notes = models.TextField(max_length=500, blank=True)
    site_name=models.CharField(max_length=100,blank=True)
    site_url  = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.post_title
    
    def malombacode_save(self):
        self.save()

class Memes(models.Model):
    meme_title = models.CharField(max_length=100)
    meme_description=models.TextField(max_length=100 )
    meme_image = models.ImageField(upload_to='memes/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.meme_title

    def malombacode_save(self):
        self.save()