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

    def __str__(self):
        return self.name
    
    def malombacode_save(self):
        self.save()

class malombacodes_Post (models.Model): #introduce category field
    post_title=models.CharField(max_length=100)
    post_description=models.TextField()
    post_url = models.URLField(blank=True)

    def __str__(self):
        return self.post_title
    
    def malombacode_save(self):
        self.save()