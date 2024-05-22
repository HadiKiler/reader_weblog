from ...imports import *


@login_required
def post_create(request):
    context = {}
    context['categories'] = Category.objects.filter(parent=None)
    context['tags'] = Tag.objects.all()
    
    if request.method == "GET":
        return render(request, f'{__name__.replace(".", "/")}.html', context)

    if request.method == "POST":
        title = request.POST.get('title','').strip()
        category = request.POST.get('category','').strip()
        image = request.FILES.get('image')
        content = request.POST.get('content','').strip()
        tags = request.POST.getlist('tag')
        published = bool(request.POST.get('published',''))

        with transaction.atomic():
            p = Post()
            p.title = title
            p.user = request.user
            p.category = Category.objects.get(id=category)
            p.image = image
            p.content = content
            p.published = published
            p.save()
            for tag in tags:
                p.tags.add(Tag.objects.get(id=tag))
            p.save()

        return redirect(reverse('user_panel_user_posts'))
