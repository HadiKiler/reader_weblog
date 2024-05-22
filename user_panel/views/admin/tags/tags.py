from ...imports import *


@login_required
def tags(request):
    context = {}
    context['tags'] = Tag.objects.all()

    if request.method == "GET":
        return render(request, f'{__name__.replace(".", "/")}.html', context)

    if request.method == "POST":
        name = request.POST.get('name','').strip()

        if Tag.objects.filter(name=name):
            messages.add_message(request, messages.ERROR, "name alredy exits")  # ?????????
            return render(request, f'{__name__.replace(".", "/")}.html', context)

        with transaction.atomic():
            u = Tag()
            u.name = name
            u.save()

        return redirect(reverse('user_panel_admin_tags'))