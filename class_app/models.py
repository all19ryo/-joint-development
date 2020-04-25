from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=50)
    schools = models.ManyToManyField(School,blank=True)
    def __str__(self):
        return self.name
class Circle(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    def __str__(self):
        return self.name