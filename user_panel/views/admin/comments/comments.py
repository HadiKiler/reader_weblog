from ...imports import *

@login_required
def comments(request):
    context = {}
    context['comments'] = Comment.objects.filter(parent=None)
    return render(request, f'{__name__.replace(".", "/")}.html', context)
