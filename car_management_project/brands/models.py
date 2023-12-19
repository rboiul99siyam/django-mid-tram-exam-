from django.db import models

# Create your models here.

class brandModel(models.Model):
    brand_name  = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,blank=True,null=True,unique=True)
    def __str__(self):
        return self.brand_name
