from django.conf.urls import url
from .views import LoginView, register, forgot_password

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^login/forgot$', forgot_password, name='forgot'),
]