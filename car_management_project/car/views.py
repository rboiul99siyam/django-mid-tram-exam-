from django.shortcuts import render
from django.contrib import messages
from posts.models import UserPostModel
# Create your views here.

def showCarData(request,id):
    car = UserPostModel.objects.get(id=id)
    if car.quan > 0:
        car.quan -= 1
        car.save()
        messages.success(request,'Buy car successfully !')
    else:
        messages.error(request,'Bhai stock khali ekadam !')
        
    return render(request,'profile.html',{'car':car})