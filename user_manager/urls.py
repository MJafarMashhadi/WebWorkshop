from django.conf.urls import url
from .views import login, register, forgot_password

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^login/forgot$', forgot_password, name='forgot'),
]