from .imports import *

@login_required
def dashboard(request):
    return render(request, f'{__name__.replace(".", "/")}.html')

