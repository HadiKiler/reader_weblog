from ...imports import *

@login_required
def user_edit(request, id):
    context = {}
    u = get_object_or_404(User, id=id)
    context['user'] = u

    if request.method == "GET":
        return render(request, f'{__name__.replace(".", "/")}.html', context)

    if request.method == "POST":
        username = request.POST.get('username','').strip()
        password = request.POST.get('password','').strip()
        first_name = request.POST.get('first_name','').strip()
        last_name = request.POST.get('last_name','').strip()
        email = request.POST.get('email','').strip()
        bio = request.POST.get('bio','').strip()
        is_admin = bool(request.POST.get('is_admin',''))
        image = request.FILES.get('image')
        
        if User.objects.filter(username=username).exclude(id=u.id):
            messages.add_message(request, messages.ERROR, "username alredy exits")  # ?????????
            return render(request, f'{__name__.replace(".", "/")}.html', context)
        
        with transaction.atomic():
            u.username = username
            if password:
                u.password = make_password(password)
            u.first_name = first_name
            u.last_name = last_name
            u.email = email
            u.bio = bio
            u.is_superuser = is_admin
            if image:
                u.image = image
            u.save()

        return redirect(reverse('user_panel_admin_users'))
