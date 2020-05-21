from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	pass

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	display_name = models.CharField(max_length=50)
	bio = models.CharField(max_length=500)
	#picture = CharField()

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.CharField(max_length=500)
	created = models.DateTimeField()

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.CharField(max_length=500)
	created = models.DateTimeField()