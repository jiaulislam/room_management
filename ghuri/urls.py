from django.urls import path
from . import views 

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-expense/', views.add_expense, name='add_expense'),
    path('add-meal/', views.add_meal, name='add_meal'),
    path('list-expenses/', views.list_expenses, name='list_expenses'),
    path('list-meals/', views.list_meals, name='list_meals'),
]