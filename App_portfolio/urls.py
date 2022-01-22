from django.urls import path
from App_portfolio import views

urlpatterns = [
    path('', views.demo, name='demo'),
]