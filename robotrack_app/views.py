from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, CompetitionForms, RefreeForms
from django import forms
from robotrack_app.models import *


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'robotrack_app/login.html', {'form': form})


def logout_user(request):
    pass


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'robotrack_app/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'robotrack_app/register.html', {'user_form': user_form})


def create_competition(request):
    if request.method == 'POST':
        pass
    else:
        items = dict()
        items['name'] = CompetitionForms()
        items['referee'] = RefreeForms()
        return render(request, 'robotrack_app/create_competition.html', {'competition_form': items})
