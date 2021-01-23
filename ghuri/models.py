from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Expense(models.Model):
    objects = models.Manager()
    name = models.ForeignKey(User,
            on_delete=models.DO_NOTHING,
            related_name='expenses',
    )
    expense_amount = models.DecimalField(max_digits=6, decimal_places=2)
    items_description = models.TextField(max_length=100, blank=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-date",]

    def __str__(self):
        return f"Created by: {self.name.get_full_name()} --> Expense: {self.expense_amount}"

class Meal(models.Model):
    objects = models.Manager()
    
    name = models.ForeignKey(User,
            on_delete=models.DO_NOTHING,
            related_name='meals',
        )
    meal_count = models.IntegerField(default=1)
    description = models.TextField(max_length=100, blank=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-date",]

    def __str__(self):
        return f"You added {self.meal_count} meal on {self.date}"
