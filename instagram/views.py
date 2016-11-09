from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect


# @login_required
# from django.views.decorators.http import require_POST, require_GET, require_http_methods
# @require_http_methods(['GET', "POST", "DELETE"])
def home(request):
    """
    redirect_url = reverse('profile:profile', kwargs={
        'username': 'realdonaldtrump'
    })
    return HttpResponseRedirect(redirect_url)
    """

    # return redirect('profile:profile', username='realdonaldtrump')
    return redirect('user_manager:login')