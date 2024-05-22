

from ...imports import *

@login_required
def post_edit(request,id):
    p = get_object_or_404(Post, id=id)
    context = {}
    context['post'] = p
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
            p.title = title
            p.user = request.user
            p.category = Category.objects.get(id=category)
            if image:
                p.image = image
            p.content = content
            p.published = published
            p.save()
            for tag in tags:
                p.tags.add(Tag.objects.get(id=tag))
            p.save()

            # for the remove and add new tags 
            add = []
            delete = []
            old_tags = p.tags.values_list('id', flat=True)
            tag_ids = [int(p) for p in tags]

            for item in tag_ids:
                if item not in old_tags:
                    add.append(item)
            for item in old_tags:
                if item not in tag_ids:
                    delete.append(item)

            for item in add:
                p.tags.add(Tag.objects.get(id=item))
            for item in delete:
                p.tags.remove(Tag.objects.get(id=item))

        return redirect(reverse('user_panel_user_posts'))
