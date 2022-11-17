
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save

# Create your models here.



class Authur(models.Model):
    name=models.CharField(max_length=50)
    family=models.CharField(max_length=50)
    email=models.EmailField(unique=True)

    def __str__(self):
        return (self.name) (self.family)




class Article (models.Model):
    STATUS_CHOICES=(
    ("d","draft"),
    ("p","publish"),
    )

    authur=models.ForeignKey(User,on_delete=models.CASCADE, blank=True, db_constraint=False, null=True)
    title = models.CharField(max_length=200,blank=True)
    slug= models.SlugField (max_length=100,unique=True)
    description = models.TextField(blank=True)
    thumbnail= models.ImageField(upload_to="images",blank=True)
    publish= models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=1,choices=STATUS_CHOICES)


    def __str__(self):
        return self.title


#class Profile(models.Model):

        #user = models.OneToOneField(auth.models.User, on_delete=models.CASCADE)
        #avatar = models.ImageField(default='1.jpg', upload_to='displays', height_field=None, width_field=None, max_length=None)
    





