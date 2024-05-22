from .imports import *

def about_me(request):
    return render(request, f'{__name__.replace(".", "/")}.html') 