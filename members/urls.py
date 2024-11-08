from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('badrequest', views.badrequest, name='badrequest'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
]