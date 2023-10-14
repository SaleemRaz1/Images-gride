from django.urls import path
from . import views

urlpatterns = [
    path('addimg/', views.addProduct, name="addimg"),  
]