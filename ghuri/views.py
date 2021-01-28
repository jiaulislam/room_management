from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from .forms import AddExpenseForm, AddMealForm
from .models import Expense, Meal
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
import datetime


@login_required
def dashboard(request):
    today = datetime.date.today()
    current_month_total_expenses = Expense.objects.filter(date__year=today.year, date__month=today.month)
    current_month_meals = Meal.objects.filter(date__year=today.year, date__month=today.month)
    dash_meal_count = current_month_meals.aggregate(Sum('meal_count'))
    dash_expense_count = current_month_total_expenses.aggregate(Sum('expense_amount'))
    user_expenses_objects = Expense.objects.filter(name=request.user, date__year=today.year, date__month=today.month)
    user_current_month_expense = user_expenses_objects.aggregate(Sum('expense_amount'))
    user_meal_objects = Meal.objects.filter(name=request.user, date__month=today.month, date__year=today.year)
    user_meal_month_meals = user_meal_objects.aggregate(Sum('meal_count'))
    view_context = {
        'title': 'Dashboard',
        'act': 'dashboard',
        'total_expense': dash_expense_count['expense_amount__sum'],
        'total_meal': dash_meal_count['meal_count__sum'],
        'user_expense': user_current_month_expense['expense_amount__sum'],
        'user_meals': user_meal_month_meals['meal_count__sum'],
    }
    return render(request, 'ghuri/dashboard.html', view_context)


@login_required
def add_expense(request):
    title = 'Add Expense'
    if request.method == 'POST':
        form = AddExpenseForm(request.POST, initial={'name': request.user})
        if form.is_valid():
            form.save()
            return redirect('add_expense')
    else:
        form = AddExpenseForm(initial={'name': request.user})

    view_context = {
        'title': title,
        'form': form,
    }
    return render(request, 'ghuri/add_expense.html', view_context)


@login_required
def add_meal(request):
    title = 'Add Meal'
    if request.method == 'POST':
        form = AddMealForm(request.POST, initial={'name': request.user})
        if form.is_valid():
            form.save()
            return redirect('add_meal')
    else:
        form = AddMealForm(initial={'name': request.user})

    view_context = {
        'title': title,
        'form': form,
    }
    return render(request, 'ghuri/add_meal.html', view_context)


@login_required
def list_expenses(request):
    expense_list = Expense.objects.all()
    paginator = Paginator(expense_list, per_page=10, orphans=3)

    page_number = request.GET.get('page')

    try:
        expenses = paginator.page(page_number)
    except PageNotAnInteger:
        expenses = paginator.page(1)
    except EmptyPage:
        expenses = paginator.page(paginator.num_pages)
    view_context = {
        'title': 'Expenses List',
        'items': expenses,
    }
    return render(request, 'ghuri/list_expenses.html', view_context)


@login_required
def list_meals(request):
    meal_list = Meal.objects.all()
    paginator = Paginator(meal_list, per_page=10, orphans=3)

    page_number = request.GET.get('page')

    try:
        meals = paginator.page(page_number)
    except PageNotAnInteger:
        meals = paginator.page(1)
    except EmptyPage:
        meals = paginator.page(paginator.num_pages)
    view_context = {
        'title': 'Meals List',
        'items': meals,
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
        'title': 'Update Expense',
        'pk': pk,
        'form': form,
    }
    return render(request, 'ghuri/add_expense.html', context=context)


@login_required
def delete_expense(request, pk):
    expense = Expense.objects.get(id=pk)
    if request.method == "POST":
        expense.delete()
        return redirect('list_expenses')
    context = {'expense': expense, 'title': 'Confirm Delete'}
    return render(request, 'ghuri/delete_expense.html', context)


def index(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'ghuri/index.html', context)


@login_required
def update_meal(request, pk):
    existing_meal = Meal.objects.get(id=pk)
    form = AddMealForm(instance=existing_meal)

    if request.method == "POST":
        form = AddMealForm(request.POST, instance=existing_meal)
        if form.is_valid():
            form.save()
            return redirect("list_meals")
    context = {
        'pk': pk,
        'form': form,
        'title': 'Update Meal',
    }
    return render(request, template_name='ghuri/add_meal.html', context=context)


@login_required
def delete_meal(request, pk):
    meal = Meal.objects.get(id=pk)
    if request.method == "POST":
        meal.delete()
        return redirect('list_meals')
    context = {'meal': meal}
    return render(request, 'ghuri/delete_meal.html', context)
