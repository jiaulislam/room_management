from django.db import models
from datetime import date

from django.db.models import Sum


class ExpenseManager(models.Manager):
    today = date.today()

    def with_sum(self, user_id):
        queryset = self.get_queryset().filter(name=user_id, date__month=self.today.month, date__year=self.today.year)
        expense = queryset.aggregate(Sum('expense_amount'))
        print(expense)
        return expense['expense_amount__sum']


class MealManager(models.Manager):
    today = date.today()

    def with_sum(self, user_id):
        queryset = self.get_queryset().filter(name=user_id, date__month=self.today.month, date__year=self.today.year)
        meals_of_user = queryset.aggregate(Sum('meal_count'))
        print(meals_of_user)
        return meals_of_user['meal_count__sum']