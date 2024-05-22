from .imports import *

def home(request):
    context = {}
    context['controversial_post'] = Post.objects.filter(published=True).order_by('-comment').first()
    context['popular_post'] = Post.objects.filter(published=True).order_by('-like').first()
    context['random_posts'] = Post.objects.filter(published=True).order_by('?')[:6]
    context['news_posts'] = Post.objects.filter(published=True).order_by('-created_at')[:3]
    context['tags'] = Tag.objects.all()

    return render(request, f'{__name__.replace(".", "/")}.html', context)