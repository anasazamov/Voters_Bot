from django.db import models

# Create your models here.

class Voters(models.Model):
    
    chat_id = models.IntegerField(default=0)
    first_start = models.BooleanField(default=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,blank=True)
    position = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
class Candidates(models.Model):
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    yes = models.IntegerField(default=0)
    no =  models.IntegerField(default=0)
    voter = models.ManyToManyField(Voters)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    

