from django.db import models

class User(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
        

class Ad(models.Model):
    title = models.CharField(max_length=50) 
    price = models.FloatField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    





