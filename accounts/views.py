from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect, render

from ChatBec.models import Profile
from ChatBec.forms import ProfileEditForm, UserEditForm


@login_required
def edit(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    user_form = UserEditForm(instance=request.user)
    profile_form = ProfileEditForm(instance=profile)

    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('edit')

    return render(request, 'edit.html', {'user_form': user_form, 'profile_form': profile_form})



