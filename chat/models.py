from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.
class Rooms(models.Model):
    name=models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    description=models.TextField(max_length=300)
    slug=models.SlugField(unique=True,blank=True)
    def __str__(self) :
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug or self.slug=="":
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
 

class Message(models.Model):
    room=models.ForeignKey(Rooms,on_delete=models.CASCADE,related_name='messages')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    content=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content