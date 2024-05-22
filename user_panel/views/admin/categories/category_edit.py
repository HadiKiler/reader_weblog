from ...imports import *
from django.contrib.auth.hashers import make_password

@login_required
def category_edit(request, id):
    context = {}
    c = get_object_or_404(Category, id=id)
    context['category'] = c
    context['categories'] = Category.objects.all()

    if request.method == "GET":
        return render(request, f'{__name__.replace(".", "/")}.html', context)

    if request.method == "POST":
        parent = request.POST.get('parent', '')
        name = request.POST.get('name','').strip()
        image = request.FILES.get('image')



        if Category.objects.filter(name=name).exclude(id=id):
            messages.add_message(request, messages.ERROR, "name alredy exits")  # ?????????
            return render(request, f'{__name__.replace(".", "/")}.html', context)

        if str(c.id) == parent:
            messages.add_message(request, messages.ERROR, "self join impossible")  # ?????????
            return render(request, f'{__name__.replace(".", "/")}.html', context)

        c.name = name

        if parent:
            c.parent = Category.objects.get(id=parent)
        if image:
            c.image = image
        c.save()

        return redirect(reverse('user_panel_admin_categories'))