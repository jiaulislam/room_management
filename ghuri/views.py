from django.shortcuts import render, redirect
from .forms import AddExpenseForm, AddMealForm
from .models import Expense, Meal
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

@login_required
def dashboard(request):
    total_expenses = Expense.objects.aggregate(Sum('expense_amount'))
    view_context = {
        'title': 'Dashboard',
        'act': 'dashboard',
        'total_expense': total_expenses['expense_amount__sum']
    }
    return render(request, 'ghuri/dashboard.html', view_context)

@login_required
def add_expense(request):
    title = 'Add Expense'
    if request.method == 'POST':
        form = AddExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_expense')
    else:
        form = AddExpenseForm()

    view_context = {
        'title': title,
        'form': form,
    }
    return render(request, 'ghuri/add_expense.html', view_context)  

@login_required
def add_meal(request):
    title = 'Add Meal'

    if request.method == 'POST':
        form = AddMealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_meal')
    else:
        form = AddMealForm()

    view_context = {
        'title': title,
        'form': form,
    }
    return render(request, 'ghuri/add_meal.html', view_context)

@login_required
def list_expenses(request):
    expenses = Expense.objects.all()

    view_context = {
        'title': 'Expenses List',
        'expenses': expenses,
    }
    return render(request, 'ghuri/list_expenses.html', view_context)

@login_required
def list_meals(request):
    meals = Meal.objects.all()
    view_context = {
        'title': 'Meals List',
        'meals': meals,
    }
    return render(request, 'ghuri/list_meals.html', view_context)


def index(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'ghuri/index.html', context)
