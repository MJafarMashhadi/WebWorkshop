from django.shortcuts import render


def login(request):
    return render(request, 'user_manager/login.html', {

    })


def register(request):
    pass


def forgot_password(request):
    pass
