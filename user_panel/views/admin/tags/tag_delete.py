from ...imports import *

@login_required
def tag_delete(request, id):
    t = get_object_or_404(Tag, id=id)
    t.delete()
    return redirect(reverse('user_panel_admin_tags'))
