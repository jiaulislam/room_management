from django.db import models
from django.contrib.auth.models import User


class Expenses(models.Model):
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
        return f"{self.person.username} spent {self.expense_amount}Tk."

class Meals(models.Model):
    meal_count = models.IntegerField(default=1)
    description = models.TextField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.ForeignKey(
            User,
            on_delete=models.DO_NOTHING,
            related_name='meals'
        )

    class Meta:
        ordering = ["-created",]

    def __str__(self):
        return f"{self.person.first_name} had {self.meal_count} meals on {self.created}"
