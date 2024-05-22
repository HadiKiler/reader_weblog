from .imports import *
from django.db.models import Q


def categories(request):
    key = request.GET.get('search','')
    cat = request.GET.get('cat','')
    tag = request.GET.get('tag','')
    
    posts = Post.objects.filter(published=True)
    if cat:
        posts = posts.filter(category_id=cat)
        cat = int(cat)
    if tag:
        posts = posts.filter(tags__in=tag)
        tag = int(tag)
    if key:
        posts = posts.filter(Q(title__icontains=key) | Q(content__icontains=key))

    
    context = {}
    context['posts'] = posts
    context['search'] = key
    context['active_tag'] = tag
    context['active_cat'] = cat
    context['categories'] = Category.objects.all()
    context['tags'] = Tag.objects.all()
    context['popular_blogers'] = User.objects.order_by('post')[:3]

    return render(request, f'{__name__.replace(".", "/")}.html', context)