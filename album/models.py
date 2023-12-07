from django.db import models
from musician.models import musician_model

# Create your models here.
class album_model(models.Model):
    album_Name = models.CharField(max_length=100)
    album_release_date=models.DateField(auto_now_add=True)
    ratings=[
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
    ]
    album_rating=models.IntegerField(choices=ratings)
    musician_relation=models.ForeignKey(musician_model,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.album_Name