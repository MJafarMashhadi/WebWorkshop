from django.conf.urls import url

from user_profile.views import profile, followers, followings

urlpatterns = [
    url(r'^(?P<username>[a-zA-Z0-9_.]{4,})/', profile),
    url(r'^(?P<username>[a-zA-Z0-9_.]{4,})/followers', followers),
    url(r'^(?P<username>[a-zA-Z0-9_.]{4,})/followings', followings),
]


"""

pattern =>

(?P<username>pattern)

"""
