from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    objects = models.Manager()
    name = models.ForeignKey(User,
            on_delete=models.DO_NOTHING,
            related_name='expenses'
    )
    expense_amount = models.IntegerField()
    items_description = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created",]

    def __str__(self):
        return f"Added Expense - {self.expense_amount} bdt."

class Meal(models.Model):
    name = models.ForeignKey(
            User,
            on_delete=models.DO_NOTHING,
            related_name='meals'
        )
    meal_count = models.IntegerField(default=1)
    description = models.TextField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created",]

    def __str__(self):
        return f"You added {self.meal_count} on {self.created}"
