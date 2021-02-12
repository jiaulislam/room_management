from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(
            instance=request.user,
            data=request.POST,
            initial={'username': request.user})
        print(request.user.username)
        print(user_form.has_changed())
        profile_form = ProfileUpdateForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile has been updated !")
            return redirect('profile')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserUpdateForm(instance=request.user,
                                   initial={'username': request.user})
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'act': 'profile',
        'user_form': user_form,
        'profile_form': profile_form,
        # 'title': username
    }
    return render(request, 'users/profile.html', context)
