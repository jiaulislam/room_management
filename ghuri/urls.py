from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index-ghuri'),
    path('dashboard/', views.dashboard, name='dashboard-ghuri'),
    path('add-expense/', views.add_expense, name='add_expense'),
    path('add-meal/', views.add_meal, name='add_meal'),
    path('list-expenses/', views.list_expenses, name='list_expenses'),
    path('list-meals/', views.list_meals, name='list_meals'),
    path('update-expense/<int:pk>/', views.update_expense, name='update-expense'),
    path('update-meal/<int:pk>/', views.update_meal, name='update-meal'),
    path('delete-expense/<int:pk>/', views.delete_expense, name='delete_expense'),
    path('delete-meal/<int:pk>/', views.delete_meal, name='delete_meal'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
