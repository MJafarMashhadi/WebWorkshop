from django.shortcuts import render

from user_manager.models import Member, Media


def profile(request, username):
    current_user = Member.objects.get(username=username)
    media = Media.objects.filter(uploader=current_user)\
        .order_by('-created')
    return render(request, 'user_profile/homepage.html', {
        'username': username,
        'user': current_user,
        'media': media
    })


def followers(request, username):
    pass


def followings(request, username):
    pass
