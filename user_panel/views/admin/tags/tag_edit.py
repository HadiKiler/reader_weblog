from ...imports import *

@login_required
def tag_edit(request, id):
    context = {}
    t = get_object_or_404(Tag, id=id)
    context['tag'] = t

    if request.method == "GET":
        return render(request, f'{__name__.replace(".", "/")}.html', context)

    if request.method == "POST":
        name = request.POST.get('name','').strip()

        if Tag.objects.filter(name=name).exclude(id=id):
            messages.add_message(request, messages.ERROR, "name alredy exits")  # ?????????
            return render(request, f'{__name__.replace(".", "/")}.html', context)

        t.name = name
        t.save()

        return redirect(reverse('user_panel_admin_tags'))