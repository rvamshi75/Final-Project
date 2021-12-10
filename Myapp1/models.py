from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tasklist(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE , default=None)
    task = models.CharField(max_length=200)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task+"-"+str(self.done) #here adiing 2nd field "done" , it's a boolean type so we need to convert to string
