from django.db import models
from django.contrib.auth.models import User


class Expenses(models.Model):
    objects = models.Manager()
    items_description = models.TextField(max_length=100)
    expense_amount = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    person = models.ForeignKey(User,
            on_delete=models.DO_NOTHING,
            related_name='expenses'
    )

    class Meta:
        ordering = ["-created",]

    def __str__(self):
        return f"{self.person.username} spent {self.expense_amount}Tk."

class Meals(models.Model):
    meal_count = models.IntegerField(default=1)
    description = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    person = models.ForeignKey(
            User,
            on_delete=models.DO_NOTHING,
            related_name='meals'
        )

    class Meta:
        ordering = ["-created",]

    def __str__(self):
        return f"{self.person.first_name} had {self.meal_count} meals on {self.created}"
