from ..imports import *


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('home'))
  