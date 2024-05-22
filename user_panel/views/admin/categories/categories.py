from ...imports import *

@login_required
def categories(request):
    context = {}
    context['categories'] = Category.objects.all()

    if request.method == "GET":
        return render(request, f'{__name__.replace(".", "/")}.html', context)

    if request.method == "POST":
        parent = request.POST.get('parent', '')
        name = request.POST.get('name','').strip()
        image = request.FILES.get('image')



        if Category.objects.filter(name=name):
            messages.add_message(request, messages.ERROR, "name alredy exits")  # ?????????
            return render(request, f'{__name__.replace(".", "/")}.html')


        with transaction.atomic():
            u = Category()
            if parent:
                u.parent = Category.objects.get(id=parent)
            u.name = name
            u.image = image
            u.save()

        return redirect(reverse('user_panel_admin_categories'))