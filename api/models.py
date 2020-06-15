from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.timezone import now

class User(AbstractUser):
	pass

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	display_name = models.CharField(max_length=50)
	bio = models.CharField(max_length=500)
	picture = models.CharField(max_length=130, default='profile_default.jpeg')
	following = models.ManyToManyField('self', related_name="followers", symmetrical=False)

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.CharField(max_length=500)
	created = models.DateTimeField(default=now)
	likes = models.ManyToManyField(User, related_name='liked_posts')
	comments = models.ManyToManyField(User, through='Comment', related_name='commented_posts')

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
	text = models.CharField(max_length=500)
	created = models.DateTimeField()
