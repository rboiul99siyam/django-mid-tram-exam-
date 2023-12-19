from django.urls import path,include
from . import views
urlpatterns = [
    path('showdata/', views.show_data,name='showData'),
    path('Details/<int:id>', views.Details.as_view(),name='del'),
]