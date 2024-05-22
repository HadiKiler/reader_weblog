from ...imports import *

@login_required
def users(request):
    context = {}
    context['users'] = User.objects.all()
    return render(request, f'{__name__.replace(".", "/")}.html', context)