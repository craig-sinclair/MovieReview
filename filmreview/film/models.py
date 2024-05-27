from django.db import models
from django.contrib.auth.models import AbstractUser

class Movie(models.Model):
    name = models.CharField(max_length=128)
    director = models.CharField(max_length=128, null=True)
    release_date = models.DateField(null=True)
    cover_art = models.ImageField(null=True)
    
    
    def __str__(self):
        return self.name
    
class SavedMovie(models.Model):
    movie_id = models.IntegerField(unique=True)
    
    def __str__(self):
        return str(self.movie_id)

class CustomUser(AbstractUser):
    saved_movies = models.ManyToManyField('SavedMovie', related_name='saved_by_users', blank=True)
