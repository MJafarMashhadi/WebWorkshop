from django.shortcuts import render


def profile(request, username):
    print('Hello', username)

    return render(request, 'user_profile/homepage.html', {
        'username': username
    })

def followers(request, username):
    pass


def followings(request, username):
    pass
