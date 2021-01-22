from django.shortcuts import render, redirect
from .forms import AddExpenseForm, AddMealForm
from .models import Expense, Meal
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
import datetime

@login_required
def dashboard(request):
    today = datetime.date.today()
    currnet_month_total_expenses = Expense.objects.filter(date__year=today.year, date__month=today.month)
    current_month_meals = Meal.objects.filter(date__year=today.year, date__month=today.month)
    dash_meal_count = current_month_meals.aggregate(Sum('meal_count'))
    dash_expense_count = currnet_month_total_expenses.aggregate(Sum('expense_amount'))
    view_context = {
        'title': 'Dashboard',
        'act': 'dashboard',
        'total_expense': dash_expense_count['expense_amount__sum'],
        'total_meal' : dash_meal_count['meal_count__sum']
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

@login_required
def update_expense(request, pk):
    existing_data = Expense.objects.get(id=pk)
    form = AddExpenseForm(instance=existing_data)
    if request.method == 'POST':
        form = AddExpenseForm(request.POST, instance=existing_data)
        if form.is_valid():
            form.save()
            return redirect('list_expenses')

    context = {
        'title': 'Update',
        'pk': pk,
        'form': form,
    }
    return render(request, 'ghuri/add_expense.html', context=context)

@login_required
def delete_expense(request, pk):
    expense = Expense.objects.get(id=pk)
    expense.delete()
    return redirect('list_expenses')

def index(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'ghuri/index.html', context)
