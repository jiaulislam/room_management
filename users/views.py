from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages


@login_required
def profile(request, username):
    if request.POST == 'POST':
        u_form = UserUpdateForm(data=request.POST, instance=request.user)
        p_form = ProfileUpdateForm(data=request.POST, files=request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your profile has been updated !")
            return redirect('profile')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'act': 'profile',
        'user_form': u_form,
        'profile_form': p_form,
        'username': username
    }
    return render(request, 'users/profile.html', context)
