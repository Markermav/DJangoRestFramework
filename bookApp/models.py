from django.db import models

# Create your models here.

class Books(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    price = models.IntegerField()
    image = models.CharField(max_length=255)


    def __repr__(self):
        return '<Books {self.id} {self.name}>'

