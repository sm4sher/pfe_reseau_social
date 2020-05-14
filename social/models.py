from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	pass

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	#bio, photo....

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.CharField(max_length=500)
	created = models.DateTimeField()
