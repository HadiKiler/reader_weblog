from ...imports import *

@login_required
def comment_show(request, id):
    c = get_object_or_404(Comment, id=id)
    c.checked = True
    c.save()
    return redirect(reverse('blog_post_details', kwargs={'id': c.post.id})+f"#comment{id}")