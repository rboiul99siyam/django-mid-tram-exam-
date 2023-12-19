from django.db import models
from django.forms import forms
from brands.models import brandModel
# Create your models here.
class UserPostModel(models.Model):
    car_name = models.CharField(max_length=200)
    car_price = models.CharField(max_length=200)
    details = models.TextField()
    quan  = models.IntegerField(default = None)
    brand = models.ManyToManyField(brandModel)
    image = models.ImageField(upload_to='posts/media/uploads/',blank=True,null=True)
    buyer = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.car_name


class commentModel(models.Model):
    userPost = models.ForeignKey(UserPostModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30) 
    email =models.EmailField()
    body = models.TextField()
    createTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'comment by {self.name}'