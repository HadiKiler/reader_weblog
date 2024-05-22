from ...imports import *

@login_required
def likes(request):
    context = {}
    context['likes'] = Like.objects.all()
    return render(request, f'{__name__.replace(".", "/")}.html', context)
