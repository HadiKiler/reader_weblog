from ...imports import *


@login_required
def profile(request):
    if request.method == "GET":
        return render(request, f'{__name__.replace(".", "/")}.html')

    if request.method == "POST":
        username = request.POST.get('username','').strip()
        first_name = request.POST.get('first_name','').strip()
        last_name = request.POST.get('last_name','').strip()
        email = request.POST.get('email','').strip()
        bio = request.POST.get('bio','').strip()
        image = request.FILES.get('image')
        
        
        if User.objects.filter(username=username).exclude(id=request.user.id):
            messages.add_message(request, messages.ERROR, "username alredy exits")  # ?????????
            return render(request, f'{__name__.replace(".", "/")}.html')
        
        with transaction.atomic():
            u = request.user
            u.username = username
            u.first_name = first_name
            u.last_name = last_name
            u.email = email
            u.bio = bio
            if image:
                u.image = image
            u.save()

        return render(request, f'{__name__.replace(".", "/")}.html')
