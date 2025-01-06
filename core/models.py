from django.db import models

from userauth.models import User



class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(max_length=300)
    
    def __str__(self):
        return self.text