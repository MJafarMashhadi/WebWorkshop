from django.conf.urls import url
from .views import LoginView, RegisterView, forgot_password

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/forgot$', forgot_password, name='forgot'),
]