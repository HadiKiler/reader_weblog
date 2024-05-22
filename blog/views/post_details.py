from .imports import *


def post_details(request, id):
    context = {}
    p = get_object_or_404(Post, id=id)
    context['post'] = p
    context['liked'] = False

    for like in p.like_set.all():
        if like.user == request.user:
            context['liked'] = True

    if request.method == "GET":
        return render(request, f'{__name__.replace(".", "/")}.html', context)



def post_comment(request,id):
    content = request.POST.get('comment', '')
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')

    with transaction.atomic():
        c = Comment()
        c.post = get_object_or_404(Post, id=id)
        c.name = name
        c.email = email
        c.content = content
        if request.user.is_authenticated:
            c.user = request.user
        c.save()

    return redirect(reverse('blog_post_details',kwargs={'id': id})+'#comments')
        


def post_reply(request, post_id, comment_id):
    content = request.POST.get('comment', '')
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')

    with transaction.atomic():
        c = Comment()
        c.post = get_object_or_404(Post, id=post_id)
        c.parent = get_object_or_404(Comment, id=comment_id)
        c.name = name
        c.email = email
        c.content = content
        if request.user.is_authenticated:
            c.user = request.user
        c.save()
        
    return redirect(reverse('blog_post_details',kwargs={'id': post_id})+'#comments')
    

@login_required
def post_comment_delete(request, post_id, comment_id):
    c = get_object_or_404(Comment, id=comment_id)
    c.delete()    
    return redirect(reverse('blog_post_details',kwargs={'id': post_id})+'#comments')
    

@login_required
def post_like(request, post_id):
    p = get_object_or_404(Post, id=post_id)
    liked = False

    for like in p.like_set.all():
        if like.user == request.user:
            like.delete()
            liked = True

    if not liked:
        l = Like()
        l.user = request.user
        l.post = p
        l.save()

    return redirect(reverse('blog_post_details',kwargs={'id': post_id})+'#like')
    