from django import forms
from django.forms import Form
from ghuri.models import Person, Expenses, Meals


class AddExpenseForm(forms.Form):
    name = forms.CharField(label="User")
    expenses = forms.IntegerField(label="Amount")
    expense_details = forms.CharField(
        label="Comments", required=False, widget=forms.Textarea, max_length=100)


class AddMealsForm(forms.Form):
    name = forms.CharField(label="User")
    meal_count = forms.IntegerField(label="Meal unit")
    expense_details = forms.CharField(
        label="Comments", required=False, widget=forms.Textarea, max_length=100)





