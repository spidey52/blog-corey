from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
## for prevent to forcely access profile page
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateFom, ProfileUpdateForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        registrationForm = UserRegisterForm(request.POST)
        if registrationForm.is_valid():
            registrationForm.save()
            username = registrationForm.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}')
            return redirect('login')
    else:
        registrationForm = UserRegisterForm()
    return render(request, 'users/register.html', {'form': registrationForm })
    
    
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateFom(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.warning(request, f'your account has been updated. ')
            return redirect('profile')
    else:
        u_form = UserUpdateFom(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'updateForm': u_form,
        'profileForm': p_form
    }
    return render(request, 'users/profile.html', context)

    

