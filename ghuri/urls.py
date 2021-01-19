from django.urls import path
from . import views 

urlpatterns = [
	path('', views.index, name='index-ghuri'),
    path('dashboard/', views.dashboard, name='dashboard-ghuri'),
    path('add-expense/', views.add_expense, name='add_expense'),
    path('add-meal/', views.add_meal, name='add_meal'),
    path('list-expenses/', views.list_expenses, name='list_expenses'),
    path('list-meals/', views.list_meals, name='list_meals'),
    path('login/', views.login, name='login-ghuri'),
    path('logout/', views.logout, name='logout-ghuri'),
]