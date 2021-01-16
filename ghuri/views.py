from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
    view_context = {
        'title': 'Dashboard',
    }
    return render(request, 'ghuri/dashboard.html', view_context)
