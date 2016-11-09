from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.views.generic import View
from .forms import LoginForm


class LoginView(View):
    def get(self, request):
        form = LoginForm()

        return render(request, 'user_manager/login.html', {
            'form': form
        })

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)

            return redirect('profile:profile', username=user.username)

        return render(request, 'user_manager/login.html', {
            'form': form
        })


def register(request):
    pass


def forgot_password(request):
    pass
