from ...imports import *

@login_required
def comment_show(request, id):
    c = get_object_or_404(Comment, id=id)
    c.checked = True
    c.save()
    return redirect(reverse(''))