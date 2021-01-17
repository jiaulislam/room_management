from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
    view_context = {
        'title': 'Dashboard',
    }
    return render(request, 'ghuri/dashboard.html', view_context)


def add_expense(request):
    view_context = {
        'title': 'Add Expense',
    }
    return render(request, 'ghuri/add_expense.html', view_context)


def add_meal(request):
    view_context = {
        'title': 'Add Meals',
    }
    return render(request, 'ghuri/add_meal.html', view_context)


def list_expenses(request):
    view_context = {
        'title': 'Expenses List',
    }
    return render(request, 'ghuri/list_expenses.html', view_context)


def list_meals(request):
    view_context = {
        'title': 'Meals List',
    }
    return render(request, 'ghuri/list_meals.html', view_context)