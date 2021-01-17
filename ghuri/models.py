from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=14)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Expenses(models.Model):
    items_description = models.TextField(max_length=100)
    expense_amount = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    person = models.ForeignKey(
            Person,
            on_delete=models.DO_NOTHING,
            related_name='expenses'
    )

    class Meta:
        ordering = ["-created",]

    def __str__(self):
        return f"{Person.first_name} spent {self.expense_amount} on {self.created}"

class Meals(models.Model):
    meal_count = models.IntegerField(default=1)
    description = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    person = models.ForeignKey(
            Person,
            on_delete=models.DO_NOTHING,
            related_name='meals'
        )

    class Meta:
        ordering = ["-created",]

    def __str__(self):
        return f"{Person.first_name} had {self.meal_count} meals on {self.created}"
