from django import forms
from django.forms import Form
from ghuri.models import Expense, Meal
from django.contrib.auth.models import User

class AddExpenseForm(forms.ModelForm):
    
    class Meta:
        model = Expense
        fields = "__all__"


class AddMealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = "__all__"
