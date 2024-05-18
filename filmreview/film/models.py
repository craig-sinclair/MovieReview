from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=128)
    director = models.CharField(max_length=128, null=True)
    release_date = models.DateField(null=True)
    cover_art = models.ImageField(null=True)
    
    
    def __str__(self):
        return self.name