from django.contrib.auth.models import AbstractUser
from django.db import models

from movies.models import Comment, Genre, Movie


# Create your models here.
class User(AbstractUser):
    comments = models.ManyToManyField(Comment, related_name='user_comments')
    like_genres = models.ManyToManyField(Genre)
