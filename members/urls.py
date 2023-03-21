from django.urls import path
from . import views

urlpatterns = [
    
    path('testing/', views.testing, name="testing"),
    path('members/details/<int:id>', views.details, name='details'),
    path('members/', views.members, name='members'),
]