from django import forms
from django.forms import Form
from ghuri.models import Expenses, Meals


class AddExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = "__all__"

class AddMealsForm(forms.ModelForm):
    class Meta:
        model = Meals
        fields = "__all__"




