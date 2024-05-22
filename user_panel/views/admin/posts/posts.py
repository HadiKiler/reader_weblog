from ...imports import *


@login_required
def posts(request):
    context = {}
    cat = request.GET.get('cat', '')
    if cat:
        all_posts_ids = get_object_or_404(Category, id=cat).children()
        context['posts'] = Post.objects.filter(id__in=all_posts_ids)
    else:
        context['posts'] = Post.objects.all()
    context['categories'] = Category.objects.all()
    return render(request, f'{__name__.replace(".", "/")}.html', context)
