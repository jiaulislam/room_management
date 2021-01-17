from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddExpenseForm, AddMealsForm
from .models import Expenses


def dashboard(request):

    view_context = {
        'title': 'Dashboard',
        'expenses': expenses,
    }
    return render(request, 'ghuri/dashboard.html', view_context)


def add_expense(request):

    if request.method == 'POST':
        form = AddExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_expense')
    else:
        form = AddExpenseForm()

    view_context = {
        'title': 'Add Expense',
        'form': form,
    }
    return render(request, 'ghuri/add_expense.html', view_context)


def add_meal(request):
    title = 'Add Meals'

    if request.method == 'POST':
        form = AddMealsForm(request.POST)
        if form.is_valid():
            return redirect('add_meal')
    else:
        form = AddMealsForm()

    view_context = {
        'title': title,
        'form': form,
    }
    return render(request, 'ghuri/add_meal.html', view_context)


def list_expenses(request):
    expenses = Expenses.objects.all()

    view_context = {
        'title': 'Expenses List',
        'expenses': expenses,
    }
    return render(request, 'ghuri/list_expenses.html', view_context)


def list_meals(request):
    view_context = {
        'title': 'Meals List',
    }
    return render(request, 'ghuri/list_meals.html', view_context)
