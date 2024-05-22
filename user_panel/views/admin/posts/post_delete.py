from ...imports import *

@login_required
def post_delete(request, id):
    p = get_object_or_404(Post, id=id)
    p.delete()
    return redirect(reverse('user_panel_admin_posts'))