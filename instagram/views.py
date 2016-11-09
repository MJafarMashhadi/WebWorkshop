from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect


def home(request):
    """
    redirect_url = reverse('profile:profile', kwargs={
        'username': 'realdonaldtrump'
    })
    return HttpResponseRedirect(redirect_url)
    """

    # return redirect('profile:profile', username='realdonaldtrump')
    return redirect('user_manager:login')