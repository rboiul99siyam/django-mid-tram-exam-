from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   path('register/', views.register, name='register'),
   path('login/', views.UserLogIn.as_view(), name='login'),
   path('logout/', views.UserLogOut.as_view(), name='logout'),
   path('update_profile/' , views.changeProfile,name='updata_profile'),
   path('update_password/' , views.change_pass,name='password'),
]
