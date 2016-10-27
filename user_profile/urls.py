from django.conf.urls import url

from user_profile.views import profile

urlpatterns = [
    url(r'^profile/[a-zA-Z0-9_.]{4,}/', profile)
]

