from ..imports import *
from django.contrib.auth import authenticate, login



def user_login(request):
    if request.method == 'GET':
        return render(request, f'{__name__.replace(".", "/")}.html')
    
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect(reverse('blog_home'))
        
        messages.add_message(request, messages.ERROR, "username or password wrong !")  # ?????????
        return render(request, f'{__name__.replace(".", "/")}.html')
    