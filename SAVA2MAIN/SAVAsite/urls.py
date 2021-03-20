from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='Home Page'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    
]
