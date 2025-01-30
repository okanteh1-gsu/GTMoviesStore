from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    released_date = models.DateTimeField(blank=True,null=True)
    duration = models.IntegerField()
    genre = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    movie_poster = models.ImageField(blank=True)
    def __str__(self):
        return self.title

