from ...imports import *

@login_required
def category_delete(request, id):
    c = get_object_or_404(Category, id=id)
    c.delete()
    return redirect(reverse('user_panel_admin_categories'))