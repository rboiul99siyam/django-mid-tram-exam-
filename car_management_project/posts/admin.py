from django.contrib import admin

# Register your models here.
from posts.models import UserPostModel,commentModel

admin.site.register(UserPostModel)
admin.site.register(commentModel)