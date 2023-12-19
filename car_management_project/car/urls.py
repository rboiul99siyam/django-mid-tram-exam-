from django.urls import path,include
from . import views
urlpatterns = [
   path('car/<int:id>', views.showCarData,name='car'),
]