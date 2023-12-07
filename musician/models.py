from django.db import models
# from album.models import album_model
# Create your models here.
class musician_model(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email= models.EmailField()
    phone_number = models.IntegerField()
    instrument_type=models.CharField(max_length=50)
    # album=models.ForeignKey(album_model,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.first_name