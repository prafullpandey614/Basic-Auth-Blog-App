from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=200,null=True,blank=True)
    
class Blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    banner = models.ImageField(upload_to="media/uploads")
    likes_count = models.IntegerField(default=0)
    def __str__(self) -> str:
        return f"{self.author} "
    
    # added in main