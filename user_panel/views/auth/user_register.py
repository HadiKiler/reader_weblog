from ..imports import *
from django.contrib.auth.hashers import make_password

def user_register(request):
    if request.method == "GET":
        return render(request, f'{__name__.replace(".", "/")}.html')
    
    elif request.method == "POST":
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        repassword = request.POST.get('repassword', '')

        if User.objects.filter(username=username):
            messages.add_message(request, messages.ERROR, "username alredy exits")  # ?????????
            return render(request, f'{__name__.replace(".", "/")}.html')

        if User.objects.filter(email=email):
            messages.add_message(request, messages.ERROR, "email alredy exits")  # ?????????
            return render(request, f'{__name__.replace(".", "/")}.html')
        
        u = User()
        u.username = username
        u.email = email
        if password != repassword:
            messages.add_message(request, messages.ERROR, "password didn't mached !")  # ?????????
            return render(request, f'{__name__.replace(".", "/")}.html')
        u.password = make_password(password)
        u.save()        

        messages.add_message(request, messages.ERROR, "Account Created, login Please.")
        return redirect(reverse('user_panel_login'))