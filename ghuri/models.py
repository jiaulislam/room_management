from django.db import models
from django.utils import timezone
from django.conf import settings

from ghuri.managers import MealManager, ExpenseManager


class Expense(models.Model):
    objects = models.Manager()
    expenses = ExpenseManager()
    name = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.DO_NOTHING,
                             related_name='expenses',
                             )
    expense_amount = models.DecimalField(max_digits=6, decimal_places=2)
    items_description = models.TextField(max_length=100, blank=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-date", ]

    def __str__(self):
        return f"{self.name} --> Expense: {self.expense_amount}"


class Meal(models.Model):
    objects = models.Manager()
    meals = MealManager()

    name = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.DO_NOTHING,
                             related_name='meals',
                             )
    meal_count = models.IntegerField(default=1)
    description = models.TextField(max_length=100, blank=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-date", ]

    def __str__(self):
        return f"{self.name} --> Meal: {self.meal_count}"
