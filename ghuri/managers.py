from django.db import models
from datetime import date

from django.db.models import Sum


class ExpenseManager(models.Manager):
    today = date.today()

    def with_sum_total_month(self):
        queryset = self.get_queryset().filter(date__month=self.today.month,
                                              date__year=self.today.year)
        expense_of_month = queryset.aggregate(Sum('expense_amount'))
        return expense_of_month['expense_amount__sum']

    def with_sum(self, user_id):
        queryset = self.get_queryset().filter(name=user_id, date__month=self.today.month, date__year=self.today.year)
        expense = queryset.aggregate(Sum('expense_amount'))
        return expense['expense_amount__sum']


class MealManager(models.Manager):
    today = date.today()

    def with_sum_total_month(self):
        queryset = self.get_queryset().filter(date__month=self.today.month,
                                              date__year=self.today.year)
        sum_of_meal = queryset.aggregate(Sum('meal_count'))
        return sum_of_meal['meal_count__sum']

    def with_sum(self, user_id):
        queryset = self.get_queryset().filter(name=user_id,
                                              date__month=self.today.month,
                                              date__year=self.today.year)
        meals_of_user = queryset.aggregate(Sum('meal_count'))
        return meals_of_user['meal_count__sum']